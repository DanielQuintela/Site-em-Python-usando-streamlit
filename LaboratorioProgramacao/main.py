import pandas as pd
import streamlit as st
import sqlite3

con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

#cadastro de pesquisador, inicialmente chamado no código de user

def create_usertable():
    cursor.execute('CREATE TABLE IF NOT EXISTS pesquisador(nome TEXT,senha TEXT,ocupacao TEXT, cpf NUMERIC UNIQUE, situacao TEXT)')


def add_userdata(nome, senha, ocupacao, cpf,situacao):
    cursor.execute('INSERT INTO pesquisador(nome,senha,ocupacao, cpf, situacao) VALUES (?,?,?,?,?)', (nome, senha, ocupacao, cpf,situacao))
    con.commit()


def login_user(nome, senha,situacao):
    cursor.execute('SELECT * FROM pesquisador WHERE nome = ? AND senha = ? AND situacao = ?', (nome, senha, situacao))
    data = cursor.fetchall()
    return data

def create_presdenttable():
    cursor.execute('CREATE TABLE IF NOT EXISTS presidente(nome TEXT,senha TEXT)')

def add_presidente(nome, senha):
    cursor.execute('INSERT INTO presidente(nome,senha) VALUES (?,?)', (nome, senha))
    con.commit()

def login_presidente(nome, senha):
    cursor.execute('SELECT * FROM presidente WHERE nome = ? AND senha = ?', (nome, senha))
    data = cursor.fetchall()
    return data

#registro de autenticação no banco
#de Pesquisador!! AGORA VAI

def add_data(nomex):

    #cursor.execute('CREATE TABLE IF NOT EXISTS pesquisadores_aprovados(nome TEXT)')
    cursor.execute(f'UPDATE pesquisador SET situacao = "aprovado" WHERE nome = "{nomex}" ')
    con.commit()

#cadastro da funcionára

def create_secretaria():
    cursor.execute('CREATE TABLE IF NOT EXISTS secretaria2(nome TEXT,senha TEXT)')

def add_secretaria(nome, senha):
    cursor.execute('INSERT INTO secretaria2(nome,senha) VALUES (?,?)', (nome, senha))
    con.commit()

def login_secretaria(nome, senha):
    cursor.execute('SELECT * FROM secretaria2 WHERE nome = ? AND senha = ?', (nome, senha))
    data = cursor.fetchall()
    return data

def view_all_titles():
	cursor.execute('SELECT DISTINCT nome FROM pesquisador')
	data = cursor.fetchall()
	return data

def delete_data(resultado):
	cursor.execute('DELETE FROM pesquisador WHERE nome="{}"'.format(resultado))
	con.commit()

paginaSelecionada = st.sidebar.selectbox('Selecione o caminho',['Tela de inicio', 'Área do Pesquisador', 'Login Secretária', 'Login Presidente'])

if paginaSelecionada == 'Tela de inicio':
    st.title('Tela principal')


elif paginaSelecionada == 'Área do Pesquisador':
    st.sidebar.title("Login Pesquisador")
    funcionarios = st.sidebar.selectbox('Selecione o caminho', ['Login', 'Cadastro'])

    if funcionarios == 'Login':
        nome = st.sidebar.text_input('Insira seu nome')
        senha = st.sidebar.text_input('Insira a senha', type='password')
        situacao = st.sidebar.selectbox('Situação ?', ['aprovado'])
        if st.sidebar.checkbox('Login'):
            # if input_senha_func == '1234':
            create_usertable()
            result = login_user(nome, senha,situacao)
            if result:

                st.sidebar.title(f"Logado como: {nome}")
                st.title(f'Bem vindo de Volta {nome}')

            else:
                st.warning("Usuário incorreto ou Não Aprovado")

    if funcionarios == 'Cadastro':
        st.title('Cadastro de Pesquisador')
        input_name = st.text_input(label='Insira o seu nome')
        input_senha = st.text_input(label='Insira a senha', type="password")
        input_cpf = st.text_input(label='Insira o seu CPF')
        input_occupation = st.selectbox('selecione sua profissão', ['Pesquisador'])
        situacao = st.sidebar.selectbox('Situação atual:', ['Não Aprovado'])

        if st.button("Enviar Dados"):
            create_usertable()
            add_userdata(input_name, input_senha, input_occupation, input_cpf,situacao)
            st.success('Adicionado com sucesso !!')
            st.info("Vá para o menu de login!!")
        

elif paginaSelecionada == 'Login Secretária':
    st.sidebar.title("Login Secretária")
    nome = st.sidebar.text_input('Insira seu nome')
    senha = st.sidebar.text_input('Insira a senha', type='password')
    if st.sidebar.checkbox('Login'):
        create_secretaria()
        result = login_secretaria(nome, senha)
        if result:
            if login_secretaria:
                st.sidebar.title('Secretária logada')
                st.title("Área da Secretária")
                y = st.selectbox('Escolha um caminho', ['Aprovação de pesquisadores', 'NULL'])
                if y == 'Aprovação de pesquisadores':
                    tabela = st.checkbox('Mostar Dados')
                    if tabela:
                        st.subheader('Pesquisadores em análise')
                        resultado = cursor.execute('SELECT nome,cpf,situacao from pesquisador')
                        pesquisa = pd.DataFrame(resultado, columns=['Pesquisadores', 'CPF','Situação'])
                        st.dataframe(pesquisa)
                        with st.form(key='include_cliente'):
                            st.subheader('Selecione o que deseja realizar')
                            aprovar = st.form_submit_button("Aprovar")
                            remover = st.form_submit_button("Remover")

                            unique_titles = [i[0] for i in view_all_titles()]
                            selecao = st.selectbox("Pesquisadores", unique_titles)
                            new_df = resultado
                            if aprovar:
                                add_data(selecao)
                                st.warning("Aprovado: '{}'".format(selecao))

                            if remover:
                                delete_data(selecao)
                                st.warning("Removido: '{}'".format(selecao))




        else:
            st.warning("Usuário incorreto")



elif paginaSelecionada == 'Login Presidente':
    st.sidebar.title("Login Presidente")
    nome = st.sidebar.text_input('Insira seu nome')
    senha = st.sidebar.text_input('Insira a senha', type='password')
    if st.sidebar.checkbox('Login'):
        create_presdenttable()
        result = login_presidente(nome, senha)
        if result:
            st.sidebar.title(f"Logado como: {nome}")
            st.title(f'Bem vindo de Volta Sr {nome}')
            st.text('Presidente na Área')
            secretaria = st.selectbox('Escolha a função',['Inicio','Cadastro de Secretária'])
            if secretaria == 'Cadastro de Secretária':
                st.title('Cadastro de Secretaria')
                input_name = st.text_input(label='Insira o seu nome')
                input_senha = st.text_input(label='Insira sua senha', type="password")
                if st.button("Enviar Dados"):
                    create_secretaria()
                    add_secretaria(input_name, input_senha)
                    st.success(f'{input_name} Adicionada com sucesso !!')
                    st.info("Vá para o menu de login!!")
            elif secretaria == 'Inicio':
                st.title('Pagina do Diretor')
                st.subheader('Lista de Secretárias')
                dados_secretaria = cursor.execute('SELECT nome from secretaria2')
                clean_db = pd.DataFrame(dados_secretaria, columns=['Secretárias ativas'])
                st.dataframe(clean_db)


        else:
            st.warning("Usuário incorreto")

#esse elif é para fica oculto do sistema.
#apenas para o cadastro do presidente
elif paginaSelecionada == 'Cadastro presidente':
    #só pra quebrar o galho no banco
    st.title('Cadastro de Presidente')
    input_name = st.text_input(label='Insira o seu nome')
    input_senha = st.text_input(label='Insira a senha', type="password")

    if st.button("Enviar Dados"):
        create_presdenttable()
        add_presidente(input_name, input_senha)
        st.success('Adicionado com sucesso !!')
        st.info("Vá para o menu de login!!")
