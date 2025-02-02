from fastapi import APIRouter, UploadFile, File
import os
from src.services.speech_to_text import process_audio  # Corrected Import

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../uploads")
UPLOAD_DIR = os.path.normpath(UPLOAD_DIR)  # Normalize the path

os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure folder exists

router = APIRouter()

@router.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())  # Ensure async read
    
    print(f"✅ File saved at: {file_path}")  # Debugging print
    
    text = process_audio(file_path)  # AI Processing
    
    return {"message": "Audio processed", "text": text, "file_path": file_path}
