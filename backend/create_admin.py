from extensions import db
from models.user import User
from werkzeug.security import generate_password_hash
from app import create_app

app = create_app()

with app.app_context():
    username = "admin"
    password = "Admin123!"  # Change ce mot de passe à ta convenance
    role = "admin"

    # Vérifier si admin existe déjà
    existing_admin = User.query.filter_by(username=username).first()
    if existing_admin:
        print("L'administrateur existe déjà.")
    else:
        admin_user = User(
            username=username,
            password=generate_password_hash(password),
            role=role
        )
        db.session.add(admin_user)
        db.session.commit()
        print(f"Admin créé avec username: {username} et password: {password}")
