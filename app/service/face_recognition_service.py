import face_recognition

class FaceRecognitionService:
    def encode_face(self, image):
        encodings = face_recognition.face_encodings(image)
        if not encodings:
            raise ValueError("Aucun visage trouvé dans l'image.")
        return encodings[0]

    def compare_faces(self, reference_encoding, test_image):
        face_locations = face_recognition.face_locations(test_image)
        face_encodings = face_recognition.face_encodings(test_image, face_locations)

        results = []
        for (top, right, left, bottom), face_encoding in zip(face_locations, face_encodings):
            match = face_recognition.compare_faces([reference_encoding], face_encoding)[0]
            results.append(((top, right, left, bottom), match))
        return results
