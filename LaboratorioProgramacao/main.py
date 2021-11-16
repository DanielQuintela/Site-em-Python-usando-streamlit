import streamlit as st
import sqlite3

con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()


def create_usertable():
    cursor.execute('CREATE TABLE IF NOT EXISTS pesquisador(nome TEXT,senha TEXT,ocupacao TEXT, cpf NUMERIC)')


def add_userdata(nome, senha, ocupacao, cpf):
    cursor.execute('INSERT INTO pesquisador(nome,senha,ocupacao, cpf) VALUES (?,?,?,?)', (nome, senha, ocupacao, cpf))
    con.commit()


def login_user(nome, senha):
    cursor.execute('SELECT * FROM pesquisador WHERE nome = ? AND senha = ?', (nome, senha))
    data = cursor.fetchall()
    return data


def aprovar_cadastro():
    escolha = st.selectbox('', ['Escolha uma função', 'aprovar', 'remover'])
    if escolha == 'Escolha uma função':
        st.title('Pesquisador em análise:')
        cursor.execute('SELECT nome from pesquisador')
        x = cursor.fetchone()
        for i in x:
            st.title(i)

    if escolha == 'aprovar':
        cursor.execute('SELECT nome from pesquisador')
        k = cursor.fetchone()
        for a in k:
            st.title(a)
        cursor.execute('SELECT senha from pesquisador')
        l = cursor.fetchone()
        for b in l:
            st.title(b)
        cursor.execute('SELECT cpf from pesquisador')
        m = cursor.fetchone()
        for c in m:
            st.title(c)

        cursor.execute(f'INSERT INTO pesquisadores_aprovados VALUES (?,?,?)', (a,b,c))

        st.title('Funcionário aceito!')

    if escolha == 'remover':
        cursor.execute('DELETE from pesquisador')
        st.title('Funcionário não aceito!')


paginaSelecionada = st.sidebar.selectbox('Selecione o caminho',['Tela de inicio', 'Área do funcionário', 'Login Secretária', 'Login Presidente'])

if paginaSelecionada == 'Tela de inicio':
    st.title('Tela principal')


elif paginaSelecionada == 'Área do funcionário':
    st.sidebar.title("Login Funcionário")
    funcionarios = st.sidebar.selectbox('Selecione o caminho', ['Login', 'Cadastro'])

    if funcionarios == 'Login':
        nome = st.sidebar.text_input('Insira seu nome')
        senha = st.sidebar.text_input('Insira a senha', type='password')
        if st.sidebar.checkbox('Login'):
            # if input_senha_func == '1234':
            create_usertable()
            result = login_user(nome, senha)
            if result:
                st.sidebar.title(f"Logado como: {nome}")
                st.title(f'Bem vindo de Volta {nome}')

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
            add_userdata(input_name, input_senha, input_occupation, input_cpf)
            st.success('Adicionado com sucesso !!')
            st.info("Vá para o menu de login!!")


elif paginaSelecionada == 'Login Secretária':
    login_secretaria = st.sidebar.checkbox('Login')
    if login_secretaria:
        st.sidebar.title('Secretária logada')
        st.title("Área da Secretária")
        y = st.selectbox('Escolha um caminho', ['Aprovação de pesquisadores', 'NULL'])
        if y == 'Aprovação de pesquisadores':
            aprovar_pesquisador = st.title(aprovar_cadastro())



elif paginaSelecionada == 'Login Presidente':
    st.sidebar.title("Login Presidente")
    login_presidente = st.sidebar.checkbox('Login')
    if login_presidente:
        st.title('teste')
