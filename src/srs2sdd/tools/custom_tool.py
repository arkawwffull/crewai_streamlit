# tools/custom_tool.py
from crewai.tools import BaseTool
from pydantic import Field
import docx

class FileReaderTool(BaseTool):
    name: str = "File Reader"
    description: str = "Reads content from .txt or .docx files."
    
    # Declare file_path as a class-level field
    file_path: str = Field(..., description="The path to the file to be read. Supported formats: .txt, .docx.")
    
    def _run(self) -> str:
        """
        Reads the content of the file based on its type.
        
        Returns:
            str: The content of the file.
        
        Raises:
            ValueError: If the file format is unsupported.
            FileNotFoundError: If the file does not exist.
        """
        try:
            if self.file_path.endswith(".txt"):
                with open(self.file_path, "r", encoding="utf-8") as file:
                    return file.read()
            elif self.file_path.endswith(".docx"):
                doc = docx.Document(self.file_path)
                return "\n".join([para.text for para in doc.paragraphs])
            else:
                raise ValueError("Unsupported file format. Please provide a .txt or .docx file.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{self.file_path}' was not found.")
