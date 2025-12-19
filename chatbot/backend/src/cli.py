"""
Command Line Interface for RAG Chatbot Backend
"""
import argparse
import sys
from datetime import datetime
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


def index_book_content(file_path: str):
    """
    Index book content from a file
    """
    logger.info(f"Starting to index book content from: {file_path}")

    try:
        from src.agents.rag_agent import RAGAgent
        from src.models.data_models import BookContent
        import os
        import uuid
        from datetime import datetime

        print(f"Indexing book content from: {file_path}")

        # Initialize the RAG agent
        agent = RAGAgent()
        print("RAG Agent initialized successfully")

        # Check if file_path is a directory (like the docs folder)
        if os.path.isdir(file_path):
            print(f"Processing directory: {file_path}")
            indexed_count = 0

            # Process all markdown files in the directory and subdirectories
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    if file.endswith(('.md', '.mdx', '.txt')):
                        file_path_full = os.path.join(root, file)
                        print(f"Processing file: {file_path_full}")

                        with open(file_path_full, 'r', encoding='utf-8') as f:
                            content = f.read()

                        if content.strip():  # Only process non-empty files
                            # Create a BookContent object
                            book_content = BookContent(
                                id=str(uuid.uuid4()),
                                title=file,
                                content=content,
                                metadata={
                                    "source_file": file,
                                    "source_path": root,
                                    "size": len(content),
                                    "indexed_at": str(datetime.now())
                                }
                            )

                            # Use the agent to index the content
                            success = agent.index_book_content(book_content)
                            if success:
                                print(f"Successfully indexed: {file}")
                                indexed_count += 1
                            else:
                                print(f"Failed to index: {file}")

            print(f"Indexing completed! Indexed {indexed_count} files successfully.")

        else:
            # Process a single file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if content.strip():
                # Create a BookContent object
                book_content = BookContent(
                    id=str(uuid.uuid4()),
                    title=os.path.basename(file_path),
                    content=content,
                    metadata={
                        "source_file": os.path.basename(file_path),
                        "size": len(content),
                        "indexed_at": str(datetime.now())
                    }
                )

                # Use the agent to index the content
                success = agent.index_book_content(book_content)
                if success:
                    print(f"Successfully indexed: {os.path.basename(file_path)}")
                else:
                    print(f"Failed to index: {os.path.basename(file_path)}")

            print("Indexing completed successfully!")

    except Exception as e:
        logger.error(f"Error during indexing: {e}")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

    return True


def main():
    parser = argparse.ArgumentParser(description="RAG Chatbot Backend CLI")
    parser.add_argument(
        "command",
        choices=["index-book"],
        help="Command to execute"
    )
    parser.add_argument(
        "--file",
        "-f",
        type=str,
        help="Path to book content file for indexing"
    )

    args = parser.parse_args()

    if args.command == "index-book":
        if not args.file:
            print("Error: --file argument is required for index-book command")
            sys.exit(1)

        success = index_book_content(args.file)
        if not success:
            sys.exit(1)


if __name__ == "__main__":
    main()