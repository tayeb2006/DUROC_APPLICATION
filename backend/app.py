from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db  # <-- Import de db ici

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)

    # Import des modèles *après* la création de l'app et initialisation db
    # pour éviter les imports circulaires
    with app.app_context():
        from models import employee, department, position, project, employee_project, salary, leave, user

    from routes.employee_routes import employee_bp
    from routes.department_routes import department_bp
    from routes.position_routes import position_bp
    from routes.project_routes import project_bp
    from routes.salary_routes import salary_bp

    app.register_blueprint(employee_bp)
    app.register_blueprint(department_bp)
    app.register_blueprint(position_bp)
    app.register_blueprint(project_bp)
    app.register_blueprint(salary_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
