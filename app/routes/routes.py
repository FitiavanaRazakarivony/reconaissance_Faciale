from flask import Blueprint, request, jsonify
from app.controller.face_recognition_controller import FaceRecognitionController

# Initialisation de Blueprint
face_recognition_bp = Blueprint('face_recognition', __name__)
controller = FaceRecognitionController()

@face_recognition_bp.route('/recognize', methods=['POST'])
def recognize_faces():
    data = request.get_json()
    test_image_path = data.get('test_image_path')
    reference_image_path = data.get('reference_image_path')

    result = controller.recognize_faces(test_image_path, reference_image_path)
    return jsonify({"result": result})
