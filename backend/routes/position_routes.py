from flask import Blueprint, request, jsonify
from extensions import db
from models.position import Position

position_bp = Blueprint('position_bp', __name__, url_prefix='/api/positions')

@position_bp.route('/', methods=['POST'])
def create_position():
    data = request.get_json()
    position = Position(title=data['title'], description=data.get('description', ''))
    db.session.add(position)
    db.session.commit()
    return jsonify({"message": "Poste créé avec succès"}), 201

@position_bp.route('/', methods=['GET'])
def get_positions():
    positions = Position.query.all()
    return jsonify([{"id": p.id, "title": p.title, "description": p.description} for p in positions])

@position_bp.route('/<int:id>', methods=['GET'])
def get_position(id):
    p = Position.query.get_or_404(id)
    return jsonify({"id": p.id, "title": p.title, "description": p.description})

@position_bp.route('/<int:id>', methods=['PUT'])
def update_position(id):
    p = Position.query.get_or_404(id)
    data = request.get_json()
    p.title = data.get('title', p.title)
    p.description = data.get('description', p.description)
    db.session.commit()
    return jsonify({"message": "Poste mis à jour"})

@position_bp.route('/<int:id>', methods=['DELETE'])
def delete_position(id):
    p = Position.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify({"message": "Poste supprimé"})
