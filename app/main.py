from flask import Flask
from  app.routes.routes import face_recognition_bp
from flask_cors import CORS  # Importer CORS

app = Flask(__name__)

# Configuration de CORS pour autoriser les demandes de votre application Angular
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

# Enregistrement du blueprint pour les routes de reconnaissance faciale
app.register_blueprint(face_recognition_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
