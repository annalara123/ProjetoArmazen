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

def listar_usuarios():
    conexao = conectar_localBD()
    cursor = conexao.cursor()
    sql = 'select * from usuarios '
    cursor.execute(sql)

    results =curso.fetchall()
    print(results)


def login(usuario,senha , tipo):
    conexao = conectar_localBD()
    cursor = conexao.cursor()
    sql = "select * from usuarios where email='{usuario}' , senha='{senha} and tipo'{tipo}'"
    cursor.execute(sql)

