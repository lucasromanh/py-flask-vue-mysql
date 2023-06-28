from app import app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

# Ruta al archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), 'app/.env')

# Cargar las variables de entorno desde el archivo .env
load_dotenv(dotenv_path)

# Crear una instancia de MySQL
mysql = MySQL()

# Configurar la conexión a MySQL utilizando las variables de entorno
app.config['MYSQL_USER'] = app.config.get('MYSQL_USER') or 'root'
app.config['MYSQL_PASSWORD'] = app.config.get('MYSQL_PASSWORD') or 'micram123'
app.config['MYSQL_HOST'] = app.config.get('MYSQL_HOST') or 'localhost'
app.config['MYSQL_DB'] = app.config.get('MYSQL_DB') or 'crudflask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Inicializar la conexión a MySQL
mysql.init_app(app)
