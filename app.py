import streamlit as st

st.title("Adivinhe seu signo")

birthDate = st.date_input("escolha sua data de nascimento")

sendForm = st.button("enviar")

if sendForm:
    with open("datas.csv", "a") as datasFile:
        datasFile.write(f"{birthDate},\n ")
        st.success("gravado com sucesso")