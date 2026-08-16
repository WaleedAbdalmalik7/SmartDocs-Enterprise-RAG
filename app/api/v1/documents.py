"""Document upload and management endpoints."""
from fastapi import APIRouter, UploadFile, File, Depends
from ...schemas.schemas import DocumentOut, DocumentCreate
from ..deps import get_db_dep

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/upload", response_model=DocumentOut)
async def upload_document(payload: DocumentCreate, file: UploadFile = File(...), db=Depends(get_db_dep)):
    # Save file and metadata
    return {"id": "doc-1", "title": payload.title, "description": payload.description}


@router.get("/", response_model=list[DocumentOut])
def list_documents(db=Depends(get_db_dep)):
    return []
