import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    layout='wide',
    page_title='Junia Alvarenga - Pacientes'
)

if st.session_state["authentication_status"]:
    df_pacientes = st.session_state['pacientes']

    pacientes = df_pacientes['Nome'].unique()

    paciente = st.sidebar.selectbox('Selecione o paciente', pacientes)

    df_pacientes_filtrado = df_pacientes[df_pacientes['Nome'] == paciente]
    st.markdown(f"# {df_pacientes_filtrado['Nome'].iloc[0]} #")

    df_pacientes_filtrado['Data Nascimento'] = pd.to_datetime(df_pacientes_filtrado['Data Nascimento'])
    # Data atual
    data_atual = datetime.now()

    # Calcular a idade da primeira pessoa no DataFrame
    idade_em_dias = (data_atual - df_pacientes_filtrado['Data Nascimento'].iloc[0]).days
    idade_em_anos = idade_em_dias // 365  # Aproximadamente, ignorando os anos bissextos

    # Convertendo a data de nascimento para o formato desejado (dia/mês/ano)
    data_nascimento_formatada = df_pacientes_filtrado['Data Nascimento'].iloc[0].strftime('%d/%m/%Y')

    # Mostrar a idade e a data de nascimento formatada no Streamlit
    st.markdown(f"__Idade:__ {idade_em_anos} anos")
    st.markdown(f"__Data de Nascimento:__ {data_nascimento_formatada}")
    st.markdown(f"__Telefone:__ {df_pacientes_filtrado['Telefone'].iloc[0]}")
    st.markdown(f"__Observações:__ {df_pacientes_filtrado['Observacao'].iloc[0]}")
else:
    st.error('Usuário não logado. Favor inserir login e senha na tela inicial!')