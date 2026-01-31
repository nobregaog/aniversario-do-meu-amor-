import streamlit as st
import time

mensagem = (
    "oi meu amor feliz aniversario!!!\n"
    "tomara que voce goste do presente :b\n"
    "que seu dia seja maravilhoso e que sua vida seja repleta de benças.\n"
    "espero que voce aproveite muito seu dia e que vc nunca esqueça que eu te amo!\n"
)

st.write(mensagem)

senha = st.text_input("Digite a senha enviada pelo WhatsApp", type="password")

if senha == "040209":
    st.write("Senha correta, esta preparada?")
    resposta = st.text_input("Preparada para a surpresa?").lower()

    if resposta in ["sim", "simmm", "s", "logico"]:
        if st.button("Começar surpresa"):
            for i in range(3, 0, -1):
                st.write(i)
                time.sleep(1)

            st.write("FECHE OS OLHOS E ABRA AS MAOS")

    elif resposta != "":
        st.write("Certeza?")

elif senha != "":
    st.write("Senha incorreta, tente novamente!")