from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurações do banco de dados 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

# Inicializando banco de dados
db = SQLAlchemy(app)

# Criando o model User para o banco de dados
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.nome}>'

# Página principal
@app.route('/')
def home():
    usuarios = User.query.all()
    return render_template('index.html', usuarios=usuarios)

if __name__ == '__main__':
    # Cria banco de dados quando inicia aplicação 
    with app.app_context():
        db.create_all()

    app.run(debug=True)