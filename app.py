from flask import *

app = Flask(__name__)
app.secret_key = "jk2h3kj23hrk2h5"

@app.route("/") #decorator
def minhaPag():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == "admin" and password == "senha123":
        session ['username'] = username
        return render_template('menu.html')
    else:
        texto = 'login ou senha incorretos'
        return render_template('login.html', aviso=texto)
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    username = request.form['username']
    password = request.form['password']
    foto = request.files['foto']
    texto = 'Cadastro realizado com sucesso!'
    return render_template('login.html', aviso=texto)

@app.route('/menu')
def menu():
    return render_template('menu.html')
@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/sair')
def logout():
    session.pop('username', None)
    response = make_response('Você foi desconectado.')
    response.set_cookie('username', '', max_age=0)
    return render_template('login.html', response=response)


@app.route('/produtos')
def produtos():
    produtos = [
        {"nome": "Product 1", "imagem": "product1.jpg"},
        {"nome": "Product 2", "imagem": "product2.jpg"},

    ]
    return render_template('produtos.html', produtos=produtos)

if __name__ == '__main__':
	app.run(debug=True)