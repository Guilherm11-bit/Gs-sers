
import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(
    page_title="Neighborhood Action Dashboard",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Neighborhood Action Dashboard")
st.subheader("Monitoramento de Energia Sustentável")
st.write(
    "Sistema de análise energética para iluminação "
    "sustentável de praças comunitárias."
)



consumo_convencional = 288.0
consumo_led = 115.2
consumo_solar = 54.72

tarifa = 0.43416
fator_co2 = 0.0461  # tCO2/MWh

custo_convencional = consumo_convencional * tarifa
custo_led = consumo_led * tarifa
custo_solar = 0.0

economia_led = (
    (consumo_convencional - consumo_led)
    / consumo_convencional
) * 100

economia_solar = (
    (consumo_convencional - consumo_solar)
    / consumo_convencional
) * 100

co2_ev_itado = (
    consumo_convencional * 12 / 1000
) * fator_co2 * 1000



pagina = st.sidebar.selectbox(
    "Selecione uma seção",
    [
        "Visão Geral",
        "Consumo Energético",
        "Comparação",
        "Sustentabilidade"
    ]
)

# ==========================================
# VISÃO GERAL
# ==========================================

if pagina == "Visão Geral":

    st.header("Indicadores principais")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Consumo convencional",
        f"{consumo_convencional:.2f} kWh/mês"
    )

    col2.metric(
        "Consumo equivalente solar",
        f"{consumo_solar:.2f} kWh/mês"
    )

    col3.metric(
        "Economia energética",
        f"{economia_solar:.1f}%"
    )

    st.divider()

    st.subheader("Características do projeto")

    st.write("""
    - 8 luminárias LED.
    - Potência individual de 40 W.
    - Alimentação por painéis solares.
    - Armazenamento em baterias.
    - Sensores de presença.
    - Monitoramento digital.
    """)

    st.info(
        "Os valores apresentados são estimativas "
        "acadêmicas e não medições reais."
    )

# ==========================================
# CONSUMO ENERGÉTICO
# ==========================================

elif pagina == "Consumo Energético":

    st.header("Análise do consumo")

    dados = pd.DataFrame({
        "Sistema": [
            "Convencional",
            "LED conectado à rede",
            "LED solar com sensores"
        ],
        "Consumo (kWh/mês)": [
            consumo_convencional,
            consumo_led,
            consumo_solar
        ]
    })

    grafico = px.bar(
        dados,
        x="Sistema",
        y="Consumo (kWh/mês)",
        title="Comparação do consumo energético mensal",
        text_auto=".2f"
    )

    st.plotly_chart(grafico, use_container_width=True)

    st.dataframe(
        dados,
        use_container_width=True,
        hide_index=True
    )

# ==========================================
# COMPARAÇÃO
# ==========================================

elif pagina == "Comparação":

    st.header("Comparação das alternativas")

    dados = pd.DataFrame({
        "Alternativa": [
            "Convencional",
            "LED conectado à rede",
            "LED solar com sensores"
        ],
        "Energia equivalente (kWh/mês)": [
            consumo_convencional,
            consumo_led,
            consumo_solar
        ],
        "Custo da energia (R$/mês)": [
            custo_convencional,
            custo_led,
            custo_solar
        ]
    })

    col1, col2 = st.columns(2)

    with col1:
        grafico = px.bar(
            dados,
            x="Alternativa",
            y="Energia equivalente (kWh/mês)",
            title="Demanda energética"
        )
        st.plotly_chart(
            grafico,
            use_container_width=True
        )

    with col2:
        grafico = px.bar(
            dados,
            x="Alternativa",
            y="Custo da energia (R$/mês)",
            title="Custo mensal estimado"
        )
        st.plotly_chart(
            grafico,
            use_container_width=True
        )

    st.dataframe(
        dados,
        use_container_width=True,
        hide_index=True
    )

# ==========================================
# SUSTENTABILIDADE
# ==========================================

elif pagina == "Sustentabilidade":

    st.header("Indicadores ambientais")

    col1, col2 = st.columns(2)

    col1.metric(
        "Energia renovável local",
        "100%"
    )

    col2.metric(
        "CO2 evitado estimado",
        f"{co2_ev_itado:.2f} kg/ano"
    )

    st.subheader("Economia energética")

    st.write(
        f"Alternativa LED: {economia_led:.1f}%"
    )

    st.write(
        f"Alternativa solar: {economia_solar:.1f}%"
    )

    st.subheader("Impacto ambiental")

    st.write("""
    A utilização de energia solar reduz a necessidade
    de eletricidade proveniente da rede.

    A estimativa de emissões evitadas utiliza o fator
    médio de emissão do Sistema Interligado Nacional.
    """)

    st.caption(
        "Dados simulados para fins acadêmicos. "
        "Os resultados reais dependem da implantação."
    )

# ==========================================
# RODAPÉ
# ==========================================

st.divider()

st.caption(
    "Global Solution 2026.2 | FIAP | SERS | CitizenTech"
)
