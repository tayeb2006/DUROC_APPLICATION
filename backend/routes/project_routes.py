from flask import Blueprint, request, jsonify
from extensions import db
from models.project import Project

project_bp = Blueprint('project_bp', __name__, url_prefix='/api/projects')

@project_bp.route('/', methods=['POST'])
def create_project():
    data = request.get_json()
    project = Project(name=data['name'], description=data.get('description', ''))
    db.session.add(project)
    db.session.commit()
    return jsonify({"message": "Projet créé avec succès"}), 201

@project_bp.route('/', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([{"id": p.id, "name": p.name, "description": p.description} for p in projects])

@project_bp.route('/<int:id>', methods=['GET'])
def get_project(id):
    p = Project.query.get_or_404(id)
    return jsonify({"id": p.id, "name": p.name, "description": p.description})

@project_bp.route('/<int:id>', methods=['PUT'])
def update_project(id):
    p = Project.query.get_or_404(id)
    data = request.get_json()
    p.name = data.get('name', p.name)
    p.description = data.get('description', p.description)
    db.session.commit()
    return jsonify({"message": "Projet mis à jour"})

@project_bp.route('/<int:id>', methods=['DELETE'])
def delete_project(id):
    p = Project.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify({"message": "Projet supprimé"})
