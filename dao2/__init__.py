import psycopg2
from psycopg2.extras import RealDictCursor

def conectarDB():
    return conectar_localBD()

def conectar_localBD():
    con = psycopg2.connect(
        host= 'localhost',
        database= 'projeto_de_rene',
        user= 'postgres',
        password= '12345'
    )
    return con


def listar_produtos():
    conexao = conectar_localBD()
    cursor = conexao.cursor()
    sql = 'select * from produtos '
    cursor.execute(sql)

    results = cursor.fetchall()
    print(results())


def produtos(nome,marca ,validade , preco , quantidade_dispónivel):
    conexao = conectar_localBD()
    cursor = conexao.cursor()
    sql = "select * from produtos where nome='{nome}' , marca='{marca}', validade='{validade}', preco='{preco}', quantidade_dispónive='{ quantidade_dispónive}'"
    cursor.execute(sql)