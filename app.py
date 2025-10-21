
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Farmacia Lorca IA — Demo", layout="wide")

st.title("💊 Farmacia Lorca IA — Demo (Streamlit)")
st.caption("Simulador con datos de ejemplo (sin conexión a Farmatic). By @FarmaciaLorcaIA")

DATA_DIR = Path("data")

@st.cache_data
def load_csv(name):
    return pd.read_csv(DATA_DIR / name)

tabs = st.tabs(["📊 Dashboard", "🔮 Predicciones", "📦 Productos", "🚨 Faltas", "ℹ️ Info"])

with tabs[0]:
    st.subheader("Resumen general")
    productos = load_csv("productos.csv")
    faltas = load_csv("faltas.csv")
    preds = load_csv("predicciones.csv")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Productos", len(productos))
    col2.metric("Faltas (30d)", len(faltas))
    col3.metric("Riesgo CRÍTICO", (preds["riesgo"] == "CRITICO").sum())
    col4.metric("Ticket medio (demo)", "13,80€")

    st.markdown("### Rotación y stock")
    st.dataframe(productos.sort_values("rotacion_30d", ascending=False), use_container_width=True)

with tabs[1]:
    st.subheader("Riesgo y recomendaciones")
    preds = load_csv("predicciones.csv")
    filtro = st.multiselect("Filtra por nivel de riesgo", options=preds["riesgo"].unique().tolist(), default=None)
    df = preds if not filtro else preds[preds["riesgo"].isin(filtro)]
    st.dataframe(df.sort_values(["riesgo", "prob"], ascending=[True, False]), use_container_width=True)

    st.markdown("#### Top recomendaciones")
    for _, row in df.sort_values("prob", ascending=False).head(5).iterrows():
        st.write(f"• **CN {row['cn']}** → {row['recomendacion']} (riesgo {row['riesgo']}, prob={row['prob']:.2f})")

with tabs[2]:
    st.subheader("Catálogo de productos (demo)")
    productos = load_csv("productos.csv")
    buscar = st.text_input("Buscar por nombre o CN")
    if buscar:
        productos = productos[productos["nombre"].str.contains(buscar, case=False) | productos["cn"].astype(str).str.contains(buscar)]
    st.dataframe(productos, use_container_width=True)

with tabs[3]:
    st.subheader("Histórico de faltas (demo)")
    faltas = load_csv("faltas.csv")
    st.dataframe(faltas.sort_values("fecha", ascending=False), use_container_width=True)

with tabs[4]:
    st.subheader("Acerca de esta demo")
    st.markdown('''
**Qué es:** Una demostración de *Farmacia Lorca IA* funcionando en modo **simulado**,
con datos de muestra. No accede a servidores reales ni a Farmatic.

**Tecnologías:** Streamlit, CSV locales (mock), despliegue en Hugging Face Spaces.

**Cómo conectar con tu backend real:** En el proyecto principal dispones de un frontend y un backend (FastAPI)
orquestados con Docker. Esta demo permite enseñar un prototipo sin exponer datos sensibles.
    ''')
