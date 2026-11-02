
import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh


# Configuracao do projeto
BASE_DIR = Path(__file__).resolve().parent.parent
BANCO_DADOS = BASE_DIR / "data" / "flowhome.db"

st.set_page_config(
    page_title="FlowHome | Monitoramento",
    page_icon="🏠",
    layout="wide"
)

# Atualiza o dashboard a cada 5 segundos
st_autorefresh(
    interval=5000,
    key="flowhome_atualizacao"
)


def carregar_dados():
    with sqlite3.connect(BANCO_DADOS) as conexao:
        df = pd.read_sql_query("""
            SELECT
                id,
                temperatura,
                umidade,
                data_hora
            FROM medicoes
            ORDER BY id DESC
            
        """, conexao)

    if not df.empty:
        df["data_hora"] = pd.to_datetime(df["data_hora"])
        df = df.sort_values("data_hora")

    return df


# Interface
st.title("FlowHome")
st.caption("Sistema de monitoramento ambiental")

if not BANCO_DADOS.exists():
    st.error("Banco de dados nao encontrado.")
    st.stop()

dados = carregar_dados()

if dados.empty:
    st.warning("Nenhuma medicao encontrada.")
    st.stop()

# Ultima medicao
ultima = dados.iloc[-1]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Temperatura atual",
        f"{ultima['temperatura']:.2f} °C"
    )

with col2:
    st.metric(
        "Umidade atual",
        f"{ultima['umidade']:.2f} %"
    )

with col3:
    st.metric(
        "Total de mediçoes",
        len(dados)
    )

st.divider()

# Graficos
st.subheader("Historico de temperatura")

grafico_temperatura = dados.set_index("data_hora")[["temperatura"]]

st.line_chart(grafico_temperatura)

st.subheader("Historico de umidade")

grafico_umidade = dados.set_index("data_hora")[["umidade"]]

st.line_chart(grafico_umidade)

st.divider()

# Historico tabular
st.subheader("Ultimas medicoes")

historico = dados.sort_values("id", ascending=False).copy()

historico["data_hora"] = historico["data_hora"].dt.strftime(
    "%d/%m/%Y %H:%M:%S"
)

st.dataframe(
    historico,
    use_container_width=True,
    hide_index=True
)

st.caption("FlowHome | Monitoramento com Arduino, Python e SQLite")
