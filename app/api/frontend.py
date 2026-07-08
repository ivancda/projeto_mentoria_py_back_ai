from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path

router = APIRouter()

@router.get("/")
async def serve_index():
    template_path = Path(__file__).parent.parent / "templates" / "index.html"
    return FileResponse(template_path, media_type="text/html")
