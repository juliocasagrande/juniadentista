import pandas as pd
import streamlit as st
import webbrowser as web
from datetime import datetime
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os
import toml
from streamlit_gsheets import get_gsheet_url

# Parte do streamlit
st.set_page_config(
    layout='wide',
    page_title='Junia Alvarenga - Home'
)

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
nome_arquivo = 'config.yaml'
caminho_completo = os.path.join(diretorio_atual, nome_arquivo)

with open(caminho_completo, 'r') as arquivo:
    config = yaml.load(arquivo, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Bem-vindo ao nosso site! *{st.session_state["name"]}*')
    if st.button('Acesse a planilha de preenchimento dos dados'):
        web.open_new_tab('https://docs.google.com/spreadsheets/d/1qe7p_-rsysUkW1BPA86Hi_nNeSuIFq-697A6iVeTmtg/edit#gid=167923064')
        
    # Create a connection object.
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)

    df_atendimento = conn.read(worksheet='Atendimento')
    df_pacientes = conn.read(worksheet='Pacientes')
    df_leads = conn.read(worksheet='Leads')

    st.markdown('# JÚNIA ALVARENGA ODONTOLOGIA E ESTÉTICA 💎 #')

    df_atendimento.dropna(how="all", inplace=True)
    df_atendimento.fillna("", inplace=True)
    df_pacientes.dropna(how="all", inplace=True)
    df_leads.dropna(how="all", inplace=True)

    if "atendimento" not in st.session_state:
        st.session_state['atendimento'] =  df_atendimento
    if "pacientes" not in st.session_state:
        st.session_state['pacientes'] = df_pacientes
    if "leads" not in st.session_state:
        st.session_state['leads'] = df_leads

    st.header('Retornos Mensais')
    df_retorno = df_atendimento

    mes_atual = datetime.now().month
    df_retorno[['Dia','Mes','Ano']] = df_retorno['Data Retorno'].str.split('/', expand=True)
    df_retorno['Dia'] = pd.to_numeric(df_retorno['Dia'], errors='coerce')
    df_retorno['Mes'] = pd.to_numeric(df_retorno['Mes'], errors='coerce')
    df_retorno['Ano'] = pd.to_numeric(df_retorno['Ano'], errors='coerce')

    df_retorno = df_retorno[df_retorno['Mes'] == mes_atual]

    colunas_retorno = ['Paciente', 'Telefone', 'Data', 'Procedimento', 'Data Retorno', 'Valor Recebido']
    df_retorno


    st.header('Aniversariantes do Mês')
    df_pacientes[['Dia','Mes','Ano']] = df_pacientes['Data Nascimento'].str.split('/', expand=True)
    df_pacientes['Dia'] = pd.to_numeric(df_pacientes['Dia'], errors='coerce')
    df_pacientes['Mes'] = pd.to_numeric(df_pacientes['Mes'], errors='coerce')
    df_pacientes['Ano'] = pd.to_numeric(df_pacientes['Ano'], errors='coerce')
    df_aniversario = df_pacientes[df_pacientes['Mes'] == mes_atual]
    colunas_aniversario = ['Nome', 'Data Nascimento','Telefone','Observacao']
    df_aniversario = df_aniversario[df_aniversario['Mes'] == mes_atual]
    df_aniversario[colunas_aniversario]

    st.header('Gráfico de Evolução')
    st.bar_chart(df_atendimento, x='Data',y='Valor Recebido')

elif st.session_state["authentication_status"] is False:
    st.error('Usuário ou senha incorreta!')
elif st.session_state["authentication_status"] is None:
    st.warning('Por favor, insira usuário e senha')