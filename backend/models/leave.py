from extensions import db

class Leave(db.Model):
    __tablename__ = 'leaves'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.Enum('en_attente', 'approuve', 'refuse', name='leave_status'), default='en_attente')
    reason = db.Column(db.Text)
