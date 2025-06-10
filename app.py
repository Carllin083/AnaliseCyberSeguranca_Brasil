import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard de Segurança Cibernética", layout="wide")
st.title("📊 Dashboard de Segurança Cibernética no Brasil (2015–2024)")

# Dados Nacionais
st.header("🔵 Visão Geral Nacional")

# Número de ataques por ano
ataques_ano = pd.DataFrame({
    "Ano": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Ataques": [30, 28, 37, 29, 26, 31, 34, 25, 30, 35]
})
fig1 = px.line(ataques_ano, x="Ano", y="Ataques", title="Número de Ataques por Ano", markers=True)
st.plotly_chart(fig1, use_container_width=True)

# Impacto financeiro
impacto_financeiro = pd.DataFrame({
    "Ano": [2019, 2020, 2021, 2022, 2023, 2024],
    "Prejuízo (milhões USD)": [1183.03, 1500.00, 1977.69, 1600.00, 1700.00, 1844.04]
})
fig2 = px.bar(impacto_financeiro, x="Ano", y="Prejuízo (milhões USD)", title="Prejuízo Financeiro por Ano")
st.plotly_chart(fig2, use_container_width=True)

# Gráfico de linha do prejuízo financeiro
fig2_line = px.line(impacto_financeiro, x="Ano", y="Prejuízo (milhões USD)", title="Evolução do Prejuízo Financeiro", markers=True)
st.plotly_chart(fig2_line, use_container_width=True)

# Indústrias mais afetadas
industrias = pd.DataFrame({
    "Setor": ["Saúde", "TI", "Bancos", "Educação"],
    "Ataques": [50, 50, 47, 47]
})
fig3 = px.pie(industrias, names="Setor", values="Ataques", title="Setores Mais Afetados")
st.plotly_chart(fig3, use_container_width=True)

# Tipos de ataque no Brasil
st.header("🇧🇷 Tipos de Ataque no Brasil")
tipos_ataque = pd.DataFrame({
    "Tipo de Ataque": ["DDoS", "SQL Injection", "Phishing", "Malware"],
    "Ocorrências": [61, 57, 54, 51]
})
fig4 = px.bar(tipos_ataque, x="Tipo de Ataque", y="Ocorrências", title="Principais Tipos de Ataque no Brasil")
st.plotly_chart(fig4, use_container_width=True)

# Vulnerabilidades exploradas
st.header("🔓 Vulnerabilidades Mais Exploradas")
vulnerabilidades = pd.DataFrame({
    "Vulnerabilidade": ["Zero-day", "Senhas fracas", "Engenharia social"],
    "Ataques": [85, 82, 81]
})
fig5 = px.bar(vulnerabilidades, x="Vulnerabilidade", y="Ataques", title="Falhas de Segurança Mais Utilizadas")
st.plotly_chart(fig5, use_container_width=True)

# Dados por estado - template
st.header("🗺️ Ataques por Estado ")
dados_estaduais = pd.DataFrame({
    "Estado": ["SP", "RJ", "MG", "BA", "RS"],
    "DDoS": [10, 7, 6, 5, 4],
    "SQL Injection": [8, 6, 5, 4, 3],
    "Phishing": [9, 6, 5, 4, 3],
    "Malware": [7, 5, 4, 3, 2]
})
dados_estaduais["Total de Ataques"] = dados_estaduais.iloc[:, 1:].sum(axis=1)
fig6 = px.bar(dados_estaduais, x="Estado", y="Total de Ataques", title="Total de Ataques por Estado")
st.plotly_chart(fig6, use_container_width=True)

st.dataframe(dados_estaduais)