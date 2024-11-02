import os
import face_recognition

class ImageRepository:
    @staticmethod
    def load_image(file_path):
        if not file_path or not isinstance(file_path, str) or not os.path.isfile(file_path):
            raise FileNotFoundError(f"Le fichier {file_path} n'existe pas ou n'est pas valide.")
        return face_recognition.load_image_file(file_path)