import streamlit as st
import sqlite3

con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

paginaSelecionada = st.sidebar.selectbox('Selecione o caminho', ['Tela de inicio','Login Presidente','Login Secretária','Login funcionário'])

if paginaSelecionada == 'Tela de inicio':
    st.title('Tela principal')

elif paginaSelecionada == 'Login funcionário':
    st.title("Login Funcionário")
    funcionarios = st.selectbox('Selecione o caminho',['Login','Cadastro'])

    if funcionarios == 'Login':
        with st.form(key='include_cliente'):
            input_cpf_func = st.text_input(label='Insira o seu CPF')
            input_senha_func = st.text_input(label='Insira a senha', type="password")
            input_button_login = st.form_submit_button("Login")
        if input_button_login:
            st.title('Logado')

    if funcionarios == 'Cadastro':
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
    st.title("Login Secretária")
    genre = st.radio("Escolha um pesquisador", ('teste1', 'teste2', 'teste3'))
    if genre == 'teste1':
        st.write('Você seleionou um pesquisador.')


elif paginaSelecionada == 'Login Presidente':
    st.title("Login Presidente")

    with st.form(key='include_cliente'):
        input_button_login_Presidente = st.form_submit_button('Login')
