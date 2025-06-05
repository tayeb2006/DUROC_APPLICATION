from extensions import db

class EmployeeProject(db.Model):
    __tablename__ = 'employee_project'

    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), primary_key=True)

    employee = db.relationship('Employee', back_populates='projects')
    project = db.relationship('Project', back_populates='employees')
