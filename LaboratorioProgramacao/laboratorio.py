import streamlit as st

st.title('video exemplo')
st.selectbox('Escolhan um ', ['Pilula vermelha','Pilula Azul'])
st.sidebar.title('menu')
st.sidebar.selectbox('Oi meu chapa', ['Para a pagina 2', 'Para a pagina 3'])
number = st.slider("Pick a number", 0, 100)