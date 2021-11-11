import streamlit as st
import sqlite3

con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

paginaSelecionada = st.sidebar.selectbox('Selecione o caminho', ['Tela de inicio','Login Presidente','Login Secretária','Registro funcionário'])

if paginaSelecionada == 'Tela de inicio':
    st.title('Tela principal')

elif paginaSelecionada == 'Registro funcionário':
    st.title("Tela Cadastro")

    with st.form(key='include_cliente'):
        input_name = st.text_input(label='Insira o seu nome')
        input_senha = st.text_input(label='Insira a senha', type="password")
        input_cpf = st.text_input(label ='Insira o seu CPF')
        input_occupation = st.selectbox('selecione sua profissão', ['Pesquisador'])
        input_button_enviar = st.form_submit_button("Enviar Dados")

    if input_button_enviar:
        cursor.execute(f"INSERT INTO cadastro VALUES ('{input_name}','{input_senha}',{input_cpf},'{input_occupation}')")
        con.commit()

        st.success('Adicionado com sucesso !!')

elif paginaSelecionada == 'Login Secretária':
    st.title("Login Secretária")

    with st.form(key='include_cliente'):
        input_button_login_Secretaria = st.form_submit_button('Login')


elif paginaSelecionada == 'Login Presidente':
    st.title("Login Presidente")

    with st.form(key='include_cliente'):
        input_button_login_Presidente = st.form_submit_button('Login')

