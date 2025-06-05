from app import app, db

with app.app_context():
    db.create_all()
    print("Base de données et tables créées avec succès !")
