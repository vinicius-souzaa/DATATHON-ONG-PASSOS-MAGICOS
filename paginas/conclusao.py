import streamlit as st
from util.layout import layout_saida

st.set_page_config(
    page_title="Conclusão | Tech Challenge 4",
    layout="wide",
    page_icon="☁️"
)
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
    st.header(":blue[Conclusão]", divider="blue")
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
        O presente projeto teve como objetivo analisar e prever o impacto 
        da ONG Passos Mágicos na vida educacional de crianças e jovens em 
        situação de vulnerabilidade social. Utilizando um extenso conjunto 
        de dados educacionais e socioeconômicos dos anos de 2020 a 2022, 
        foram realizadas análises estatísticas e desenvolvidos modelos 
        preditivos para compreender a evolução dos alunos atendidos pela 
        instituição.
    </p>

    <p class="special-indent">
        As análises revelaram que, apesar dos desafios impostos pela 
        pandemia de COVID-19, houve uma recuperação significativa no 
        desempenho educacional dos alunos em 2022. Indicadores como o INDE, 
        IAA, IEG e IDA mostraram melhorias, evidenciando a eficácia das 
        intervenções da Passos Mágicos. Notou-se que alunos bolsistas 
        apresentaram desempenho superior e maior probabilidade de atingir 
        pontos de virada, indicando o impacto positivo do suporte financeiro 
        e educacional oferecido.
    </p>

    <p class="special-indent">
        A análise dos "Tipos de Pedras" demonstrou que houve um aumento no 
        número de alunos classificados nas categorias de desempenho mais 
        elevado (Ametista e Topázio), especialmente em 2022. Isso sugere 
        que os programas da ONG estão contribuindo para o avanço educacional 
        contínuo dos alunos. Além disso, a análise por gênero e idade revelou 
        que meninas tendem a apresentar maior autoconfiança e engajamento, 
        enquanto meninos mostraram ligeira vantagem em desempenho acadêmico.
    </p>

    <p class="special-indent">
        Os motivos de evasão identificados, como falta de retorno ao contato 
        e mudanças de residência, destacam a importância de estratégias de 
        retenção e suporte logístico. A análise preditiva do INDE, 
        com um modelo de rede neural que alcançou um R² de 0,9462, 
        reforça a capacidade de prever o desempenho dos alunos com alta 
        precisão, permitindo intervenções mais direcionadas.
    </p>

    <p class="special-indent">
        Os insights gerados pelo modelo preditivo e pelas análises 
        estatísticas apontam para a necessidade de intensificar o suporte 
        psicossocial e psicopedagógico, especialmente para alunos que 
        enfrentam maiores desafios. A ONG pode se beneficiar ao expandir 
        programas de bolsas e reforçar estratégias de engajamento, 
        visando reduzir a evasão e promover o desenvolvimento educacional 
        sustentável.
    </p>

    <p class="special-indent">
        Em suma, o projeto evidencia o impacto positivo e transformador 
        da Passos Mágicos na vida de seus alunos, ao mesmo tempo em que 
        destaca áreas para melhoria contínua. A combinação de análises 
        detalhadas e modelos preditivos fornece uma base sólida para a ONG 
        tomar decisões informadas, otimizar recursos e ampliar seu alcance, 
        cumprindo assim sua missão de iluminar vidas através da educação.
    </p>
    """, unsafe_allow_html=True)

    
