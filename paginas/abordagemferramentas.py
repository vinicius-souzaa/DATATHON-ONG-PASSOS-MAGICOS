import streamlit as st
from util.layout import layout_saida


st.set_page_config(
    page_title="Metodologia",
    layout="wide",
)

with st.container():
    st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")
    st.header(":red[Abordagem e Ferramentas]", divider='red')
    
    st.markdown(
        """
        <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

        Nesta seção, exploramos os principais aspectos da metodologia 
        aplicada ao desenvolvimento do projeto e as ferramentas tecnológicas 
        que foram fundamentais para sua execução. Através de uma abordagem 
        estruturada, explicamos como os dados foram tratados, analisados e 
        transformados em insights valiosos. Além disso, destacamos as 
        tecnologias e bibliotecas utilizadas para construir modelos preditivos 
        e análises que ajudam a entender o impacto educacional da ONG 
        Passos Mágicos.

        Nossa abordagem foi projetada para garantir que as análises e 
        previsões fossem feitas de maneira rigorosa e eficaz, utilizando 
        processos de validação e otimização contínua. Complementando esse 
        trabalho, ferramentas robustas como Python e bibliotecas especializadas 
        permitiram que cada etapa fosse realizada com precisão, 
        desde o tratamento inicial dos dados até o deploy final em uma 
        interface interativa.</h1>
        """,unsafe_allow_html=True
        )
    
    

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
                        <h1 style='text-align:justify; 
                                    font-size:15px;
                                    font-family: Arial, sans-serif; 
                                    font-weight: normal;
                                    line-height:1.5'>
                    
                Nesta página, explicaremos a metodologia aplicada ao 
                desenvolvimento do projeto preditivo, focado na análise e 
                previsão de desempenho educacional dos alunos da ONG Passos 
                Mágicos. Abaixo, detalhamos os principais passos seguidos no 
                processo.

                **1. Coleta e Tratamento de Dados:**
                    
                O projeto iniciou com a coleta de dados fornecidos pela ONG, 
                    contendo informações sobre desempenho acadêmico, dados 
                    socioeconômicos e indicadores educacionais. Esses dados 
                    foram tratados para remover valores ausentes, corrigir 
                    inconsistências e transformar variáveis categóricas e 
                    numéricas em formatos adequados para análise.

                **2. Exploração e Análise Descritiva:**
                    
                Na etapa de exploração dos dados, foi realizada uma análise 
                descritiva para identificar padrões, correlações e possíveis 
                outliers. Foram utilizados gráficos de distribuição, 
                boxplots, e correlações para entender a relação entre as 
                variáveis educacionais, como o desempenho dos alunos e seus 
                fatores socioeconômicos.

                **3. Criação do Modelo Preditivo:**
                    
                Com os dados preparados, partimos para a construção de 
                um modelo preditivo. Dividimos os dados em conjuntos de 
                treino e teste, garantindo que o modelo fosse treinado 
                em um subconjunto e avaliado em outro para evitar 
                overfitting. Diferentes tipos de modelos foram considerados, 
                incluindo regressão e redes neurais, para prever o desempenho 
                educacional (INDE) e outros indicadores.

                **4. Validação do Modelo:**
                    
                A validação cruzada foi usada para garantir que o modelo 
                tivesse bom desempenho em diferentes subconjuntos dos dados. 
                Este processo permitiu avaliar a consistência dos resultados 
                e ajustar os hiperparâmetros do modelo para maximizar sua 
                precisão.

                **5. Ajustes e Otimizações:**
                    
                Durante a fase de validação, o modelo foi ajustado para 
                otimizar seu desempenho. Técnicas como normalização dos dados,
                eliminação de variáveis irrelevantes e ajuste de camadas e 
                neurônios em redes neurais foram implementadas para melhorar 
                a acurácia e reduzir o erro.

                **6. Deploy do Modelo:**
                    
                Após o desenvolvimento e validação, o modelo foi implementado 
                em produção através de uma aplicação interativa desenvolvida 
                no Streamlit, permitindo que usuários e gestores da ONG 
                visualizem os resultados das previsões e façam consultas 
                dinâmicas aos dados. </h1>  
                
                """, unsafe_allow_html=True)

        

        
    
    with tab1:
        st.subheader(':red[Ferramentas]'
                        , divider='red')
        with st.expander("Python"):
            st.markdown("""
                        <h1 style='text-align:justify; 
                                    font-size:15px;
                                    font-family: Arial, sans-serif; 
                                    font-weight: normal;
                                    line-height:1.5'>
                     A linguagem central do projeto, utilizada para manipulação 
                    de dados, treinamento de modelos e desenvolvimento da 
                    interface do usuário. Python foi escolhido pela sua 
                    versatilidade e pelo rico ecossistema de bibliotecas 
                    voltadas para ciência de dados. 
                        </h1>  
                
                    """, unsafe_allow_html=True)
        with st.expander("VSCode"):
            st.markdown("""
                        <h1 style='text-align:justify; 
                                    font-size:15px;
                                    font-family: Arial, sans-serif; 
                                    font-weight: normal;
                                    line-height:1.5'>
                     O editor de código principal utilizado para desenvolver e 
                    testar o código do projeto. O Visual Studio Code oferece 
                    um ambiente de desenvolvimento integrado (IDE) com 
                    funcionalidades que facilitam a escrita de código e a 
                    gestão de pacotes. 
                        </h1>  
                
                    """, unsafe_allow_html=True)
            
        with st.expander("Pandas"):
            st.markdown("""
                        <h1 style='text-align:justify; 
                                    font-size:15px;
                                    font-family: Arial, sans-serif; 
                                    font-weight: normal;
                                    line-height:1.5'>
                     Essa biblioteca foi essencial para o processamento e 
                    análise de dados. Com ela, foi possível realizar 
                    operações de limpeza, transformação e análise descritiva 
                    de grandes volumes de dados educacionais.
                         </h1>  
                
                    """, unsafe_allow_html=True)
        
        with st.expander("Scikit-learn"):
            st.markdown("""
                        <h1 style='text-align:justify; 
                                    font-size:15px;
                                    font-family: Arial, sans-serif; 
                                    font-weight: normal;
                                    line-height:1.5'>
                     Uma das principais bibliotecas para aprendizado de máquina em Python, Scikit-learn foi usada para dividir os dados em treino e teste, aplicar validação cruzada e construir pipelines de pré-processamento que incluíam normalização e codificação de variáveis. </h1>  
                
                    """, unsafe_allow_html=True)
        
        with st.expander("Keras com TensorFlow"):
            st.markdown("""
                        <h1 style='text-align:justify; 
                                    font-size:15px;
                                    font-family: Arial, sans-serif; 
                                    font-weight: normal;
                                    line-height:1.5'>
                     Para a construção de redes neurais, utilizamos o Keras, que é uma API de alto nível, rodando sobre o TensorFlow. Essa combinação foi utilizada para treinar modelos de redes neurais artificiais para prever o desempenho acadêmico com base em variáveis educacionais e socioeconômicas. </h1>  
                
                    """, unsafe_allow_html=True)
            
        with st.expander("Numpy"):
            st.markdown("""
                        <h1 style='text-align:justify; 
                                    font-size:15px;
                                    font-family: Arial, sans-serif; 
                                    font-weight: normal;
                                    line-height:1.5'>
                     Essa biblioteca foi usada para manipulação de arrays e cálculos numéricos, facilitando operações matemáticas de alto desempenho durante o pré-processamento dos dados e na validação dos modelos.XTO </h1>  
                
                    """, unsafe_allow_html=True)
        
        with st.expander("SciPy"):
            st.markdown("""
                        <h1 style='text-align:justify; 
                                    font-size:15px;
                                    font-family: Arial, sans-serif; 
                                    font-weight: normal;
                                    line-height:1.5'>
                     SciPy foi utilizada para realizar testes estatísticos e outras operações avançadas de manipulação numérica, complementando o trabalho com Numpy e Pandas, principalmente na análise de correlações entre variáveis. </h1>  
                
                    """, unsafe_allow_html=True)

        with st.expander("Streamlit"):
            st.markdown("""
                        <h1 style='text-align:justify; 
                                    font-size:15px;
                                    font-family: Arial, sans-serif; 
                                    font-weight: normal;
                                    line-height:1.5'>
                     Streamlit foi a ferramenta escolhida para criar a interface do projeto, permitindo a criação de uma aplicação interativa onde os resultados das análises e previsões podem ser visualizados de forma dinâmica e acessível.
                
                    """, unsafe_allow_html=True)
        
        with st.expander("Plotly"):
            st.markdown("""
                        <h1 style='text-align:justify; 
                                    font-size:15px;
                                    font-family: Arial, sans-serif; 
                                    font-weight: normal;
                                    line-height:1.5'>
                        A biblioteca Plotly foi utilizada neste projeto para criar visualizações 
                        interativas e atraentes dos dados educacionais e socioeconômicos dos 
                        alunos atendidos pela ONG Passos Mágicos. Ao empregar o Plotly, foi 
                        possível desenvolver gráficos dinâmicos que permitem explorar os 
                        indicadores de desempenho, identificar padrões e tendências ao longo 
                        dos anos, e comparar diferentes grupos de alunos. Essas visualizações 
                        enriquecem a análise dos dados, facilitando a compreensão dos resultados 
                        e auxiliando na comunicação dos insights obtidos, o que é fundamental 
                        para o storytelling e para a tomada de decisões informadas pela ONG.
                        </h1>
                
                    """, unsafe_allow_html=True)
        

    
        
layout_saida()
        
    