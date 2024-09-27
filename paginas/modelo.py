import streamlit as st
from util.layout import layout_saida

st.set_page_config(
    page_title="Modelo Preditivo | Tech Challenge 4",
    layout="wide",
    page_icon="💻"
)
layout_saida()

with st.container():
    st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")   
    st.header(":red[Prevendo o Índice de Desenvolvimento Educacional] 💻")
    st.subheader(f":red[Objetivo]", divider="red")
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
                    Este modelo preditivo foi desenvolvido para prever o <strong>INDE - Índice de Desenvolvimento Educacional</strong> dos alunos da Passos Mágicos, com base em variáveis educacionais e socioeconômicas. A escolha das variáveis e metodologia busca fornecer uma análise robusta que auxilie a ONG a entender melhor os fatores que influenciam o desempenho dos alunos, permitindo intervenções mais direcionadas.
                </p>
                """, unsafe_allow_html=True)

    st.subheader(f":red[Metodologia]", divider="red")
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
                small {
                    font-size: 12px;
                }
                </style>

                <p class="special-indent">
                    O modelo foi criado utilizando uma rede neural, com camadas densas e dropout para regularização, em um pipeline que processa variáveis numéricas e categóricas. A combinação de Machine Learning e Deep Learning foi escolhida pela sua capacidade de identificar padrões complexos em dados heterogêneos, como os relacionados à educação e ao desempenho psicológico dos alunos.
                </p>
                
                <strong>Variáveis Utilizadas no Modelo</strong><br>

                <strong>Categóricas:</strong><br>

                <small>- INSTITUICAO_ENSINO_ALUNO_2020,</small><br> 
                <small>- BOLSISTA_2022,</small><br>
                <small>- PEDRA_2022,</small><br>
                <small>- NOTA_PORT_2022,</small><br> 
                <small>- NOTA_MAT_2022,</small><br>
                <small>- NOTA_ING_2022,</small><br>
                <small>- PONTO_VIRADA_2022</small><br>

                <strong>Numéricas:</strong><br>

                <small>- IDADE_ALUNO_2020,</small><br>
                <small>- ANO_INGRESSO_2022,</small><br>
                <small>- QTD_AVAL_2022,</small><br>
                <small>- IEG_2022,</small><br>
                <small>- IPS_2022,</small><br>
                <small>- IAA_2022,</small><br>
                <small>- IDA_2022,</small><br>
                <small>- IPP_2022,</small><br>
                <small>- IPV_2022,</small><br>
                <small>- FASE_2022</small><br>

                <p class="special-indent">
                    O pré-processamento inclui tratamento de valores faltantes (imputação) e escalonamento dos dados numéricos, além de codificação das variáveis categóricas.
                </p>
                """, unsafe_allow_html=True)

    st.subheader(f":red[Desempenho do Modelo]", divider="red")
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
                    O modelo apresentou os seguintes resultados durante a validação cruzada:
                </p>

                <strong>RMSE (Root Mean Squared Error): 0.2473</strong><br>
                <p class="special-indent">
                    O RMSE indica o quão distantes, em média, estão as previsões do modelo em relação aos valores reais do INDE_2022. Um valor menor indica previsões mais precisas.
                </p>

                <strong>MAE (Mean Absolute Error): 0.1916</strong><br>
                <p class="special-indent">
                    O MAE mede a média dos erros absolutos entre as previsões e os valores reais. Como no caso do RMSE, valores mais baixos indicam um melhor ajuste do modelo aos dados.
                </p>

                <strong>MAPE (Mean Absolute Percentage Error): 2.91%</strong><br>
                <p class="special-indent">
                    O MAPE mostra o erro percentual médio entre os valores previstos e reais. Um valor de 2.91% significa que, em média, o modelo erra em 2.91% a previsão do INDE.
                </p>

                <strong>R² (Coeficiente de Determinação): 0.9462</strong><br>
                <p class="special-indent">
                    O R² indica a proporção da variabilidade dos dados que o modelo consegue explicar. Um valor de 0.9462 significa que o modelo explica cerca de 94.62% da variação no INDE_2022, o que é um resultado muito robusto.
                </p>
                """, unsafe_allow_html=True)

    st.subheader(f":red[Testes com Outras Variáveis]", divider="red")
    
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
                    Outras variáveis, como indicadores de feedback e recomendações das equipes avaliadoras, foram testadas no modelo, mas os resultados foram inferiores. Com variáveis como:
                </p>

                <small><strong>'DESTAQUE_IEG_2020',</strong></small><br>
                <small><strong>'DESTAQUE_IDA_2020',</strong></small><br>
                <small><strong>'DESTAQUE_IPV_2020',</strong></small><br>
                <small><strong>'REC_EQUIPE_1_2021',</strong></small><br>
                <small><strong>'REC_EQUIPE_2_2021',</strong></small><br>
                <small><strong>'REC_EQUIPE_3_2021',</strong></small><br>
                <small><strong>'REC_EQUIPE_4_2021',</strong></small><br>
                <small><strong>'REC_AVA_1_2022',</strong></small><br>
                <small><strong>'REC_AVA_2_2022',</strong></small><br>
                <small><strong>'REC_AVA_3_2022',</strong></small><br>
                <small><strong>'REC_AVA_4_2022'</strong></small><br>

                <p class="special-indent">
                    <strong>RMSE: 0.2787</strong> - 
                    <strong>MAE: 0.2022</strong> - 
                    <strong>MAPE: 3.17%</strong> - 
                    <strong>R²: 0.9321</strong>
                </p>

                <p class="special-indent">
                    Esses resultados indicam que essas variáveis não contribuíram significativamente para melhorar a performance do modelo.
                </p>
                """, unsafe_allow_html=True)

        
    st.subheader(f":red[Insights Gerados pelo Modelo]", divider="red")
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
                    <strong>Intervenções Personalizadas:</strong> 
                    O modelo pode ajudar a identificar os fatores mais relevantes para o desempenho dos alunos, permitindo que a ONG Passos Mágicos direcione recursos e intervenções de forma mais eficaz, como suporte psicopedagógico ou acompanhamento psicológico específico para determinados grupos.
                </p>

                <p class="special-indent">
                    <strong>Análise de Bolsistas:</strong> 
                    Variáveis como BOLSISTA_2022 podem revelar se o apoio financeiro tem impacto direto no desempenho educacional, ajudando a ONG a otimizar os programas de bolsas.
                </p>

                <p class="special-indent">
                    <strong>Avaliação do Ponto de Virada:</strong> 
                    O campo PONTO_VIRADA_2022 sinaliza se o aluno atingiu um marco de mudança significativa. O modelo pode prever quais alunos estão mais próximos de alcançar este marco, permitindo intervenções antecipadas.
                </p>
                """, unsafe_allow_html=True)

    
    st.subheader(f":red[Sugestões de Melhoria]", divider="red")
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
                    <strong>Criação de Novas Variáveis:</strong> 
                    A inclusão de variáveis temporais ou que capturem a evolução contínua do desempenho pode melhorar a previsibilidade. Por exemplo, calcular a evolução ano a ano dos indicadores como IAA e IPS, e criar métricas de "taxa de progresso".
                </p>

                <p class="special-indent">
                    <strong>Engenharia de Features Avançada:</strong> 
                    Combinar indicadores (como uma média ponderada entre desempenho acadêmico e envolvimento psicossocial) pode aumentar a precisão.
                </p>

                <p class="special-indent">
                    <strong>Modelagem com Redes Neurais mais Profundas:</strong> 
                    Testar redes mais profundas ou adicionar camadas adicionais pode capturar melhor as interações complexas entre as variáveis.
                </p>
                """, unsafe_allow_html=True)

    
    st.subheader(f":red[Conclusão sobre o Modelo]", divider="red")
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
                    O modelo preditivo desenvolvido alcançou resultados expressivos, demonstrando sua capacidade de prever o INDE_2022 com precisão. Ele oferece à Passos Mágicos uma ferramenta valiosa para prever o sucesso dos alunos e ajustar suas ações para maximizar o impacto educacional e social.
                </p>
                """, unsafe_allow_html=True)

    
    

    
    


    
