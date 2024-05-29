import psycopg2
from psycopg2.extras import RealDictCursor
import hashlib


def conectarDB():
    return conectar_localBD()

def conectar_localBD():
    try:
        con = psycopg2.connect(
            host="localhost",
            database="projeto_de_rene",
            user="postgres",
            password="12345"
        )
        return con
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def listar_usuarios():
    conexao = conectar_localBD()
    if conexao is None:
        return

    cursor = conexao.cursor(cursor_factory=RealDictCursor)
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)

    resultados = cursor.fetchall()
    conexao.close()
    return resultados


print(listar_usuarios())
def cadastrar_usuario(nome, email, senha, tipo):
    conexao = conectar_localBD()
    if conexao is None:
        return

    cursor = conexao.cursor()

    senha_criptografada = hashlib.sha256(senha.encode('utf-8')).hexdigest()

    sql = """
        INSERT INTO usuarios (nome, email, senha, tipo)
        VALUES (%s, %s, %s, %s)
    """
    valores = (nome, email, senha_criptografada, tipo)
    cursor.execute(sql, valores)

    conexao.commit()
    conexao.close()

def logar_usuario(email, senha, tipo):
    conexao = conectar_localBD()
    if conexao is None:
        return None

    cursor = conexao.cursor(cursor_factory=RealDictCursor)


    senha_criptografada = hashlib.sha256(senha.encode('utf-8')).hexdigest()

    sql = """
        SELECT * FROM usuarios
        WHERE email = %s AND senha = %s AND tipo = %s
    """
    valores = (email, senha_criptografada, tipo)
    cursor.execute(sql, valores)

    usuario = cursor.fetchone()
    conexao.close()
    return usuario

def get_tipo_usuario():
    conexao = conectar_localBD()
    if conexao is None:
        return None

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE tipo = %s", ('Admin',))
        resultado = cursor.fetchone()
        return resultado
    finally:
        conexao.close()

def deletar_usuario(email):
    conexao = conectar_localBD()
    if conexao is None:
        return

    cursor = conexao.cursor()

    sql = "DELETE FROM usuarios WHERE email = %s"
    cursor.execute(sql, (email,))

    conexao.commit()
    conexao.close()
