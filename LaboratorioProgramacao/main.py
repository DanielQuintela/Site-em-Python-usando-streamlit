import streamlit as st
import sqlite3

con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

st.title("Tela Cadastro :3")

with st.form(key='include_cliente'):
    input_name = st.text_input(label='Insira o seu nome')
    input_senha = st.text_input(label='Insira a senha', type="password"  )
    input_occupation = st.selectbox('selecione sua profissão', ['Gerente', 'Pesquisador'])
    input_button_enviar = st.form_submit_button("Enviar Dados")

if input_button_enviar:
    st.write(f'Nome{input_name}')
    cursor.execute(f"INSERT INTO cadastro VALUES ('{input_name}','{input_senha}','{input_occupation}')")
    con.commit()

    
