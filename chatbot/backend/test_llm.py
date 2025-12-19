#!/usr/bin/env python3
"""
Test script to verify that the LLM service can access the model
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services.llm_service import LLMService
from src.utils.config import config

def test_llm():
    print("Testing LLM service...")

    try:
        # Initialize the LLM service
        llm_service = LLMService()
        print("[SUCCESS] LLM Service initialized successfully")

        # Test a simple generation
        test_response = llm_service.generate_response(
            context="This is a test context about Physical AI and Humanoid Robotics.",
            question="What is this about?"
        )

        if test_response:
            print("[SUCCESS] LLM service is working correctly!")
            print(f"Sample response: {test_response[:100]}...")
        else:
            print("[ERROR] LLM service returned empty response")

    except Exception as e:
        print(f"[ERROR] Error with LLM service: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Check if API key is configured
    if not config.GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY is not configured in .env file")
    else:
        print("GEMINI_API_KEY is configured")
        test_llm()