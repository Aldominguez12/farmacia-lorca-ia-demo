import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Lorca Pilot — Farmacia IA", page_icon="💊", layout="wide")

DATA_DIR = Path(__file__).parent / "data"

RISK_ORDER = ["CRITICO", "ALTO", "MEDIO", "BAJO"]
RISK_COLORS = {
    "CRITICO": "#dc2626",
    "ALTO": "#ea580c",
    "MEDIO": "#ca8a04",
    "BAJO": "#16a34a",
}

SECTIONS = ["📋 Resumen", "🔮 Predicciones", "📦 Inventario", "🚨 Faltas", "🤖 Asistente IA"]


@st.cache_data
def load_csv(name, date_cols=None):
    df = pd.read_csv(DATA_DIR / name)
    if date_cols:
        for col in date_cols:
            df[col] = pd.to_datetime(df[col])
    return df


@st.cache_data
def load_data():
    productos = load_csv("productos.csv")
    predicciones = load_csv("predicciones.csv")
    faltas = load_csv("faltas.csv", date_cols=["fecha"])
    return productos, predicciones, faltas


def risk_badge(riesgo):
    color = RISK_COLORS.get(riesgo, "#64748b")
    return f'<span class="risk-badge" style="background:{color}20;color:{color};border:1px solid {color}66">{riesgo}</span>'


st.markdown(
    """
    <style>
    :root {
        --lorca-primary: #4f46e5;
        --lorca-primary-dark: #3730a3;
        --lorca-bg-card: #f8fafc;
    }
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--lorca-primary) 0%, var(--lorca-primary-dark) 100%);
    }
    section[data-testid="stSidebar"] * {
        color: #eef2ff !important;
    }
    section[data-testid="stSidebar"] .stRadio > label {
        display: none;
    }
    div[data-testid="stMetric"] {
        background: var(--lorca-bg-card);
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 14px 16px;
    }
    .lorca-card {
        background: var(--lorca-bg-card);
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px 18px;
        margin-bottom: 10px;
    }
    .risk-badge {
        padding: 2px 10px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 600;
    }
    .lorca-banner {
        background: #fef9c3;
        border: 1px solid #eab308;
        color: #713f12;
        border-radius: 10px;
        padding: 10px 16px;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    @media (max-width: 640px) {
        div[data-testid="stMetric"] { padding: 10px 12px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

productos, predicciones, faltas = load_data()
datos = predicciones.merge(productos, on="cn", how="left")

with st.sidebar:
    st.markdown("## 💊 Lorca Pilot")
    st.caption("Copiloto IA para farmacia")
    seccion = st.radio("Navegación", SECTIONS, label_visibility="collapsed")
    st.markdown("---")
    st.caption("Farmacia Lorca IA · Demo")

st.markdown(
    '<div class="lorca-banner">⚠️ Entorno simulado: los datos son de ejemplo y no existe conexión con Farmatic ni con ningún sistema real.</div>',
    unsafe_allow_html=True,
)


def alertas_prioritarias(datos, top_n=5):
    orden = {r: i for i, r in enumerate(RISK_ORDER)}
    df = datos.copy()
    df["_orden_riesgo"] = df["riesgo"].map(orden)
    return df.sort_values(["_orden_riesgo", "prob"], ascending=[True, False]).head(top_n)


if seccion == "📋 Resumen":
    st.title("Centro de control")

    top = alertas_prioritarias(datos, top_n=1)
    if not top.empty:
        principal = top.iloc[0]
        st.info(
            f"**Recomendación del día:** {principal['recomendacion']} para "
            f"**{principal['nombre']}** (CN {principal['cn']}) — riesgo {principal['riesgo']}, "
            f"probabilidad {principal['prob']:.0%}."
        )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Productos en catálogo", len(productos))
    col2.metric("Faltas registradas (30d)", len(faltas))
    col3.metric("Riesgo CRÍTICO", int((predicciones["riesgo"] == "CRITICO").sum()))
    valor_stock = (productos["stock"] * productos["pvp"]).sum()
    col4.metric("Valor stock (PVP)", f"{valor_stock:,.2f} €")

    st.markdown("### Rotación de productos (30 días)")
    st.bar_chart(productos.set_index("nombre")["rotacion_30d"])

    st.markdown("### Prioridades por riesgo")
    prioritarios = alertas_prioritarias(datos, top_n=5)
    for _, row in prioritarios.iterrows():
        st.markdown(
            f'<div class="lorca-card">{risk_badge(row["riesgo"])} &nbsp; '
            f'<b>{row["nombre"]}</b> (CN {row["cn"]}) — stock {int(row["stock"])}, '
            f'demanda 7d {int(row["demanda_7d"])}, prob {row["prob"]:.0%}<br>'
            f'<span style="color:#475569">→ {row["recomendacion"]}</span></div>',
            unsafe_allow_html=True,
        )

elif seccion == "🔮 Predicciones":
    st.title("Predicciones de demanda")

    niveles = st.multiselect(
        "Filtrar por nivel de riesgo",
        options=RISK_ORDER,
        default=RISK_ORDER,
    )
    vista = datos[datos["riesgo"].isin(niveles)] if niveles else datos

    col1, col2, col3 = st.columns(3)
    col1.metric("Productos filtrados", len(vista))
    col2.metric("Riesgo CRÍTICO", int((vista["riesgo"] == "CRITICO").sum()))
    col3.metric("Confianza media", f"{vista['prob'].mean():.0%}" if len(vista) else "—")

    orden = {r: i for i, r in enumerate(RISK_ORDER)}
    vista = vista.assign(_orden=vista["riesgo"].map(orden)).sort_values(
        ["_orden", "prob"], ascending=[True, False]
    )
    tabla = vista[["cn", "nombre", "stock", "demanda_7d", "riesgo", "prob", "recomendacion"]].assign(
        prob=lambda d: (d["prob"] * 100).round(0)
    ).rename(
        columns={
            "cn": "CN",
            "nombre": "Producto",
            "stock": "Stock",
            "demanda_7d": "Demanda 7d",
            "riesgo": "Riesgo",
            "prob": "Confianza",
            "recomendacion": "Recomendación",
        }
    )
    st.dataframe(
        tabla,
        use_container_width=True,
        column_config={"Confianza": st.column_config.ProgressColumn("Confianza", min_value=0, max_value=100, format="%.0f%%")},
        hide_index=True,
    )

elif seccion == "📦 Inventario":
    st.title("Inventario")

    buscar = st.text_input("Buscar por nombre o CN")
    vista = productos
    if buscar:
        vista = vista[
            vista["nombre"].str.contains(buscar, case=False)
            | vista["cn"].astype(str).str.contains(buscar)
        ]

    col1, col2, col3 = st.columns(3)
    col1.metric("Unidades en stock", int(vista["stock"].sum()))
    col2.metric("Referencias", len(vista))
    col3.metric("Valoración (PVP)", f"{(vista['stock'] * vista['pvp']).sum():,.2f} €")

    st.dataframe(
        vista.rename(
            columns={"cn": "CN", "nombre": "Producto", "stock": "Stock", "rotacion_30d": "Rotación 30d", "pvp": "PVP (€)"}
        ),
        use_container_width=True,
        hide_index=True,
    )

elif seccion == "🚨 Faltas":
    st.title("Histórico de faltas")

    enriquecido = faltas.merge(productos[["cn", "nombre"]], on="cn", how="left").sort_values(
        "fecha", ascending=False
    )

    col1, col2 = st.columns(2)
    col1.metric("Incidencias registradas", len(enriquecido))
    col2.metric("Reintentos totales", int(enriquecido["pedidos_reintentos"].sum()))

    st.dataframe(
        enriquecido[["fecha", "cn", "nombre", "motivo", "pedidos_reintentos"]]
        .assign(fecha=lambda d: d["fecha"].dt.strftime("%Y-%m-%d"))
        .rename(
            columns={
                "fecha": "Fecha",
                "cn": "CN",
                "nombre": "Producto",
                "motivo": "Motivo",
                "pedidos_reintentos": "Reintentos",
            }
        ),
        use_container_width=True,
        hide_index=True,
    )

elif seccion == "🤖 Asistente IA":
    st.title("Copiloto farmacéutico")
    st.caption("Responde a partir de las predicciones simuladas disponibles en esta demo.")

    consultas_sugeridas = [
        "¿Qué producto tiene más riesgo de rotura?",
        "¿Cuántas unidades pide para el CN 722402?",
        "¿Cuál es el stock de VITAMINA D3?",
    ]
    consulta = st.radio("Consultas rápidas", consultas_sugeridas, index=None)
    texto_libre = st.text_input("O escribe tu propia pregunta")
    pregunta = texto_libre.strip() or consulta

    if st.button("Preguntar", type="primary") or (consulta and not texto_libre):
        if not pregunta:
            st.warning("Escribe una pregunta o elige una consulta rápida.")
        else:
            pregunta_lower = pregunta.lower()

            def encontrar_producto(pregunta_lower):
                for _, fila in productos.iterrows():
                    if str(fila["cn"]) in pregunta_lower:
                        return fila
                    palabras = [w for w in fila["nombre"].lower().replace(",", " ").split() if len(w) >= 4]
                    if any(w in pregunta_lower for w in palabras):
                        return fila
                return None

            producto_encontrado = encontrar_producto(pregunta_lower)

            if "riesgo" in pregunta_lower and producto_encontrado is None:
                top = alertas_prioritarias(datos, top_n=1).iloc[0]
                st.success(
                    f"El producto con mayor riesgo ahora mismo es **{top['nombre']}** "
                    f"(CN {top['cn']}), con riesgo **{top['riesgo']}** y probabilidad "
                    f"{top['prob']:.0%}. Recomendación: {top['recomendacion']}."
                )
            elif producto_encontrado is not None:
                fila = producto_encontrado
                pred = datos[datos["cn"] == fila["cn"]]
                if not pred.empty:
                    p = pred.iloc[0]
                    st.success(
                        f"**{fila['nombre']}** (CN {fila['cn']}): stock actual {int(fila['stock'])} uds, "
                        f"riesgo {p['riesgo']} (prob {p['prob']:.0%}), demanda estimada 7d {int(p['demanda_7d'])}. "
                        f"Recomendación: {p['recomendacion']}."
                    )
                else:
                    st.success(f"**{fila['nombre']}** (CN {fila['cn']}): stock actual {int(fila['stock'])} uds.")
            else:
                st.info(
                    "No encontré un producto que coincida con tu pregunta en los datos de demo. "
                    "Prueba con el nombre o el código nacional (CN)."
                )
