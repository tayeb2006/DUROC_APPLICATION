from flask import Blueprint, request, jsonify
from extensions import db
from models.department import Department

department_bp = Blueprint('department_bp', __name__, url_prefix='/api/departments')

@department_bp.route('/', methods=['POST'])
def create_department():
    data = request.get_json()
    department = Department(name=data['name'], description=data.get('description', ''))
    db.session.add(department)
    db.session.commit()
    return jsonify({"message": "Département créé avec succès"}), 201

@department_bp.route('/', methods=['GET'])
def get_departments():
    departments = Department.query.all()
    return jsonify([{"id": d.id, "name": d.name, "description": d.description} for d in departments])

@department_bp.route('/<int:id>', methods=['GET'])
def get_department(id):
    d = Department.query.get_or_404(id)
    return jsonify({"id": d.id, "name": d.name, "description": d.description})

@department_bp.route('/<int:id>', methods=['PUT'])
def update_department(id):
    d = Department.query.get_or_404(id)
    data = request.get_json()
    d.name = data.get('name', d.name)
    d.description = data.get('description', d.description)
    db.session.commit()
    return jsonify({"message": "Département mis à jour"})

@department_bp.route('/<int:id>', methods=['DELETE'])
def delete_department(id):
    d = Department.query.get_or_404(id)
    db.session.delete(d)
    db.session.commit()
    return jsonify({"message": "Département supprimé"})
