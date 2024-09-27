import streamlit as st
import locale
from st_pages import show_pages, Page


def format_number(number, format='%0.0f'):
    return locale.format(format, number, grouping=True)

def layout_saida():
       
    show_pages(
        [
            Page("./main.py", "Datathon", "🛠️"),
            Page("./paginas/ONG.py","ONG Passos Magicos", "🌍"),
            Page("./paginas/abordagemferramentas.py","Abordagem e Ferramentas", "📚"),
            Page("./paginas/analiseeda.py","Analise Exploratória de Dados", "📊"),
            Page("./paginas/modelo.py", "Modelo Preditivo", "💻"),
            Page("./paginas/conclusao.py","Conclusão","☁️"),
        ]
    )

    st.markdown("""
                <style>
                    [data-testid=stSidebar] {
                        background-color: #ff000050;
                    }
                </style>
                """, unsafe_allow_html=True)
        
    with st.sidebar:
        st.subheader("Alunos - Grupo 22 - Turma 3DTAT")
        
        st.markdown("""
                    <h1 style=font-size:16px; 
                    font-family: Arial, sans-serif; 
                    font-weight: normal;>

                    Vinicius Abreu Ernestino Souza\n
                    RM 353049\n
                    Fernando Abud Rojas Marin\n
                    RM353098
                    </h1>
                    """, unsafe_allow_html=True)
       
        
        

