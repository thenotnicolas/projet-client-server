from flask import Flask, render_template,request
import requests
app = Flask(__name__)

# Rota raiz
@app.route('/')
def index():
    return render_template('index.html')

# Rota para cadastro de usuários
@app.route('/users', methods=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        # Lógica de comunicação com o servidor Flask do server.py
        response = requests.post('http://localhost:5000/users', json={'nome': nome, 'email': email, 'senha': senha})
        print(response.text)

    return render_template('users.html')

# Rota para login
@app.route('/login', methods=['GET', 'POST'])
def fazer_login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Lógica de comunicação com o servidor Flask do server.py
        response = requests.post('http://localhost:5000/login', json={'email': email, 'senha': senha})
        print(response.text)

    return render_template('login.html')

# Rota para logout
@app.route('/logout')
def fazer_logout():
    # Lógica de comunicação com o servidor Flask do server.py
    response = requests.get('http://localhost:5000/logout')
    print(response.text)
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(port=5001,debug=True)