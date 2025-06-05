from flask import Blueprint, request, jsonify
from extensions import db
from models.salary import Salary

salary_bp = Blueprint('salary_bp', __name__, url_prefix='/api/salaries')

@salary_bp.route('/', methods=['POST'])
def create_salary():
    data = request.get_json()
    salary = Salary(
        employee_id=data['employee_id'],
        amount=data['amount'],
        start_date=data['start_date'],
        end_date=data.get('end_date', None)
    )
    db.session.add(salary)
    db.session.commit()
    return jsonify({"message": "Salaire créé avec succès"}), 201

@salary_bp.route('/', methods=['GET'])
def get_salaries():
    salaries = Salary.query.all()
    return jsonify([{
        "id": s.id,
        "employee_id": s.employee_id,
        "amount": s.amount,
        "start_date": str(s.start_date),
        "end_date": str(s.end_date) if s.end_date else None
    } for s in salaries])

@salary_bp.route('/<int:id>', methods=['GET'])
def get_salary(id):
    s = Salary.query.get_or_404(id)
    return jsonify({
        "id": s.id,
        "employee_id": s.employee_id,
        "amount": s.amount,
        "start_date": str(s.start_date),
        "end_date": str(s.end_date) if s.end_date else None
    })

@salary_bp.route('/<int:id>', methods=['PUT'])
def update_salary(id):
    s = Salary.query.get_or_404(id)
    data = request.get_json()
    s.amount = data.get('amount', s.amount)
    s.start_date = data.get('start_date', s.start_date)
    s.end_date = data.get('end_date', s.end_date)
    db.session.commit()
    return jsonify({"message": "Salaire mis à jour"})

@salary_bp.route('/<int:id>', methods=['DELETE'])
def delete_salary(id):
    s = Salary.query.get_or_404(id)
    db.session.delete(s)
    db.session.commit()
    return jsonify({"message": "Salaire supprimé"})
