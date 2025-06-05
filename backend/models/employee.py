from extensions import db

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    hire_date = db.Column(db.Date)

    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    position_id = db.Column(db.Integer, db.ForeignKey('positions.id'))

    department = db.relationship('Department', back_populates='employees')
    position = db.relationship('Position', back_populates='employees')
    salaries = db.relationship('Salary', backref='employee', lazy=True)
    leaves = db.relationship('Leave', backref='employee', lazy=True)
    projects = db.relationship('EmployeeProject', back_populates='employee')
    user = db.relationship('User', backref='employee', uselist=False)
