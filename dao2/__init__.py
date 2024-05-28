import psycopg2
from psycopg2.extras import RealDictCursor


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

def listar_produtos():
    conexao = conectar_localBD()
    if conexao is None:
        return

    cursor = conexao.cursor(cursor_factory=RealDictCursor)
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)

    resultados = cursor.fetchall()
    conexao.close()
    return resultados

def cadastrar_produto(nome, marca, validade, preco, quantidade_disponivel , foto_caminho):
    conexao = conectar_localBD()
    if conexao is None:
        return

    cursor = conexao.cursor()

    sql = """
        INSERT INTO produtos (nome, marca, validade, preco, quantidade_disponivel , foto_caminho)
        VALUES (%s, %s, %s, %s, %s)
    """
    valores = (nome, marca, validade, preco, quantidade_disponivel , foto_caminho)
    cursor.execute(sql, valores)

    conexao.commit()
    conexao.close()

def editar_produto( nome, marca, validade, preco, quantidade_disponivel , foto_caminho):
    conexao = conectar_localBD()
    if conexao is None:
        return

    cursor = conexao.cursor()

    sql = """
        UPDATE produtos
        SET nome = %s, marca = %s, validade = %s, preco = %s, quantidade_disponivel = %s
        WHERE foto_caminho = %s
    """
    valores = (nome, marca, validade, preco, quantidade_disponivel, foto_caminho)
    cursor.execute(sql, valores)

    conexao.commit()
    conexao.close()
