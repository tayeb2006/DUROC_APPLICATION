from flask import Blueprint, request, jsonify
from extensions import db
from models.department import Department

department_bp = Blueprint('department_bp', __name__, url_prefix='/api/departments')

# 🔹 Créer un département
@department_bp.route('/', methods=['POST'])
def create_department():
    data = request.get_json()
    new_dept = Department(name=data['name'])
    db.session.add(new_dept)
    db.session.commit()
    return jsonify({"message": "Département créé avec succès"}), 201

# 🔹 Récupérer tous les départements
@department_bp.route('/', methods=['GET'])
def get_departments():
    departments = Department.query.all()
    return jsonify([
        {"id": d.id, "name": d.name} for d in departments
    ])

# 🔹 Récupérer un seul département
@department_bp.route('/<int:id>', methods=['GET'])
def get_department(id):
    d = Department.query.get_or_404(id)
    return jsonify({"id": d.id, "name": d.name})

# 🔹 Mettre à jour un département
@department_bp.route('/<int:id>', methods=['PUT'])
def update_department(id):
    d = Department.query.get_or_404(id)
    data = request.get_json()
    d.name = data.get('name', d.name)
    db.session.commit()
    return jsonify({"message": "Département mis à jour"})

# 🔹 Supprimer un département
@department_bp.route('/<int:id>', methods=['DELETE'])
def delete_department(id):
    d = Department.query.get_or_404(id)
    db.session.delete(d)
    db.session.commit()
    return jsonify({"message": "Département supprimé"})
