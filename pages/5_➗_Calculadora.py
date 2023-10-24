import streamlit as st

st.set_page_config(
    layout='wide',
    page_title='Junia Alvarenga - Pacientes'
)

if st.session_state["authentication_status"]:
    st.title('Calculadora Botox')
    col1, col2, col3 = st.columns(3)
    col1.subheader('💵 VALORES DOS MATERIAIS')
    tox_bot = col1.number_input('💰 Valor da toxina (R$):', value=967)
    qtde_us = col1.number_input('➗ Quantidade de Us:', value=145)
    seringa_aplicacao = col1.number_input('💉 Valor Seringa Aplicação:')
    seringa_diluicao = col1.number_input('💉Valor Seringa Diluição:')
    soro = col1.number_input('🧪 Valor da Soro:')
    luva = col1.number_input('🧤 Valor da Luva:')
    clorex = col1.number_input('🧽 Valor da Clorexidina:')
    gaze = col1.number_input('🩹 Valor da Gaze:')
    babador = col1.number_input('🤤 Valor do Babador:')
    anestesico = col1.number_input('✨ Valor do Anestésico:')

    col2.subheader('💉 QUANTIDADE UTILIZADA')
    qtde_seringa_aplica = col2.number_input('💉 Qtde Seringas Aplicação:')
    qtde_seringa_dilu = col2.number_input('💉 Qtde Seringas Diluição:')
    qtde_soro = col2.number_input('🧪 Qtde de Soros:')
    qtde_luva = col2.number_input('🧤 Qtde de Luvas:')
    qtde_clorex = col2.number_input('🧽 Qtde de Clorexidina:')
    qtde_gaze = col2.number_input('🩹 Qtde de Gazes:')
    qtde_babador = col2.number_input('🤤 Qtde de Babadores:')
    qtde_anestesico = col2.number_input('✨ Qtde de Anestésicos:')

    col3.subheader('🚏 PONTOS POR REGIÃO')
    frontal = col3.number_input('Frontal:')
    procero = col3.number_input('Prócero:')
    corrugador = col3.number_input('Corrugador:')
    orb1 = col3.number_input('Orbicular 1ª Linha:')
    orb2 = col3.number_input('Orbicular 2ª Linha:')
    nasal = col3.number_input('Nasal:')
    sorriso_geng = col3.number_input('Sorriso Gengival:')
    ang_boca = col3.number_input('Abaixo do Ângulo Boca:')
    mentual = col3.number_input('Mentual:')

    st.subheader('Custos Finais')
    valor_u = tox_bot/qtde_us
    st.write(f"__Valor por U:__ R$ {round(valor_u,2)}")
    qtde_us_utilizados = (frontal*2)+(procero*4)+(corrugador*4)+((orb1+orb2+nasal)*2)+(sorriso_geng*4)+(ang_boca*2)+(mentual*4)
    st.write(f"__Quantidade de Us utilizados:__ {qtde_us_utilizados}")
    valor_final = (valor_u*qtde_us_utilizados) + ((seringa_aplicacao*qtde_seringa_aplica)+(seringa_diluicao*qtde_seringa_dilu)+(soro*qtde_soro)+(luva*qtde_luva)+(clorex*qtde_clorex)+(gaze*qtde_gaze)+(babador*qtde_babador)+(anestesico*qtde_anestesico))
    st.write(f"__Valor Final da Aplicação:__ R$ {round(valor_final,2)}")

elif st.session_state["authentication_status"] is False:
    st.error('Usuário ou senha incorreta!')
elif st.session_state["authentication_status"] is None:
    st.warning('Por favor, insira usuário e senha')