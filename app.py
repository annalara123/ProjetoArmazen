from flask import *
from dao import *
from dao2 import *

app = Flask(__name__)
app.secret_key = "jk2h3kj23hrk2h5"

@app.route("/") #decorator
def minhaPag():
    return render_template('login.html')

@app.route('/loginDeUsuario', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    usuario = logar_usuario(email, password)

    if usuario:
        session['username'] = usuario['email']
        return render_template('menu.html')
    else:
        texto = 'login ou senha incorretos'
        return render_template('login.html', aviso=texto)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('password')
    tipo = request.form.get('tipo')

    cadastrar_usuario(nome, email, senha, tipo)

    texto = 'Cadastro realizado com sucesso!'
    return render_template('login.html', aviso=texto)

@app.route('/menu')
def menu():
    tipo_usuario = get_tipo_usuario()  # assume this function returns the tipo of the current user
    if tipo_usuario == "Admin":
        mostrar_controle_de_usuarios = True
    else:
        mostrar_controle_de_usuarios = False

    return render_template('menu.html', mostrar_controle_de_usuarios=mostrar_controle_de_usuarios)
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
    produtos = listar_produtos()
    return render_template('produtos.html', produtos=produtos)
@app.route('/cadastroProdutos', methods=['GET', 'POST'])
def cadastroProdutos():
    if request.method == 'POST':
        nome = request.form['nome']
        marca = request.form['marca']
        validade = request.form['validade']
        preco = request.form['preco']
        quantidade_disponivel = request.form['quantidade_disponivel']
        foto_caminho = request.files['foto_caminho']

        cadastrar_produto(nome, marca, validade, preco, quantidade_disponivel, foto_caminho)

        return 'Produto cadastrado com sucesso!'
    else:
        return render_template('cadastroProdutos.html')


if __name__ == '__main__':
	app.run(debug=True)