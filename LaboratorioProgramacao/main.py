import streamlit as st
import sqlite3

con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

paginaSelecionada = st.sidebar.selectbox('Selecione o caminho', ['Tela de inicio','Login Presidente','Login Secretária','Login funcionário'])

if paginaSelecionada == 'Tela de inicio':
    st.title('Tela principal')

elif paginaSelecionada == 'Login funcionário':
    st.sidebar.title("Login Funcionário")
    funcionarios = st.sidebar.selectbox('Selecione o caminho',['Login','Cadastro'])

    if funcionarios == 'Login':
            input_cpf_func = st.sidebar.text_input(label='Insira o seu CPF')
            input_senha_func = st.sidebar.text_input(label='Insira a senha', type="password")
            login_pesquisador = st.sidebar.checkbox('Login')
            if login_pesquisador:
               st.sidebar.title('Funcionário logado')
               st.title('TESTE')

    if funcionarios == 'Cadastro':
        st.title('Cadastro de Pesquisador')
        with st.form(key='include_cliente'):
            input_name = st.text_input(label='Insira o seu nome')
            input_senha = st.text_input(label='Insira a senha', type="password")
            input_cpf = st.text_input(label='Insira o seu CPF')
            input_occupation = st.selectbox('selecione sua profissão', ['Pesquisador'])
            input_button_enviar = st.form_submit_button("Enviar Dados")

        if input_button_enviar:
            cursor.execute(
                f"INSERT INTO cadastro VALUES ('{input_name}','{input_senha}',{input_cpf},'{input_occupation}')")
            con.commit()

            st.success('Adicionado com sucesso !!')


elif paginaSelecionada == 'Login Secretária':
    login_secretaria = st.sidebar.checkbox('Login')
    if login_secretaria:
        st.sidebar.title('Secretária logada')
        st.title("Área da Secretária")
        genre = st.radio("Escolha um pesquisador", ('teste1', 'teste2', 'teste3'))
        if genre == 'teste1':
           st.write('Você seleionou um pesquisador.')


elif paginaSelecionada == 'Login Presidente':
    st.sidebar.title("Login Presidente")
    login_presidente = st.sidebar.checkbox('Login')
    if login_presidente:
        st.title('teste')
