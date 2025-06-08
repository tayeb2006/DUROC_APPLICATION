from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.user import User
from extensions import db
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Création admin par défaut si n'existe pas (uniquement pour test)
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin',
            password=generate_password_hash('Admin123!'),
            role='admin'
        )
        db.session.add(admin)
        db.session.commit()

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.username, additional_claims={"role": user.role})


        return jsonify(access_token=access_token), 200

    return jsonify({'message': 'Utilisateur ou mot de passe invalide'}), 401
