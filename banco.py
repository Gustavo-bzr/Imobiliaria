
import sqlite3

ARQUIVO_BANCO = "imobiliaria.db"


def conectar():
    conexao = sqlite3.connect(ARQUIVO_BANCO)
    conexao.row_factory = sqlite3.Row  
    return conexao


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT,
            email TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS imoveis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            endereco TEXT NOT NULL,
            valor REAL NOT NULL,
            quartos INTEGER,
            status TEXT DEFAULT 'Disponível'
        )
    """)

    conexao.commit()
    conexao.close()



def listar_clientes(busca=""):
    termo = "%" + busca + "%"
    conexao = conectar()
    linhas = conexao.execute(
        """SELECT * FROM clientes
           WHERE nome LIKE ? OR cpf LIKE ? OR telefone LIKE ? OR email LIKE ?
           ORDER BY nome""",
        (termo, termo, termo, termo),
    ).fetchall()
    conexao.close()
    return [dict(linha) for linha in linhas]


def adicionar_cliente(nome, cpf, telefone, email):
    conexao = conectar()
    conexao.execute(
        "INSERT INTO clientes (nome, cpf, telefone, email) VALUES (?, ?, ?, ?)",
        (nome, cpf, telefone, email),
    )
    conexao.commit()
    conexao.close()


def modificar_cliente(id, nome, cpf, telefone, email):
    conexao = conectar()
    conexao.execute(
        "UPDATE clientes SET nome = ?, cpf = ?, telefone = ?, email = ? WHERE id = ?",
        (nome, cpf, telefone, email, id),
    )
    conexao.commit()
    conexao.close()


def excluir_cliente(id):
    conexao = conectar()
    conexao.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()



def listar_imoveis(busca="", tipo="", status=""):
    termo = "%" + busca + "%"
    conexao = conectar()
    linhas = conexao.execute(
        """SELECT * FROM imoveis
           WHERE endereco LIKE ?
             AND (? = '' OR tipo = ?)
             AND (? = '' OR status = ?)
           ORDER BY id DESC""",
        (termo, tipo, tipo, status, status),
    ).fetchall()
    conexao.close()
    return [dict(linha) for linha in linhas]


def adicionar_imovel(tipo, endereco, valor, quartos, status):
    conexao = conectar()
    conexao.execute(
        "INSERT INTO imoveis (tipo, endereco, valor, quartos, status) VALUES (?, ?, ?, ?, ?)",
        (tipo, endereco, valor, quartos, status),
    )
    conexao.commit()
    conexao.close()


def modificar_imovel(id, tipo, endereco, valor, quartos, status):
    conexao = conectar()
    conexao.execute(
        "UPDATE imoveis SET tipo = ?, endereco = ?, valor = ?, quartos = ?, status = ? WHERE id = ?",
        (tipo, endereco, valor, quartos, status, id),
    )
    conexao.commit()
    conexao.close()


def excluir_imovel(id):
    conexao = conectar()
    conexao.execute("DELETE FROM imoveis WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
