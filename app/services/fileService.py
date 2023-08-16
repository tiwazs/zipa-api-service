import os
import shutil
from fastapi import UploadFile


class FileService:
    def save(self, file: UploadFile, path: str, filename: str):
        filepath = os.path.join(path, filename)
        with open(filepath, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)    
        return filepath