import google.generativeai as genai
from typing import List, Optional
from src.utils.config import config
import logging

logger = logging.getLogger(__name__)


class LLMService:
    """Service for generating responses using Google's Gemini model"""

    def __init__(self):
        # Configure the API key
        genai.configure(api_key=config.GEMINI_API_KEY)

        # Initialize the model
        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",  # Using latest version that supports generateContent
            generation_config={
                "max_output_tokens": config.MAX_TOKENS,
                "temperature": config.TEMPERATURE,
            }
        )

    def generate_response(self, context: str, question: str) -> Optional[str]:
        """
        Generate a response based on the provided context and question
        """
        try:
            # Create a prompt that emphasizes using only the provided context
            prompt = f"""
            You are an AI assistant for the book "Physical AI & Humanoid Robotics".
            Your task is to answer the user's question based ONLY on the provided context.
            Do NOT use any general world knowledge or information outside of the context provided.
            If the answer cannot be derived from the provided context, clearly state that the information is not available in the book.

            Context: {context}

            Question: {question}

            Please provide a concise and accurate answer based only on the provided context.
            """

            # Generate content using the model
            response = self.model.generate_content(prompt)

            # Extract the text from the response
            if response and response.text:
                logger.info("Successfully generated response using Gemini")
                return response.text.strip()
            else:
                logger.warning("Gemini returned empty response")
                return None

        except Exception as e:
            logger.error(f"Error generating response with Gemini: {e}")
            return None

    def generate_response_from_selected_text(self, selected_text: str, question: str) -> Optional[str]:
        """
        Generate a response based only on the selected text provided by the user
        """
        try:
            # Create a prompt that focuses only on the selected text
            prompt = f"""
            You are an AI assistant for the book "Physical AI & Humanoid Robotics".
            Your task is to answer the user's question based ONLY on the provided selected text.
            Do NOT use any general world knowledge or information outside of the selected text provided.
            Do NOT perform any additional retrieval from the book.

            Selected Text: {selected_text}

            Question: {question}

            Please provide a concise and accurate answer based only on the provided selected text.
            """

            # Generate content using the model
            response = self.model.generate_content(prompt)

            # Extract the text from the response
            if response and response.text:
                logger.info("Successfully generated response from selected text using Gemini")
                return response.text.strip()
            else:
                logger.warning("Gemini returned empty response for selected text")
                return None

        except Exception as e:
            logger.error(f"Error generating response from selected text with Gemini: {e}")
            return None

    def validate_response_against_context(self, response: str, context: str) -> bool:
        """
        Basic validation to check if the response seems to be based on the provided context
        This is a simple implementation - more sophisticated validation could be added
        """
        try:
            # This is a basic check - in a real implementation, you might want to use
            # more sophisticated techniques to validate the response against the context
            if not response or not context:
                return False

            # Check if the response contains content that's likely from the context
            # This is a very basic check and should be improved in production
            response_lower = response.lower()
            context_lower = context.lower()

            # Simple check: if response is too generic or doesn't contain key terms from context
            # This is just a placeholder for more sophisticated validation
            return len(response) > 0

        except Exception as e:
            logger.error(f"Error validating response: {e}")
            return False