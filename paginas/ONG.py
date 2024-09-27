import streamlit as st
from util.layout import layout_saida


st.set_page_config(
    page_title="ONG PASSOS MAGICOS",
    layout="wide",
    page_icon="🌍"
)


with st.container():
    st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

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
    
    col1,_,col2 = st.columns(3)

    with col1:
        st.markdown("""
                <h1 style='white-space: nowrap; color: red;'>
                    ONG - PASSOS MAGICOS 🌍
                </h1>
            """, unsafe_allow_html=True)

    with col2:
        st.image("imagens/Passos-magicos-icon-cor.png", width=200)

    
    
    st.subheader(':red[Historia]'
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
                    Fundada em 1992 por Michelle Flues e Dimitri Ivanoff, a Associação Passos Mágicos nasceu com o propósito de transformar a vida de crianças e jovens em situação de vulnerabilidade no município de Embu-Guaçu, São Paulo. Inicialmente, a organização atuava em orfanatos, oferecendo apoio educacional e psicossocial. Com o passar do tempo, o impacto positivo das suas ações cresceu, e em 2016, a Passos Mágicos se consolidou como um projeto social e educacional abrangente. A ONG passou a oferecer não apenas educação de qualidade, mas também suporte psicológico, psicopedagógico e atividades culturais, ampliando a visão de mundo dos jovens e fomentando o protagonismo juvenil.
                </p>
                <p class="special-indent">
                    Hoje, com mais de 30 anos de atuação, a Passos Mágicos continua a transformar vidas, com programas voltados para a aceleração do conhecimento, a integração sociocultural e o desenvolvimento integral dos alunos. A ONG tem sido um farol de esperança para centenas de jovens, oferecendo-lhes novas oportunidades através da educação e de uma abordagem centrada no ser humano.
                </p>
                """, unsafe_allow_html=True)

    

    


    st.subheader(':red[Missão e Valores]'
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
                    A missão da Passos Mágicos é proporcionar uma educação de qualidade e holística para crianças e jovens de baixa renda, capacitando-os para enfrentar os desafios da vida e oferecendo oportunidades de crescimento pessoal e acadêmico. A organização acredita que a educação é o caminho para a transformação social, e por isso, promove um modelo de ensino que combina o desenvolvimento intelectual com o fortalecimento emocional e social dos alunos.
                </p>
                
                <p>
                    <strong>Os valores centrais da ONG incluem:</strong>
                </p>
                
                <p>
                    <strong>Educação de qualidade:</strong> Por meio de programas como a Aceleração do Conhecimento, a ONG oferece aulas de alfabetização, português, matemática e inglês, atendendo alunos desde a fase de alfabetização até o ensino médio.
                </p>
                
                <p>
                    <strong>Suporte emocional:</strong> Reconhecendo a importância do bem-estar emocional no processo de aprendizado, a Passos Mágicos oferece assistência psicológica e psicopedagógica tanto para os alunos quanto para suas famílias.
                </p>
                
                <p>
                    <strong>Protagonismo juvenil:</strong> A ONG incentiva os alunos a assumirem papéis de liderança em suas próprias vidas, promovendo o autoconhecimento e o senso de responsabilidade por suas escolhas e ações.
                </p>
                """, unsafe_allow_html=True)

    


    st.subheader(':red[Impacto na Comunidade]'
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
                    O impacto da Passos Mágicos na vida das crianças e jovens é significativo. Em 2023, a ONG impactou diretamente mais de 4.400 pessoas, considerando o impacto estendido às famílias dos alunos. O programa de Aceleração do Conhecimento conta com 1.100 alunos, sendo que muitos deles são bolsistas em instituições de ensino particular ou estão cursando o ensino superior.
                </p>
                
                <p class="special-indent">
                    Além dos resultados acadêmicos, a ONG proporciona vivências culturais e intercâmbios, ampliando os horizontes dos alunos e conectando-os a diferentes realidades. Programas como o de apadrinhamento oferecem a oportunidade para os alunos estudarem em escolas particulares, com a ONG monitorando o progresso acadêmico e pessoal de cada bolsista.
                </p>
                
                <p class="special-indent">
                    A organização também realiza ações sociais, como campanhas de arrecadação de materiais escolares, roupas e alimentos, além de eventos como o "Natal Mágico", que reúne toda a comunidade para celebrar as conquistas do ano. Esses programas e ações reforçam o compromisso da Passos Mágicos em transformar vidas e promover um futuro mais justo e inclusivo para os jovens de Embu-Guaçu.
                </p>
                """, unsafe_allow_html=True)


    
        
layout_saida()
        
    
