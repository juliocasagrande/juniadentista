import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    layout='wide',
    page_title='Junia Alvarenga - Pacientes'
)

if st.session_state["authentication_status"]:
    df_pacientes = st.session_state['atendimento']
    pacientes = df_pacientes['Paciente'].unique()
    paciente = st.sidebar.selectbox('Selecione o paciente', pacientes)

    df_paciente_filtrado = df_pacientes[df_pacientes['Paciente'] == paciente]
    st.markdown(f"# {df_paciente_filtrado['Paciente'].iloc[0]} #")

    colunas = ['Data','Procedimento','Data Retorno','Valor Cobrado']
    df_paciente_filtrado = df_paciente_filtrado.loc[:,colunas].set_index('Data')
    df_paciente_filtrado

    soma = df_paciente_filtrado['Valor Cobrado'].sum()
    st.write(f"**Valor Gasto Total do Paciente:** R$ {soma}")

else:
    st.error('Usuário não logado. Favor inserir login e senha na tela inicial!')