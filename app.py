import streamlit as st
import time

# Configuração da página
st.set_page_config(
    page_title="Surpresa de Aniversário",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Fundo e fonte usando CSS
st.markdown(
    """
    <style>
    body {
        background-color: #ffe6e6;  /* Fundo rosa claro */
        color: #333333;              /* Cor do texto */
        font-family: 'Arial', sans-serif;
    }
    .big-text {
        font-size: 30px;
        text-align: center;
        font-weight: bold;
    }
    .medium-text {
        font-size: 22px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Mensagem inicial centralizada
st.markdown("<div class='big-text'>Oi meu amor, feliz aniversário!!!</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='medium-text'>Tomara que você goste do presente.<br>"
    "Que seu dia seja maravilhoso e que sua vida seja repleta de bênçãos.<br>"
    "Espero que você aproveite muito seu dia e que nunca esqueça que eu te amo!</div>",
    unsafe_allow_html=True
)

# Entrada da senha
senha = st.text_input("Digite a senha enviada pelo WhatsApp", type="password")

if senha == "040209":
    st.write("Senha correta, está preparada?")
    resposta = st.text_input("Preparada para a surpresa?").lower()

    if resposta in ["sim", "simmm", "s", "logico"]:
        if st.button("Começar surpresa"):
            # Contagem regressiva centralizada
            for i in range(3, 0, -1):
                st.markdown(f"<h1 style='text-align: center;'>{i}</h1>", unsafe_allow_html=True)
                time.sleep(1)

            # Mensagem final centralizada e grande
            st.markdown("<h2 style='text-align: center;'>FECHE OS OLHOS E ABRA AS MAOS</h2>", unsafe_allow_html=True)

    elif resposta != "":
        st.write("Certeza?")

elif senha != "":
    st.write("Senha incorreta, tente novamente!")
