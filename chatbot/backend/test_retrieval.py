#!/usr/bin/env python3
"""
Test script to verify that the Qdrant collection has been populated
and that the retrieval service works correctly.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services.retrieval_service import RetrievalService
from src.services.embedding_service import EmbeddingService
from src.utils.config import config

def test_collection():
    print("Testing Qdrant collection...")

    # Initialize services
    retrieval_service = RetrievalService()
    embedding_service = EmbeddingService()

    # Get all content IDs to verify collection is populated
    content_ids = retrieval_service.get_all_content_ids()
    print(f"Number of documents in collection: {len(content_ids)}")

    if len(content_ids) > 0:
        print("[SUCCESS] Collection has documents!")

        # Test retrieval with a sample query
        sample_query = "What is Physical AI and Humanoid Robotics?"
        query_embedding = embedding_service.generate_query_embedding(sample_query)

        if query_embedding:
            print("[SUCCESS] Successfully generated query embedding")

            # Retrieve relevant content
            retrieved_content = retrieval_service.retrieve_relevant_content(query_embedding, limit=3)
            print(f"[SUCCESS] Retrieved {len(retrieved_content)} relevant documents")

            if len(retrieved_content) > 0:
                print("[SUCCESS] Retrieval service is working correctly!")
                print(f"Sample retrieved content title: {retrieved_content[0].retrieval_metadata.get('title', 'N/A')}")
                print(f"Sample content preview: {retrieved_content[0].content[:100]}...")
            else:
                print("[ERROR] No content retrieved - there might be an issue")
        else:
            print("[ERROR] Failed to generate query embedding")
    else:
        print("[ERROR] Collection is still empty - indexing may have failed")

if __name__ == "__main__":
    test_collection()