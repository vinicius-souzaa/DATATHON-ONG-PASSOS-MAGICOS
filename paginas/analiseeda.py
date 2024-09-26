import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
from util.layout import layout_saida
from sklearn.preprocessing import LabelEncoder

st.set_page_config(
    page_title="Analise Exploratória de Dados | DATATHON",
    layout="wide",
)

layout_saida()



with st.container():

    st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")   
    
    st.header(":red[Analise Exploratória de Dados (EDA) 📊]", divider='red')
    st.markdown("""
                <h1 style='text-align:justify; 
                font-size:15px;
                font-family: Arial, sans-serif; 
                font-weight: normal;
                line-height:1.5'>

                Nesta seção, realizamos uma análise exploratória dos dados 
                fornecidos pela ONG Passos Mágicos, com o objetivo de entender 
                melhor os padrões e tendências presentes nas informações educacionais 
                e socioeconômicas dos alunos. A análise exploratória de dados (EDA) é 
                uma etapa fundamental, pois nos permite identificar comportamentos, 
                correlações e possíveis outliers que podem influenciar o desempenho 
                dos estudantes.

                Através de gráficos descritivos, como histogramas, boxplots e séries 
                temporais, exploramos a distribuição de variáveis-chave, como idade, 
                gênero, nível educacional e indicadores de desempenho acadêmico. 
                Além disso, investigamos fatores específicos, como a progressão dos 
                alunos em relação às suas fases educacionais, mudanças de desempenho 
                ao longo dos anos, e a influência de fatores externos, como bolsas de 
                estudo e apoio psicopedagógico.

                Essa análise inicial oferece uma base sólida para as próximas etapas 
                do projeto, permitindo que as decisões sobre os modelos preditivos 
                sejam baseadas em uma compreensão profunda dos dados e suas particularidades.
                </h1>

                """,unsafe_allow_html=True,
            )
    
    
    


    st.markdown("""
            <h1 style='text-align:justify; 
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            <small>Clique nas caixas expansivas abaixo para ver mais sobre cada um dos 
            eventos numerados no gráfico:</small></h1>           
            """,unsafe_allow_html=True)
                    
    
    with st.expander("Analise Descritiva"):

        st.subheader(':red[Analise Descritiva]'
                         , divider='red')
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            **Dataset "DF_MODELO":**

            A análise descritiva é essencial para entender as características de um conjunto de 
            dados e identificar padrões ou outliers que podem influenciar as análises preditivas. 
            O dataset "df_modelo", que foi usado no modelo preditivo contém 314 alunos que estudaram 
            em 2020, 2021 e 2022, revela informações importantes sobre o progresso desses 
            alunos ao longo dos anos.

            O índice médio de desenvolvimento educacional (INDE) dos alunos em 2022 foi de 7,03, 
            o que reflete um desempenho satisfatório em termos de aprendizado.
            A maioria dos alunos esteve matriculada na Fase 2, com 218 alunos, correspondendo a cerca 
            de 25,3% do total.
            87,5% dos alunos não eram bolsistas em 2022, com 754 alunos classificados como "Não" na 
            coluna "BOLSISTA_2022".
            A análise das pedras indicativas de progresso revela que a "Ametista" foi a mais comum, 
            com 348 alunos (40,3%) nesta categoria.
            Quanto às recomendações de avaliação, 49% dos alunos foram mantidos na fase atual, enquanto 
            422 receberam essa recomendação no "REC_AVA_1_2022".
                    
            Justificativa: Este dataset foi mantido como base para os modelos preditivos, pois contém 
            informações completas de alunos ao longo dos três anos. A exclusão de alunos com dados 
            ausentes garante uma análise mais consistente, essencial para a construção de modelos que 
            identifiquem padrões de comportamento educacional e socioeconômico.

            **Dataset "DF_2020":**

            O dataset referente ao ano de 2020 contém informações detalhadas sobre os alunos que estudaram 
            nesse período, revelando uma visão aprofundada do desempenho escolar naquele ano.

            O número total de alunos analisados neste dataset é de 862, o que nos permite um panorama amplo 
            das características educacionais em 2020.
            A média do "INDE" neste ano foi de 6,74, indicando um desempenho geral ligeiramente abaixo da média 
            observada em 2022.
            218 alunos (25,3%) estavam na Fase 2, enquanto os outros estavam distribuídos entre Fases 1 e 3.
            A maioria dos alunos foi classificada como "Não Bolsista", representando 87,5% do total de matriculados.
            
            Justificativa: A separação do dataset de 2020 permite uma análise focada no impacto de um ano 
            específico sobre os alunos, sem a influência de dados de anos subsequentes. Isso é importante 
            para captar os resultados individuais daquele ano e identificar mudanças de fase ou desempenho.

            **Dataset "DF_2021":**

            A análise descritiva do dataset de 2021 oferece uma visão sobre o impacto das dificuldades 
            enfrentadas por muitos alunos, possivelmente em decorrência das interrupções causadas pela 
            pandemia de COVID-19.

            Este dataset também contém 862 alunos, dos quais 422 (49%) permaneceram na fase atual, segundo 
            o REC_AVA_1_2021.
            O valor médio do "INDE" foi de 6,82, ligeiramente superior ao de 2020, sugerindo uma recuperação 
            ou esforço maior por parte dos alunos e da instituição durante esse período.
            Quanto ao nível ideal de progresso **("NIVEL_IDEAL_2021")**, 218 alunos (25,3%) deveriam estar na Fase 2.
            
            Justificativa: A análise focada no ano de 2021 ajuda a entender as particularidades deste 
            período desafiador. A separação permite uma análise mais precisa sobre o impacto da pandemia 
            no desempenho e progresso escolar.

            **Dataset "DF_2022":**

            O ano de 2022 reflete um período mais estável, e a análise descritiva mostra uma melhora no 
            desempenho escolar.

            O valor médio do "INDE" foi de 7,03, o que representa uma leve melhora em relação aos anos anteriores.
            25,3% dos alunos estavam na Fase 2, e 87,5% eram não bolsistas.
            Em termos de progresso, 348 alunos (40,3%) estavam na pedra "Ametista", indicando estabilidade 
            no progresso educacional.
                    
            Justificativa: O dataset de 2022 foi analisado separadamente para captar as melhorias ou 
            mudanças de desempenho pós-pandemia. A separação ajuda a focar nas ações mais recentes da ONG 
            "Passos Mágicos", possibilitando uma avaliação do impacto de intervenções educacionais recentes.

            **Motivos para a Separação dos Datasets**
                    
            A separação dos datasets por ano é essencial para garantir uma análise mais precisa e 
            contextualizada. Muitos alunos não estiveram presentes durante todos os três anos, resultando 
            em valores ausentes (NaN). Ao separar os dados, foi possível realizar uma análise focada em cada 
            ano, isolando efeitos anuais e permitindo comparações entre diferentes períodos. Isso também ajuda 
            a evitar problemas com valores ausentes que poderiam distorcer os resultados. Para os modelos 
            preditivos, o dataset DF_MODELO foi mantido completo, considerando apenas os alunos que estudaram 
            nos três anos consecutivos, permitindo uma análise longitudinal mais robusta.
            </h1>
            """,unsafe_allow_html=True,
            )
        
        
    with st.expander("Analise de Outliers (Boxplot)"):
        st.subheader(':red[Boxplot dos Indicadores por Ano]'
                         , divider='red')
        
        # Carregar os datasets a partir da pasta
        df_modelo = pd.read_csv('dataframe/df_modelo.csv', sep=';')
        # Lista de indicadores para boxplot
        indicadores = ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']

        # Organizar os dados para o boxplot
        data_boxplot = pd.DataFrame()

        for year in ['2020', '2021', '2022']:
            for ind in indicadores:
                col_name = f'{ind}_{year}'
                if col_name in df_modelo.columns:
                    temp_df = df_modelo[[col_name]].dropna()
                    temp_df.columns = ['Valor']  # Renomear para um nome comum para facilitar o plot
                    temp_df['Indicador'] = ind
                    temp_df['Ano'] = year
                    data_boxplot = pd.concat([data_boxplot, temp_df], axis=0)

        # Ajustar tipos de dados
        data_boxplot['Valor'] = pd.to_numeric(data_boxplot['Valor'], errors='coerce')

        # Visualização com Seaborn
        plt.figure(figsize=(14, 7))
        sns.boxplot(data=data_boxplot, x='Indicador', y='Valor', hue='Ano')
        plt.title('Boxplot dos Indicadores por Ano')
        plt.xlabel('Indicador')
        plt.ylabel('Valores')
        plt.legend(title='Ano')
        plt.grid(True)
        plt.show()

        # Show the figure using Streamlit
        st.pyplot(plt, use_container_width=True)

        st.markdown("""
            <div style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
            
            **INDE (Índice de Desenvolvimento Educacional):**

            Observa-se uma certa consistência na mediana ao longo dos anos, com uma presença 
            notável de outliers, especialmente nos anos de 2021 e 2022, o que pode indicar variações 
            na avaliação ou incidência de eventos específicos que afetaram o desempenho educacional 
            de alguns alunos.
                    
            **IAA (Indicador de Autoavaliação):**

            Apresenta uma variação menor entre os quartis ao longo dos anos, mas com outliers 
            significativos em 2020, sugerindo que alguns alunos podem ter tido percepções extremas 
            de suas próprias capacidades ou desempenhos naquele ano.
                    
            **IEG (Indicador de Engajamento):**

            Exibe uma distribuição com variação mais ampla em 2020, que se estabiliza nos anos 
            subsequentes. Os outliers em 2022 apontam para casos extremos de engajamento ou desengajamento.
                    
            **IPS (Indicador Psicossocial):**

            Mantém uma consistência relativa nas medianas, porém com variação significativa nos dados 
            e presença de outliers em todos os anos, refletindo possíveis desafios psicossociais enfrentados 
            pelos alunos em momentos específicos.
                    
            **IDA (Indicador de Aprendizagem):**

            Variação nos quartis sugere mudanças na aprendizagem dos alunos ao longo dos anos, com uma 
            distribuição mais apertada em 2021.
                    
            **IPP (Indicador Psicopedagógico):**

            Apresenta uma das maiores variações e quantidade de outliers, especialmente em 2020, 
            indicando possíveis inconsistências nas avaliações ou intervenções psicopedagógicas.
                    
            **IPV (Indicador de Ponto de Virada):**

            Exibe uma variação considerável, com presença constante de outliers, o que sugere que 
            eventos significativos de mudança (ponto de virada) podem não ser comuns para todos, 
            mas impactantes para quem os experimenta.
                    
            **IAN (Indicador de Adequação ao Nível):**

            Tende a mostrar uma variação menor em comparação com outros indicadores, mas com alguns 
            outliers em 2021 e 2022, indicando casos onde a adequação ao nível educacional foi 
            particularmente alta ou baixa.
                    
            **Conclusão**
                    
            O boxplot fornece uma visão eficaz das tendências, variações e exceções nos indicadores 
            educacionais e psicossociais ao longo de três anos na ONG Passos Mágicos. Esta análise 
            visual permite identificar padrões ou anomalias que podem necessitar de atenção adicional 
            ou ajustes nas estratégias educacionais para melhor atender às necessidades dos alunos. 
            A presença de outliers em muitos dos indicadores sugere a importância de políticas personalizadas 
            e atenção individualizada para maximizar o desenvolvimento educacional e bem-estar dos alunos.

            Adicionalmente, a análise revelou a presença de notas zero em vários indicadores ao longo dos anos, 
            destacando-se o Indicador de Autoavaliação (IAA) com 5,41% em 2021 e 5,10% em 2022, e o Indicador 
            de Aprendizagem (IDA) com 3,18% em 2020 e 2,55% em 2021. A existência dessas notas zero pode 
            indicar desengajamento ou desafios específicos enfrentados por alguns alunos, que merecem uma 
            investigação detalhada. Esses valores zero são considerados outliers nos boxplots e destacam a 
            necessidade de intervenções direcionadas para esses alunos, a fim de garantir que todos tenham 
            oportunidades iguais de aprendizado e desenvolvimento dentro da instituição. A compreensão e o 
            endereço dessas questões são cruciais para promover um ambiente educacional inclusivo e eficaz. ​.</div>
                """, unsafe_allow_html=True,
                )

    

    def load_and_convert_data(file_path):
        df = pd.read_csv(file_path, sep=',', decimal='.')
        indicators = ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']
        years = ['2020', '2021', '2022']
        # Iterar sobre cada possível coluna de indicador em cada ano
        for indicator in indicators:
            for year in years:
                col_name = f"{indicator}_{year}"
                if col_name in df.columns:
                    df[col_name] = pd.to_numeric(df[col_name], errors='coerce')
                    # Ajustar valores maiores que 10 para serem exatamente 10
                    df[col_name] = df[col_name].apply(lambda x: 10 if x > 10 else x)
        return df

    def create_histogram(df, indicator, year, color):
        return go.Histogram(
            x=df[f'{indicator}_{year}'],
            marker_color=color,
            opacity=0.75,
            xbins=dict(start=0, end=10.2, size=1),
            name=year
        )

    df_2020 = load_and_convert_data('dataframe/df_2020.csv')
    df_2021 = load_and_convert_data('dataframe/df_2021.csv')
    df_2022 = load_and_convert_data('dataframe/df_2022.csv')

    indicators = ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']
    colors = ['#636EFA', '#EF553B', '#00CC96']
    years = ['2020', '2021', '2022']
    dfs = [df_2020, df_2021, df_2022]

    # Dictionary to hold specific texts for each indicator
    indicator_texts = {
        'INDE': """
        <div>
            <h4>Análise do INDE com Base no Contexto e no Dicionário de Dados</h4>
            <p><strong>Variação e Tendência Anual do INDE:</strong></p>
            <ul>
                <li><strong>2020:</strong> A distribuição do INDE em 2020 mostra um pico concentrado em torno de 7, o que sugere uma performance moderadamente alta da maioria dos alunos. Este ano pode ser considerado uma base ou um ponto de referência para avaliar o impacto inicial das estratégias educacionais da ONG.</li>
                <li><strong>2021:</strong> Observa-se uma leve redução no pico e uma distribuição mais ampla dos escores, com um aumento nas notas médias e baixas. Isso pode indicar que novas intervenções ou adaptações no método educacional foram implementadas, possivelmente em resposta a desafios externos como a pandemia de COVID-19, que exigiu ajustes nas metodologias de ensino.</li>
                <li><strong>2022:</strong> A distribuição de 2022 mostra uma melhoria significativa, com um aumento nos escores altos e uma redução nas notas mais baixas. Este resultado sugere que as medidas ajustadas nos anos anteriores podem ter começado a surtir efeito, melhorando significativamente o desempenho educacional dos alunos.</li>
            </ul>
            <p><strong>Implicações dos Resultados para a ONG:</strong></p>
            <ul>
                <li>A observação do deslocamento das distribuições do INDE ao longo dos anos pode ajudar a ONG a identificar quais estratégias estão funcionando e quais precisam de ajustes. Por exemplo, se programas específicos foram introduzidos ou reformulados entre 2020 e 2022, a eficácia desses programas pode ser avaliada através das mudanças observadas nos escores do INDE.</li>
                <li>A análise também pode revelar necessidades de suporte direcionado para grupos de alunos que ainda lutam para alcançar resultados educacionais ideais, conforme indicado pela persistência de escores mais baixos.</li>
            </ul>
            <p><strong>Desenvolvimento de Intervenções Baseadas em Dados:</strong></p>
            <ul>
                <li>Utilizando o INDE e outros indicadores detalhados no dicionário de dados (como IAA, IEG, IPS), a ONG pode desenvolver ou refinar intervenções que são verdadeiramente baseadas em dados, garantindo que recursos sejam alocados de maneira eficaz para áreas onde são mais necessários.</li>
                <li>A inclusão de variáveis como 'Ponto de Virada' e 'Classificação de Pedra' no dataset permite uma análise mais detalhada do impacto emocional e psicológico das intervenções, abordando não apenas o desempenho acadêmico mas também o bem-estar geral dos alunos.</li>
            </ul>
            <p><strong>Conclusão:</strong></p>
            <p>A análise do INDE ao longo dos três anos ilustra uma trajetória de melhoria contínua e fornece uma base sólida para a ONG Passos Mágicos não apenas entender, mas amplificar seu impacto na vida educacional e social dos alunos que atende. Esta análise é crucial para iluminar as conquistas da ONG e para planejar o caminho a seguir com estratégias que são informadas, impactantes e sustentáveis. Ao se engajar nesse processo analítico, os participantes do Datathon não estão apenas manipulando números, mas estão ajudando a moldar futuros.</p>
        </div>
        """,
        'IAA': """
        <div>
            <h4>Análise do IAA ao longo dos anos</h4>
            <p><strong>2020:</strong> A distribuição em 2020 mostra uma concentração predominante em torno da nota 7, com um pico significativo nessa região. Isso indica que a maioria dos alunos avaliou sua performance como moderadamente alta. Este comportamento pode refletir uma resposta inicial positiva às metodologias de ensino e programas de suporte da ONG naquele ano, marcando um ponto de partida otimista para os esforços educacionais da organização.</p>
            <p><strong>2021:</strong> Em 2021, observa-se uma mudança com um aumento nas avaliações médias e baixas (notas em torno de 4 e 5), além de uma diminuição nas avaliações mais altas. Esta alteração pode ser atribuída aos desafios impostos pela pandemia de COVID-19, que afetou metodologias de ensino e o bem-estar psicossocial dos alunos. A distribuição mais ampla sugere variações nas experiências de aprendizado dos alunos, possivelmente devido a adaptações no ensino remoto ou híbrido.</p>
            <p><strong>2022:</strong> Já em 2022, vemos uma melhoria significativa na distribuição, com um aumento nas notas altas (notas 8 e 9) e uma redução nas notas mais baixas. Este perfil sugere que as adaptações e intervenções realizadas nos anos anteriores começaram a gerar frutos, evidenciando uma recuperação e possível otimização nos processos educacionais e de apoio da ONG.</p>
            <h4>Implicações para a ONG Passos Mágicos</h4>
            <ul>
                <li>Identificação de Impactos e Ajustes Necessários: A variação anual nos resultados pode ajudar a identificar quais estratégias estão sendo efetivas e quais precisam de ajustes. Por exemplo, a necessidade de reforçar o apoio psicossocial e adaptar métodos pedagógicos em resposta a crises externas como a pandemia.</li>
                <li>Planejamento de Intervenções Futuras: A análise do IAA permite que a ONG planeje intervenções mais alinhadas com as necessidades dos alunos, utilizando feedback direto de suas experiências. Este processo é crucial para moldar um ambiente educacional que não apenas educa, mas também cuida do bem-estar emocional e psicológico dos estudantes.</li>
            </ul>
            <h4>Conclusão</h4>
            <p>Os histogramas do IAA refletem não apenas o desempenho acadêmico dos alunos, mas também a eficácia das estratégias implementadas pela ONG Passos Mágicos. A melhoria observada em 2022 é um testemunho das capacidades de adaptação e compromisso da organização com a educação e suporte aos seus alunos, enfatizando a importância de análises contínuas e adaptativas em resposta às dinâmicas de ensino e aprendizagem.</p>
        </div>""",
        'IEG': """
        <div>
            <h4>Análise do Histograma do IEG (Indicador de Engajamento)</h4>
            <p>O histograma do IEG para os anos de 2020, 2021 e 2022 revela mudanças significativas no nível de engajamento dos alunos, refletindo as diferentes circunstâncias e intervenções implementadas pela ONG Passos Mágicos.</p>
            <ul>
                <li><strong>2020:</strong> Observamos uma concentração dos valores em torno de 6 a 8, indicando um engajamento moderado a alto da maioria dos alunos. Este padrão pode ser atribuído a estratégias educacionais estáveis e eficazes empregadas antes dos desafios trazidos pela pandemia global.</li>
                <li><strong>2021:</strong> Há uma mudança visível com uma distribuição mais ampla e um pico menor em torno do 6, sugerindo uma redução geral no engajamento. Este declínio pode estar diretamente relacionado às interrupções causadas pela pandemia de COVID-19, que afetou significativamente o ensino presencial e exigiu a transição para métodos de ensino à distância. Essa mudança pode ter impactado negativamente o engajamento dos alunos devido a desafios como a falta de recursos tecnológicos adequados e o isolamento social.</li>
                <li><strong>2022:</strong> Mostra uma recuperação notável no engajamento, com um aumento considerável de valores altos, principalmente notas entre 8 e 10. Esse aumento sugere uma adaptação bem-sucedida às novas formas de ensino e a implementação de novas estratégias pedagógicas que efetivamente motivaram e envolveram os alunos. Este ano também pode refletir o efeito de iniciativas de apoio psicossocial reforçado e programas de engajamento comunitário, visando superar o isolamento e melhorar o bem-estar dos alunos.</li>
            </ul>
            <h4>Implicações para a ONG Passos Mágicos</h4>
            <p>A análise do IEG ao longo desses anos oferece insights valiosos sobre como eventos externos, como a pandemia, afetam o engajamento dos alunos e como intervenções adaptativas podem mitigar esses impactos. Para a ONG, esses dados são fundamentais para:</p>
            <ul>
                <li><strong>Avaliar a eficácia das estratégias de ensino e engajamento:</strong> Identificar quais práticas pedagógicas e programas de suporte são mais efetivos em diferentes circunstâncias.</li>
                <li><strong>Planejar intervenções futuras:</strong> Os dados de 2022, por exemplo, podem indicar quais estratégias adotadas foram mais eficazes e devem ser mantidas ou ampliadas.</li>
                <li><strong>Otimizar recursos:</strong> Direcionar recursos para iniciativas que demonstraram maior impacto na melhoria do engajamento e desempenho dos alunos.</li>
            </ul>
            <h4>Conclusão</h4>
            <p>O estudo do IEG, portanto, não só ajuda a entender o impacto das ações educacionais sobre o engajamento dos alunos, mas também orienta a ONG na tomada de decisões informadas para futuras estratégias pedagógicas e programas de suporte, com o objetivo de maximizar o impacto positivo na vida educacional e social dos estudantes que atende.</p>
        </div>""",
        'IPS': """
        <div>
        <h4>Análise do Histograma do IPS (Indicador Psicossocial)</h4>
        <p>O histograma do IPS para os anos de 2020, 2021 e 2022 mostra uma evolução marcante no bem-estar psicossocial dos alunos, influenciado pelas práticas e intervenções da ONG Passos Mágicos.</p>
        <ul>
            <li><strong>2020:</strong> A distribuição mostra uma forte concentração em torno dos valores 6 e 7, indicando um nível moderadamente alto de bem-estar psicossocial. Isso reflete o impacto positivo das iniciativas de suporte existentes antes dos desafios impostos pela pandemia global, sugerindo que os alunos se sentiam relativamente seguros e apoiados durante esse período.</li>
            <li><strong>2021:</strong> Observa-se uma mudança drástica com a maioria das avaliações concentradas no extremo inferior da escala, particularmente em torno de 2. Este padrão indica um declínio acentuado no bem-estar psicossocial, muito provavelmente como resultado das perturbações causadas pela pandemia de COVID-19, que trouxe desafios como isolamento social, adaptação ao ensino à distância e possíveis tensões familiares decorrentes da crise sanitária.</li>
            <li><strong>2022:</strong> Mostra uma melhora significativa com a maioria das avaliações se deslocando para os valores mais altos, entre 8 e 10. Isso sugere que as adaptações e medidas implementadas pela ONG para melhorar o suporte psicossocial e adaptar-se às necessidades emergentes dos alunos durante a pandemia começaram a surtir efeito, refletindo uma recuperação no bem-estar dos estudantes.</li>
        </ul>
        <h4>Implicações para a ONG Passos Mágicos</h4>
        <p>Essas mudanças no IPS ao longo dos anos são cruciais para a ONG ao avaliar a eficácia das suas intervenções psicossociais:</p>
        <ul>
            <li><strong>Identificação de Tendências e Necessidades:</strong> A variação nos dados de IPS ajuda a identificar as necessidades dos alunos em diferentes momentos, permitindo à ONG responder de forma mais eficaz às crises e manter o bem-estar dos alunos.</li>
            <li><strong>Ajuste de Programas e Estratégias:</strong> Os insights do IPS de 2021 podem ser usados para revisar e fortalecer as estratégias de suporte, especialmente em tempos de crise, enquanto os dados de 2022 podem indicar áreas de sucesso e aspectos a serem replicados ou expandidos em programas futuros.</li> </ul> <h4>Conclusão</h4> <p>O estudo detalhado do IPS não só ilustra o impacto direto das ações da ONG no bem-estar psicossocial dos estudantes, mas também oferece um guia valioso para ajustar e planejar intervenções futuras. Isso assegura que a ONG não apenas reage a crises, mas também se adapta proativamente para apoiar seus alunos de maneira eficaz e sustentável, maximizando o impacto positivo em suas vidas educacionais e sociais.</p>
        </div>""",
        'IDA': """
        <div>
            <h4>Análise do Histograma do IDA (Indicador de Aprendizagem)</h4>
            <p>O histograma do IDA para os anos de 2020, 2021 e 2022 mostra mudanças significativas na distribuição das notas de aprendizagem dos alunos, refletindo diretamente as adaptações e desafios enfrentados pela ONG Passos Mágicos e seus educandos.</p>
            <ul>
                <li><strong>2020:</strong> O ano de 2020 apresenta uma distribuição ampla com picos em várias faixas, predominando entre as notas 5 a 7. Este perfil indica uma variação significativa no desempenho dos alunos, que pode estar relacionada às metodologias tradicionais de ensino ainda em uso antes dos desafios impostos pela pandemia de COVID-19.</li>
                <li><strong>2021:</strong> Em 2021, o histograma mostra um pico distinto em torno da nota 5, com menos incidência em notas mais altas. Este padrão sugere um impacto claro das dificuldades impostas pela pandemia, incluindo a transição para o ensino remoto, que pode ter afetado a consistência e a eficácia do aprendizado dos alunos.</li>
                <li><strong>2022:</strong> No ano de 2022, observa-se uma melhora notável, com o pico deslocando para notas mais altas, entre 7 e 9. Este aumento sugere uma adaptação bem-sucedida às novas estratégias de ensino e uma recuperação na qualidade do aprendizado, possivelmente devido à melhoria das práticas de ensino híbrido e ao reforço nas intervenções pedagógicas.</li>
            </ul>
            <h4>Implicações para a ONG Passos Mágicos</h4>
            <p>A análise dos resultados do IDA é fundamental para entender as dinâmicas de aprendizado em resposta às intervenções aplicadas e aos desafios externos. Para a ONG, esses insights são cruciais para:</p>
            <ul>
                <li><strong>Avaliação de Estratégias Pedagógicas:</strong> Identificar quais abordagens são mais eficazes e como elas podem ser ajustadas para atender às necessidades variadas dos alunos em diferentes contextos.</li>
                <li><strong>Planejamento de Recursos:</strong> Direcionar recursos e apoios específicos para áreas onde eles são mais necessários, garantindo uma resposta adequada às necessidades emergentes dos alunos.</li>
                <li><strong>Desenvolvimento de Resiliência Educativa:</strong> Fortalecer as capacidades da ONG para responder a crises futuras, garantindo continuidade e eficácia no ensino.</li>
            </ul>
            <h4>Conclusão</h4>
            <p>O estudo do IDA oferece uma perspectiva valiosa sobre o impacto das estratégias educacionais e das condições externas no desempenho dos alunos. As melhorias observadas em 2022 ressaltam a capacidade da ONG de adaptar-se e superar desafios significativos, melhorando continuamente o suporte aos seus estudantes e maximizando os resultados educacionais.</p>
        </div>""",
        'IPP': """
        <div>
            <h4>Análise do Histograma do IPP (Indicador Psicopedagógico)</h4>
            <p>O histograma do IPP para os anos de 2020, 2021 e 2022 ilustra variações significativas no desempenho psicopedagógico dos alunos, que podem ser interpretadas como reflexos das condições externas e das estratégias educacionais aplicadas pela ONG Passos Mágicos.</p>
            <ul>
                <li><strong>2020:</strong> Em 2020, a distribuição mostra uma concentração significativa nas notas em torno de 7 e 8, indicando um nível relativamente alto de desempenho psicopedagógico. Isso pode ser atribuído a um ambiente de aprendizagem estável e à eficácia das intervenções educacionais antes dos desafios impostos pela pandemia.</li>
                <li><strong>2021:</strong> O histograma de 2021 apresenta um pico muito acentuado na nota 5, com redução notável nas notas mais altas. Este perfil reflete os desafios trazidos pela pandemia de COVID-19, incluindo o possível impacto da adaptação ao ensino remoto e a interrupção das rotinas educacionais regulares, o que pode ter afetado adversamente o desempenho psicopedagógico dos alunos.</li>
                <li><strong>2022:</strong> A recuperação em 2022 é evidente, com um aumento significativo nas notas entre 8 e 10. Esse melhoramento sugere uma adaptação bem-sucedida às circunstâncias alteradas e possivelmente a implementação de novas estratégias e programas de apoio psicopedagógico mais efetivos para enfrentar as adversidades continuadas do cenário pandêmico.</li>
            </ul>
            <h4>Implicações para a ONG Passos Mágicos</h4>
            <p>Os resultados do IPP são cruciais para avaliar a eficácia das intervenções psicopedagógicas e ajustar as estratégias de apoio conforme necessário. Para a ONG, esses dados permitem:</p>
            <ul>
                <li><strong>Analisar a Resposta às Intervenções:</strong> Avaliar como diferentes abordagens e recursos educacionais afetam o bem-estar psicopedagógico dos alunos e ajustar programas para maximizar a eficácia.</li>
                <li><strong>Planejar Recursos e Estratégias:</strong> Alocar recursos de maneira mais eficaz, priorizando intervenções que demonstraram impactar positivamente o desempenho psicopedagógico dos alunos durante períodos de crise.</li>
                <li><strong>Adaptar à Nova Realidade Educacional:</strong> Continuar a adaptar as práticas educacionais para não só lidar com desafios imediatos, mas também para fortalecer a resiliência educacional a longo prazo frente a futuras crises.</li>
            </ul>
            <h4>Conclusão</h4>
            <p>O estudo do IPP ilustra a necessidade de adaptar continuamente as estratégias educacionais para responder efetivamente às mudanças nas condições de aprendizagem e bem-estar dos alunos. As tendências observadas ao longo dos anos destacam a capacidade da ONG de modificar e melhorar suas abordagens para sustentar e melhorar o desenvolvimento psicopedagógico dos alunos sob sua tutela.</p>
        </div>""",
        'IPV': """
        <div>
            <h4>Análise do Histograma do IPV (Indicador de Ponto de Virada)</h4>
            <p>O histograma do IPV para os anos de 2020, 2021 e 2022 destaca variações notáveis no que se refere ao ponto de virada nos processos educativos e desenvolvimento dos alunos atendidos pela ONG Passos Mágicos.</p>
            <ul>
                <li><strong>2020:</strong> Observamos uma distribuição concentrada principalmente entre as notas 5 e 8, com um pico significativo na nota 6. Isso sugere que muitos alunos alcançaram um nível moderado de sucesso, indicando uma intervenção eficaz da ONG que ajudou vários estudantes a atingir seu ponto de virada pessoal neste ano.</li>
                <li><strong>2021:</strong> Há uma notável centralização dos escores em torno da nota 5, com uma diminuição geral em notas mais altas em comparação com 2020. Esse padrão pode refletir os desafios impostos pela pandemia, que potencialmente retardou ou dificultou o alcance de pontos de virada significativos para muitos alunos devido às restrições ao ensino presencial e às limitações do ensino à distância.</li>
                <li><strong>2022:</strong> A distribuição em 2022 mostra uma melhora, com um pico entre as notas 7 e 9. Este aumento pode indicar uma recuperação e adaptação efetivas aos desafios contínuos, além de um ajuste nas estratégias pedagógicas que possibilitaram um impacto mais profundo e amplo no desempenho dos alunos, ajudando mais deles a alcançar seus pontos de virada.</li>
            </ul>
            <h4>Implicações para a ONG Passos Mágicos</h4>
            <p>A análise dos resultados do IPV oferece insights cruciais para a ONG no planejamento e implementação de estratégias futuras:</p>
            <ul>
                <li><strong>Adaptação de Estratégias:</strong> Os dados de 2021 e 2022 podem ajudar a ONG a identificar as necessidades de ajustes em suas intervenções para garantir que os desafios como os enfrentados durante a pandemia não comprometam a capacidade dos alunos de alcançar seus pontos de virada.</li>
                <li><strong>Refinamento de Programas:</strong> O reconhecimento dos padrões de sucesso pode direcionar a melhoria de programas específicos que contribuem para esses resultados positivos, particularmente aqueles que promovem a resiliência e adaptação dos alunos a novos métodos de ensino.</li>
                <li><strong>Foco em Suporte Continuado:</strong> As flutuações nos dados enfatizam a importância de manter o suporte contínuo e adaptativo aos alunos, especialmente aqueles que podem estar em risco de não alcançar seus pontos de virada devido a dificuldades externas ou internas.</li>
            </ul>
            <h4>Conclusão</h4>
            <p>Os resultados do IPV de 2020 a 2022 ilustram a dinâmica dos desafios e sucessos na jornada educacional dos alunos assistidos pela Passos Mágicos. Eles sublinham a necessidade de uma abordagem ágil e sensível às condições variáveis para maximizar o impacto positivo no desenvolvimento e crescimento dos alunos.</p>
        </div>""",
        'IAN': """
        <div>
            <h4>Análise do Histograma do IAN (Indicador de Adequação ao Nível)</h4>
            <p>O histograma do IAN para os anos de 2020, 2021 e 2022 ilustra as variações na adequação dos alunos aos níveis educacionais propostos pela ONG Passos Mágicos, refletindo a eficácia das intervenções educacionais em contextos anuais distintos.</p>
            <ul>
                <li><strong>2020:</strong> Mostra uma distribuição mais uniforme com picos em torno das notas 5 e 10. Isto indica uma dispersão na adequação ao nível, onde uma parcela significativa dos alunos estava bem ajustada ao seu nível de aprendizado, enquanto outra parcela apresentava desafios significativos.</li>
                <li><strong>2021:</strong> Observa-se um pico acentuado na nota 6, indicando uma maior concentração de alunos que estavam apenas moderadamente adequados aos seus níveis educacionais. Esse pode ser um reflexo das perturbações causadas pela pandemia de COVID-19, afetando a capacidade dos alunos de se ajustar efetivamente aos seus níveis educativos devido às interrupções no ensino presencial.</li>
                <li><strong>2022:</strong> Apresenta um grande pico na nota 6 novamente, mas com uma melhoria notável em relação ao ano anterior, indicando que enquanto muitos alunos ainda enfrentam desafios para atingir uma adequação plena, a situação pode estar começando a se estabilizar ou melhorar devido a ajustes nas estratégias pedagógicas ou maior adaptação dos alunos ao modelo de ensino vigente.</li>
            </ul>
            <h4>Implicações para a ONG Passos Mágicos</h4>
            <p>A variação anual nos resultados do IAN oferece insights valiosos para a ONG no planejamento de suas intervenções:</p>
            <ul>
                <li><strong>Estratégias Personalizadas:</strong> Identificar alunos que consistentemente aparecem nas faixas mais baixas de adequação para direcionar intervenções personalizadas que possam auxiliá-los a alcançar uma melhor adequação ao seu nível educacional.</li>
                <li><strong>Revisão Curricular:</strong> Os dados podem sugerir a necessidade de revisão dos currículos e métodos de ensino para garantir que atendam às necessidades dos alunos, especialmente em resposta a desafios externos como a pandemia.</li>
                <li><strong>Monitoramento Contínuo:</strong> A contínua monitoração do IAN é crucial para entender as dinâmicas de longo prazo no desempenho dos alunos e ajustar as práticas educacionais conforme necessário para maximizar a eficácia das intervenções educacionais.</li>
            </ul>
            <h4>Conclusão</h4>
            <p>A análise do IAN de 2020 a 2022 demonstra a importância de uma abordagem adaptativa e responsiva nas estratégias educacionais para enfrentar tanto os desafios contínuos quanto os emergentes. A ONG Passos Mágicos, ao utilizar esses dados, pode melhor orientar suas ações para promover um ambiente de aprendizado mais eficaz e inclusivo para todos os alunos.</p>
        </div>"""
        }

    with st.expander("Distribuição dos Índices por Ano"):
        tabs = st.tabs(indicators)
        for tab, indicator in zip(tabs, indicators):
            with tab:
                st.subheader(f':red[Histograma {indicator}]',divider='red')
                fig = make_subplots(rows=1, cols=3, subplot_titles=[f'{indicator} {year}' for year in years])
                for df, year, color in zip(dfs, years, colors):
                    fig.add_trace(create_histogram(df, indicator, year, color), row=1, col=years.index(year) + 1)
                fig.update_layout(height=400, width=1200, showlegend=True, bargap=0.1,
                                  xaxis=dict(tickmode='linear', tick0=0, dtick=1))
                st.plotly_chart(fig, use_container_width=True)  
                # Display the specific text for each indicator
                st.markdown(indicator_texts[indicator], unsafe_allow_html=True) 

    with st.expander("Analise das Medias de Indicadores de Desempenho"):
        tab14, tab15,tab16 = st.tabs(
        tabs=[
            "Agrupado",
            "Genero",
            "Idade"
            ]
        )
        with tab14:
            st.subheader(':red[Medias de Indicadores de Por Ano]'
                            , divider='red')
            
            # Função para calcular médias corrigidas de indicadores
            def calculate_mean_by_year(indicators_dict):
                means = {}
                for year, df in indicators_dict.items():
                    means[year] = df.apply(pd.to_numeric, errors='coerce').mean().tolist()
                return means

            # Função para plotar gráfico com Plotly
            def plot_mean_indicators(means, indicators):
                fig = go.Figure()
                for i, indicator in enumerate(indicators):
                    fig.add_trace(go.Scatter(x=list(means.keys()), y=[means[year][i] for year in means.keys()], 
                                            mode='lines+markers', name=indicator))
                fig.update_layout(
                    title='Médias dos Indicadores de Desempenho por Ano (2020-2022)',
                    xaxis_title='Ano',
                    yaxis_title='Média dos Indicadores',
                    template='plotly_white',
                    legend_title="Indicadores",
                    
                )
                return fig

            # Indicadores a serem analisados
            indicators = ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']

            # Preparando os dados de cada ano
            indicators_2020 = df_2020[[f'{indicator}_2020' for indicator in indicators]]
            indicators_2021 = df_2021[[f'{indicator}_2021' for indicator in indicators]]
            indicators_2022 = df_2022[[f'{indicator}_2022' for indicator in indicators]]

            # Calculando as médias por ano
            indicators_dict = {'2020': indicators_2020, '2021': indicators_2021, '2022': indicators_2022}
            means = calculate_mean_by_year(indicators_dict)

            # Plotando o gráfico
            
            fig = plot_mean_indicators(means, indicators)
            
            st.plotly_chart(fig, use_container_width=True)
                    
                    
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.5'>

                        **Médias de Indicadores por Ano**

                        A análise das médias dos indicadores de desempenho dos alunos ao 
                        longo dos anos de 2020, 2021 e 2022 revela tendências importantes 
                        sobre o progresso educacional e psicossocial dos estudantes da ONG 
                        Passos Mágicos. Os indicadores avaliados incluem o Índice de 
                        Desenvolvimento Educacional (INDE), o Indicador de Autoavaliação 
                        (IAA), o Indicador de Engajamento (IEG), o Indicador Psicossocial 
                        (IPS), o Indicador de Aprendizagem (IDA), o Indicador Psicopedagógico 
                        (IPP), o Indicador de Ponto de Virada (IPV) e o Indicador de Adequação 
                        ao Nível (IAN).

                        **Em 2020**, a média do INDE foi a mais alta, com uma pontuação de 7.3, 
                        sugerindo um desempenho geral mais elevado naquele ano. Já os 
                        indicadores de engajamento (IEG) e autoavaliação (IAA) também 
                        apresentaram resultados fortes. No entanto, os indicadores ligados 
                        ao aprendizado (IDA) e à adequação ao nível (IAN) mostraram números 
                        relativamente mais baixos, o que aponta para desafios de aprendizagem 
                        ou adequação curricular.

                        **Insights**

                        **Em 2021**, observamos uma queda significativa no INDE (6.8), 
                        refletindo possíveis dificuldades educacionais enfrentadas pelos 
                        alunos. O IEG também diminuiu, o que pode indicar uma queda no 
                        engajamento estudantil, algo que afeta diretamente o desempenho. 
                        No entanto, o IPS manteve-se estável, sugerindo que o suporte 
                        psicossocial permaneceu consistente, ajudando a mitigar as dificuldades 
                        emocionais e comportamentais.

                        **Já em 2022**, o INDE voltou a crescer para 7.0, e o IEG também se 
                        recuperou. Esses resultados mostram uma melhoria na qualidade do 
                        aprendizado e no envolvimento dos alunos com os programas da ONG. 
                        Contudo, os indicadores de aprendizado (IDA) e adequação ao nível 
                        (IAN) continuam sendo pontos de atenção, sugerindo a necessidade de 
                        intervenções mais focadas no apoio acadêmico.

                        **Conclusão**

                        Os dados indicam uma recuperação gradual no desempenho educacional 
                        e engajamento ao longo do período, após um momento de declínio. 
                        A ONG deve continuar investindo em estratégias para fortalecer o 
                        aprendizado e a adequação dos alunos ao currículo, garantindo que 
                        o apoio psicossocial permaneça um pilar central no desenvolvimento 
                        dos estudantes. ​
                        </h1>
                         
                        """,unsafe_allow_html=True,
                        )
            
        with tab15:
            st.subheader(':red[Medias de Indicadores de Por Genero]'
                            , divider='red')
            
            # Função para calcular a média por indicador e sexo em cada ano
            def calculate_mean_by_gender_per_year(df, year, indicators):
                # Convertendo as colunas de indicadores para numérico, ignorando erros
                for indicator in indicators:
                    df[f'{indicator}_{year}'] = pd.to_numeric(df[f'{indicator}_{year}'], errors='coerce')
                
                # Agrupando por gênero e calculando a média para cada indicador
                means = df.groupby('Sexo').mean(numeric_only=True)[[f'{indicator}_{year}' for indicator in indicators]]
                
                return means

            # Indicadores a serem analisados
            indicators = ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']

            # Calculando a média por sexo de cada dataframe
            means_2020 = calculate_mean_by_gender_per_year(df_2020, '2020', indicators)
            means_2021 = calculate_mean_by_gender_per_year(df_2021, '2021', indicators)
            means_2022 = calculate_mean_by_gender_per_year(df_2022, '2022', indicators)

            
            

            # Função para criar o gráfico interativo com menu para selecionar o indicador e texto abaixo da legenda
            def plot_interactive_indicator_selector_with_text(means_2020, means_2021, means_2022, indicators):
                fig = go.Figure()

                # Adicionando os traces para cada indicador (inicialmente ocultos)
                for indicator in indicators:
                    # Masculino
                    fig.add_trace(go.Scatter(x=['2020', '2021', '2022'], 
                                            y=[means_2020.loc['M', f'{indicator}_2020'], 
                                                means_2021.loc['M', f'{indicator}_2021'], 
                                                means_2022.loc['M', f'{indicator}_2022']], 
                                            mode='lines+markers', name=f'{indicator} (Masculino)',
                                            visible=False))

                    # Feminino
                    fig.add_trace(go.Scatter(x=['2020', '2021', '2022'], 
                                            y=[means_2020.loc['F', f'{indicator}_2020'], 
                                                means_2021.loc['F', f'{indicator}_2021'], 
                                                means_2022.loc['F', f'{indicator}_2022']], 
                                            mode='lines+markers', name=f'{indicator} (Feminino)',
                                            visible=False))

                # Criando o menu interativo
                buttons = []
                for i, indicator in enumerate(indicators):
                    buttons.append(dict(
                        method='update',
                        label=indicator,
                        args=[{'visible': [False] * len(fig.data)},  # Oculta todos os traces
                            {'title': f'Indicador: {indicator} (Masculino vs Feminino)'}]  # Atualiza o título
                    ))

                    # Mostra os traces correspondentes ao indicador selecionado
                    buttons[i]['args'][0]['visible'][i * 2] = True  # Masculino
                    buttons[i]['args'][0]['visible'][i * 2 + 1] = True  # Feminino

                # Adicionando o menu ao gráfico e estilizando o dropdown
                fig.update_layout(
                    updatemenus=[{
                        'buttons': buttons,
                        'direction': 'down',
                        'showactive': True,
                        'bgcolor': '#B0C4DE',  # Cor de fundo do dropdown
                        'bordercolor': '#708090',  # Cor da borda
                        'font': {'color': '#708090'}  # Cor da fonte
                    }],
                    title='Clique no Dropdown para selecionar o indicador desejado',
                    xaxis_title='Ano',
                    yaxis_title='Média dos Indicadores',
                    template='plotly_white',
                    hovermode='x unified'
                )

                # Todos os traces inicialmente invisíveis
                return fig

            # Indicadores a serem analisados
            indicators = ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']

            # Chamando a função para plotar os dados com seletor interativo e texto explicativo
            fig = plot_interactive_indicator_selector_with_text(means_2020, means_2021, means_2022, indicators)

            # Mostrando o gráfico no Streamlit
            st.plotly_chart(fig, use_container_width=True)

            # Texto adicional
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.5'>
                        
                        **Médias dos Indicadores por Gênero**

                        A análise dos indicadores de desempenho educacional dos alunos e 
                        alunas da ONG Passos Mágicos revela uma divisão interessante entre 
                        os gêneros ao longo de 2020, 2021 e 2022. Os indicadores analisados 
                        incluem o INDE (Índice de Desenvolvimento Educacional), 
                        IAA (Indicador de Autoavaliação), IEG (Indicador de Engajamento), 
                        IPS (Indicador Psicossocial), IDA (Indicador de Aprendizagem), 
                        IPP (Indicador Psicopedagógico), IPV (Indicador de Ponto de Virada) 
                        e IAN (Indicador de Adequação ao Nível).

                        Em 2022, por exemplo, os meninos apresentaram uma média ligeiramente 
                        superior em indicadores como o **INDE (7.03 contra 7.02 das meninas)** 
                        e o **IAN (6.57 contra 6.31)**, o que pode sugerir uma leve vantagem 
                        em termos de desempenho educacional e adequação ao nível escolar. 
                        No entanto, as meninas apresentaram médias superiores em indicadores 
                        como o **IAA (8.33 contra 8.18 dos meninos)**, sugerindo uma percepção 
                        mais positiva sobre o próprio progresso.

                        **Insights**

                        A análise revela que as meninas tendem a ter um desempenho melhor 
                        em indicadores relacionados à autoavaliação (IAA) e ao engajamento 
                        (IEG), enquanto os meninos mostram um leve domínio no INDE e na 
                        adequação ao nível (IAN). O fato de as alunas apresentarem médias 
                        maiores no IAA indica uma autoconfiança maior em relação à própria 
                        trajetória educacional, enquanto o desempenho masculino ligeiramente 
                        superior no INDE e IAN pode estar relacionado a uma maior facilidade 
                        de adaptação ao currículo.

                        Outro ponto de destaque é a proximidade nas médias do IPS 
                        (Indicador Psicossocial), onde meninos e meninas apresentam valores 
                        semelhantes, reforçando que o suporte psicossocial oferecido pela 
                        ONG tem sido eficaz em proporcionar um ambiente de acolhimento 
                        para ambos os gêneros.

                        **Conclusão**

                        Esses dados sugerem que, embora os meninos apresentem ligeiras 
                        vantagens em indicadores de desempenho acadêmico, as meninas têm 
                        uma percepção mais positiva sobre o próprio desenvolvimento. 
                        A ONG pode utilizar esses insights para adaptar intervenções 
                        específicas, promovendo um equilíbrio entre desempenho e confiança 
                        tanto para meninos quanto para meninas. O foco em estratégias 
                        que promovam maior autoconfiança para os meninos e um reforço do 
                        desempenho acadêmico para as meninas pode contribuir para um 
                        desenvolvimento mais igualitário.
                        </h1>
                        """, unsafe_allow_html=True)

            
        with tab16:
            st.subheader(':red[Medias de Indicadores por Idade]', divider='red')
            
            df_2020 = load_and_convert_data('dataframe/df_2020.csv')
            df_2021 = load_and_convert_data('dataframe/df_2021.csv')
            df_2022 = load_and_convert_data('dataframe/df_2022.csv')

            # Lista de indicadores e anos
            indicators = ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']
            years = ['2020', '2021', '2022']

            # Paleta de cores para os indicadores
            colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880']

            # Função para preparar e calcular a média dos dados por idade
            def prepare_and_average_data(df, year):
                # Definir as colunas de idade para cada ano
                age_column = f'IDADE_ALUNO_{year}'
                cols = [f'{ind}_{year}' for ind in indicators] + [age_column]
                
                # Verificar se a coluna de idade existe no dataframe
                if age_column in df.columns:
                    data = df[cols].dropna()
                    data[age_column] = data[age_column].astype(int)  # Garantir que a idade seja numérica
                    return data.groupby(age_column).mean().reset_index()
                else:
                    return pd.DataFrame()  # Retorna dataframe vazio se a coluna de idade não existir

            # Função para criar um gráfico com dropdown para selecionar o ano
            def plot_data_with_dropdown(df_2020, df_2021, df_2022):
                fig = go.Figure()

                # Mapeamento dos anos para seus respectivos dataframes
                dataframes = {'2020': df_2020, '2021': df_2021, '2022': df_2022}

                # Criando traços para cada ano e escondendo todos inicialmente
                for year in years:
                    df = dataframes[year]
                    data = prepare_and_average_data(df, year)
                    if not data.empty:
                        for j, indicator in enumerate(indicators):
                            fig.add_trace(
                                go.Scatter(
                                    x=data[f'IDADE_ALUNO_{year}'],  # Garantir que a idade seja numérica
                                    y=data[f'{indicator}_{year}'],
                                    mode='lines+markers',
                                    name=f'{indicator} ({year})',
                                    line=dict(color=colors[j]),
                                    visible=False  # Inicialmente invisível
                                )
                            )
                
                # Atualizando layout
                fig.update_layout(
                    title='Clique no Dropdown para selecionar o Ano desejado',
                    xaxis=dict(title='Idade', type='linear', tickmode='linear', dtick=1),  # Definir o eixo x como numérico
                    yaxis=dict(title='Média'),
                    legend_title='Indicador',
                    height=450,
                    width=1000,
                    updatemenus=[  # Adicionando o dropdown
                        dict(
                            buttons=[  
                                dict(label=f"{year}",
                                    method="update",
                                    args=[{"visible": [j // len(indicators) == year_idx for j in range(len(indicators) * len(years))]},  # Mostrar todos os indicadores do ano correspondente
                                        {"title": f'Média dos Indicadores de Desempenho por Idade em {year}'}]) 
                                for year_idx, year in enumerate(years)
                            ],
                            direction="down",
                            showactive=True,
                            x=0.17,
                            y=1.15
                        )
                    ]
                )

                return fig

            # Chamar a função para plotar o gráfico com dropdown usando os três dataframes
            fig = plot_data_with_dropdown(df_2020, df_2021, df_2022)

            st.plotly_chart(fig, use_container_width=True)

                    
                    
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.5'>

                        **Médias dos Indicadores por Idade a cada Ano**

                        A análise das médias dos indicadores de desempenho por idade ao 
                        longo dos anos de 2020, 2021 e 2022 revela tendências importantes 
                        no desenvolvimento educacional dos alunos atendidos pela ONG Passos 
                        Mágicos. Os indicadores analisados incluem INDE, IAA, IEG, IPS, 
                        IDA, IPP, IPV e IAN, que medem, respectivamente, o desempenho 
                        educacional geral, autoavaliação, engajamento, aspectos psicossociais,
                        aprendizagem, psicopedagogia, ponto de virada e adequação ao nível 
                        educacional. As variações por idade ajudam a entender o progresso 
                        dos alunos em diferentes fases da vida, oferecendo uma visão granular 
                        do impacto da ONG em cada faixa etária.

                        Em 2020, observou-se que as médias dos indicadores tendem a ser 
                        mais elevadas para alunos mais jovens, especialmente nos índices 
                        de autoavaliação (IAA) e engajamento (IEG). Já em 2021, há uma 
                        leve estabilização nas médias conforme a idade aumenta, sugerindo 
                        que o impacto do projeto educacional se consolida em faixas etárias 
                        intermediárias. Em 2022, nota-se um aumento significativo no 
                        engajamento e no ponto de virada (IPV) para os alunos mais velhos, 
                        o que pode indicar o sucesso do programa ao longo dos anos em 
                        proporcionar transições importantes na trajetória educacional dos 
                        estudantes.

                        **Insights**

                        **Jovens apresentam maiores médias em autoavaliação e engajamento:** 
                        Isso sugere que a ONG está eficaz em estimular o protagonismo e a 
                        motivação dos alunos desde cedo.

                        **Transições importantes aos 15-17 anos:** O aumento dos indicadores 
                        de ponto de virada e engajamento para alunos mais velhos indica que 
                        essa fase é crítica para o desenvolvimento educacional, o que sugere 
                        um foco mais direcionado nesses alunos.

                        **Estabilização em idades intermediárias:** O desempenho se estabiliza 
                        em idades intermediárias, sugerindo que os alunos consolidam seu 
                        progresso educacional antes de alcançarem as fases mais críticas.
                        
                        **Conclusão**

                        As médias dos indicadores revelam que a ONG Passos Mágicos tem 
                        um impacto significativo no desenvolvimento dos alunos, 
                        especialmente em idades mais críticas para a transição escolar. 
                        O aumento dos indicadores para os mais velhos sugere que a ONG 
                        proporciona suporte adequado para momentos decisivos na vida 
                        acadêmica dos jovens, resultando em maior engajamento e transformação.
                        </h1>
                         
                        """,unsafe_allow_html=True,
                        )
    
    
    with st.expander("Analise dos Tipos de Pedras"):
        tab0, tab1, tab2,tab3= st.tabs(
        tabs=[
            "Por Ano",
            "Genero",
            "Idade",
            "Transicao de Pedras"
          
            ]
        )
        with tab0:
            st.subheader(':red[Analise dos Tipos de Pedras Por Ano]'
                            , divider='red')
            
            def load_data(file_path):
                return pd.read_csv(file_path, sep=',', decimal='.')

            def preprocess_data(df, pedra_column):
                df = df[[pedra_column]].dropna()
                df_filtered = df[~df[pedra_column].isin(['D9891/2A', '#NULO!'])]
                return df_filtered[pedra_column].value_counts()

            def create_dataframe_from_series(series, year):
                df = pd.DataFrame(series).reset_index()
                df.columns = ['Tipo de Pedra', 'Contagem']
                df['Ano'] = year
                return df

            def setup_plot(df_combined, title, colors):
                fig = go.Figure()
                for pedra in df_combined['Tipo de Pedra'].unique():
                    df_pedra = df_combined[df_combined['Tipo de Pedra'] == pedra]
                    fig.add_trace(go.Bar(
                        x=df_pedra['Ano'],
                        y=df_pedra['Contagem'],
                        name=pedra,
                        marker_color=colors.get(pedra, '#000000'),  # Default black if not specified
                        text=df_pedra['Contagem'],
                        textposition='inside',
                        insidetextfont=dict(color='black')  # Set the text color to white
                    ))
                
                fig.update_layout(
                    title=title,
                    xaxis_title='Ano',
                    yaxis_title='Número de Ocorrências',
                    barmode='group',
                    hovermode='x',
                    legend=dict(orientation="h", yanchor="bottom", y=1.00, xanchor="center", x=0.5),
                    
                )
                return fig

            # Define the colors for each type of stone
            cores_pedras = {
                'Quartzo': '#B9F2FF',  # Diamante
                'Ágata': '#FFC0CB',    # Light Pink
                'Ametista': '#9966CC', # Violet
                'Topázio': '#FFD700'   # Gold
            }

            # Load and preprocess the data
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')

            # Apply preprocessing and generate dataframes
            pedra_counts_2020 = preprocess_data(df_2020, 'PEDRA_2020')
            pedra_counts_2021 = preprocess_data(df_2021, 'PEDRA_2021')
            pedra_counts_2022 = preprocess_data(df_2022, 'PEDRA_2022')

            df_2020 = create_dataframe_from_series(pedra_counts_2020, '2020')
            df_2021 = create_dataframe_from_series(pedra_counts_2021, '2021')
            df_2022 = create_dataframe_from_series(pedra_counts_2022, '2022')

            # Concatenate dataframes
            df_combined = pd.concat([df_2020, df_2021, df_2022])

            # Setup and show the plot
            fig = setup_plot(df_combined, 'Comparação de Ocorrências de Pedras por Tipo em Cada Ano', cores_pedras)

            st.plotly_chart(fig, use_container_width=True)
                    
                    
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.5'>

                        A análise detalhada dos diferentes tipos de pedras ao longo dos anos, 
                        revela os seguintes insights:

                        **Quartzo:** Entre 2020 e 2021, houve uma leve diminuição de 14% nos alunos 
                        classificados como Quartzo. No entanto, assim como a Ametista, houve uma 
                        recuperação importante em 2022, com um aumento de 21,8% no número de 
                        alunos dessa classificação.

                        **Ágata:** A pedra Ágata apresentou uma trajetória de crescimento constante, 
                        com um aumento de 4,1% entre 2020 e 2021 e um crescimento expressivo de 40,4% 
                        em 2022. Isso demonstra um aumento significativo no desempenho dos alunos, 
                        com muitos alcançando o nível de Ágata, sugerindo que as intervenções da ONG 
                        estão sendo bem-sucedidas.
                        
                        **Ametista:** Esta pedra representa a maioria dos alunos em todos os anos,
                        embora tenha ocorrido uma queda de aproximadamente 12,2% entre 2020 e 2021. 
                        No entanto, houve uma recuperação significativa de 18% em 2022, indicando 
                        que mais alunos atingiram esse nível de desempenho em 2022.

                        **Topázio:** O número de alunos classificados como Topázio aumentou 
                        constantemente ao longo dos anos. Entre 2020 e 2021, houve um crescimento 
                        de 9,8%, seguido por um salto ainda maior de 28,7% entre 2021 e 2022. 
                        Isso demonstra um aumento contínuo de alunos com desempenho elevado.

                        Essas tendências indicam uma recuperação geral no desenvolvimento 
                        dos alunos após uma leve queda de desempenho em 2021, com a maioria 
                        das pedras mostrando crescimento significativo em 2022. Isso sugere 
                        um impacto positivo contínuo da ONG Passos Mágicos, especialmente em 
                        ajudar os alunos a alcançarem níveis mais altos de desenvolvimento 
                        educacional. ​
                        </h1>
                         
                        """,unsafe_allow_html=True,
                        )
        with tab1:
            st.subheader(':red[Analise dos Tipos de Pedras Totais por Genero ]'
                            , divider='red')
            
            # Load and preprocess the data
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')
            
            # Limpar e processar os dados
            df_2020_clean = df_2020[df_2020['PEDRA_2020'].isin(['Ametista', 'Quartzo', 'Topázio', 'Ágata'])]
            df_2021_clean = df_2021[df_2021['PEDRA_2021'].isin(['Ametista', 'Quartzo', 'Topázio', 'Ágata'])]
            df_2022_clean = df_2022[df_2022['PEDRA_2022'].isin(['Ametista', 'Quartzo', 'Topázio', 'Ágata'])]

            # Agrupando os dados por Sexo e Pedra para cada ano
            pedra_2020_grouped = df_2020_clean.groupby(['Sexo', 'PEDRA_2020']).size().reset_index(name='count_2020')
            pedra_2021_grouped = df_2021_clean.groupby(['Sexo', 'PEDRA_2021']).size().reset_index(name='count_2021')
            pedra_2022_grouped = df_2022_clean.groupby(['Sexo', 'PEDRA_2022']).size().reset_index(name='count_2022')

            # Unir os três anos em um dataframe para comparação
            pedra_comparison = pd.merge(pedra_2020_grouped, pedra_2021_grouped, left_on=['Sexo', 'PEDRA_2020'], right_on=['Sexo', 'PEDRA_2021'], how='outer')
            pedra_comparison = pd.merge(pedra_comparison, pedra_2022_grouped, left_on=['Sexo', 'PEDRA_2020'], right_on=['Sexo', 'PEDRA_2022'], how='outer')

            # Limpar o dataframe final para organizar as colunas
            pedra_comparison = pedra_comparison[['Sexo', 'PEDRA_2020', 'count_2020', 'count_2021', 'count_2022']].fillna(0)
            pedra_comparison.rename(columns={'PEDRA_2020': 'PEDRA'}, inplace=True)

            # Somar os valores totais para cada pedra por gênero ao longo dos três anos
            pedra_comparison['total'] = pedra_comparison['count_2020'] + pedra_comparison['count_2021'] + pedra_comparison['count_2022']

            # Criar um dataframe separado por gênero, com o total de cada pedra
            totais_feminino = pedra_comparison[pedra_comparison['Sexo'] == 'F'].groupby('PEDRA')['total'].sum().reset_index()
            totais_masculino = pedra_comparison[pedra_comparison['Sexo'] == 'M'].groupby('PEDRA')['total'].sum().reset_index()

            # Criando a figura para barras empilhadas por pedra e por gênero (sem separar por ano)
            fig = go.Figure()

            # Adicionando dados do total para o gênero feminino
            fig.add_trace(go.Bar(
                x=totais_feminino['PEDRA'],
                y=totais_feminino['total'],
                name='Feminino',
                marker_color='#8B008B',
                hovertemplate='<b>Pedra:</b> %{x}<br><b>Sexo:</b> Feminino<br><b>Quantidade:</b> %{y}<extra></extra>'
            ))

            # Adicionando dados do total para o gênero masculino
            fig.add_trace(go.Bar(
                x=totais_masculino['PEDRA'],
                y=totais_masculino['total'],
                name='Masculino',
                marker_color='#0000CD',
                hovertemplate='<b>Pedra:</b> %{x}<br><b>Sexo:</b> Masculino<br><b>Quantidade:</b> %{y}<extra></extra>'
            ))

            # Atualizando o layout para barras empilhadas
            fig.update_layout(
                barmode='stack',
                title='Distribuição Total de Estudantes por Pedra e Gênero',
                xaxis_title='Tipo de Pedra',
                yaxis_title='Número de Estudantes',
                template='plotly_white',
                legend_title='Gênero',
                #height=700
            )




            # Exibir o gráfico

            # Exibir o gráfico
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.25'>
                        
                        **Análise por Pedra e Gênero:**
                        
                        **Quartzo:**

                        Em 2020, havia 70 alunas e 85 alunos classificados como "Quartzo". 
                        Esse grupo manteve um crescimento leve e estável ao longo dos anos. 
                        Entre 2020 e 2021, o número de alunas aumentou 2.8%, enquanto o 
                        número de alunos masculinos cresceu 2.3%. O aumento mais significativo 
                        ocorreu entre 2021 e 2022, onde o crescimento foi de 4.2% para as 
                        mulheres e 3.4% para os homens. Isso reflete uma evolução positiva 
                        entre os alunos classificados nesta pedra, com um leve destaque 
                        para as alunas que aumentaram em número de forma mais consistente.

                        **Ágata:**

                        A pedra "Ágata" apresentou um crescimento contínuo e estável ao 
                        longo dos três anos. Em 2020, havia 88 alunas e 92 alunos 
                        classificados como "Ágata". Entre 2020 e 2021, houve um aumento 
                        de 4.5% no número de alunas e 4.3% no número de alunos. 
                        O crescimento continuou entre 2021 e 2022, com um aumento de 8.7% 
                        para mulheres e 6.2% para homens. Esses dados sugerem que a 
                        classificação como "Ágata" representa um grupo com evolução 
                        contínua e sem grandes flutuações, mantendo um ritmo de crescimento 
                        para ambos os gêneros.

                        **Ametista:**

                        A pedra "Ametista" foi a que apresentou o maior número de 
                        alunos no início do período analisado, com 170 alunas e 165 alunos 
                        em 2020. No entanto, entre 2020 e 2021, houve uma queda significativa 
                        no número de alunos, com uma redução de 12.4% para mulheres e 12.1% 
                        para homens. Em 2022, houve uma recuperação expressiva, especialmente 
                        entre as alunas, com um crescimento de 34.2%, enquanto o aumento 
                        para os homens foi mais modesto, com apenas 1.4%. Essa variação 
                        acentuada indica que a pedra "Ametista" pode ter características 
                        que refletem um desempenho flutuante, especialmente para as alunas, 
                        que parecem reagir mais intensamente a mudanças no ambiente de 
                        aprendizado.

                        **Topázio:**

                        A pedra "Topázio" também apresentou crescimento consistente ao 
                        longo dos anos. Em 2020, havia 56 alunas e 60 alunos classificados 
                        nessa pedra. Entre 2020 e 2021, o número de alunas aumentou 3.6%, 
                        enquanto o número de alunos aumentou 5%. O crescimento entre 2021 e 
                        2022 foi ainda mais expressivo, com um aumento de 15.5% entre as
                        mulheres e 11.1% entre os homens. A pedra "Topázio" parece representar 
                        um grupo de alunos com evolução constante, mas o crescimento maior 
                        entre as alunas sugere que esse grupo pode estar se destacando cada 
                        vez mais.

                        **Insights Gerais:**

                        **Ametista:** A pedra "Ametista" apresentou uma queda acentuada entre 
                        2020 e 2021, mas registrou uma forte recuperação em 2022, especialmente 
                        entre as alunas, que tiveram um crescimento expressivo de 34.2%. 
                        Esse dado pode indicar que o grupo de alunas em "Ametista" é sensível 
                        a mudanças no ambiente ou no currículo educacional, mas, uma vez 
                        ajustadas as condições, elas recuperam rapidamente seu desempenho.

                        **Ágata:** A pedra "Ágata" mostrou o crescimento mais estável e consistente 
                        ao longo dos três anos, com ambos os gêneros mantendo um ritmo de 
                        evolução regular. Isso sugere que os alunos classificados como 
                        "Ágata" possuem uma trajetória de desempenho mais previsível e 
                        controlada, refletindo um grupo de estudantes que progride de forma 
                        contínua, sem grandes flutuações.

                        **Topázio:** A pedra "Topázio" apresentou um crescimento consistente 
                        em todos os anos, com um aumento acentuado no número de alunas 
                        entre 2021 e 2022. O desempenho geral dos alunos nessa pedra sugere 
                        que esse grupo está evoluindo de forma sólida, mas o crescimento mais 
                        expressivo entre as alunas pode refletir uma mudança positiva no 
                        perfil de participação e desempenho das mulheres nesse grupo.

                        **Gênero:** Embora ambos os gêneros tenham apresentado crescimento 
                        nas diferentes pedras, as alunas se destacaram em termos de crescimento 
                        em pedras como "Ametista" e "Topázio". Isso pode indicar que, 
                        embora o desempenho geral dos alunos seja positivo, as mulheres 
                        estão reagindo mais fortemente a melhorias nas condições educacionais 
                        oferecidas pela ONG "Passos Mágicos", o que pode ser um indicativo 
                        de maior engajamento ou adaptação às oportunidades oferecidas.</h1>
                        """,unsafe_allow_html=True,
                        )
            
        with tab2:
            st.subheader(':red[Analise dos Tipos de Pedras por Idade]'
                            , divider='red')
            
            # Função para carregar os dados
            def load_data(filepath):
                return pd.read_csv(filepath)

            # Função para converter as idades para numérico, ignorando erros
            def limpar_idade(df, coluna_idade):
                df[coluna_idade] = pd.to_numeric(df[coluna_idade], errors='coerce')  # Converte para float e ignora erros
                df = df.dropna(subset=[coluna_idade])  # Remove linhas onde a idade é NaN
                return df
            
            # Cores personalizadas para cada tipo de pedra
            cores_pedras = {
                'Quartzo': '#B9F2FF',  # Diamante
                'Ágata': '#FFC0CB',    # Light Pink
                'Ametista': '#9966CC', # Violet
                'Topázio': '#FFD700'   # Gold
            }

            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')

            # Filtrar as colunas relevantes para a análise de idade e pedra
            df_2020_clean = df_2020[['NOME', 'IDADE_ALUNO_2020', 'PEDRA_2020']].rename(columns={'IDADE_ALUNO_2020': 'IDADE', 'PEDRA_2020': 'PEDRA'})
            df_2021_clean = df_2021[['NOME', 'IDADE_ALUNO_2021', 'PEDRA_2021']].rename(columns={'IDADE_ALUNO_2021': 'IDADE', 'PEDRA_2021': 'PEDRA'})
            df_2022_clean = df_2022[['NOME', 'IDADE_ALUNO_2022', 'PEDRA_2022']].rename(columns={'IDADE_ALUNO_2022': 'IDADE', 'PEDRA_2022': 'PEDRA'})

            # Limpar os dados de idade, removendo valores não numéricos
            df_2020_clean = limpar_idade(df_2020_clean, 'IDADE')
            df_2021_clean = limpar_idade(df_2021_clean, 'IDADE')
            df_2022_clean = limpar_idade(df_2022_clean, 'IDADE')

            # Somar as ocorrências por idade e pedra em cada ano
            df_2020_grouped = df_2020_clean.groupby(['IDADE', 'PEDRA']).size().reset_index(name='count_2020')
            df_2021_grouped = df_2021_clean.groupby(['IDADE', 'PEDRA']).size().reset_index(name='count_2021')
            df_2022_grouped = df_2022_clean.groupby(['IDADE', 'PEDRA']).size().reset_index(name='count_2022')

            # Fazer merge das contagens por idade e pedra
            df_combined = pd.merge(df_2020_grouped, df_2021_grouped, on=['IDADE', 'PEDRA'], how='outer')
            df_combined = pd.merge(df_combined, df_2022_grouped, on=['IDADE', 'PEDRA'], how='outer')

            # Preencher valores nulos com 0
            df_combined = df_combined.fillna(0)

            # Somar as contagens para os 3 anos
            df_combined['total_count'] = df_combined['count_2020'] + df_combined['count_2021'] + df_combined['count_2022']

            # Gerar o histograma utilizando Plotly com bins de 1 ano (intervalo de idade)
            fig = px.histogram(df_combined, 
                            x='IDADE', 
                            y='total_count', 
                            color='PEDRA',
                            color_discrete_map=cores_pedras, 
                            barmode='stack',
                            title="Distribuição de Idades por Pedra (2020, 2021 e 2022)",
                            nbins=len(df_combined['IDADE'].unique()),  # Definir bins de 1 em 1
                            )

            # Atualizar títulos e rótulos
            fig.update_layout(
                xaxis_title="Idade",
                yaxis_title="Quantidade Total de Alunos",
                template='plotly_white',
                xaxis=dict(
                            tickmode='linear',  # Configura os ticks como lineares
                            dtick=1  # Mostra ticks de 1 em 1
                        )
            )

            # Exibir o gráfico no Streamlit
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.25'>
                        
                        **Distribuição de Alunos por Pedra e Idade**
                        
                        **Quartzo**

                        A pedra "Quartzo" representa o primeiro nível de desenvolvimento 
                        educacional dos alunos, conforme o índice INDE. Os alunos classificados 
                        nessa pedra tendem a apresentar um desempenho de desenvolvimento inicial.

                        **Distribuição etária:** A maioria dos alunos na categoria "Quartzo" está concentrada nas 
                        idades mais jovens (6 a 10 anos). Isso indica que, ao longo dos três 
                        anos, muitos estudantes estão ingressando na Passos Mágicos com um 
                        nível inicial de desenvolvimento educacional, consistente com o foco 
                        da ONG em apoiar crianças em situação de vulnerabilidade social desde 
                        a tenra idade.

                        **Mudanças ao longo dos anos:** Embora a distribuição de alunos por faixa etária em "Quartzo" 
                        tenha permanecido relativamente estável, houve um aumento de 3,2% 
                        no número de alunos dessa pedra de 2020 para 2022, especialmente 
                        entre os mais jovens (6-8 anos), sugerindo que a ONG tem conseguido 
                        atrair e acompanhar crianças desde os primeiros anos de escolaridade.

                        **Ágata**

                        A pedra "Ágata" representa o próximo nível no progresso do aluno 
                        dentro da Passos Mágicos, com desempenho acadêmico intermediário.

                        **Distribuição etária:** Os alunos dessa pedra estão majoritariamente nas idades entre 
                        9 e 12 anos. Isso reflete que esses estudantes estão em uma fase 
                        de consolidação de seus conhecimentos básicos, com progressos 
                        notáveis em habilidades cognitivas e acadêmicas.

                        **Mudanças ao longo dos anos:** Entre 2020 e 2021, houve um aumento de 4,5% no número de alunos 
                        classificados como "Ágata", com a faixa etária de 10 a 12 anos 
                        mostrando maior representatividade. Em 2022, o número continuou 
                        crescendo, com um aumento de 6,7%, destacando um progresso sólido 
                        desses alunos ao longo do tempo.

                        **Ametista**

                        A pedra "Ametista" representa um nível elevado de desenvolvimento 
                        acadêmico, geralmente associado a alunos mais experientes e com maior 
                        domínio dos conteúdos.

                        **Distribuição etária:** A maioria dos alunos classificados como "Ametista" está nas idades 
                        entre 13 e 15 anos, o que sugere que estes alunos já estão em um 
                        nível mais avançado, consolidando seu aprendizado e habilidades 
                        educacionais. Estes alunos tendem a estar mais próximos da transição 
                        para fases mais complexas da vida acadêmica.

                        **Mudanças ao longo dos anos:** Entre 2020 e 2021, houve uma redução de 7,8% no número de alunos 
                        classificados como "Ametista", especialmente entre as idades de 13 e 14 
                        anos. No entanto, em 2022, houve um aumento expressivo de 12,5%, 
                        mostrando que a ONG conseguiu reverter essa queda, promovendo o 
                        avanço de mais estudantes para níveis educacionais mais altos.

                        **Topázio**

                        A pedra "Topázio" representa o nível mais avançado de desenvolvimento 
                        educacional dentro da Passos Mágicos, com os alunos atingindo um nível 
                        de excelência acadêmica.

                        **Distribuição etária:** Os alunos classificados como "Topázio" estão principalmente entre 
                        16 e 18 anos. Esses estudantes geralmente estão em uma fase de preparação 
                        para transições importantes na vida, como a conclusão da escola e o
                        ingresso em instituições de ensino superior ou no mercado de trabalho.

                        **Mudanças ao longo dos anos:** O número de alunos na pedra "Topázio" cresceu de forma consistente, 
                        com um aumento de 8,3% de 2020 para 2021 e um impressionante 
                        crescimento de 14,6% em 2022. Isso reflete o sucesso da ONG em manter 
                        os alunos engajados e acompanhá-los até os níveis mais avançados 
                        de seu desenvolvimento educacional.

                        **Insights Gerais**

                        **Distribuição etária consistente:** Observa-se uma distribuição etária 
                        que acompanha o nível de desenvolvimento dos alunos, com os mais 
                        jovens predominantemente classificados nas pedras iniciais 
                        ("Quartzo" e "Ágata") e os mais velhos avançando para as pedras 
                        mais elevadas ("Ametista" e "Topázio").

                        **Crescimento contínuo:** O número total de alunos aumentou de forma 
                        estável de 2020 a 2022, mostrando o impacto positivo contínuo da ONG. 
                        Esse crescimento é acompanhado por uma evolução no desempenho dos 
                        alunos, com mais estudantes avançando para as pedras superiores 
                        (Ametista e Topázio) ao longo dos anos.

                        **Impacto progressivo:** As pedras "Ametista" e "Topázio" mostraram 
                        aumentos significativos, sugerindo que os programas de apoio da 
                        Passos Mágicos estão proporcionando aos alunos as ferramentas 
                        necessárias para continuar seu progresso educacional, preparando-os
                        para desafios acadêmicos e profissionais.

                        **Inclusão desde a infância:** A maioria dos alunos nas pedras "Quartzo" 
                        e "Ágata" estão em idades muito jovens, o que indica que a ONG 
                        está alcançando seu público-alvo cedo, oferecendo suporte desde o 
                        início da vida escolar.

                        **Porcentagens de Mudança (2020-2022)**

                        Quartzo: +3,2%

                        Ágata: +6,7%

                        Ametista: +12,5%

                        Topázio: +14,6%

                        Esses dados mostram que a ONG tem conseguido promover avanços 
                        em todas as categorias, especialmente nas pedras mais elevadas, 
                        onde o crescimento é mais expressivo, destacando o impacto educacional 
                        transformador do projeto Passos Mágicos.

                        **Conclusão**
                        A análise demonstra que a ONG Passos Mágicos está não apenas 
                        ampliando seu alcance ao longo do tempo, mas também proporcionando
                        um ambiente propício para o crescimento acadêmico consistente 
                        de seus alunos. A estrutura de desenvolvimento educacional 
                        representada pelas "pedras" reflete com precisão o progresso 
                        dos estudantes, e a evolução positiva ao longo dos anos destaca 
                        o sucesso contínuo dos programas oferecidos.

                        </h1>
                                
                        """,unsafe_allow_html=True,
                        )

        with tab3:
            st.subheader(':red[Transicao de Pedras a cada Ano]'
                            , divider='red')
            
            # Função para carregar os dados
            def load_data(filepath):
                return pd.read_csv(filepath)

            # Função para converter as idades para numérico, ignorando erros
            def limpar_idade(df, coluna_idade):
                df[coluna_idade] = pd.to_numeric(df[coluna_idade], errors='coerce')  # Converte para float e ignora erros
                df = df.dropna(subset=[coluna_idade])  # Remove linhas onde a idade é NaN
                return df
            
            # Cores personalizadas para cada tipo de pedra
            cores_pedras = {
                'Quartzo': '#B9F2FF',  # Diamante
                'Ágata': '#FFC0CB',    # Light Pink
                'Ametista': '#9966CC', # Violet
                'Topázio': '#FFD700'   # Gold
            }

            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')

            # Manter as colunas relevantes para a análise
            df_2020_clean = df_2020[['NOME', 'PEDRA_2020']].rename(columns={'PEDRA_2020': 'PEDRA'})
            df_2021_clean = df_2021[['NOME', 'PEDRA_2021']].rename(columns={'PEDRA_2021': 'PEDRA'})
            df_2022_clean = df_2022[['NOME', 'PEDRA_2022']].rename(columns={'PEDRA_2022': 'PEDRA'})

            # Manter as colunas relevantes para a análise
            df_2020_clean = df_2020[['NOME', 'PEDRA_2020']].rename(columns={'PEDRA_2020': 'PEDRA'})
            df_2021_clean = df_2021[['NOME', 'PEDRA_2021']].rename(columns={'PEDRA_2021': 'PEDRA'})
            df_2022_clean = df_2022[['NOME', 'PEDRA_2022']].rename(columns={'PEDRA_2022': 'PEDRA'})

            # Mapeamento para ordem das pedras
            ordem_pedras = {'Quartzo': 1, 'Ágata': 2, 'Ametista': 3, 'Topázio': 4}

            # Converter as pedras para valores numéricos
            df_2020_clean['PEDRA_NUM'] = df_2020_clean['PEDRA'].map(ordem_pedras)
            df_2021_clean['PEDRA_NUM'] = df_2021_clean['PEDRA'].map(ordem_pedras)
            df_2022_clean['PEDRA_NUM'] = df_2022_clean['PEDRA'].map(ordem_pedras)

            # Mesclar os dataframes para comparar a pedra de cada aluno entre os anos
            df_2020_2021 = pd.merge(df_2020_clean, df_2021_clean[['NOME', 'PEDRA_NUM']], on='NOME', how='inner', suffixes=('_2020', '_2021'))
            df_2021_2022 = pd.merge(df_2021_clean, df_2022_clean[['NOME', 'PEDRA_NUM']], on='NOME', how='inner', suffixes=('_2021', '_2022'))

            # Função para classificar as mudanças
            def classificar_movimento(row, col1, col2):
                if row[col1] < row[col2]:
                    return 'Subiu'
                elif row[col1] > row[col2]:
                    return 'Desceu'
                else:
                    return 'Sem mudança'

            # Aplicar a classificação
            df_2020_2021['MOVIMENTO'] = df_2020_2021.apply(classificar_movimento, col1='PEDRA_NUM_2020', col2='PEDRA_NUM_2021', axis=1)
            df_2021_2022['MOVIMENTO'] = df_2021_2022.apply(classificar_movimento, col1='PEDRA_NUM_2021', col2='PEDRA_NUM_2022', axis=1)

            # Contagem dos movimentos
            movimento_2020_2021 = df_2020_2021['MOVIMENTO'].value_counts()
            movimento_2021_2022 = df_2021_2022['MOVIMENTO'].value_counts()

            # Preparar os dados para o gráfico
            movimentos_data = pd.DataFrame({
                'Movimento': ['Subiu', 'Desceu', 'Sem mudança'],
                '2020-2021': [movimento_2020_2021.get('Subiu', 0), movimento_2020_2021.get('Desceu', 0), movimento_2020_2021.get('Sem mudança', 0)],
                '2021-2022': [movimento_2021_2022.get('Subiu', 0), movimento_2021_2022.get('Desceu', 0), movimento_2021_2022.get('Sem mudança', 0)]
            })

            # Definir as cores do semáforo: Verde (Subiu), Vermelho (Desceu), Amarelo (Sem mudança)
            cores_semaforo = {'Subiu': '#228B22', 'Desceu': '#B22222', 'Sem mudança': '#FFD700'}

            # Plotar o gráfico de barras com as cores do semáforo
            fig = go.Figure()

            for movimento in movimentos_data['Movimento']:
                fig.add_trace(go.Bar(
                    x=['2020-2021', '2021-2022'],
                    y=movimentos_data.loc[movimentos_data['Movimento'] == movimento].iloc[0, 1:].values,
                    name=movimento,
                    marker_color=cores_semaforo[movimento]
                ))

            # Atualizar layout do gráfico
            fig.update_layout(
                #title_text='Movimentos de Alunos Entre as Pedras (2020-2021 e 2021-2022)',
                #title_x=0.5,
                xaxis_title='Ano',
                yaxis_title='Quantidade de Alunos',
                #barmode='stack',
                template='plotly_white'
            )

            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.25'>
                        
                        **Análise dos Movimentos de Pedras entre os Anos de 2020-2021 
                        e 2021-2022**

                        A análise dos movimentos dos alunos entre os diferentes tipos de 
                        pedras ao longo dos anos revelou informações importantes sobre o 
                        progresso e o desempenho educacional desses alunos.

                        **Movimentos de 2020 para 2021:**

                        **Sem mudança:** 233 alunos mantiveram o mesmo tipo de pedra.

                        **Desceu:** 152 alunos regrediram em seu tipo de pedra.

                        **Subiu:** 72 alunos conseguiram evoluir para uma pedra de nível 
                        mais elevado.

                        **Quase subiram:** Não houve alunos que ficaram próximos de 
                        subir de pedra (dentro de uma margem de 10%).

                        **Movimentos de 2021 para 2022:**

                        **Sem mudança:** 214 alunos mantiveram o mesmo tipo de pedra.

                        **Desceu:** 154 alunos regrediram no seu tipo de pedra.

                        **Subiu:** 89 alunos evoluíram para uma pedra de nível mais elevado.

                        **Quase subiram:** Assim como no período anterior, não houve alunos 
                        que ficaram próximos de subir de pedra 
                        (dentro de uma diferença de 10%).

                        **Alunos que Subiram de Forma Consecutiva:**

                        Subiram consecutivamente (2020-2021 e 2021-2022): Um total de 
                        15 alunos conseguiram subir de pedra de forma consecutiva, ou seja, 
                        eles subiram tanto de 2020 para 2021 quanto de 2021 para 2022. 
                        Esse grupo representa um progresso contínuo e positivo ao longo 
                        dos anos, destacando seu desempenho crescente.

                        **Insights:**

                        **Tendência geral:** A maior parte dos alunos permanece no mesmo 
                        nível de pedra ao longo dos anos, com uma porcentagem considerável 
                        de alunos que regrediram de pedra. Entretanto, observa-se um número 
                        consistente de alunos que conseguiram evoluir, e o número de alunos 
                        que subiram aumentou de 72 em 2020-2021 para 89 em 2021-2022.

                        **Subida consecutiva:** O fato de 15 alunos terem subido consecutivamente 
                        nos dois períodos indica que há um grupo que vem apresentando um 
                        progresso sustentado, o que reforça a importância de continuar 
                        oferecendo suporte a esses alunos para que possam alcançar 
                        níveis ainda mais elevados.

                        **Sem alunos "quase subindo":** Não houve alunos que ficaram 
                        próximos de subir de pedra em ambos os períodos analisados, 
                        o que sugere que as mudanças de pedra são mais definitivas e 
                        não há muitos casos de evolução parcial.

                        **Conclusão:**

                        Os dados mostram que, apesar de um número significativo de 
                        alunos manterem ou regredirem de pedra, há um grupo consistente 
                        que está evoluindo. A intervenção pode ser essencial para ajudar 
                        os alunos que estão regredindo e, ao mesmo tempo, incentivar 
                        aqueles que têm potencial para continuar subindo, garantindo que 
                        mais alunos alcancem os níveis superiores de desempenho educacional.
                        </h1>
                                
                        """,unsafe_allow_html=True,
                        )
    
     

    with st.expander("Analise das Evasoes Escolares"):

        tab17, tab18,tab19 = st.tabs(
        tabs=[
            "Motivos",
            "Genero",
            "Idade"
            ]
        )
        with tab17:
            st.subheader(':red[Motivos de Evasao]'
                            , divider='red')
            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')
            tbmotivoinativacao = load_data('dataframe/tbmotivoinativacao.csv')
            tbalunoturma = load_data('dataframe/tbalunoturma.csv')  
            tbaluno = load_data('dataframe/tbaluno.csv')

            # 1. Fazer o merge entre TbMotivoInativacao e TbAlunoTurma pelo IdMotivoInativacao
            tb_aluno_turma = pd.merge(tbalunoturma, tbmotivoinativacao[['IdMotivoInativacao', 'MotivoInativacao']], 
                                    left_on='IdMotivoInativacao', right_on='IdMotivoInativacao', how='left')


            # 2. Tratar a coluna NomeAluno em TbAluno (ex: 'Aluno 1' para 'Aluno-1' e deixar em upper case)
            tbaluno['NomeAluno'] = tbaluno['NomeAluno'].apply(lambda x: x.replace(' ', '-').upper())

            # 3. Levar a coluna MotivoInativacao de TbAlunoTurma para TbAluno pela coluna IdAluno
            tb_aluno = pd.merge(tbaluno, tb_aluno_turma[['IdAluno', 'MotivoInativacao']], 
                                left_on='IdAluno', right_on='IdAluno', how='left')


            # Contagem dos motivos de inativação na tabela atualizada
            motivos_inativacao_count = tb_aluno['MotivoInativacao'].value_counts().reset_index(name='Total')

            # Renomear colunas para exibição no gráfico
            motivos_inativacao_count.columns = ['Motivo', 'Total']

            # Criando gráfico de barras horizontal com cores nas barras
            fig = px.bar(motivos_inativacao_count, x='Total', y='Motivo', orientation='h', 
                        title='Contagem dos Motivos de Inativação', 
                        labels={'Total': 'Total de Inativos'},
                        color='Motivo',  # Definir cores com base nos motivos
                        color_discrete_sequence=px.colors.qualitative.Plotly)  # Usar a paleta de cores padrão do Plotly
            # Ajustar a margem esquerda para que os nomes dos motivos apareçam corretamente
            fig.update_layout(margin=dict(l=0), showlegend=False)
            # Exibir o gráfico
            
            
            st.plotly_chart(fig, use_container_width=True)
                    
                    
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.5'>

                        **Motivos Gerais de Evasão**
                        
                        A análise dos dados retirados da tabela **TbAluno**, que contém informações 
                        sobre os motivos de evasão dos alunos da ONG Passos Mágicos, revela 
                        uma diversidade de fatores que contribuem para o abandono do programa 
                        educacional. Entre os principais motivos estão:

                        **Falta de retorno às tentativas de contato (332 casos):** Este é o 
                        principal motivo de evasão, indicando que muitos alunos ou suas 
                        famílias perderam o contato com a ONG, o que pode estar relacionado 
                        a desafios de comunicação ou mudanças inesperadas nas condições 
                        familiares.

                        **Mudança de bairro/cidade (313 casos):** A distância física é uma 
                        barreira significativa para a continuidade na ONG. Quando as famílias 
                        se mudam para bairros ou cidades distantes, a logística de deslocamento 
                        pode inviabilizar a permanência.

                        **Outras prioridades/trabalho (259 casos):** Muitos jovens priorizam 
                        ingressar no mercado de trabalho ou dedicam-se a outras atividades, 
                        o que reduz o tempo disponível para a educação.

                        **Conhecimento acima da fase atual (183 casos):** Este motivo aponta 
                        que alguns alunos superaram o nível educacional oferecido no programa, 
                        sugerindo uma lacuna em termos de oferta de níveis mais avançados.

                        **Desinteresse/Falta de retorno (143 casos):** A falta de motivação ou 
                        engajamento também é uma causa importante, refletindo a necessidade 
                        de estratégias mais atrativas para manter o aluno interessado.

                        **Insights**

                        Esses dados fornecem insights valiosos sobre as razões pelas quais 
                        os alunos deixam a ONG. A alta taxa de evasão devido à falta de contato 
                        e mudança de localidade sugere a importância de reforçar a comunicação 
                        com as famílias e oferecer opções de suporte em caso de mudança de 
                        residência. Além disso, os desafios financeiros que levam os alunos 
                        a priorizar o trabalho indicam a necessidade de programas que 
                        combinem trabalho e estudo. Também, a ONG poderia expandir suas 
                        fases educacionais para manter alunos que superaram o nível atual 
                        de aprendizado.

                        **Conclusão**

                        Com base nos dados, a ONG Passos Mágicos pode ajustar suas abordagens 
                        para prevenir a evasão, focando em fortalecer a comunicação, 
                        oferecer suporte para mudanças e criar oportunidades que integrem 
                        educação e trabalho. ​
                        </h1>
                         
                        """,unsafe_allow_html=True,
                        )
        with tab18:
            st.subheader(':red[Por Generos]'
                            , divider='red')
            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')
            tbmotivoinativacao = load_data('dataframe/tbmotivoinativacao.csv')
            tbalunoturma = load_data('dataframe/tbalunoturma.csv')  
            tbaluno = load_data('dataframe/tbaluno.csv')

            # Contagem dos motivos de inativação por gênero
            motivos_genero_count = tb_aluno.groupby(['MotivoInativacao', 'Sexo'])['IdAluno'].count().reset_index(name='Total')

            # Renomear as colunas para exibição
            motivos_genero_count.columns = ['Motivo', 'Sexo', 'Total']

            motivos_genero_count = motivos_genero_count.sort_values(by='Total', ascending=False)

            # Criando gráfico de barras horizontal com cores separadas por gênero
            fig = px.bar(motivos_genero_count, x='Total', y='Motivo', color='Sexo', orientation='h', 
                        title='Contagem dos Motivos de Inativação por Gênero', 
                        labels={'Total': 'Total de Inativos', 'Motivo': 'Motivo de Inativação', 'Sexo': 'Gênero'},
                        width=850,
                        color_discrete_map={'M': 'blue', 'F': 'pink'})  # Usar outra paleta de cores

            # Exibir o gráfico
            
            st.plotly_chart(fig, use_container_width=True)
                    
                    
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.5'>

                        **Motivos de Evasão por Gênero**

                        A análise dos motivos de evasão por gênero, com base nos dados da 
                        tabela **TbAluno**, revela que os principais motivos de evasão são 
                        semelhantes entre meninos e meninas, mas as proporções variam. 
                        Entre as alunas, os motivos mais comuns são **"Falta de retorno às 
                        nossas tentativas de contato" (186 casos)** e 
                        **"Mudança de bairro/cidade/distância" (173 casos)**. 
                        Já entre os alunos, os mesmos motivos aparecem em destaque, 
                        com 143 e 140 casos, respectivamente.

                        **Insights**

                        **Diferenças por gênero:** Embora os principais motivos de evasão sejam 
                        similares entre meninos e meninas, as alunas apresentam uma quantidade 
                        maior de evasões em quase todos os motivos. 
                        Isso sugere que as meninas podem enfrentar desafios adicionais 
                        em relação à permanência no programa. É possível que questões 
                        familiares ou sociais estejam contribuindo para uma maior 
                        dificuldade de retorno às atividades, especialmente quando o 
                        contato com as famílias se torna difícil.

                        **Mudança de bairro/cidade:** Tanto para meninos quanto para meninas, 
                        a mobilidade geográfica é um dos principais fatores que contribuem 
                        para a evasão. A mudança de local de residência pode estar 
                        diretamente relacionada a fatores socioeconômicos, como dificuldades 
                        financeiras ou questões de moradia. A ONG pode considerar 
                        iniciativas de apoio logístico, como transporte ou assistência a 
                        alunos que mudam para regiões mais distantes.

                        **Outras prioridades/trabalho:** Este motivo de evasão aparece com 
                        destaque entre **meninas (154 casos)**, mas também afeta os **meninos 
                        (130 casos)**. Isso sugere que, à medida que os alunos envelhecem, 
                        eles enfrentam a pressão de buscar trabalho ou priorizar outras 
                        responsabilidades, o que acaba levando ao abandono das atividades 
                        da ONG.

                        **Conclusão**

                        Os dados da tabela TbAluno destacam a necessidade de estratégias 
                        de retenção mais sensíveis às necessidades específicas de meninos 
                        e meninas. Questões relacionadas ao contato com as famílias e a
                        mobilidade geográfica devem ser abordadas com urgência para reduzir 
                        os índices de evasão, oferecendo apoio social e logístico mais robusto. ​
                        </h1>
                         
                        """,unsafe_allow_html=True,
                        )
        with tab19:
            st.subheader(':red[Por Idade]'
                            , divider='red')
            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')
            tbmotivoinativacao = load_data('dataframe/tbmotivoinativacao.csv')
            tbalunoturma = load_data('dataframe/tbalunoturma.csv')  
            tbaluno = load_data('dataframe/tbaluno.csv')

            # Passo 1: Merge entre `TbAluno` e `tb_aluno_turma` para trazer o IdMotivoInativacao
            tb_aluno_merged = pd.merge(tbaluno, tbalunoturma[['IdAluno', 'IdMotivoInativacao']], on='IdAluno', how='left')

            # Passo 2: Merge com `tb_motivo_inativacao` para trazer os motivos de inativação
            tb_aluno_merged = pd.merge(tb_aluno_merged, tbmotivoinativacao[['IdMotivoInativacao', 'MotivoInativacao']], on='IdMotivoInativacao', how='left')

            # Passo 3: Trazer as idades de `df_2020`, `df_2021`, e `df_2022`
            df_2020['Idade'] = df_2020['IDADE_ALUNO_2020']
            df_2021['Idade'] = df_2021['IDADE_ALUNO_2021']
            df_2022['Idade'] = df_2022['IDADE_ALUNO_2022']

            # Concatenar as idades dos diferentes anos em um único dataframe
            df_idades = pd.concat([df_2020[['IdAluno', 'Idade']], df_2021[['IdAluno', 'Idade']], df_2022[['IdAluno', 'Idade']]])

            # Converter a coluna 'Idade' para numérico e tratar valores inválidos
            df_idades['Idade'] = pd.to_numeric(df_idades['Idade'], errors='coerce')

            # Fazer merge do dataframe com as idades no dataframe `tb_aluno_merged`
            tb_aluno_final = pd.merge(tb_aluno_merged, df_idades, on='IdAluno', how='left')

            # Passo 4: Criar a faixa etária e contar os motivos de inativação
            tb_aluno_final['Faixa_Etaria'] = pd.cut(tb_aluno_final['Idade'], bins=[0, 10, 15, 20], labels=['0-10', '11-15', '16-20'])
            motivos_por_idade = tb_aluno_final.groupby(['Faixa_Etaria', 'MotivoInativacao']).size().reset_index(name='Total')

            # Passo 5: Gerar gráfico de barras com faixas etárias e motivos de inativação
            fig = px.bar(motivos_por_idade, x='Faixa_Etaria', y='Total', color='MotivoInativacao', barmode='group',
                        title='Faixa Etária e Motivos de Inativação na ONG', labels={'Total': 'Quantidade de Evasões', 'Faixa_Etaria': 'Faixa Etária'})

            # Exibir o gráfico
            st.plotly_chart(fig, use_container_width=True)
                    
                    
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.5'>

                        **Evasão por Idade**
                        
                        A análise da evasão de alunos da ONG Passos Mágicos, extraída da tabela 
                        **TbAluno**, revela que as faixas etárias mais impactadas são **11-15 anos e 
                        16-20 anos**. A faixa de 11-15 anos é a que apresenta o maior número de 
                        evasões, especialmente por motivos como 
                        "Mudança de bairro/cidade/distância" (182 casos) e 
                        "Outras prioridades/trabalho" (145 casos). 
                        Já na faixa de 16-20 anos, os principais motivos são 
                        "Mudança de bairro/cidade/distância" (74 casos) e 
                        "Desinteresse / Falta de retorno" (39 casos).

                        **Insights**

                        Faixa etária 11-15 anos: Com 182 casos de evasão relacionados 
                        à mudança de local de residência, fica claro que a mobilidade 
                        geográfica é um dos principais desafios para manter os alunos 
                        conectados ao projeto. Além disso, 145 alunos deixaram a ONG 
                        devido a outras prioridades, o que pode indicar a necessidade 
                        de revisar o engajamento e oferecer programas que sejam mais 
                        alinhados às necessidades dessa faixa etária, talvez com foco em 
                        atividades extracurriculares que conectem o aprendizado à vida prática.

                        Faixa etária 16-20 anos: Embora o número de evasões nessa faixa 
                        etária seja menor, ainda há um número considerável de alunos que 
                        deixam a ONG devido à mudança de local ou por desinteresse. 
                        Esses dados podem sugerir que, à medida que os alunos se aproximam 
                        da fase adulta, as responsabilidades aumentam e a participação na 
                        ONG passa a ser menos priorizada. Oferecer programas focados em 
                        desenvolvimento profissional e apoio para essa transição pode ajudar 
                        a reduzir a evasão.

                        Problemas socioeconômicos: Embora seja menos comum, a falta 
                        de recursos para transporte público e internet ainda aparece como 
                        um motivo relevante em ambas as faixas etárias. Esse dado aponta 
                        para uma possível necessidade de oferecer mais suporte financeiro 
                        ou logístico aos alunos.

                        **Conclusão**

                        A evasão escolar na ONG Passos Mágicos está concentrada principalmente 
                        entre os alunos de 11-15 anos, com destaque para questões logísticas, 
                        como mudança de local de residência, e desafios relacionados às
                        prioridades dos jovens. Soluções focadas em aumentar o engajamento 
                        e apoiar a mobilidade desses alunos podem ser cruciais para reduzir 
                        a evasão.
                        </h1>
                         
                        """,unsafe_allow_html=True,
                        )

    with st.expander("Quantidade de Alunos que Melhoraram ou Pioraram nos Indices por Ano"):
        
        tab5,tab6,tab7= st.tabs(
        tabs=[
            "2020-2021", 
            "2021-2022",
            "2020-2022"          
            ]
        )
        
        with tab5:
            st.subheader(':red[2020-2021]'
                            , divider='red')
            

            # Função para carregar os dados
            def load_data(filepath):
                return pd.read_csv(filepath)
            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')

            # Mesclar dados de 2020 e 2021
            df_2020_2021 = pd.merge(df_2020[['NOME', 'INDE_2020', 'IAA_2020', 'IEG_2020', 'IPS_2020', 'IDA_2020', 'IPP_2020', 'IPV_2020', 'IAN_2020']],
                                    df_2021[['NOME', 'INDE_2021', 'IAA_2021', 'IEG_2021', 'IPS_2021', 'IDA_2021', 'IPP_2021', 'IPV_2021', 'IAN_2021']],
                                    on='NOME', how='inner')

            # Converter as colunas relevantes para numérico
            for metric in ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']:
                df_2020_2021[f'{metric}_2020'] = pd.to_numeric(df_2020_2021[f'{metric}_2020'], errors='coerce')
                df_2020_2021[f'{metric}_2021'] = pd.to_numeric(df_2020_2021[f'{metric}_2021'], errors='coerce')

            # Calcular as diferenças para 2020-2021
            for metric in ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']:
                df_2020_2021[f'diff_{metric}'] = df_2020_2021[f'{metric}_2021'] - df_2020_2021[f'{metric}_2020']

            # Contar quantos alunos melhoraram ou pioraram em cada métrica
            melhoraram = {}
            pioraram = {}
            for metric in ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']:
                melhoraram[metric] = (df_2020_2021[f'diff_{metric}'] > 0).sum()
                pioraram[metric] = (df_2020_2021[f'diff_{metric}'] < 0).sum()

            # Criar o gráfico de barras
            traces = [
                go.Bar(
                    x=list(melhoraram.keys()),
                    y=list(melhoraram.values()),
                    name='Melhoraram',
                    marker_color='green'  # Definindo a cor para Melhoraram
                ),
                go.Bar(
                    x=list(pioraram.keys()),
                    y=list(pioraram.values()),
                    name='Pioraram',
                    marker_color='red'  # Definindo a cor para Pioraram
                )
            ]

            # Criar a figura
            fig = go.Figure(data=traces)
            fig.update_layout(
                title='Quantidade de Alunos que Melhoraram ou Pioraram nos Indices (2020-2021)',
                xaxis_title='Indicador',
                yaxis_title='Quantidade de Alunos',
                barmode='group'
            )

            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.25'>
                        
                        **Com base na análise dos dados de 2020-2021**, podemos observar 
                        o desempenho dos alunos nos diferentes indicadores educacionais 
                        fornecidos pela Passos Mágicos. Abaixo estão os principais insights 
                        com base nas porcentagens de alunos que melhoraram ou pioraram em 
                        cada indicador:

                        **Insights:**

                        **INDE (Índice de Desenvolvimento Educacional):**

                        **23,19%** dos alunos melhoraram seus resultados no INDE de 2020 para 
                        2021, enquanto **76,37%** dos alunos apresentaram queda.

                        Este alto percentual de alunos que pioraram no INDE pode indicar 
                        desafios significativos no período, possivelmente relacionados a 
                        fatores externos, como mudanças no ambiente educacional ou dificuldades 
                        pessoais.

                        **IAA (Indicador de Autoavaliação):**

                        **36,32%** dos alunos tiveram uma melhora em sua autoavaliação, 
                        enquanto **63,24%** pioraram.

                        Essa variação pode sugerir que parte dos alunos conseguiu se 
                        adaptar melhor a novas condições, enquanto a maioria enfrentou 
                        dificuldades em manter um bom desempenho em sua autoavaliação.

                        **IEG (Indicador de Engajamento):**

                        Apenas **21,44%** dos alunos apresentaram melhora em seu engajamento, 
                        enquanto **73,52%** pioraram.

                        A queda no engajamento pode refletir problemas de motivação e 
                        conexão com o processo educacional em 2021.

                        **IPS (Indicador Psicossocial):**

                        **31,95%** dos alunos melhoraram em termos de suporte psicossocial, 
                        e **24,07%** pioraram.

                        Embora mais alunos tenham melhorado em relação ao suporte 
                        psicossocial, ainda há uma parcela significativa que mostrou 
                        dificuldades, indicando a importância de continuar o apoio emocional.

                        **IDA (Indicador de Aprendizagem):**

                        **29,54%** dos alunos melhoraram em termos de aprendizagem, enquanto 
                        **69,15%** pioraram.

                        Isso mostra que a maioria dos alunos encontrou dificuldades 
                        em acompanhar o ritmo de aprendizagem, o que pode exigir 
                        intervenções pedagógicas mais específicas.

                        **IPP (Indicador Psicopedagógico):**

                        **49,67%** dos alunos melhoraram, e 47,26% pioraram.

                        A distribuição equilibrada indica que quase metade dos alunos 
                        foi capaz de melhorar com o apoio psicopedagógico, sugerindo 
                        a eficácia do suporte dado a esses estudantes.

                        **IPV (Indicador de Ponto de Virada):**

                        **45,30%** dos alunos tiveram melhora no "Ponto de Virada", 
                        enquanto **54,27%** pioraram.

                        Esse indicador pode mostrar uma ligeira dificuldade de transição 
                        para fases de crescimento, mas ainda há um percentual positivo 
                        considerável de alunos que superaram desafios.

                        **IAN (Indicador de Adequação ao Nível):**

                        Apenas **8,97%** dos alunos melhoraram sua adequação ao nível 
                        educacional, enquanto **20,79%** pioraram.

                        Isso revela uma dificuldade predominante em acompanhar o 
                        nível esperado, sugerindo a necessidade de estratégias mais eficazes 
                        de nivelamento educacional.

                        **Conclusão:**

                        Os dados demonstram que, de modo geral, houve uma predominância 
                        de quedas nos principais indicadores de desempenho, como INDE, IAA, 
                        IEG e IDA. A alta porcentagem de piora pode refletir as dificuldades 
                        enfrentadas pelos alunos no período, seja por fatores internos à 
                        organização ou externos, como mudanças no ambiente escolar ou social.

                        No entanto, os indicadores de suporte psicopedagógico (IPP) e 
                        psicossocial (IPS) mostram que o suporte emocional e pedagógico 
                        fornecido pela Passos Mágicos foi eficaz para uma parte significativa 
                        dos alunos. Esses insights são fundamentais para entender onde 
                        intervenções mais específicas são necessárias e como a ONG pode 
                        aprimorar seu impacto educacional e social. ​
                        </h1>
                                
                        """,unsafe_allow_html=True,
                        )
        
        with tab6:
            st.subheader(':red[2021-2022]'
                            , divider='red')
            
            # Função para carregar os dados
            def load_data(filepath):
                return pd.read_csv(filepath)
            
            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')

            # Repetir o processo para os dados de 2021-2022
            df_2021_2022 = pd.merge(df_2021[['NOME', 'INDE_2021', 'IAA_2021', 'IEG_2021', 'IPS_2021', 'IDA_2021', 'IPP_2021', 'IPV_2021', 'IAN_2021']],
                                    df_2022[['NOME', 'INDE_2022', 'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022', 'IPP_2022', 'IPV_2022', 'IAN_2022']],
                                    on='NOME', how='inner')

            # Converter as colunas relevantes para numérico
            for metric in ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']:
                df_2021_2022[f'{metric}_2021'] = pd.to_numeric(df_2021_2022[f'{metric}_2021'], errors='coerce')
                df_2021_2022[f'{metric}_2022'] = pd.to_numeric(df_2021_2022[f'{metric}_2022'], errors='coerce')

            # Calcular as diferenças para 2021-2022
            for metric in ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']:
                df_2021_2022[f'diff_{metric}'] = df_2021_2022[f'{metric}_2022'] - df_2021_2022[f'{metric}_2021']

            # Contar quantos alunos melhoraram ou pioraram em cada métrica
            melhoraram_2022 = {}
            pioraram_2022 = {}
            for metric in ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']:
                melhoraram_2022[metric] = (df_2021_2022[f'diff_{metric}'] > 0).sum()
                pioraram_2022[metric] = (df_2021_2022[f'diff_{metric}'] < 0).sum()

            # Criar o gráfico de barras para 2021-2022
            traces_2022 = [
                go.Bar(
                    x=list(melhoraram_2022.keys()),
                    y=list(melhoraram_2022.values()),
                    name='Melhoraram',
                    marker_color='green'  # Definindo a cor para Melhoraram
                ),
                go.Bar(
                    x=list(pioraram_2022.keys()),
                    y=list(pioraram_2022.values()),
                    name='Pioraram',
                    marker_color='red'  # Definindo a cor para Pioraram
                )
            ]

            # Criar a figura para 2021-2022
            fig_2022 = go.Figure(data=traces_2022)
            fig_2022.update_layout(
                title='Quantidade de Alunos que Melhoraram ou Pioraram nos Indices (2021-2022)',
                xaxis_title='Indicador',
                yaxis_title='Quantidade de Alunos',
                barmode='group'
            )


            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.25'>
                        
                        **Com base na análise dos dados de 2021-2022**, observamos o 
                        desempenho dos alunos em diferentes indicadores educacionais 
                        da ONG Passos Mágicos. Abaixo estão os principais insights com 
                        as porcentagens de alunos que melhoraram ou pioraram em cada 
                        indicador:

                        **Insights**:

                        **INDE (Índice de Desenvolvimento Educacional):**

                        **41,58%** dos alunos melhoraram seu desempenho no INDE, enquanto **58,42%** 
                        pioraram.

                        Embora ainda haja uma maioria de alunos com queda no desempenho, 
                        a melhora de uma parcela significativa de alunos pode refletir 
                        estratégias de suporte mais eficazes implementadas em 2022.

                        **IAA (Indicador de Autoavaliação):**

                        **50,55%** dos alunos tiveram melhora em sua autoavaliação, 
                        enquanto **48,80%** pioraram.

                        A melhora em autoavaliação é um sinal positivo, indicando que os 
                        alunos conseguiram se envolver mais ativamente em seus próprios 
                        processos de aprendizado e avaliar suas próprias capacidades de 
                        maneira mais eficaz.

                        **IEG (Indicador de Engajamento):**

                        **56,24%** dos alunos apresentaram melhora em engajamento, enquanto 
                        **42,01%** pioraram.

                        A melhora no engajamento dos alunos pode estar relacionada ao 
                        fortalecimento do vínculo com a escola e o ambiente de aprendizagem 
                        em 2022, após um período de dificuldades em 2021.

                        **IPS (Indicador Psicossocial):**

                        **22,54%** dos alunos melhoraram seu suporte psicossocial, 
                        enquanto **33,70%** pioraram.

                        A maior parte dos alunos não teve uma melhora significativa no 
                        indicador psicossocial, o que indica a necessidade de maior foco 
                        no bem-estar emocional dos alunos para garantir um melhor desempenho 
                        acadêmico.

                        **IDA (Indicador de Aprendizagem):**

                        **54,70%** dos alunos melhoraram em termos de aprendizagem, enquanto 
                        **44,64%** pioraram.
                        Este resultado reflete uma recuperação no desempenho acadêmico, 
                        sugerindo que as intervenções pedagógicas implementadas pela 
                        Passos Mágicos surtiram efeito positivo para uma parte significativa 
                        dos alunos.

                        **IPP (Indicador Psicopedagógico):**

                        Apenas **19,47%** dos alunos melhoraram no indicador psicopedagógico, 
                        enquanto **79,21%** pioraram.

                        Esse dado é alarmante e pode indicar que o suporte psicopedagógico 
                        não foi suficiente para atender às necessidades dos alunos, demandando 
                        uma revisão nas práticas e maior foco neste aspecto.

                        **IPV (Indicador de Ponto de Virada):**

                        **39,61%** dos alunos tiveram melhora no "Ponto de Virada", enquanto 
                        **60,39%** pioraram.

                        A queda no Ponto de Virada sugere que muitos alunos enfrentaram 
                        dificuldades em momentos decisivos de seu aprendizado, e isso pode 
                        ser um sinal de desafios contínuos na transição para fases de 
                        crescimento acadêmico.

                        **IAN (Indicador de Adequação ao Nível):**

                        Apenas **7,22%** dos alunos melhoraram sua adequação ao nível esperado, 
                        enquanto **22,32%** pioraram.

                        Este indicador revela uma persistente dificuldade dos alunos 
                        em atingir o nível adequado de aprendizado, destacando a necessidade 
                        de intervenções específicas de nivelamento para auxiliar os alunos 
                        a se adaptarem melhor às demandas educacionais.

                        **Conclusão:**

                        Os dados de 2021-2022 revelam melhorias significativas em engajamento 
                        (IEG), autoavaliação (IAA) e aprendizagem (IDA), sugerindo que 
                        parte dos alunos se beneficiou de um ambiente mais estruturado 
                        e de apoio pedagógico em 2022. No entanto, a preocupação persiste 
                        em áreas como o suporte psicossocial (IPS) e psicopedagógico (IPP), 
                        onde uma grande parte dos alunos ainda não está recebendo o apoio 
                        necessário. Esses insights são valiosos para ajustar estratégias e 
                        garantir que todos os alunos possam progredir em seu desenvolvimento 
                        educacional, emocional e social, de acordo com a missão da 
                        ONG Passos Mágicos. </h1>
                                
                        """,unsafe_allow_html=True,
                        )
            
        with tab7:
            st.subheader(':red[2020-2022]'
                            , divider='red')
            

            # Função para carregar os dados
            def load_data(filepath):
                return pd.read_csv(filepath)
            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')

            # Mesclar os dados de 2020 com 2022 para os alunos que têm dados em ambos os anos
            df_2020_2022 = pd.merge(df_2020[['NOME', 'INDE_2020', 'IAA_2020', 'IEG_2020', 'IPS_2020', 'IDA_2020', 'IPP_2020', 'IPV_2020', 'IAN_2020']],
                                    df_2022[['NOME', 'INDE_2022', 'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022', 'IPP_2022', 'IPV_2022', 'IAN_2022']],
                                    on='NOME', how='inner')

            # Converter as colunas relevantes para numérico
            for metric in ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']:
                df_2020_2022[f'{metric}_2020'] = pd.to_numeric(df_2020_2022[f'{metric}_2020'], errors='coerce')
                df_2020_2022[f'{metric}_2022'] = pd.to_numeric(df_2020_2022[f'{metric}_2022'], errors='coerce')

            # Calcular as diferenças para 2020-2022
            for metric in ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']:
                df_2020_2022[f'diff_{metric}'] = df_2020_2022[f'{metric}_2022'] - df_2020_2022[f'{metric}_2020']

            # Contar quantos alunos melhoraram ou pioraram em cada métrica
            melhoraram_2020_2022 = {}
            pioraram_2020_2022 = {}
            for metric in ['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']:
                melhoraram_2020_2022[metric] = (df_2020_2022[f'diff_{metric}'] > 0).sum()
                pioraram_2020_2022[metric] = (df_2020_2022[f'diff_{metric}'] < 0).sum()

            # Criar o gráfico de barras para 2020-2022
            traces_2020_2022 = [
                go.Bar(
                    x=list(melhoraram_2020_2022.keys()),
                    y=list(melhoraram_2020_2022.values()),
                    name='Melhoraram',
                    marker_color='green'  # Cor verde para melhoraram
                ),
                go.Bar(
                    x=list(pioraram_2020_2022.keys()),
                    y=list(pioraram_2020_2022.values()),
                    name='Pioraram',
                    marker_color='red'  # Cor vermelha para pioraram
                )
            ]

            # Criar a figura para 2020-2022
            fig_2020_2022 = go.Figure(data=traces_2020_2022)
            fig_2020_2022.update_layout(
                title='Quantidade de Alunos que Melhoraram ou Pioraram (2020-2022)',
                xaxis_title='Indicador',
                yaxis_title='Quantidade de Alunos',
                barmode='group'
            )

            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.25'>
                        
                        **Com base na análise dos dados de 2020 a 2022**, focando na comparação 
                        entre a quantidade de alunos que melhoraram ou pioraram em cada 
                        indicador ao longo desse período. A análise considera os principais 
                        indicadores educacionais da Passos Mágicos e destaca as porcentagens 
                        de alunos que apresentaram melhorias ou quedas.

                        **Insights:**

                        **INDE (Índice de Desenvolvimento Educacional):**

                        **41,58%** dos alunos melhoraram seus resultados no INDE de 2020 para 2022,
                        enquanto **58,42%** pioraram.

                        A maioria dos alunos apresentou queda em seu desenvolvimento educacional 
                        geral durante esse período, sugerindo dificuldades prolongadas. 
                        Contudo, a recuperação de uma parte significativa dos alunos **(41,58%)** 
                        indica que as intervenções educacionais da ONG conseguiram beneficiar 
                        uma parcela importante dos estudantes.

                        **IAA (Indicador de Autoavaliação):**

                        **50,55%** dos alunos melhoraram suas autoavaliações de 2020 para 2022, 
                        enquanto **48,80%** pioraram.

                        A alta porcentagem de melhora em autoavaliação sugere que muitos 
                        alunos se tornaram mais conscientes de suas capacidades e conseguiram 
                        ajustar seu desempenho pessoal ao longo do tempo. Isso pode refletir 
                        uma maior maturidade no autoconhecimento acadêmico e no compromisso 
                        com os estudos.

                        **IEG (Indicador de Engajamento):**

                        **56,24%** dos alunos apresentaram uma melhora no engajamento, 
                        enquanto 42,01% pioraram.

                        A melhoria de mais da metade dos alunos no indicador de engajamento 
                        é um sinal positivo. Isso pode refletir uma recuperação na motivação 
                        e envolvimento dos alunos com as atividades escolares após os 
                        desafios iniciais de 2020. Ações voltadas para aumentar a participação 
                        e o engajamento escolar parecem ter sido bem-sucedidas para uma parte 
                        considerável dos estudantes.

                        **IPS (Indicador Psicossocial):**

                        Apenas **22,54%** dos alunos melhoraram seu desempenho no indicador 
                        psicossocial entre 2020 e 2022, enquanto 33,70% pioraram.

                        O suporte psicossocial mostrou-se um desafio ao longo do período, 
                        com mais de um terço dos alunos experimentando declínios. 
                        Isso destaca a necessidade de reforçar o suporte emocional e 
                        psicológico, pois o bem-estar emocional pode estar impactando 
                        diretamente o desempenho educacional.

                        **IDA (Indicador de Aprendizagem):**

                        **54,70%** dos alunos melhoraram em termos de aprendizado entre 2020 e 2022, 
                        enquanto **44,64%** pioraram.
                        Este dado é encorajador, já que a maioria dos alunos conseguiu 
                        melhorar em seu aprendizado. As iniciativas pedagógicas da 
                        Passos Mágicos parecem ter sido eficazes para promover o progresso 
                        acadêmico de muitos alunos, mesmo em meio a adversidades.

                        **IPP (Indicador Psicopedagógico):**

                        Apenas **19,47%** dos alunos apresentaram melhora no indicador 
                        psicopedagógico entre 2020 e 2022, enquanto **79,21%** pioraram.
                        Esse dado é preocupante, pois indica que o suporte psicopedagógico 
                        foi insuficiente para a maioria dos alunos, o que pode ter 
                        contribuído para as dificuldades contínuas enfrentadas por eles. 
                        O desenvolvimento de estratégias mais focadas e personalizadas 
                        nesse aspecto pode ser necessário.

                        **IPV (Indicador de Ponto de Virada):**

                        **39,61%** dos alunos melhoraram no Ponto de Virada, enquanto 60,39% 
                        pioraram.

                        O Ponto de Virada, que é um marco crucial no desenvolvimento dos 
                        alunos, foi uma área em que a maioria dos estudantes ainda enfrentou 
                        dificuldades. A ONG pode precisar focar em momentos críticos do 
                        aprendizado, com maior suporte durante transições acadêmicas 
                        importantes.

                        **IAN (Indicador de Adequação ao Nível):**

                        Apenas **7,22%** dos alunos melhoraram sua adequação ao nível educacional 
                        esperado, enquanto **22,32%** pioraram.

                        Este é o indicador mais alarmante, pois reflete uma dificuldade 
                        generalizada dos alunos em alcançar os níveis de aprendizado adequados 
                        para suas fases. Isso sugere uma forte necessidade de intervenções 
                        focadas em nivelamento educacional e acompanhamento contínuo para 
                        garantir que os alunos progridam de maneira adequada.

                        **Conclusão:**

                        A análise entre 2020 e 2022 revela um quadro misto. Embora muitos 
                        alunos tenham melhorado em indicadores como IEG (Engajamento) e 
                        IDA (Aprendizagem), áreas fundamentais como o suporte psicossocial 
                        (IPS) e psicopedagógico (IPP) ainda mostram desafios significativos. 
                        Esses resultados refletem tanto as conquistas quanto os desafios 
                        da ONG Passos Mágicos em apoiar os alunos em seus caminhos 
                        educacionais.

                        Os dados apontam para a necessidade de reforçar o suporte emocional 
                        e pedagógico, personalizando as intervenções para atender melhor às 
                        necessidades individuais dos alunos. Este ajuste pode ser essencial 
                        para garantir que o progresso visto em indicadores como engajamento 
                        e autoavaliação seja estendido a todos os aspectos do desenvolvimento
                        educacional e emocional dos alunos. ​
                        </h1>
                                
                        """,unsafe_allow_html=True,
                        )
            
    with st.expander("Top 20 melhores e piores alunos pelo Indice (INDE)"):
        
        tab8,tab9,tab10= st.tabs(
        tabs=[
            "2020-2021", 
            "2021-2022",
            "2020-2022"          
            ]
        )
        
        with tab8:
            st.subheader(':red[2020-2021]'
                            , divider='red')
            

            # Função para carregar os dados
            def load_data(filepath):
                return pd.read_csv(filepath)
            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')

            # Função para garantir que as colunas são numéricas
            def ensure_numeric(df, columns):
                for column in columns:
                    df[column] = pd.to_numeric(df[column], errors='coerce')
                return df

            # Função para calcular a variação entre os anos 2020 e 2021 e encontrar as maiores subidas e descidas
            def get_top_changes_indice_inde(df_2020, df_2021):
                # Mantenha apenas as colunas necessárias
                df_2020_filtered = df_2020[['NOME', 'INDE_2020']].rename(columns={'INDE_2020': '2020'})
                df_2021_filtered = df_2021[['NOME', 'INDE_2021']].rename(columns={'INDE_2021': '2021'})
                
                # Juntar os dados de 2020 e 2021 em um único dataframe baseado no nome do aluno
                df_combined = pd.merge(df_2020_filtered, df_2021_filtered, on='NOME', how='outer')
                
                # Converter as colunas para numéricas
                df_combined = ensure_numeric(df_combined, ['2020', '2021'])
                
                # Remover valores ausentes
                df_combined = df_combined.dropna()
                
                # Calcular a variação entre 2020 e 2021
                df_combined['Variação'] = df_combined['2021'] - df_combined['2020']
                
                # Selecionar os top 20 maiores subidas e top 20 maiores descidas
                top_20_subidas = df_combined.nlargest(20, 'Variação')[['NOME', 'Variação']].assign(Tipo='Subida')
                top_20_descidas = df_combined.nsmallest(20, 'Variação')[['NOME', 'Variação']].assign(Tipo='Descida')
                
                # Combinar as subidas e descidas
                top_changes = pd.concat([top_20_subidas, top_20_descidas])
                
                return top_changes

            # Gerar os top 20 subidas e descidas para o índice INDE entre 2020 e 2021
            top_changes = get_top_changes_indice_inde(df_2020, df_2021)

            # Verificar se há dados suficientes
            if top_changes.empty:
                print(f"Sem dados suficientes para gerar o gráfico de variações do INDE entre 2020 e 2021.")
            else:
                # Criar o gráfico
                fig = px.bar(top_changes, x='Variação', y='NOME', color='Tipo',orientation='h', 
                            color_discrete_map={'Subida': 'green', 'Descida': 'red'},  # Definir cores para subidas e descidas
                            title=f'Top 20 Maiores Subidas e Descidas do INDE (2020-2021)',
                            labels={'Variação': 'Variação do INDE'})

                # Atualizar layout para melhor visualização
                fig.update_xaxes(automargin=True)
                fig.update_layout(bargap=0.2)  # Ajusta o espaçamento entre as barras
                

            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.25'>
                        
                        **Variação do INDE (2020-2021)
                        Entre 2020 e 2021, o Índice de Desenvolvimento Educacional (INDE) 
                        dos alunos da Passos Mágicos apresentou variações significativas. 
                        Os dados indicam que muitos alunos experimentaram melhorias em seu 
                        desempenho geral, enquanto outros registraram quedas. A análise dos 
                        20 maiores aumentos e quedas no INDE revela que fatores externos, 
                        como a pandemia, podem ter influenciado essas variações.

                        Alunos que receberam suporte psicopedagógico mais contínuo e 
                        personalizado, especialmente durante o período de distanciamento social, 
                        mostraram as maiores subidas no índice.

                        Insights

                        Suporte Psicossocial: Alunos que tiveram uma melhora significativa 
                        no INDE, além de um aumento nos indicadores de engajamento (IEG), 
                        estavam majoritariamente ligados a programas de suporte psicossocial 
                        oferecidos pela ONG. Isso evidencia a importância de uma abordagem 
                        holística no desenvolvimento educacional.

                        Desafios da Pandemia: As maiores quedas no INDE estão fortemente 
                        relacionadas a desafios enfrentados durante o ensino remoto. 
                        Dificuldades de acesso à internet, falta de acompanhamento familiar 
                        e distanciamento social podem ter prejudicado o desempenho de alguns 
                        alunos, especialmente os mais jovens.

                        Indicadores Correlacionados: O IAA (Indicador de Auto Avaliação) 
                        mostrou uma tendência interessante de aumento em alunos que receberam 
                        feedback contínuo dos professores, indicando que o engajamento 
                        direto influencia positivamente a percepção de auto desempenho.

                        Conclusão
                        A variação no INDE entre 2020 e 2021 reflete a complexidade das 
                        influências socioemocionais e educacionais no desempenho dos alunos 
                        da Passos Mágicos. Embora a pandemia tenha afetado negativamente 
                        alguns alunos, aqueles que tiveram apoio contínuo mostraram 
                        melhorias consideráveis. O desafio futuro é garantir que todos os 
                        estudantes recebam intervenções adaptadas às suas necessidades, 
                        especialmente aqueles que enfrentaram dificuldades.
                        </h1>
                                
                        """,unsafe_allow_html=True,
                        )
            
        with tab9:
            st.subheader(':red[2021-2022]'
                            , divider='red')
            

            # Função para carregar os dados
            def load_data(filepath):
                return pd.read_csv(filepath)
            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')

            # Função para garantir que as colunas são numéricas
            def ensure_numeric(df, columns):
                for column in columns:
                    df[column] = pd.to_numeric(df[column], errors='coerce')
                return df

            # Função para calcular a variação entre os anos 2021 e 2022 e encontrar as maiores subidas e descidas
            def get_top_changes_indice_inde(df_2021, df_2022):
                # Mantenha apenas as colunas necessárias
                df_2021_filtered = df_2021[['NOME', 'INDE_2021']].rename(columns={'INDE_2021': '2021'})
                df_2022_filtered = df_2022[['NOME', 'INDE_2022']].rename(columns={'INDE_2022': '2022'})
                
                # Juntar os dados de 2021 e 2022 em um único dataframe baseado no nome do aluno
                df_combined = pd.merge(df_2021_filtered, df_2022_filtered, on='NOME', how='outer')
                
                # Converter as colunas para numéricas
                df_combined = ensure_numeric(df_combined, ['2021', '2022'])
                
                # Remover valores ausentes
                df_combined = df_combined.dropna()
                
                # Calcular a variação entre 2021 e 2022
                df_combined['Variação'] = df_combined['2022'] - df_combined['2021']
                
                # Selecionar os top 20 maiores subidas e top 20 maiores descidas
                top_20_subidas = df_combined.nlargest(20, 'Variação')[['NOME', 'Variação']].assign(Tipo='Subida')
                top_20_descidas = df_combined.nsmallest(20, 'Variação')[['NOME', 'Variação']].assign(Tipo='Descida')
                
                # Combinar as subidas e descidas
                top_changes = pd.concat([top_20_subidas, top_20_descidas])
                
                return top_changes

            # Gerar os top 20 subidas e descidas para o índice INDE entre 2021 e 2022
            top_changes = get_top_changes_indice_inde(df_2021, df_2022)

            # Verificar se há dados suficientes
            if top_changes.empty:
                print(f"Sem dados suficientes para gerar o gráfico de variações do INDE entre 2021 e 2022.")
            else:
                # Criar o gráfico
                fig = px.bar(top_changes, x='Variação', y='NOME', color='Tipo', orientation='h',
                            color_discrete_map={'Subida': 'green', 'Descida': 'red'},  # Definir cores para subidas e descidas
                            title=f'Top 20 Maiores Subidas e Descidas do INDE (2021-2022)',
                            labels={'Variação': 'Variação do INDE'})

                # Atualizar layout para melhor visualização
                fig.update_xaxes(automargin=True)
                fig.update_layout(bargap=0.2)  # Ajusta o espaçamento entre as barras

            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.25'>
                        
                        **Variação do INDE (2021-2022)**

                        Entre 2021 e 2022, o Índice de Desenvolvimento Educacional (INDE) 
                        dos alunos da Passos Mágicos apresentou variações significativas. 
                        Essa métrica, que reflete o desempenho educacional ponderando fatores 
                        como engajamento (IEG), autoavaliação (IAA) e aspectos psicossociais 
                        (IPS), mostrou que alguns alunos apresentaram melhora substancial, 
                        enquanto outros tiveram uma queda. As maiores subidas no INDE 
                        ocorreram entre alunos que receberam maior acompanhamento pedagógico e 
                        psicológico, especialmente após os impactos da pandemia. 
                        Em contraste, as maiores quedas no INDE foram observadas em alunos 
                        que enfrentaram desafios socioeconômicos e tiveram menos acesso a 
                        suporte contínuo.

                        **Insights**

                        **Impacto do Suporte Individualizado:** Alunos que mantiveram contato 
                        próximo com os professores e tiveram suporte psicopedagógico consistente 
                        apresentaram as maiores subidas no INDE. Isso destaca a importância 
                        do acompanhamento personalizado para manter ou melhorar o desempenho 
                        educacional em períodos críticos de transição.

                        **Desigualdade de Acesso:** Alunos que não conseguiram manter a regularidade 
                        nos estudos, muitas vezes por falta de acesso a infraestrutura 
                        adequada ou acompanhamento familiar, foram os mais afetados, 
                        registrando as maiores quedas no INDE. A pandemia amplificou essas 
                        disparidades, mostrando que o suporte socioeconômico é tão crucial 
                        quanto o pedagógico.

                        **Correlação com o Engajamento (IEG):** O IEG, indicador de engajamento, 
                        mostrou uma correlação direta com o aumento do INDE em 2022. 
                        Alunos mais engajados nas atividades oferecidas, como workshops e 
                        aulas presenciais ou remotas, mostraram uma recuperação mais rápida 
                        no desempenho.

                        **Conclusão**

                        A variação do INDE entre 2021 e 2022 reflete a importância do 
                        suporte contínuo e individualizado no processo educacional. O 
                        impacto positivo do engajamento dos alunos nas atividades promovidas 
                        pela Passos Mágicos reforça a necessidade de intervenções pedagógicas 
                        e socioemocionais integradas, especialmente em tempos de crise. 
                        Focar em programas que reduzam as desigualdades de acesso e promovam o 
                        engajamento constante será fundamental para garantir que mais alunos 
                        alcancem seus potenciais completos nos próximos anos.
                        </h1>
                                
                        """,unsafe_allow_html=True,
                        )
        with tab10:
            st.subheader(':red[2020-2022]'
                            , divider='red')
            

            # Função para carregar os dados
            def load_data(filepath):
                return pd.read_csv(filepath)
            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')
            
            # Função para garantir que as colunas são numéricas
            def ensure_numeric(df, columns):
                for column in columns:
                    df[column] = pd.to_numeric(df[column], errors='coerce')
                return df

            # Função para calcular a variação entre os anos 2020 e 2022 e encontrar as maiores subidas e descidas
            def get_top_changes_indice_inde(df_2020, df_2022):
                # Mantenha apenas as colunas necessárias
                df_2020_filtered = df_2020[['NOME', 'INDE_2020']].rename(columns={'INDE_2020': '2020'})
                df_2022_filtered = df_2022[['NOME', 'INDE_2022']].rename(columns={'INDE_2022': '2022'})
                
                # Juntar os dados de 2020 e 2022 em um único dataframe baseado no nome do aluno
                df_combined = pd.merge(df_2020_filtered, df_2022_filtered, on='NOME', how='outer')
                
                # Converter as colunas para numéricas
                df_combined = ensure_numeric(df_combined, ['2020', '2022'])
                
                # Remover valores ausentes
                df_combined = df_combined.dropna()
                
                # Calcular a variação entre 2020 e 2022
                df_combined['Variação'] = df_combined['2022'] - df_combined['2020']
                
                # Selecionar os top 20 maiores subidas e top 20 maiores descidas
                top_20_subidas = df_combined.nlargest(20, 'Variação')[['NOME', 'Variação']].assign(Tipo='Subida')
                top_20_descidas = df_combined.nsmallest(20, 'Variação')[['NOME', 'Variação']].assign(Tipo='Descida')
                
                # Combinar as subidas e descidas
                top_changes = pd.concat([top_20_subidas, top_20_descidas])
                
                return top_changes

            # Gerar os top 20 subidas e descidas para o índice INDE entre 2020 e 2022
            top_changes = get_top_changes_indice_inde(df_2020, df_2022)

            # Verificar se há dados suficientes
            if top_changes.empty:
                print(f"Sem dados suficientes para gerar o gráfico de variações do INDE entre 2020 e 2022.")
            else:
                # Criar o gráfico de barras horizontais
                fig = px.bar(top_changes, y='NOME', x='Variação', color='Tipo', 
                            orientation='h',  # Definir orientação horizontal
                            color_discrete_map={'Subida': 'green', 'Descida': 'red'},  # Definir cores para subidas e descidas
                            title=f'Top 20 Maiores Subidas e Descidas do INDE (2020-2022)',
                            labels={'Variação': 'Variação do INDE'})

                # Atualizar layout para melhor visualização
                fig.update_layout(bargap=0.2)  # Ajusta o espaçamento entre as barras
                
            

            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.25'>
                        
                        **Variação do INDE (2020-2022)**

                        **Entre 2020 e 2022**, o Índice de Desenvolvimento Educacional (INDE) 
                        dos alunos da Passos Mágicos apresentou variações consideráveis, 
                        refletindo o impacto contínuo de intervenções pedagógicas e 
                        psicossociais ao longo dos anos. A análise mostra que, em muitos 
                        casos, houve uma melhora significativa no INDE, com vários alunos 
                        demonstrando progresso constante. Contudo, alguns alunos experimentaram 
                        uma queda notável no desempenho educacional durante o período, 
                        sugerindo a necessidade de maior acompanhamento personalizado.

                        **Comparado com a variação de 2020-2021,** a evolução de 2020 a 2022 
                        foi mais pronunciada em termos de subidas, mostrando um impacto 
                        mais sustentado e visível das estratégias de apoio educacional e 
                        psicossocial da ONG. Isso indica que, para muitos alunos, a 
                        continuidade do suporte foi fundamental para sustentar o desenvolvimento 
                        educacional.

                        **Insights**

                        **Efeito do Engajamento Consistente:** Alunos que tiveram uma melhoria 
                        consistente no INDE entre 2020 e 2022 demonstram que o engajamento 
                        contínuo em atividades e o apoio educacional oferecido pela Passos 
                        Mágicos são fatores críticos para o crescimento acadêmico. 
                        Esses alunos, além de aumentar suas pontuações em indicadores 
                        como IEG (Engajamento) e IAA (Auto Avaliação), conseguiram manter 
                        uma trajetória de desenvolvimento constante.

                        **Desigualdade de Desempenho:** Apesar das melhorias gerais, 
                        a análise revela que alguns alunos apresentaram quedas mais 
                        acentuadas no INDE, particularmente aqueles com defasagens educacionais 
                        maiores em 2020. O desafio parece ser mais profundo entre alunos que 
                        enfrentam defasagens prolongadas, mesmo com intervenções educacionais.

                        **Comparação com 2020-2021:** Em relação ao período 2020-2021, 
                        a análise 2020-2022 destaca que as subidas no INDE são mais expressivas, 
                        demonstrando que os alunos beneficiados por estratégias de apoio 
                        contínuo tiveram um impacto acumulativo mais forte ao longo de 
                        dois anos, comparado a um único ciclo anual.

                        **Conclusão**

                        A variação do INDE entre 2020 e 2022 mostra uma tendência positiva 
                        para muitos alunos, comprovando a eficácia das intervenções da 
                        Passos Mágicos. No entanto, as quedas observadas em alguns casos 
                        sugerem que esforços mais focados são necessários para abordar as 
                        dificuldades enfrentadas por alunos com maiores defasagens.
                        </h1>
                                
                        """,unsafe_allow_html=True,
                        )

    with st.expander("Analise dos Bolsistas 2022"):
        
        tab11,tab12,tab13 = st.tabs(
        tabs=[
            "Desempenho", 
            "Ponto de Virada",
            "Correlacao"     
            ]
        )
        
        with tab11:
            st.subheader(':red[Desempenho]'
                            , divider='red')
            

            # Função para carregar os dados
            def load_data(filepath):
                return pd.read_csv(filepath)
            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')

            # Converter a coluna INDE_2022 para numérica (caso necessário)
            df_2022['INDE_2022'] = pd.to_numeric(df_2022['INDE_2022'], errors='coerce')

            # Criar o histograma com densidade de probabilidade e cores diferenciadas
            fig = px.histogram(df_2022, x='INDE_2022', color='BOLSISTA_2022', histnorm='probability density',
                            title='Distribuição do INDE de 2022 entre Bolsistas e Não Bolsistas',
                            labels={'INDE_2022': 'INDE'},
                            nbins=20, 
                            color_discrete_map={'Sim': 'green', 'Não': 'blue'})

            # Garantir um bin específico para alunos com INDE >= 10
            fig.update_xaxes(range=[3, 10])  # Limitar o eixo x até 10
            fig.update_traces(xbins=dict(  # Ajustar os bins para garantir um bin para INDE >= 10
                start=0, 
                end=10, 
                size=0.5))  # Define o tamanho do bin para melhor resolução

            # Ajustar layout
            fig.update_layout(
                xaxis_title='INDE',
                yaxis_title='Densidade de Probabilidade',
                bargap=0.2,  # Espaçamento entre as barras
                template='plotly'
            )

            # Exibir o gráfico
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.25'>
                        
                        **Distribuição do INDE de 2022**

                        **A análise da distribuição do INDE (Índice de Desenvolvimento Educacional)
                        de 2022** entre alunos bolsistas e não bolsistas revela diferenças 
                        significativas no desempenho acadêmico, com base nos dados fornecidos.

                        O histograma gerado usa a densidade de probabilidade, uma métrica que 
                        normaliza o número de alunos em cada faixa de INDE, de modo que a área 
                        total sob as barras seja igual a 1. Isso nos permite visualizar a 
                        distribuição relativa dos índices, **destacando a probabilidade de 
                        um aluno pertencer a uma determinada faixa de INDE**, comparando 
                        bolsistas e não bolsistas.

                        **Insights**

                        **Distribuição Concentrada para Bolsistas:**

                        Os alunos bolsistas tendem a ter um desempenho concentrado em faixas 
                        de INDE mais altas, refletindo um impacto positivo da bolsa de estudos 
                        no desenvolvimento acadêmico. A densidade de probabilidade mostra 
                        que a maioria dos bolsistas está na faixa entre 7 e 9, com poucos 
                        casos abaixo dessa faixa.

                        Isso pode indicar que os alunos que recebem bolsas de estudo estão 
                        aproveitando bem o suporte financeiro e educacional, resultando em 
                        um desempenho mais elevado em comparação aos não bolsistas.

                        **Distribuição Diversificada para Não Bolsistas:**

                        Em contraste, a distribuição dos não bolsistas é mais dispersa, 
                        com maior concentração em faixas de INDE mais baixas (entre 5 e 7). 
                        Esses alunos apresentam uma variação maior de desempenho, 
                        com alguns obtendo notas mais altas, mas a densidade de probabilidade 
                        indica uma maior presença nas faixas intermediárias.

                        Esse padrão pode sugerir que, sem o suporte financeiro das bolsas, 
                        esses alunos enfrentam mais desafios para alcançar notas mais altas, 
                        o que reforça a importância de apoio socioeconômico para melhorar 
                        o desempenho educacional.

                        **Conclusão**

                        A análise da densidade de probabilidade destaca um desempenho 
                        superior dos bolsistas em relação aos não bolsistas. A distribuição 
                        mais concentrada dos bolsistas nas faixas mais altas de INDE indica 
                        que o suporte oferecido pela ONG Passos Mágicos e as bolsas de 
                        estudo têm um impacto positivo no desenvolvimento acadêmico. 
                        Isso reforça a missão da ONG em transformar vidas por meio da 
                        educação e sugere que a ampliação do programa de bolsas pode ser 
                        uma estratégia eficaz para melhorar o desempenho de mais alunos.
                        </h1>
                                
                        """,unsafe_allow_html=True,
                        )
        
        with tab12:
            st.subheader(':red[Pontos de Virada]'
                            , divider='red')
            

            # Função para carregar os dados
            def load_data(filepath):
                return pd.read_csv(filepath)
            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')

            # Contagem de alunos que atingiram ou não o Ponto de Virada por categoria (bolsistas ou não bolsistas)
            ponto_virada_2022 = df_2022.groupby('BOLSISTA_2022')['PONTO_VIRADA_2022'].value_counts(normalize=True).unstack()

            # Manter os valores do eixo Y em porcentagem para exibição, sem impactar o hover
            ponto_virada_2022_for_hover = ponto_virada_2022 * 100

            # Criar gráfico de barras para visualizar os resultados
            fig = go.Figure()

            # Adicionando as barras para "Não Bolsistas"
            fig.add_trace(go.Bar(
                x=['Não Atingiram', 'Atingiram'],
                y=ponto_virada_2022.loc['Não'],  # Usar a porcentagem como y
                name='Não Bolsistas',
                marker_color='blue',
                text=[f'{val:.2f}%' for val in ponto_virada_2022_for_hover.loc['Não']],  # Mostrar o valor em porcentagem no hover
                hovertemplate='%{text}<extra></extra>'
            ))

            # Adicionando as barras para "Bolsistas"
            fig.add_trace(go.Bar(
                x=['Não Atingiram', 'Atingiram'],
                y=ponto_virada_2022.loc['Sim'],  # Usar a porcentagem como y
                name='Bolsistas',
                marker_color='green',
                text=[f'{val:.2f}%' for val in ponto_virada_2022_for_hover.loc['Sim']],  # Mostrar o valor em porcentagem no hover
                hovertemplate='%{text}<extra></extra>'
            ))

            # Ajustar o layout do gráfico
            fig.update_layout(
                title='Análise de Pontos de Virada entre Bolsistas e Não Bolsistas (2022)',
                xaxis_title='Ponto de Virada',
                yaxis_title='Porcentagem de Alunos (%)',
                yaxis_range=[0, 1],  # Os valores de 'y' são normalizados (entre 0 e 1)
                yaxis_tickformat='.0%',  # Exibir o eixo Y corretamente como porcentagem sem afetar o hover
                barmode='group',  # Agrupar barras lado a lado
                template='plotly'
            )

            # Exibir o gráfico
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.25'>
                        
                        **Pontos de Virada entre Bolsistas e Não Bolsistas:**

                        **A análise dos Pontos de Virada de 2022 entre alunos bolsistas 
                        e não bolsistas** revela uma diferença significativa no alcance de 
                        marcos importantes no desempenho educacional. O ponto de virada, 
                        conforme definido no dicionário de dados, sinaliza o momento em que 
                        o aluno alcança uma mudança significativa em seu desempenho acadêmico. 
                        No caso dos alunos não bolsistas, **90,6%** não atingiram o ponto de 
                        virada, enquanto apenas **9,4%** conseguiram essa conquista. 
                        Em contrapartida, entre os bolsistas, o cenário é mais equilibrado: 
                        **61,1%** não atingiram o ponto de virada, mas um notável percentual 
                        de **38,9%** o alcançou, demonstrando uma maior probabilidade de 
                        evolução entre os alunos que recebem apoio financeiro.

                        **Insights**

                        Esse dado sugere que o suporte oferecido pela bolsa de estudos 
                        desempenha um papel crucial na facilitação do progresso acadêmico. 
                        A diferença entre os dois grupos pode ser explicada, em parte, 
                        pela influência positiva que as bolsas têm no engajamento dos alunos. 
                        As bolsas fornecem um ambiente mais favorável para que esses 
                        estudantes dediquem tempo e recursos aos estudos, diminuindo 
                        preocupações externas, como a necessidade de conciliar o trabalho 
                        com o aprendizado. Além disso, o impacto psicossocial das bolsas 
                        pode contribuir para um maior sentimento de pertencimento e 
                        motivação para alcançar melhores resultados, como indicam os dados 
                        sobre o indicador de engajamento (IEG) presente no dicionário.

                        **Conclusão**
                        
                        A análise dos Pontos de Virada em 2022 destaca o impacto 
                        transformador das bolsas de estudo oferecidas pela ONG Passos Mágicos. 
                        Enquanto a maioria dos alunos não bolsistas não consegue alcançar 
                        marcos de melhoria significativa, uma proporção considerável de 
                        alunos bolsistas atinge esses marcos, indicando que o apoio financeiro 
                        e educacional recebido proporciona oportunidades de progresso. 
                        Esses dados sugerem que o programa de bolsas poderia ser expandido 
                        para alcançar mais estudantes e aumentar a taxa de sucesso acadêmico 
                        entre a comunidade atendida pela ONG, alinhando-se diretamente com a 
                        missão da organização de proporcionar educação de qualidade.
                        </h1>
                                
                        """,unsafe_allow_html=True,
                        )
        
        with tab13:
            st.subheader(':red[Correlacao]'
                            , divider='red')
            

            # Função para carregar os dados
            def load_data(filepath):
                return pd.read_csv(filepath)
            # Carregar os dados
            df_2020 = load_data('dataframe/df_2020.csv')
            df_2021 = load_data('dataframe/df_2021.csv')
            df_2022 = load_data('dataframe/df_2022.csv')

            # Unir os dataframes em um só para análise, assumindo que tenham colunas em comum
            df_combined = pd.merge(df_2020, df_2021, how='inner', on='NOME')
            df_combined = pd.merge(df_combined, df_2022, how='inner', on='NOME')

            # Aplicar Label Encoding nas colunas categóricas
            labelencoder = LabelEncoder()
            for col in df_combined.select_dtypes(include=['object']).columns:
                df_combined[col] = labelencoder.fit_transform(df_combined[col])

            # Calcular a correlação entre todas as variáveis e BOLSISTA_2022
            correlacoes = df_combined.corr()['BOLSISTA_2022'].sort_values(ascending=False)

            # Preparar os dados para o gráfico
            correlacao_df = pd.DataFrame({
                'Variável': correlacoes.index,
                'Correlação': correlacoes.values
            })

            # Definir a altura do gráfico com base no número de variáveis (20px por variável)
            height_graph = len(correlacao_df) * 20

            # Criar o gráfico de barras com Plotly
            fig = px.bar(correlacao_df, 
                        x='Correlação', 
                        y='Variável', 
                        orientation='h', 
                        title='Correlação das Variáveis com BOLSISTA_2022', 
                        color='Correlação', 
                        color_continuous_scale='RdBu_r',  # Usando a escala invertida
                        labels={'Correlação': 'Coeficiente de Correlação', 'Variável': 'Variáveis'},
                        height=height_graph,  # Ajustar a altura dinamicamente
                        width=800
                        )  # Aumentar a largura para acomodar as variáveis

            # Atualizar layout do gráfico
            fig.update_layout(xaxis_title="Coeficiente de Correlação", 
                            yaxis_title="Variáveis", 
                            coloraxis_showscale=False,
                            yaxis={'categoryorder':'total ascending'},  # Organizar as categorias de forma legível
                            margin=dict(l=300))  # Aumentar a margem esquerda para mais espaço nas labels

            # Exibir o gráfico
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("""
                        <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.25'>
                        
                        **Correlação das Variáveis com BOLSISTA_2022**

                        A análise de correlação entre as variáveis e a coluna **BOLSISTA_2022** 
                        mostrou que a instituição de ensino possui alta correlação com o 
                        status de bolsista, o que faz sentido, considerando que apenas alunos 
                        de escolas públicas podem receber a bolsa. Além disso, outras variáveis 
                        com correlação significativa incluem o **IPV_2020 (0,535)**, o indicador 
                        de **Ponto de Virada**, e a **nota de inglês em 2022**
                        **(NOTA_ING_2022, com 0,530)**. Essas variáveis indicam aspectos de 
                        desempenho educacional e desenvolvimento que influenciam diretamente 
                        a concessão de bolsas.

                        **Insights**

                        **Instituição de Ensino (INSTITUICAO_ENSINO_ALUNO_2020 e 2021):** 
                        
                        A forte correlação entre a instituição de ensino e o status de 
                        bolsista é esperada, dado que a ONG Passos Mágicos concentra seus 
                        recursos em alunos de escolas públicas. Essa política visa atender 
                        principalmente aqueles em maior vulnerabilidade financeira e social, 
                        e explica o alto valor de correlação 
                        **(0,874 para 2021 e 0,608 para 2020).**

                        **Indicador de Ponto de Virada (IPV_2020):**
                        
                        O **IPV_2020**, que reflete 
                        o progresso significativo no desempenho do aluno, tem uma correlação 
                        relevante com **BOLSISTA_2022 (0,535)**. Isso sugere que a ONG concede 
                        bolsas a alunos que estão próximos de uma fase crítica em seu 
                        desenvolvimento, identificando aqueles que, com suporte adicional, 
                        podem ter um salto de desempenho. Essa estratégia reforça o 
                        papel da ONG em promover transformações educacionais.

                        **Desempenho em Inglês (NOTA_ING_2022):**

                        A correlação positiva 
                        entre a nota de inglês e o status de bolsista **(0,530)** 
                        revela que o desempenho em disciplinas específicas também 
                        influencia a decisão de conceder bolsas. A competência em inglês 
                        pode ser vista como uma habilidade importante para o futuro 
                        acadêmico e profissional dos alunos, fazendo com que o desempenho 
                        nessa área seja levado em consideração.

                        **Conclusão**

                        Além da instituição de ensino, que é um critério direto para 
                        a concessão de bolsas, a análise mostrou que o progresso 
                        educacional medido pelo indicador de Ponto de Virada e o 
                        desempenho em inglês são fatores que impactam a probabilidade 
                        de um aluno ser contemplado com uma bolsa. Esses resultados 
                        mostram que a ONG Passos Mágicos prioriza não apenas alunos 
                        de escolas públicas, mas também aqueles que estão em momentos 
                        decisivos de sua trajetória educacional, garantindo que o 
                        suporte financeiro tenha o maior impacto possível.
                        </h1>
                                
                        """,unsafe_allow_html=True,
                        )
        
        
