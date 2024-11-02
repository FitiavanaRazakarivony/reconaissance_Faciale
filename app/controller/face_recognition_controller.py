import cv2
from app.service.face_recognition_service import FaceRecognitionService
from app.repository.Image_repository import ImageRepository

class FaceRecognitionController:
    def __init__(self):
        self.service = FaceRecognitionService()
        self.repository = ImageRepository()

    def recognize_faces(self, test_image_path, reference_image_path):
        try:
            # Chargement des images
            test_image = self.repository.load_image(test_image_path)
            reference_image = self.repository.load_image(reference_image_path)

            # Encodage du visage de référence
            reference_encoding = self.service.encode_face(reference_image)

            # Comparaison des visages
            results = self.service.compare_faces(reference_encoding, test_image)

            # Affichage des résultats
            return self.display_results(test_image, results)

        except Exception as e:
            return str(e)

    def display_results(self, test_image, results):
        test_image_bgr = cv2.cvtColor(test_image, cv2.COLOR_RGB2BGR)
        for (top, right, left, bottom), match in results:
            label = "Mitovy" if match else "Tsy mitovy"
            cv2.rectangle(test_image_bgr, (left, top), (right, bottom), (0, 200, 0), 2)
            cv2.putText(test_image_bgr, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 200, 0), 2)

        cv2.imshow("Reconnaissance Faciale", test_image_bgr)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return "Reconnaissance faciale affichée."
