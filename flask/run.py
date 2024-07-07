from flask import Flask
from app.views import *
from app.database import test_connection, init_app

app = Flask(__name__)

# Rutas de Api-Rest 

app.route('/', methods=['GET'])(index)

# Conexión a BDD
init_app()

if __name__ == '__main__':
    app.run(debug=True)
