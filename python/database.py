
import sqlite3
from pathlib import Path

# Localizacao do banco de dados
BASE_DIR = Path(__file__).resolve().parent.parent
PASTA_DATA = BASE_DIR / "data"
BANCO_DADOS = PASTA_DATA / "flowhome.db"


def conectar():
    PASTA_DATA.mkdir(parents=True, exist_ok=True)

    conexao = sqlite3.connect(BANCO_DADOS)

    return conexao


def criar_tabela():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS medicoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                temperatura REAL NOT NULL,
                umidade REAL NOT NULL,
                data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

    print("Banco de dados e tabela preparados.")


def salvar_medicao(temperatura, umidade):
    with conectar() as conexao:
        conexao.execute("""
            INSERT INTO medicoes (temperatura, umidade)
            VALUES (?, ?)
        """, (temperatura, umidade))


if __name__ == "__main__":
    criar_tabela()
