# 🛡️ Dashboard de Segurança Cibernética no Brasil (2015–2024)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-success)]()

Um painel analítico e interativo desenvolvido em **Python** e **Streamlit** para visualização e monitoramento de métricas históricas de incidentes de segurança da informação, tipos de ameaças, vulnerabilidades exploradas e impactos financeiros no Brasil entre 2015 e 2024.

---

## 📌 Sumário
- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades e Métricas](#-funcionalidades-e-métricas)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Como Executar o Projeto](#-como-executar-o-projeto)
- [Insights dos Dados](#-principais-insights)
- [Autor](#-autor)

---

## 📖 Sobre o Projeto

Com o crescimento acelerado da transformação digital e a sofisticação das ameaças virtuais, a análise de dados em cibersegurança torna-se indispensável para a tomada de decisões estratégicas. 

Este projeto consolida dados temporais e setoriais de ciberataques no cenário brasileiro, proporcionando uma interface intuitiva e interativa voltada para gestores de TI, analistas de SOC e profissionais de segurança da informação.

---

## 📊 Funcionalidades e Métricas

O dashboard oferece uma visão 360° dividida nas seguintes dimensões:

1. **🔵 Visão Geral Nacional:**
   - **Histórico Anual de Ataques (2015–2024):** Linha de tendência do volume de incidentes reportados.
   - **Impacto Financeiro:** Gráficos de barras e linhas com o prejuízo acumulado anual (em milhões de USD).
   - **Setores Mais Afetados:** Distribuição de incidentes por verticais de mercado (*Saúde, TI, Bancos, Educação*).

2. **🇧🇷 Tipos de Ataque no Brasil:**
   - Comparativo de incidência entre os principais vetores: *DDoS, SQL Injection, Phishing e Malware*.

3. **🔓 Falhas e Vulnerabilidades Mais Exploradas:**
   - Ranking de pontos críticos de entrada: *Zero-day, Senhas fracas e Engenharia social*.

4. **🗺️ Distribuição Geográfica por Estado:**
   - Análise regionalizada por Unidades Federativas (*SP, RJ, MG, BA, RS*) detalhando o mix de ataques sofridos e volume consolidado em tabela de dados interativa.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.9+
- **Frontend / Framework Web:** [Streamlit](https://streamlit.io/)
- **Visualização de Dados:** [Plotly Express](https://plotly.com/python/) / Matplotlib
- **Processamento e Análise de Dados:** [Pandas](https://pandas.pydata.org/)

---

## 📁 Estrutura do Repositório

```text
cybersecurity-brazil-dashboard/
├── app.py              # Aplicação principal Streamlit
├── requirements.txt    # Dependências do projeto
├── README.md           # Documentação do projeto
└── assets/             # Gráficos e capturas de tela
