import pandas as pd
import streamlit as st
import sqlite3

con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

# cadastro de pesquisador, inicialmente chamado no código de user

def create_usertable():
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS pesquisador(nome TEXT,senha TEXT,ocupacao TEXT, cpf NUMERIC UNIQUE, situacao TEXT)')

def add_userdata(nome, senha, ocupacao, cpf, situacao):
    cursor.execute('INSERT INTO pesquisador(nome,senha,ocupacao, cpf, situacao) VALUES (?,?,?,?,?)',
                   (nome, senha, ocupacao, cpf, situacao))
    con.commit()

def login_user(nome, senha, situacao):
    cursor.execute('SELECT * FROM pesquisador WHERE nome = ? AND senha = ? AND situacao = ?', (nome, senha, situacao))
    data = cursor.fetchall()
    return data

# cadastro do presidente

def create_presdenttable():
    cursor.execute('CREATE TABLE IF NOT EXISTS presidente(nome TEXT,senha TEXT)')

def add_presidente(nome, senha):
    cursor.execute('INSERT INTO presidente(nome,senha) VALUES (?,?)', (nome, senha))
    con.commit()

def login_presidente(nome, senha):
    cursor.execute('SELECT * FROM presidente WHERE nome = ? AND senha = ?', (nome, senha))
    data = cursor.fetchall()
    return data

# registro de autenticação no banco
# de Pesquisador!! AGORA VAI

def add_data(nomex):
    # cursor.execute('CREATE TABLE IF NOT EXISTS pesquisadores_aprovados(nome TEXT)')
    cursor.execute(f'UPDATE pesquisador SET situacao = "aprovado" WHERE nome = "{nomex}" ')
    con.commit()

# cadastro da funcionára

def create_secretaria():
    cursor.execute('CREATE TABLE IF NOT EXISTS secretaria2(nome TEXT,senha TEXT)')

def add_secretaria(nome, senha):
    cursor.execute('INSERT INTO secretaria2(nome,senha) VALUES (?,?)', (nome, senha))
    con.commit()

def login_secretaria(nome, senha):
    cursor.execute('SELECT * FROM secretaria2 WHERE nome = ? AND senha = ?', (nome, senha))
    data = cursor.fetchall()
    return data

# seleção para ver os pesquisadores no banco

def view_all_titles():
    cursor.execute('SELECT DISTINCT nome FROM pesquisador')
    data = cursor.fetchall()
    return data

# Exclusão de pesquisador

def delete_data(resultado):
    cursor.execute('DELETE FROM pesquisador WHERE nome="{}"'.format(resultado))
    con.commit()

# Criação do banco de protocolo
def banco_protocolo():
    cursor.execute('CREATE TABLE IF NOT EXISTS protocolos(justificativa TEXT NOT NULL ,resumo_portugues TEXT, resumo_ingles TEXT,'
                   'data_inicio TEXT,data_fim TEXT, especie TEXT NOT NULL, quantidade_animais TEXT NOT NULL, bioterio TEXT NOT NULL, situacao TEXT)')

def addbanco_protocolo(input_justificativa,input_resumopt,input_resumoig,input_datainicio,input_dataterm ,input_especie ,
                       input_qntanimal,_bioterio ):
    cursor.execute('INSERT INTO protocolos(justificativa,resumo_portugues,resumo_ingles,data_inicio,data_fim,'
                   'especie,quantidade_animais,bioterio) VALUES (?,?,?,?,?,?,?,?)',
                   (input_justificativa,input_resumopt,input_resumoig,input_datainicio,input_dataterm ,input_especie ,
                    input_qntanimal,_bioterio ))
    con.commit()
# cr
def banco_bioterio():
    cursor.execute('CREATE TABLE IF NOT EXISTS bioterio(nome TEXT NOT NULL UNIQUE)')

def addbanco_bioterio(cadastro_biot):
    cursor.execute('INSERT INTO bioterio VALUES (?)',(cadastro_biot,))
    con.commit()

def view_all_bioterios():
    cursor.execute('SELECT DISTINCT nome FROM bioterio')
    data = cursor.fetchall()
    return data

def add_especie(nomex,nome_especie):
    cursor.execute('UPDATE bioterio SET animais = IIF(animais IS NULL, "{}", animais || " " || "{}" ) WHERE nome = "{}"'.format(nome_especie, nome_especie,nomex))
    con.commit()

paginaSelecionada = st.sidebar.selectbox('Selecione o caminho',
                                         ['Tela de inicio', 'Área do Pesquisador', 'Login Secretária',
                                          'Login Presidente'])

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
            result = login_user(nome, senha, situacao)
            if result:

                st.sidebar.title(f"Logado como: {nome}")
                st.title(f'Bem vindo de Volta {nome}')
                area_pesq =st.selectbox('Selecione o que deseja',['Inicio','Emitir Protocolo','Receber protocolo'])
                if area_pesq == 'Inicio':
                    st.title('Página inicial do pesquisador')
                    st.text('Selecione uma opção acima para começar os trabalhos !!')
                if area_pesq == 'Emitir Protocolo':
                    st.title('Emitir Protocolo')
                    input_justificativa = st.text_input(label='Justificativa para o uso de animais')
                    input_resumopt = st.text_input(label='Insira o resumo do trabalho em português')
                    input_resumoig = st.text_input(label='Insira o resumo do trabalho em inglês')
                    input_datainicio = st.date_input(label='Insira a data prevista para o inicio do experimento:')
                    input_dataterm = st.date_input(label='Insira a data prevista para o termino do experimento:')
                    input_especie = st.text_input(label='Insira a especie do animal')
                    input_qntanimal = st.text_input(label='Insira a quantidade de animais')
                    unique_titles = [i[0] for i in view_all_bioterios()]
                    _bioterio = st.selectbox("Escolha o Bioterio", unique_titles)
                    if st.button('Emitir Protocolo'):
                        banco_protocolo()
                        addbanco_protocolo(input_justificativa,input_resumopt,input_resumoig,input_datainicio,input_dataterm ,input_especie ,input_qntanimal,_bioterio )
                        st.success('Protocolo Emitido!')


                if area_pesq == 'Receber protocolo':
                    st.title('Receber protocolo')
                    input_parecer = st.text_input(label='Descreva seu parecer')
                    recomendar = st.selectbox('Escolha a opção',['Recomendado','Não Recomendado'])

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
            add_userdata(input_name, input_senha, input_occupation, input_cpf, situacao)
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
                y = st.selectbox('Escolha um caminho', ['Aprovação de pesquisadores', 'Cadastrar Bioterios', 'Cadastrar Espécie'])
                if y == 'Aprovação de pesquisadores':
                    tabela = st.checkbox('Mostar Dados')
                    if tabela:
                        st.subheader('Pesquisadores em análise')
                        resultado = cursor.execute('SELECT nome,cpf,situacao from pesquisador')
                        pesquisa = pd.DataFrame(resultado, columns=['Pesquisadores', 'CPF', 'Situação'])
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

                if y == 'Cadastrar Bioterios':
                    cadastro_biot = st.text_input('Insira o nome do Bioterio')
                    if st.button('Cadastrar'):
                        banco_bioterio()
                        addbanco_bioterio(cadastro_biot)
                        st.success('Bioterio Cadastrado!')

                if y == 'Cadastrar Espécie':
                    with st.form(key='cadastro_animais'):
                      st.subheader('Cadastre uma espécie em um dos biotérios')
                      nome_especie = st.text_input('Digite o nome da espécie')
                      Adicionar = st.form_submit_button("Adicionar")
                    # TODO placeholder, mudar nome da tabela e coluna quando receber lista de bioterio
                      unique_titles = [i[0] for i in view_all_bioterios()]
                      selecao = st.selectbox("Bioterios", unique_titles)
                      if Adicionar:
                         add_especie(selecao, nome_especie +"")
                         st.warning(f"Espécie {nome_especie} Cadastrada!!")

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
            escolha = st.selectbox('Escolha a função', ['Inicio','Analise de Relatorios'])

            if escolha == 'Inicio':
                st.title('Pagina do Diretor')
                st.subheader('Lista de Secretárias')
                dados_secretaria = cursor.execute('SELECT nome from secretaria2')
                clean_db = pd.DataFrame(dados_secretaria, columns=['Secretárias ativas'])
                st.dataframe(clean_db)


        else:
            st.warning("Usuário incorreto")


# esse elif é para fica oculto do sistema.
# apenas para o cadastro do presidente
elif paginaSelecionada == 'Cadastro presidente':
    # só pra quebrar o galho no banco
    st.title('Cadastro de Presidente')
    input_name = st.text_input(label='Insira o seu nome')
    input_senha = st.text_input(label='Insira a senha', type="password")

    if st.button("Enviar Dados"):
        create_presdenttable()
        add_presidente(input_name, input_senha)
        st.success('Adicionado com sucesso !!')
        st.info("Vá para o menu de login!!")


# esse elif é para fica oculto do sistema.
# apenas para o cadastro da secretária

elif paginaSelecionada == 'Cadastro de Secretária':
    st.title('Cadastro de Secretaria')
    input_name = st.text_input(label='Insira o seu nome')
    input_senha = st.text_input(label='Insira sua senha', type="password")
    if st.button("Enviar Dados"):
        create_secretaria()
        add_secretaria(input_name, input_senha)
        st.success(f'{input_name} Adicionada com sucesso !!')
        st.info("Vá para o menu de login!!")