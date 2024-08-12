
### 1. `document_processor.py`

This file defines the classes and configuration needed to process documents:

- **`DocumentProcessorConfig`**: A Pydantic-based class that holds configuration settings, such as the input directory path and whether to read files recursively.
- **`DocumentProcessor`**: The main class responsible for loading and optionally combining documents. It uses the `LlamaParse` and `SimpleDirectoryReader` classes for reading documents from a directory.

### 2. `main.py`

This is the entry point of the application. It initializes the `DocumentProcessor` with the desired configuration and processes the documents:

- **`main()`**: An asynchronous function that creates a `DocumentProcessor` instance and loads the documents from the specified directory. The documents are then printed with their file name and the first 100 characters of their content.

### 3. `.env`

This file is used to store environment variables, such as API keys. It is excluded from the repository using `.gitignore`.

### 4. `.gitignore`

This file specifies which files and directories to ignore in the Git repository. The `.env` file, `data/` folder, and `myenv/` folder are ignored.

## Setup and Usage

### Prerequisites

- Python 3.7 or higher
- `pip` for managing Python packages
- Virtual environment setup (optional but recommended)

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/document-processor.git
    cd document-processor
    ```

2. **Create and activate a virtual environment (optional but recommended)**:

    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the `.env` file**:

   Create a `.env` file in the root directory and add your environment variables, such as:

    ```
    LLAMA_CLOUD_API_KEY=your_llama_cloud_api_key
    OPENAI_API_KEY=your_openai_api_key
    ```

### Running the Project

You can run the document processing by executing `main.py`. The script can process documents either by keeping each page as a separate document or by combining pages from the same file into a single document.

```bash
python main.py
