# main.py

import nest_asyncio
import asyncio
from document_processor import DocumentProcessor, DocumentProcessorConfig

# Allow asyncio to work in Jupyter notebooks
nest_asyncio.apply()

async def main() -> None:
    # Use Pydantic configuration
    config = DocumentProcessorConfig(input_dir="./data")
    # Set one_doc_per_page to True to combine pages from the same file into a single document
    # Set one_doc_per_page to False or do not specify it to keep each page as a separate document
    one_doc_per_page = True
    processor = DocumentProcessor(config=config, one_doc_per_page=one_doc_per_page)

    # Load documents
    documents = await processor.load_documents()

    for doc in documents:
        print(doc.metadata['file_name'])
        print(doc.text[:100])  # Print the first 100 characters of each document

if __name__ == "__main__":
    # Run the main function asynchronously
    asyncio.run(main())
