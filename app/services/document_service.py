"""Document processing and storage logic."""
from pathlib import Path
from typing import Dict

STORAGE_DIR = Path("storage")
STORAGE_DIR.mkdir(exist_ok=True)


def save_document(file_obj, metadata: Dict) -> Dict:
    # Implement saving and processing (text extraction, chunking)
    return {"id": "doc-1", "path": str(STORAGE_DIR / "dummy")}
