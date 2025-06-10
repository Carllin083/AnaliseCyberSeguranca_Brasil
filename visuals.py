import plotly.express as px

def plot_ataques_ano(df):
    fig = px.line(df, x="Ano", y="Ataques", markers=True, title="Número de Ataques Cibernéticos por Ano")
    fig.update_traces(text=df["Ataques"], textposition="top center")
    fig.update_layout(yaxis_title="Número de Ataques", xaxis_title="Ano")
    return fig

def plot_prejuizos(df):
    fig = px.bar(df, x="Ano", y="Prejuizo_Milhoes", text="Prejuizo_Milhoes",
                 title="Prejuízo Financeiro com Ciberataques (em milhões USD)")
    fig.update_layout(yaxis_title="Prejuízo (milhões USD)", xaxis_title="Ano")
    return fig
