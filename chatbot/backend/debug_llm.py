#!/usr/bin/env python3
"""
Debug script to check what's happening with LLM responses
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services.llm_service import LLMService
from src.services.embedding_service import EmbeddingService
from src.services.retrieval_service import RetrievalService
from src.utils.config import config

def debug_llm():
    print("Debugging LLM response generation...")

    # Initialize services
    llm_service = LLMService()
    embedding_service = EmbeddingService()
    retrieval_service = RetrievalService()

    # Test with a simple query
    test_question = "What is Physical AI and Humanoid Robotics?"
    test_context = """# Welcome to Physical AI & Humanoid Robotics

This course teaches you how to create **embodied intelligence** – AI that lives in the real world inside humanoid robots.

### Course Focus
- Bridging digital brains with physical bodies
- Controlling humanoid robots in simulation and real life
- Using cutting-edge tools: ROS 2, Gazebo, Unity, NVIDIA Isaac
- Building robots that walk, see, grasp, and talk

### Who is this for?
- Students and developers interested in robotics and AI
- Anyone who wants to build the next generation of humanoid assistants

### What You'll Learn
- ROS 2: The nervous system of robots
- Simulation: Safe testing with digital twins
- Advanced perception and machine learning
- Conversational robotics with GPT models
- Final capstone: Build your own autonomous humanoid"""

    print("Test question:", test_question)
    print("Test context (first 200 chars):", test_context[:200], "...")

    # Test LLM response generation
    try:
        response = llm_service.generate_response(test_context, test_question)
        print("LLM Response:", repr(response))  # Using repr to see if there are hidden characters
        print("LLM Response length:", len(response) if response else 0)
        if response:
            print("LLM Response (cleaned):", response.strip())
    except Exception as e:
        print(f"Error generating LLM response: {e}")
        import traceback
        traceback.print_exc()

    # Test a more complex scenario similar to the actual flow
    print("\n" + "="*50)
    print("Testing with actual RAG flow...")

    # Generate embedding for the question
    query_embedding = embedding_service.generate_query_embedding(test_question)
    if query_embedding:
        print("Query embedding generated successfully")

        # Retrieve content
        retrieved_content = retrieval_service.retrieve_relevant_content(query_embedding, limit=3)
        print(f"Retrieved {len(retrieved_content)} content pieces")

        if retrieved_content:
            context_text = "\n\n".join([ctx.content for ctx in retrieved_content])
            print("Retrieved context (first 200 chars):", context_text[:200], "...")

            # Generate response with retrieved context
            response = llm_service.generate_response(context_text, test_question)
            print("Final RAG response:", repr(response))
            print("Final RAG response length:", len(response) if response else 0)
            if response:
                print("Final RAG response (cleaned):", response.strip())

if __name__ == "__main__":
    if not config.GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY is not configured")
    else:
        debug_llm()