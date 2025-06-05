from extensions import db

class Salary(db.Model):
    __tablename__ = 'salaries'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    amount = db.Column(db.Numeric(10, 2))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
