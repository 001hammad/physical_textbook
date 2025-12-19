#!/usr/bin/env python3
"""
Debug script to test the full RAG agent process
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.agents.rag_agent import RAGAgent
from src.models.chat import ChatMode

def debug_rag_agent():
    print("Debugging RAG Agent full process...")

    # Initialize the RAG agent
    agent = RAGAgent()

    # Test with a query
    test_question = "What is Physical AI and Humanoid Robotics?"

    print(f"Testing query: '{test_question}'")

    try:
        # Process the query through the RAG agent
        response = agent.process_query(
            question=test_question,
            selected_text=None,
            mode=ChatMode.NORMAL
        )

        print(f"Response ID: {response.response_id}")
        print(f"Query ID: {response.query_id}")
        print(f"Answer: {repr(response.answer)}")
        print(f"Answer length: {len(response.answer) if response.answer else 0}")
        print(f"Cleaned answer: '{response.answer.strip() if response.answer else ''}'")
        print(f"Sources: {response.sources}")
        print(f"Confidence: {response.confidence}")
        print(f"Timestamp: {response.timestamp}")

        if response.answer:
            print("[SUCCESS] RAG agent returned a valid answer!")
        else:
            print("[ERROR] RAG agent returned an empty answer")

    except Exception as e:
        print(f"Error in RAG agent: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_rag_agent()