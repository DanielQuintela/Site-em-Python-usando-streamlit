import streamlit as st
import sqlite3

con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

st.title("Tela Cadastro")


with st.form(key='include_cliente'):
    input_name = st.text_input(label='Insira o seu nome')
    input_senha = st.text_input(label='Insira a senha', type="password")
    input_occupation = st.selectbox('selecione sua profissão', ['Pesquisador'])
    input_button_enviar = st.form_submit_button("Enviar Dados")

if input_button_enviar:
    cursor.execute(f"INSERT INTO cadastro VALUES ('{input_name}','{input_senha}','{input_occupation}')")
    con.commit()

    st.success('Adicionado com sucesso !!')

