
# 💊 Farmacia Lorca IA — Demo (Hugging Face Space)

Demo pública de **Farmacia Lorca IA** basada en **Streamlit**, con **datos simulados** y sin conexión a ninguna base de datos real.

> Ideal para compartir con compañeros o evaluar el flujo de trabajo sin tocar tu SQL Server / Farmatic.

---

## ▶️ Cómo ejecutar en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

La app cargará CSVs de `./data/` y mostrará el dashboard, predicciones simuladas, catálogo y faltas.

---

## 🚀 Cómo desplegar en Hugging Face Spaces

1. Crea un Space nuevo en tu cuenta: **New Space → SDK: Streamlit**.
2. Sube estos archivos al Space:
   - `app.py`
   - `requirements.txt`
   - Carpeta `data/` completa
3. Guarda/Commitea. La build se iniciará automáticamente y en pocos minutos verás la URL pública.

**Sugerencia**: Nombra el Space como `farmacia-lorca-ia-demo`.

---

## 🔗 Integración con el Proyecto Real

Este Space es **solo front de demo**. El proyecto completo (backend FastAPI + ETL + IA + DB + n8n) está pensado para Docker Compose.
Cuando quieras conectar con tu backend real, puedes:
- Reemplazar la lectura de CSV por llamadas `requests.get()` a tu API.
- O bien montar el frontend del proyecto principal.

---

## 👤 Autor
**Farmacia Lorca IA** · Demo para evaluación pública  
Actualizado: 2025-10-21
