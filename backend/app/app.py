from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Ruta al archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), 'app/.env')

# Cargar las variables de entorno desde el archivo .env
load_dotenv(dotenv_path)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})


# settings por las dudas
app.secret_key = "miclavesecreta"
