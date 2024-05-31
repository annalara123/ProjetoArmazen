from flask import *

import dao2
from dao import *
from dao2 import *

app = Flask(__name__)
app.secret_key = "jk2h3kj23hrk2h5"
app.config['UPLOAD_FOLDER'] = 'static/imagens/'

@app.route("/login", methods=['GET', 'POST']) # decorator
def minhaPag():
    if request.method == 'POST':
        email = request.form.get['email']
        password = request.form.get['senha']
        usuario = logar_usuario(email, password)

        if usuario:
            session['email'] = usuario['email']
            return render_template('/menu')
        else:
            texto = 'login ou senha incorretos'
            return render_template('login.html', aviso=texto)
    else:
        return render_template('login.html')
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get['nome']
        email = request.form.get['email']
        senha = request.form.get['password']
        tipo = request.form.get['tipo']

        cadastrar_usuario(nome, email, senha, tipo)

        texto = 'Cadastro realizado com sucesso!'
        return render_template('login.html', aviso=texto)
    else:
        return render_template('cadastro.html')

@app.route('/sair')
def logout():
    session.pop('username', None)
    response = make_response('Você foi desconectado.')
    response.set_cookie('username', '', max_age=0)
    return render_template('login.html', response=response)

@app.route('/menu')
def menu():
    return render_template('menu.html')
@app.route('/meuPerfil')
def perfil():
    return render_template('perfil.html')

@app.route('/listarProdutos', methods= ['GET'])
def produtos():
    if session.get('email') != None:
        result = dao2.listar_produtos(0)
        return render_template('produtos.html', produtos=result, meuemail=session.get('email'))
    else:
        return 'Sem produtos'
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