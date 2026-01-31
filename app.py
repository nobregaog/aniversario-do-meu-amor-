import streamlit as st
import time

# Configuração da página
st.set_page_config(
    page_title="Surpresa de Aniversário",
    layout="centered"
)

# Mensagem inicial (centralizada e maior)
st.markdown(
    "<h2 style='text-align: center;'>oi meu amor feliz aniversario!!!</h2>"
    "<p style='text-align: center;'>tomara que voce goste do presente<br>"
    "que seu dia seja maravilhoso e que sua vida seja repleta de benças.<br>"
    "espero que voce aproveite muito seu dia e que vc nunca esqueça que eu te amo!</p>",
    unsafe_allow_html=True
)

# Entrada da senha
senha = st.text_input("Digite a senha enviada pelo WhatsApp", type="password")

if senha == "040209":
    st.write("Senha correta, esta preparada?")
    resposta = st.text_input("Preparada para a surpresa?").lower()

    if resposta in ["sim", "simmm", "s", "logico"]:
        if st.button("Começar surpresa"):
            # Contagem regressiva centralizada
            for i in range(3, 0, -1):
                st.markdown(f"<h1 style='text-align: center;'>{i}</h1>", unsafe_allow_html=True)
                time.sleep(1)

            # Mensagem final centralizada
            st.markdown(
                "<h2 style='text-align: center;'>FECHE OS OLHOS E ABRA AS MAOS</h2>",
                unsafe_allow_html=True
            )

    elif resposta != "":
        st.write("Certeza?")

elif senha != "":
    st.write("Senha incorreta, tente novamente!")
