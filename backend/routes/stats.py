from flask import Blueprint, jsonify
from models.salary import Salary
from extensions import db
from sqlalchemy import extract, func
from flask_jwt_extended import jwt_required
from decorators import admin_required

stats_bp = Blueprint('stats_bp', __name__, url_prefix='/api/statistics')


@stats_bp.route('/average-salary-evolution', methods=['GET'])
@jwt_required()
@admin_required
def average_salary_evolution():
    results = db.session.query(
        extract('year', Salary.start_date).label('year'),
        func.avg(Salary.amount).label('average_salary')
    ).group_by('year').order_by('year').all()

    data = {str(year): float(avg) for year, avg in results}
    return jsonify(data)
