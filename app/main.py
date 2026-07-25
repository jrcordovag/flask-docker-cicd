import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de base de datos desde variable de entorno
db_url = os.getenv('DATABASE_URL', 'sqlite:///:memory:')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo simple para la base de datos
class Noticia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)

# Crear tablas al iniciar
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return jsonify({"status": "ok", "message": "API corriendo correctamente"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

# Endpoint para listar noticias
@app.route('/noticias', methods=['GET'])
def get_noticias():
    noticias = Noticia.query.all()
    return jsonify([{"id": n.id, "titulo": n.titulo} for n in noticias]), 200

# Endpoint para crear noticia
@app.route('/noticias', methods=['POST'])
def create_noticia():
    data = request.get_json() or {}
    if not data.get('titulo'):
        return jsonify({"error": "El título es obligatorio"}), 400
    
    nueva = Noticia(titulo=data['titulo'])
    db.session.add(nueva)
    db.session.commit()
    return jsonify({"id": nueva.id, "titulo": nueva.titulo}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)