
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BANCO_DADOS = BASE_DIR / "data" / "flowhome.db"

conexao = sqlite3.connect(BANCO_DADOS)

cursor = conexao.cursor()

cursor.execute("""
    SELECT
        id,
        temperatura,
        umidade,
        data_hora
    FROM medicoes
    ORDER BY id DESC
    LIMIT 10
""")

registros = cursor.fetchall()

print("\n========== FLOWHOME ==========")
print("       HISTORICO DE MEDICOES")
print("==============================\n")

for registro in registros:
    id_medicao, temperatura, umidade, data_hora = registro

    print(f"ID: {id_medicao}")
    print(f"Temperatura: {temperatura:.2f} °C")
    print(f"Umidade: {umidade:.2f} %")
    print(f"Data/Hora: {data_hora}")
    print("-" * 35)

print(f"\nTotal de registros exibidos: {len(registros)}")

conexao.close()
