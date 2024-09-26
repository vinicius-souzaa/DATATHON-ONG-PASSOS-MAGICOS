import streamlit as st
from util.layout import layout_saida

st.set_page_config(
    page_title="Modelo Preditivo | Tech Challenge 4",
    layout="wide",
)
layout_saida()

with st.container():
    st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")   
    st.header(":red[Prevendo o Índice de Desenvolvimento Educacional]")
    st.subheader(f":red[Objetivo]", divider="red")
    st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
        Este modelo preditivo foi desenvolvido para prever o **INDE - 
        o Índice de Desenvolvimento Educacional** dos alunos da Passos Mágicos, 
        com base em variáveis educacionais e socioeconômicas. A escolha das 
        variáveis e metodologia busca fornecer uma análise robusta que auxilie 
        a ONG a entender melhor os fatores que influenciam o desempenho dos alunos,
        permitindo intervenções mais direcionadas.
                
        </h1>
            """,unsafe_allow_html=True,
            )
    st.subheader(f":red[Metodologia]", divider="red")
    st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
        O modelo foi criado utilizando uma rede neural, com camadas densas 
        e dropout para regularização, em um pipeline que processa variáveis 
        numéricas e categóricas. A combinação de Machine Learning e 
        Deep Learning foi escolhida pela sua capacidade de identificar 
        padrões complexos em dados heterogêneos, como os relacionados à 
        educação e ao desempenho psicológico dos alunos.

        **Variáveis Utilizadas no Modelo**

        **Categóricas:**
                
        <small>**-INSTITUICAO_ENSINO_ALUNO_2020,**</small> 
                
        <small>**-BOLSISTA_2022,**</small>
                
        <small>**-PEDRA_2022,**</small>
                 
        <small>**-NOTA_PORT_2022,**</small> 
                
        <small>**-NOTA_MAT_2022,**</small>
                 
        <small>**-NOTA_ING_2022,**</small>
                 
        <small>**-PONTO_VIRADA_2022**</small>
                
        **Numéricas:**
                
        <small>**-IDADE_ALUNO_2020,**</small>
                 
        <small>**-ANO_INGRESSO_2022,**</small>
                 
        <small>**-QTD_AVAL_2022,**</small>
                 
        <small>**-IEG_2022,**</small>
                
        <small>**-IPS_2022,**</small>
                
        <small>**-IAA_2022,**</small>
                 
        <small>**-IDA_2022,**</small> 
                
        <small>**-IPP_2022,**</small>
                 
        <small>**-IPV_2022,**</small>
                 
        <small>**-FASE_2022**</small>
                
        O pré-processamento inclui tratamento de valores faltantes 
        (imputação) e escalonamento dos dados numéricos, além de codificação 
        das variáveis categóricas.
        </h1>
            """,unsafe_allow_html=True,
            )
    st.subheader(f":red[Desempenho do Modelo]", divider="red")
    st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
        O modelo apresentou os seguintes resultados durante a validação 
                cruzada:

        **RMSE (Root Mean Squared Error): 0.2473**
                
        O RMSE indica o quão distantes, em média, estão as previsões 
        do modelo em relação aos valores reais do INDE_2022. 
        Um valor menor indica previsões mais precisas.

        **MAE (Mean Absolute Error): 0.1916**
                
        O MAE mede a média dos erros absolutos entre as previsões e os valores 
        reais. Como no caso do RMSE, valores mais baixos indicam um melhor
        ajuste do modelo aos dados.

        **MAPE (Mean Absolute Percentage Error): 2.91%**
                
        O MAPE mostra o erro percentual médio entre os valores previstos 
        e reais. Um valor de 2.91% significa que, em média, o modelo 
        erra em 2.91% a previsão do INDE.

        **R² (Coeficiente de Determinação): 0.9462**
                
        O R² indica a proporção da variabilidade dos dados que o modelo 
        consegue explicar. Um valor de 0.9462 significa que o modelo 
        explica cerca de 94.62% da variação no INDE_2022, o que é um 
        resultado muito robusto. 
            
        </h1>
            """,unsafe_allow_html=True,
            )
    st.subheader(f":red[Testes com Outras Variáveis]", divider="red")
    st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
        Outras variáveis, como indicadores de feedback e recomendações das 
        equipes avaliadoras, foram testadas no modelo, mas os resultados 
        foram inferiores. Com variáveis como 
                
        <small>**'DESTAQUE_IEG_2020',**</small>
                
        <small>**'DESTAQUE_IDA_2020',**</small>
                
        <small>**'DESTAQUE_IPV_2020',**</small>
                            
        <small>**'REC_EQUIPE_1_2021',**</small>
                
        <small>**'REC_EQUIPE_2_2021',**</small>
                
        <small>**'REC_EQUIPE_3_2021',**</small>
                
        <small>**'REC_EQUIPE_4_2021',**</small>
                
        <small>**'REC_AVA_1_2022',**</small>
                
        <small>**'REC_AVA_2_2022',**</small>
                
        <small>**'REC_AVA_3_2022',**</small>
                
        <small>**'REC_AVA_4_2022'**</small>

        **RMSE: 0.2787 -
        MAE: 0.2022 -
        MAPE: 3.17% -
        R²: 0.9321**
                
        Esses resultados indicam que essas variáveis não contribuíram 
        significativamente para melhorar a performance do modelo
                </h1>
            
            """,unsafe_allow_html=True,
            )
        
    st.subheader(f":red[Insights Gerados pelo Modelo]", divider="red")
    st.markdown("""
                <h1 style='text-align:justify; 
                font-size:15px;
                font-family: Arial, sans-serif; 
                font-weight: normal;
                line-height:1.5'>
                    
                **Intervenções Personalizadas:** 
                
                O modelo pode ajudar a identificar os fatores mais relevantes 
                para o desempenho dos alunos, permitindo que a ONG Passos 
                Mágicos direcione recursos e intervenções de forma mais eficaz, 
                como suporte psicopedagógico ou acompanhamento psicológico 
                específico para determinados grupos.

                **Análise de Bolsistas:** 
                
                Variáveis como BOLSISTA_2022 podem revelar se o apoio financeiro 
                tem impacto direto no desempenho educacional, ajudando a ONG 
                a otimizar os programas de bolsas.

                **Avaliação do Ponto de Virada:** 
                
                O campo PONTO_VIRADA_2022 
                sinaliza se o aluno atingiu um marco de mudança significativa. 
                O modelo pode prever quais alunos estão mais próximos de 
                alcançar este marco, permitindo intervenções antecipadas.
                </h1>
            
                """,unsafe_allow_html=True,
                )
    
    st.subheader(f":red[Sugestões de Melhoria]", divider="red")
    st.markdown("""
                <h1 style='text-align:justify; 
                font-size:15px;
                font-family: Arial, sans-serif; 
                font-weight: normal;
                line-height:1.5'>
                    
                **Criação de Novas Variáveis:** 
                
                A inclusão de variáveis temporais 
                ou que capturem a evolução contínua do desempenho pode melhorar 
                a previsibilidade. Por exemplo, calcular a evolução ano a ano 
                dos indicadores como IAA e IPS, e criar métricas de "taxa de 
                progresso".

                **Engenharia de Features Avançada:** 
                
                Combinar indicadores (como uma média ponderada entre desempenho 
                acadêmico e envolvimento psicossocial) pode aumentar a precisão.

                **Modelagem com Redes Neurais mais Profundas:** 
                
                Testar redes mais profundas ou adicionar camadas adicionais 
                pode capturar melhor as interações complexas entre as variáveis.
                </h1>
            
                """,unsafe_allow_html=True,
                )
    
    st.subheader(f":red[Conclusão]", divider="red")
    st.markdown("""
                <h1 style='text-align:justify; 
                font-size:15px;
                font-family: Arial, sans-serif; 
                font-weight: normal;
                line-height:1.5'>
                    
                O modelo preditivo desenvolvido alcançou resultados expressivos, 
                demonstrando sua capacidade de prever o INDE_2022 com precisão. 
                Ele oferece à Passos Mágicos uma ferramenta valiosa para prever 
                o sucesso dos alunos e ajustar suas ações para maximizar o 
                impacto educacional e social.
                </h1>
            
                """,unsafe_allow_html=True,
                )
    
    

    
    


    