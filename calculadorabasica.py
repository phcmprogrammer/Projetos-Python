import streamlit as st
st.title("Calculadora Básica")
numero01 = st.number_input(label="Número 1:")
numero02 = st.number_input(label="Número 2:")
if st.button("SOMA"):
    st.write(f"{numero01 + numero02}")
if st.button("SUBTRAÇÃO"):
    st.write(f"{numero01 - numero02}")
if st.button("MULTIPLICAÇÃO"):
    st.write(f"{numero01 * numero02}")
if st.button("DIVISÃO"):
    st.write(f"{numero01 / numero02}")


