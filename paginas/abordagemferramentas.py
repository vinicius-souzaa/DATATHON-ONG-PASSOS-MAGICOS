import streamlit as st
from util.layout import layout_saida


st.set_page_config(
    page_title="Metodologia",
    layout="wide",
    page_icon="📚"
)

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

    st.header(":red[Abordagem e Ferramentas 📚]", divider='red')
    
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
                    Nesta seção, exploramos os principais aspectos da metodologia aplicada ao desenvolvimento do projeto e as ferramentas tecnológicas que foram fundamentais para sua execução. Através de uma abordagem estruturada, explicamos como os dados foram tratados, analisados e transformados em insights valiosos. Além disso, destacamos as tecnologias e bibliotecas utilizadas para construir modelos preditivos e análises que ajudam a entender o impacto educacional da ONG Passos Mágicos.
                </p>
                
                <p class="special-indent">
                    Nossa abordagem foi projetada para garantir que as análises e previsões fossem feitas de maneira rigorosa e eficaz, utilizando processos de validação e otimização contínua. Complementando esse trabalho, ferramentas robustas como Python e bibliotecas especializadas permitiram que cada etapa fosse realizada com precisão, desde o tratamento inicial dos dados até o deploy final em uma interface interativa.
                </p>
                """, unsafe_allow_html=True)
    
    

    tab0, tab1 = st.tabs(
        tabs=[
            "Metodologia",
            "Ferramentas",
            
            
        ]
    )

    with tab0:
        st.subheader(':red[Metodologia]'
                         , divider='red')
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
        Nesta página, explicaremos a metodologia aplicada ao desenvolvimento do projeto preditivo, focado na análise e previsão de desempenho educacional dos alunos da ONG Passos Mágicos. Abaixo, detalhamos os principais passos seguidos no processo.
    </p>
    
    
    <strong>1. Coleta e Tratamento de Dados:</strong><br>
    <p class="special-indent">
        O projeto iniciou com a coleta de dados fornecidos pela ONG, contendo informações sobre desempenho acadêmico, dados socioeconômicos e indicadores educacionais. Esses dados foram tratados para remover valores ausentes, corrigir inconsistências e transformar variáveis categóricas e numéricas em formatos adequados para análise.
    </p>
    
    
    <strong>2. Exploração e Análise Descritiva:</strong><br>
    <p class="special-indent">
        Na etapa de exploração dos dados, foi realizada uma análise descritiva para identificar padrões, correlações e possíveis outliers. Foram utilizados gráficos de distribuição, boxplots, e correlações para entender a relação entre as variáveis educacionais, como o desempenho dos alunos e seus fatores socioeconômicos.
    </p>
    
    
    <strong>3. Criação do Modelo Preditivo:</strong><br>
    <p class="special-indent">
        Com os dados preparados, partimos para a construção de um modelo preditivo. Dividimos os dados em conjuntos de treino e teste, garantindo que o modelo fosse treinado em um subconjunto e avaliado em outro para evitar overfitting. Diferentes tipos de modelos foram considerados, incluindo regressão e redes neurais, para prever o desempenho educacional (INDE) e outros indicadores.
    </p>
    
    
    <strong>4. Validação do Modelo:</strong><br>
    <p class="special-indent">
        A validação cruzada foi usada para garantir que o modelo tivesse bom desempenho em diferentes subconjuntos dos dados. Este processo permitiu avaliar a consistência dos resultados e ajustar os hiperparâmetros do modelo para maximizar sua precisão.
    </p>
    
    
    <strong>5. Ajustes e Otimizações:</strong><br>
    <p class="special-indent">
        Durante a fase de validação, o modelo foi ajustado para otimizar seu desempenho. Técnicas como normalização dos dados, eliminação de variáveis irrelevantes e ajuste de camadas e neurônios em redes neurais foram implementadas para melhorar a acurácia e reduzir o erro.
    </p>
    
    <strong>6. Deploy do Modelo:</strong><br>
    <p class="special-indent">
        Após o desenvolvimento e validação, o modelo foi implementado em produção através de uma aplicação interativa desenvolvida no Streamlit, permitindo que usuários e gestores da ONG visualizem os resultados das previsões e façam consultas dinâmicas aos dados.
    </p>
    """, unsafe_allow_html=True)

        

        
    
    with tab1:
        st.subheader(':red[Ferramentas]'
                        , divider='red')
        with st.expander("Python"):
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
                            A linguagem central do projeto, utilizada para manipulação de dados, treinamento de modelos e desenvolvimento da interface do usuário. <strong>Python</strong> foi escolhido pela sua versatilidade e pelo rico ecossistema de bibliotecas voltadas para ciência de dados.
                        </p>
                        """, unsafe_allow_html=True)
        with st.expander("VSCode"):
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
                            O editor de código principal utilizado para desenvolver e testar o código do projeto. O <strong>Visual Studio Code</strong> oferece um ambiente de desenvolvimento integrado (IDE) com funcionalidades que facilitam a escrita de código e a gestão de pacotes.
                        </p>
                        """, unsafe_allow_html=True)
            
        with st.expander("Pandas"):
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
                            Essa biblioteca foi essencial para o processamento e análise de dados. Com ela, foi possível realizar operações de limpeza, transformação e análise descritiva de grandes volumes de dados educacionais.
                        </p>
                        """, unsafe_allow_html=True)
        
        with st.expander("Scikit-learn"):
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
                            Uma das principais bibliotecas para aprendizado de máquina em Python, <strong>Scikit-learn</strong> foi usada para dividir os dados em treino e teste, aplicar validação cruzada e construir pipelines de pré-processamento que incluíam normalização e codificação de variáveis.
                        </p>
                        """, unsafe_allow_html=True)
        
        with st.expander("Keras com TensorFlow"):
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
                            Para a construção de redes neurais, utilizamos o <strong>Keras</strong>, que é uma API de alto nível, rodando sobre o <strong>TensorFlow</strong>. Essa combinação foi utilizada para treinar modelos de redes neurais artificiais para prever o desempenho acadêmico com base em variáveis educacionais e socioeconômicas.
                        </p>
                        """, unsafe_allow_html=True)
            
        with st.expander("Numpy"):
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
                            Essa biblioteca foi usada para manipulação de arrays e cálculos numéricos, facilitando operações matemáticas de alto desempenho durante o pré-processamento dos dados e na validação dos modelos.
                        </p>
                        """, unsafe_allow_html=True)
        
        with st.expander("SciPy"):
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
                            SciPy foi utilizada para realizar testes estatísticos e outras operações avançadas de manipulação numérica, complementando o trabalho com <strong>Numpy</strong> e <strong>Pandas</strong>, principalmente na análise de correlações entre variáveis.
                        </p>
                        """, unsafe_allow_html=True)

        with st.expander("Streamlit"):
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
                            Fazer a mesma coisa para esse markdown, notar que as palavras que estão entre <strong>**</strong> são palavras que precisam estar em negrito. Trocar <strong>&lt;h1&gt;</strong> por <strong>&lt;p&gt;</strong> e adicionar o estilo abaixo:
                        </p>
                        
                        """, unsafe_allow_html=True)
        
        with st.expander("Plotly"):
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
                            A biblioteca <strong>Plotly</strong> foi utilizada neste projeto para criar visualizações interativas e atraentes dos dados educacionais e socioeconômicos dos alunos atendidos pela ONG Passos Mágicos. Ao empregar o <strong>Plotly</strong>, foi possível desenvolver gráficos dinâmicos que permitem explorar os indicadores de desempenho, identificar padrões e tendências ao longo dos anos, e comparar diferentes grupos de alunos. Essas visualizações enriquecem a análise dos dados, facilitando a compreensão dos resultados e auxiliando na comunicação dos insights obtidos, o que é fundamental para o storytelling e para a tomada de decisões informadas pela ONG.
                        </p>
                        """, unsafe_allow_html=True)
        

    
        
layout_saida()
        
    
