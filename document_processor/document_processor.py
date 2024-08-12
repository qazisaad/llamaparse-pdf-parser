# document_processor.py

import os
from typing import List, Dict, Optional
from dotenv import load_dotenv
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader, Document
from pydantic import BaseModel, Field

# Load environment variables from a .env file
load_dotenv()

# Access the API keys securely from environment variables
LLAMA_CLOUD_API_KEY: Optional[str] = os.getenv("LLAMA_CLOUD_API_KEY")
OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")

class DocumentProcessorConfig(BaseModel):
    input_dir: str = Field(..., description="The directory where documents are stored.")
    recursive: bool = Field(True, description="Whether to read files in subdirectories recursively.")

class DocumentProcessor:
    def __init__(self, config: DocumentProcessorConfig, one_doc_per_page: bool = False):
        self.input_dir = config.input_dir
        self.recursive = config.recursive
        self.one_doc_per_page = one_doc_per_page

    async def load_documents(self, result_type: str = "markdown", verbose: bool = False) -> List[Document]:
        parser = LlamaParse(result_type=result_type, verbose=verbose)
        file_extractor = {".pdf": parser}
        reader = SimpleDirectoryReader(
            input_dir=self.input_dir,
            recursive=self.recursive,
            file_extractor=file_extractor
        )
        documents: List[Document] = await reader.aload_data()
        if self.one_doc_per_page:
            documents = self.combine_documents_by_file(documents)
        return documents

    def combine_documents_by_file(self, documents: List[Document]) -> List[Document]:
        """
        Combines pages from the same file into a single document.
        """
        name_to_file_data: Dict[str, Dict[str, str]] = {}
        for d in documents:
            file_name = d.metadata['file_name']
            if file_name not in name_to_file_data:
                name_to_file_data[file_name] = {'text': d.text, 'metadata': d.metadata}
            else:
                name_to_file_data[file_name]['text'] += d.text

        combined_documents: List[Document] = [
            Document(text=value['text'], metadata=value['metadata'])
            for value in name_to_file_data.values()
        ]

        return combined_documents
