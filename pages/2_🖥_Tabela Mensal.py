import streamlit as st
import pandas as pd
from datetime import datetime

if st.session_state["authentication_status"]:
    df_atendimentos = st.session_state['atendimento']
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year
    mes_anterior = (mes_atual)-1
    df_atendimentos[['Dia','Mes','Ano']] = df_atendimentos['Data'].str.split('/', expand=True)
    df_atendimentos['Dia'] = pd.to_numeric(df_atendimentos['Dia'], errors='coerce')
    df_atendimentos['Mes'] = pd.to_numeric(df_atendimentos['Mes'], errors='coerce')
    df_atendimentos['Ano'] = pd.to_numeric(df_atendimentos['Ano'], errors='coerce')
    
    anos = df_atendimentos['Ano'].unique()
    
    colunas_para_processar = ['Custo', 'Valor Cobrado', 'Valor Recebido']

    for i in colunas_para_processar:
        df_atendimentos[i] = df_atendimentos[i].astype(str)
        df_atendimentos[i] = df_atendimentos[i].str.replace('R$ -', '')
        df_atendimentos[i] = pd.to_numeric(df_atendimentos[i], errors='coerce').round(2)

    colunas_atendimento = ['Paciente','Data','Procedimento','Custo','Tipo pagamento','Qtde vezes', 'Valor Cobrado','Valor Recebido']
    col1, col2 = st.columns(2)
    mes = col1.selectbox('Selecione o mês',[1,2,3,4,5,6,7,8,9,10,11,12], index = mes_anterior)
    df_atendimentos = df_atendimentos[(df_atendimentos['Mes'] == mes) & (df_atendimentos['Ano'] == ano_atual)]
    st.dataframe(df_atendimentos[colunas_atendimento],
                column_config={
                    'Custo': st.column_config.NumberColumn(
                        format="R$%.2f"
                    ),
                    'Valor Cobrado': st.column_config.NumberColumn(
                        format="R$%.2f"
                    ),
                    'Valor Recebido': st.column_config.NumberColumn(
                        format="R$%.2f"
                    )
                })

    soma = df_atendimentos['Valor Recebido'].sum()
    st.write(f"__Valor arrecadado:__ R$ {(soma*.6):.2f}")


    st.bar_chart(df_atendimentos,x='Data', y='Valor Recebido')
else:
    st.error('Usuário não logado. Favor inserir login e senha na tela inicial!')