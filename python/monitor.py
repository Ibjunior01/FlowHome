
import serial
import time

from database import criar_tabela, salvar_medicao

PORTA = "COM4"
BAUD_RATE = 9600

arduino = None

print("=" * 45)
print("       FLOWHOME - MONITORAMENTO")
print("=" * 45)

try:
    # Prepara o banco de dados
    criar_tabela()

    # Conecta ao Arduino
    arduino = serial.Serial(
        port=PORTA,
        baudrate=BAUD_RATE,
        timeout=2
    )

    time.sleep(2)

    print(f"Arduino conectado: {PORTA}")
    print("Monitoramento iniciado...\n")

    while True:
        linha = arduino.readline().decode(
            "utf-8",
            errors="replace"
        ).strip()

        if not linha:
            continue

        if linha == "temperatura,umidade":
            continue

        try:
            temperatura, umidade = linha.split(",")

            temperatura = float(temperatura)
            umidade = float(umidade)

            # Salva a medicao no SQLite
            salvar_medicao(temperatura, umidade)

            print("-" * 40)
            print(f"Temperatura: {temperatura:.2f} °C")
            print(f"Umidade: {umidade:.2f} %")
            print("Status: Medicao salva no banco")

        except ValueError:
            print(f"Dados invalidos: {linha}")

except serial.SerialException as erro:
    print(f"Erro na comunicacao serial: {erro}")

except KeyboardInterrupt:
    print("\nMonitoramento encerrado pelo usuario.")

finally:
    if arduino and arduino.is_open:
        arduino.close()
        print("Conexao serial encerrada.")
