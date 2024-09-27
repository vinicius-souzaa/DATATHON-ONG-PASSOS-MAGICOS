import streamlit as st
import warnings
import locale
from util.layout import layout_saida


warnings.filterwarnings("ignore")
#locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

st.set_page_config(page_title='DATATHON', layout="wide",page_icon="🛠️")

layout_saida()

with st.container():

    st.markdown(
                    body="""
                        <style>
                            .block-container{
                                    padding-top: 25px;
                                }
                        </style>
                    """, 
                    unsafe_allow_html=True
                )

    st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")   
    
    st.title(":blue[DATATHON - ONG PASSOS MAGICOS 🛠️🌍]")

    st.markdown("""""")

    col1,col2 = st.columns(2)

    with col1:
        st.image("imagens/fiap-logo.jpg", width=350)

    with col2:
        st.image("imagens/Passos-magicos-icon-cor.png", width=280)

     
    st.header(":blue[O Problema]",divider="blue")

    st.markdown("""
                <style>
                p.special-indent {
                    text-align: justify;
                    font-size: 15px;
                    font-family: Arial, sans-serif;
                    font-weight: normal;
                    line-height: 1.5;
                    text-indent: 3em;
                    
                }
                </style>
                
                <p class="special-indent">
                    Os estudantes da ONG Passos Mágicos enfrentam desafios socioeducacionais significativos que afetam diretamente suas trajetórias de aprendizagem e desenvolvimento pessoal. Muitos desses jovens vêm de contextos de vulnerabilidade social, com acesso limitado a recursos educacionais de qualidade e suporte psicossocial adequado.
                </p>
                <p class="special-indent">
                    A evasão escolar, as lacunas no desempenho acadêmico e as dificuldades emocionais são problemas recorrentes que comprometem o potencial desses estudantes. A ONG atua para mitigar essas questões, mas a complexidade do ambiente e a diversidade das necessidades dos alunos tornam essencial a análise aprofundada desses impactos para melhor direcionar as intervenções.
                </p>
                """, unsafe_allow_html=True)

    st.subheader(":blue[Objetivo]", divider="blue")

    st.markdown("""
                <style>
                p {
                text-align: justify;
                font-size: 15px;
                font-family: Arial, sans-serif;
                font-weight: normal;
                line-height: 1.5;
                text-indent: 20px;
                }
                </style>
                
                <p class="special-indent">
                    O objetivo principal deste projeto é utilizar análises descritivas e preditivas para quantificar e demonstrar o impacto das intervenções da ONG Passos Mágicos no desempenho e desenvolvimento dos estudantes. O projeto visa identificar padrões e correlações nos dados educacionais e socioeconômicos, permitindo uma compreensão mais clara de como diferentes fatores contribuem para o sucesso ou dificuldades dos alunos. Com estas análises, a ONG poderá refinar suas estratégias e programas para melhor atender às necessidades de sua população estudantil, maximizando o impacto positivo em suas vidas.
                </p>
                """, unsafe_allow_html=True)



    st.subheader(":blue[Desafio]", divider="blue")

    st.markdown("""
                <style>
                p {
                text-align: justify;
                font-size: 15px;
                font-family: Arial, sans-serif;
                font-weight: normal;
                line-height: 1.5;
                text-indent: 20px;
                }
                </style>
                
                <p class="special-indent">
                    Os desafios associados à análise dos dados da ONG são múltiplos e complexos. Primeiramente, a qualidade e a integridade dos dados podem variar, exigindo processos rigorosos de limpeza e preparação dos dados antes da análise. Além disso, a interpretação dos dados é complicada pela natureza multifacetada dos fatores que influenciam o desempenho educacional, incluindo variáveis socioeconômicas, psicológicas e acadêmicas que estão frequentemente inter-relacionadas. Outro desafio significativo é a criação de modelos preditivos que sejam robustos e adaptáveis às mudanças no perfil dos alunos e nas condições externas ao longo do tempo. Por fim, garantir que as análises e insights sejam traduzidos em ações práticas e eficazes que alinhem-se com os objetivos e capacidades operacionais da ONG requer uma estreita colaboração entre analistas de dados, educadores e gestores.
                </p>
                """, unsafe_allow_html=True)


