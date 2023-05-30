from flask import Flask, request

app = Flask(__name__)

# Rota raiz
@app.route('/')
def index():
    return """
    <h1>Comunicação Cliente-Servidor</h1>
    <ul>
        <li><a href="/users">Cadastro de Usuários</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/logout">Logout</a></li>
    </ul>
    """

# Rota para cadastro de usuários
@app.route('/users', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json()
    nome = data['nome']
    email = data['email']
    senha = data['senha']

    # Operações de cadastro no banco de dados
    # ...

    print(f'Novo usuário cadastrado: {nome} - {email} - {senha}')
    return 'Usuário cadastrado com sucesso!'


# Rota para login
@app.route('/login', methods=['POST'])
def fazer_login():
    data = request.get_json()
    email = data['email']
    senha = data['senha']

    # Operações de login
    # ...

    print(f'Login realizado: {email}, {senha}')
    return 'Login realizado com sucesso!'

# Rota para logout
@app.route('/logout', methods=['GET'])
def fazer_logout():
    print('Logout realizado')
    return 'Logout realizado com sucesso!'

if __name__ == '__main__':
    app.run(port=5000,debug=True)
