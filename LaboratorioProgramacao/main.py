import streamlit as st
import sqlite3
con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

def create_usertable():
	cursor.execute('CREATE TABLE IF NOT EXISTS pesquisador(nome TEXT,senha TEXT,ocupacao TEXT, cpf NUMERIC)')

def add_userdata(nome,senha, ocupacao, cpf):
	cursor.execute('INSERT INTO pesquisador(nome,senha,ocupacao, cpf) VALUES (?,?,?,?)',(nome,senha, ocupacao, cpf))
	con.commit()

def login_user(cpf,senha):
	cursor.execute('SELECT * FROM pesquisador WHERE cpf =? AND senha = ?',(cpf,senha))
	data = cursor.fetchall()
	return data


paginaSelecionada = st.sidebar.selectbox('Selecione o caminho', ['Tela de inicio','Área do funcionário','Login Secretária','Login Presidente'])

if paginaSelecionada == 'Tela de inicio':
    st.title('Tela principal')

elif paginaSelecionada == 'Área do funcionário':
    st.sidebar.title("Login Funcionário")
    funcionarios = st.sidebar.selectbox('Selecione o caminho',['Login','Cadastro'])

    if funcionarios == 'Login':
        cpf = st.sidebar.text_input('Insira o seu CPF')
        senha = st.sidebar.text_input('Insira a senha', type='password')
        if st.sidebar.checkbox('Login'):
        # if input_senha_func == '1234':
            create_usertable()
            result = login_user(cpf, senha)
            if result:

                st.title('Opaa, olha ai sss')
            else:
                st.warning("Usuário incorreto")

    if funcionarios == 'Cadastro':
            st.title('Cadastro de Pesquisador')
            input_name = st.text_input(label='Insira o seu nome')
            input_senha = st.text_input(label='Insira a senha', type="password")
            input_cpf = st.text_input(label='Insira o seu CPF')
            input_occupation = st.selectbox('selecione sua profissão', ['Pesquisador'])

            if st.button("Enviar Dados"):
                create_usertable()
                add_userdata(input_name,input_senha,input_occupation,input_cpf)
                st.success('Adicionado com sucesso !!')
                st.info("Vá para o menu de login!!")


elif paginaSelecionada == 'Login Secretária':
    login_secretaria = st.sidebar.checkbox('Login')
    if login_secretaria:
        st.sidebar.title('Secretária logada')
        st.title("Área da Secretária")
        genre = st.radio("Escolha um pesquisador", ('teste1', 'teste2', 'teste3'))
        if genre == 'teste1':
           st.write('Você seleionou um pesquisador.')


elif paginaSelecionada == 'Login do Presidente':
    st.sidebar.title("Login Presidente")
    login_presidente = st.sidebar.checkbox('Login')
    if login_presidente:
        st.title('teste')
