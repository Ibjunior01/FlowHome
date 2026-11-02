# FlowHome

**Sistema de monitoramento ambiental para automação residencial utilizando Arduino, Python e IoT.**

O FlowHome é um projeto experimental de automação residencial desenvolvido para integrar hardware e software, permitindo a coleta, o processamento, o armazenamento e a visualização de dados ambientais.

A primeira etapa do projeto consiste no monitoramento de temperatura e umidade utilizando um sensor DHT11 conectado a um Arduino UNO R3.

## Objetivo do projeto

Desenvolver uma base tecnológica para automação residencial, explorando a integração entre sensores, microcontroladores, aplicações Python, bancos de dados e interfaces de monitoramento.

## Tecnologias utilizadas

| Tecnologia     | Aplicação                       |
| -------------- | ------------------------------- |
| Arduino UNO R3 | Leitura do sensor               |
| C++            | Programação do Arduino          |
| DHT11          | Sensor de temperatura e umidade |
| Python         | Processamento dos dados         |
| PySerial       | Comunicação serial              |
| SQLite         | Armazenamento dos dados         |
| Pandas         | Manipulação dos dados           |
| Streamlit      | Dashboard interativo            |
| Git e GitHub   | Controle de versão              |

## Arquitetura do sistema

```text
       SENSOR DHT11
             |
             v
        ARDUINO UNO
          (C++)
             |
             v
       COMUNICAÇÃO USB
        SERIAL / CSV
             |
             v
           PYTHON
             |
       +-----+-----+
       |           |
       v           v
    SQLITE      PROCESSAMENTO
       |           |
       +-----+-----+
             |
             v
       STREAMLIT
        DASHBOARD
```

## Componentes utilizados

- Arduino UNO R3
- Sensor DHT11 de três pinos
- Protoboard
- Jumpers
- Cabo USB para comunicação com o computador

## Montagem do circuito

O sensor DHT11 é conectado diretamente ao Arduino UNO R3.

| DHT11    | Arduino UNO R3 |
| -------- | -------------- |
| GND (-)  | GND            |
| VCC (V)  | 5V             |
| DATA (S) | Digital D2     |

**Atenção:** confira as identificações dos terminais do módulo antes de realizar as conexões.

## Estrutura do projeto

```text
FlowHome/
│
├── firmware/
│   └── FlowHome_DHT11.ino
│
├── python/
│   ├── consultar_dados.py
│   ├── dashboard.py
│   ├── database.py
│   └── monitor.py
│
├── data/
│   └── flowhome.db
│
├── .gitignore
├── requirements.txt
└── README.md
```

O banco de dados é criado localmente durante a execução e não é versionado no GitHub.

## Configuração e instalação

### 1. Requisitos

- Windows 10 ou 11
- Python instalado
- Arduino IDE
- Git

### 2. Bibliotecas do Arduino

Instale pela Library Manager da Arduino IDE:

- DHT sensor library (Adafruit)
- Adafruit Unified Sensor

### 3. Bibliotecas Python

Na pasta raiz do projeto, execute:

```powershell
python -m pip install -r requirements.txt
```

### 4. Configuração da porta serial

No arquivo `python/monitor.py`, configure a porta COM correspondente ao Arduino:

```python
PORTA = "COM4"
BAUD_RATE = 9600
```

A porta COM pode variar conforme o computador e a conexão USB.

### 5. Enviar o firmware

Abra `firmware/FlowHome_DHT11.ino` na Arduino IDE.

Selecione:

- Placa: Arduino UNO
- Porta: porta COM do Arduino

Compile e envie o código para a placa.

Feche o Serial Monitor da Arduino IDE antes de executar o monitor Python.

## Executando o sistema

O sistema utiliza dois processos simultâneos.

**Terminal 1 — Monitoramento e armazenamento**

Na pasta raiz do projeto:

```powershell
python python/monitor.py
```

O programa recebe os dados do Arduino, interpreta as leituras e registra as medições no SQLite.

**Terminal 2 — Dashboard**

Em outro terminal:

```powershell
python -m streamlit run python/dashboard.py
```

O Streamlit disponibilizará o dashboard no navegador, normalmente em:

http://localhost:8501

O painel apresenta:

- Temperatura atual.
- Umidade atual.
- Quantidade de medições armazenadas.
- Gráfico histórico de temperatura.
- Gráfico histórico de umidade.
- Histórico das medições.

A interface possui atualização automática periódica.

## Funcionalidades implementadas

- [x] Leitura de temperatura e umidade com DHT11.
- [x] Comunicação serial entre Arduino e Python.
- [x] Processamento dos dados recebidos.
- [x] Armazenamento em banco SQLite.
- [x] Consulta ao histórico de medições.
- [x] Dashboard interativo com Streamlit.
- [x] Atualização automática do painel.

## Próximas etapas

- [ ] Melhorar o tratamento de falhas de comunicação.
- [ ] Implementar monitoramento de múltiplos sensores.
- [ ] Desenvolver uma API para integração com outros sistemas.
- [ ] Explorar integração com Home Assistant.
- [ ] Integrar automações utilizando n8n.
- [ ] Desenvolver funcionalidades de inteligência artificial.
- [ ] Expandir o projeto para outros dispositivos de automação residencial.

## Observações

Este projeto está em desenvolvimento e possui finalidade experimental e educacional.

O sensor DHT11 apresenta limitações de precisão, sendo utilizado nesta primeira etapa para validar a arquitetura de comunicação, processamento e armazenamento de dados.

---

**FlowHome — Conectando hardware, software e automação residencial.**
