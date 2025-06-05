from flask import Blueprint, request, jsonify
from extensions import db
from models.employee import Employee

employee_bp = Blueprint('employee_bp', __name__, url_prefix='/api/employees')

# CREATE - Ajouter un employé
@employee_bp.route('/', methods=['POST'])
def create_employee():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Données manquantes"}), 400

    employee = Employee(
        full_name=data.get('full_name'),
        email=data.get('email'),
        phone=data.get('phone'),
        hire_date=data.get('hire_date'),
        department_id=data.get('department_id'),
        position_id=data.get('position_id')
    )

    db.session.add(employee)
    db.session.commit()

    return jsonify({"message": "Employé ajouté avec succès", "id": employee.id}), 201

# READ - Obtenir la liste de tous les employés
@employee_bp.route('/', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    result = []
    for emp in employees:
        result.append({
            "id": emp.id,
            "full_name": emp.full_name,
            "email": emp.email,
            "phone": emp.phone,
            "hire_date": emp.hire_date.isoformat() if emp.hire_date else None,
            "department_id": emp.department_id,
            "position_id": emp.position_id
        })
    return jsonify(result), 200

# READ - Obtenir un employé par ID
@employee_bp.route('/<int:id>', methods=['GET'])
def get_employee(id):
    emp = Employee.query.get_or_404(id)
    return jsonify({
        "id": emp.id,
        "full_name": emp.full_name,
        "email": emp.email,
        "phone": emp.phone,
        "hire_date": emp.hire_date.isoformat() if emp.hire_date else None,
        "department_id": emp.department_id,
        "position_id": emp.position_id
    }), 200

# UPDATE - Modifier un employé par ID
@employee_bp.route('/<int:id>', methods=['PUT'])
def update_employee(id):
    emp = Employee.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return jsonify({"error": "Données manquantes"}), 400

    emp.full_name = data.get('full_name', emp.full_name)
    emp.email = data.get('email', emp.email)
    emp.phone = data.get('phone', emp.phone)
    emp.hire_date = data.get('hire_date', emp.hire_date)
    emp.department_id = data.get('department_id', emp.department_id)
    emp.position_id = data.get('position_id', emp.position_id)

    db.session.commit()

    return jsonify({"message": "Employé modifié avec succès"}), 200

# DELETE - Supprimer un employé par ID
@employee_bp.route('/<int:id>', methods=['DELETE'])
def delete_employee(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    return jsonify({"message": "Employé supprimé avec succès"}), 200
