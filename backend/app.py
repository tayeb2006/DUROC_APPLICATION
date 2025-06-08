from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db
from flask_jwt_extended import JWTManager  # ← Import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # CORS pour le frontend
    CORS(app, origins=["http://127.0.0.1:5500", "http://localhost:5500"])

    # Initialiser la base de données
    db.init_app(app)

    # JWT Config
    app.config['JWT_SECRET_KEY'] = 'votre_cle_secrete_super_sécurisée'
    jwt = JWTManager(app)

    # Importer les modèles pour les migrations / accès
    with app.app_context():
        from models import employee, department, position, project, employee_project, salary, leave, user

    # Enregistrer les blueprints
    from routes.employee_routes import employee_bp
    from routes.department_routes import department_bp
    from routes.position_routes import position_bp
    from routes.project_routes import project_bp
    from routes.salary_routes import salary_bp
    from routes.stats import stats_bp
    from routes.auth import auth_bp  # ← Ajouter blueprint pour l'authentification

    app.register_blueprint(employee_bp)
    app.register_blueprint(department_bp)
    app.register_blueprint(position_bp)
    app.register_blueprint(project_bp)
    app.register_blueprint(salary_bp)
    app.register_blueprint(stats_bp)
    app.register_blueprint(auth_bp)  # ← Enregistrement ici

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
