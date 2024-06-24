from waitress import serve
from main import app  # Importar seu aplicativo WSGI

if __name__ == "__main__":
    serve(app, host='127.0.0.1', port=8080)