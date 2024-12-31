from app import create_app, db
from app.models import VisitorIP

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crée les tables si elles n'existent pas
    app.run(debug=True)
