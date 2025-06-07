from flask import Blueprint, jsonify
from extensions import db
from models.department import Department
from models.project import Project
from models.salary import Salary
from sqlalchemy import func
from datetime import datetime


stats_bp = Blueprint('stats_bp', __name__, url_prefix='/api/statistics')

@stats_bp.route('/employees-by-department', methods=['GET'])
def employees_by_department():
    # Nombre d'employés par département
    # On suppose que le modèle Employee existe et a un champ department_id
    result = db.session.execute("""
        SELECT d.name AS department_name, COUNT(e.id) AS employee_count
        FROM departments d
        LEFT JOIN employees e ON e.department_id = d.id
        GROUP BY d.name
    """).fetchall()
    
    data = [{"department": row.department_name, "count": row.employee_count} for row in result]
    return jsonify(data)

@stats_bp.route('/projects-distribution', methods=['GET'])
def projects_distribution():
    # Répartition du nombre d'employés par projet (on suppose table employee_project)
    result = db.session.execute("""
        SELECT p.name AS project_name, COUNT(ep.employee_id) AS employee_count
        FROM projects p
        LEFT JOIN employee_project ep ON ep.project_id = p.id
        GROUP BY p.name
    """).fetchall()
    
    data = [{"project": row.project_name, "count": row.employee_count} for row in result]
    return jsonify(data)

@stats_bp.route('/average-salary-evolution', methods=['GET'])
def average_salary_evolution():
    # Moyenne des salaires par mois (format YYYY-MM)
    result = db.session.execute("""
        SELECT TO_CHAR(start_date, 'YYYY-MM') AS month, AVG(amount) AS avg_salary
        FROM salaries
        GROUP BY month
        ORDER BY month
    """).fetchall()
    
    data = [{"month": row.month, "average_salary": float(row.avg_salary)} for row in result]
    return jsonify(data)
