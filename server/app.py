from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurare bază de date in-memory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelul Task (pentru TODO-uri)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    completed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return "Lab6 Backend Server"

# TODO 1: Endpoint pentru a adăuga un task nou (POST)
@app.route('/tasks', methods=['POST'])
def add_task():
    """Adaugă un task nou în baza de date."""
    # Logica pentru a adăuga un task nou va fi aici
    pass

# TODO 2: Endpoint pentru a obține toate task-urile (GET)
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    """Obține toate task-urile din baza de date."""
    # Logica pentru a returna toate task-urile va fi aici
    pass

# TODO 3: Endpoint pentru a obține un task după id (GET)
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Obține un task pe baza ID-ului."""
    # Logica pentru a obține un task după id va fi aici
    pass

# TODO 4: Endpoint pentru a actualiza un task (PUT)
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Actualizează un task existent."""
    # Logica pentru a actualiza un task va fi aici
    pass

# TODO 5: Endpoint pentru a șterge un task (DELETE)
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Șterge un task pe baza ID-ului."""
    # Logica pentru a șterge un task va fi aici
    pass

# TODO 6: Endpoint pentru a marca un task ca finalizat (PATCH)
@app.route('/tasks/<int:task_id>/complete', methods=['PATCH'])
def complete_task(task_id):
    """Marchează un task ca finalizat."""
    # Logica pentru a marca un task ca finalizat va fi aici
    pass

# TODO 7: Validare date la crearea unui task nou
# (de ex. câmpul title să fie obligatoriu) - implementare în cadrul funcției add_task()

# TODO 8: Adăugare filtrare pentru task-uri finalizate vs nefinalizate (GET cu parametru)
@app.route('/tasks/filter', methods=['GET'])
def filter_tasks():
    """Filtrare task-uri după status (completed sau nu)."""
    # Logica pentru a filtra task-urile va fi aici
    pass

# TODO 9: Adăugare suport pentru paginare la obținerea task-urilor (GET cu paginare)
@app.route('/tasks/paginate', methods=['GET'])
def paginate_tasks():
    """Paginare pentru obținerea task-urilor."""
    # Logica pentru a implementa paginarea va fi aici
    pass

# TODO 10: Implementare căutare după titlul sau descrierea task-urilor (GET cu căutare)
@app.route('/tasks/search', methods=['GET'])
def search_tasks():
    """Căutare task-uri după titlu sau descriere."""
    # Logica pentru a implementa căutarea va fi aici
    pass

if __name__ == '__main__':
    app.run(debug=True)
