from flask import Flask
from src.routes.motocycleRoutes import motorcycle_bp
from src.database import Base, engine

app = Flask(__name__)

# Crear tablas automáticamente
Base.metadata.create_all(bind=engine)

# Registrar rutas
app.register_blueprint(motorcycle_bp, url_prefix="/api/motorcycles")

@app.route('/')
def home():
    return "API PRO funcionando 🚀"

if __name__ == '__main__':
    app.run(debug=True)