import streamlit as st
from PIL import Image
from pathlib import Path

# ======== CONFIGURACIÓN GENERAL ========
st.set_page_config(page_title="Bae App Portfolio", page_icon="👶", layout="wide")

# Colores y estilo BAE (HTML + CSS)
st.markdown("""
    <style>
        body {
            background-color: #F8FAFC;
            color: #2E2E2E;
            font-family: 'Poppins', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 2.2em;
            font-weight: 600;
            color: #6C63FF;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #5C5C5C;
            margin-bottom: 40px;
        }
        .app-box {
            background: #FFFFFF;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
            margin-bottom: 25px;
            transition: all 0.2s ease;
        }
        .app-box:hover {
            transform: scale(1.02);
            box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
        }
        .app-title {
            color: #FF7CA3;
            font-size: 1.1em;
            font-weight: 600;
        }
        a {
            color: #6C63FF;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# ======== ENCABEZADO ========
st.markdown('<p class="title">Portafolio de aplicaciones para el cuidado y desarrollo de tu bebé</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Soluciones impulsadas por IA y tecnología para entender, cuidar y acompañar a los bebés del futuro.</p>', unsafe_allow_html=True)

# ======== SIDEBAR ========
with st.sidebar:
    st.image("https://i.imgur.com/jWcDQVG.png", width=150)
    st.markdown("### 🌱 Aplicaciones con Inteligencia Artificial")
    st.write(
        "La inteligencia artificial impulsa la detección temprana, el análisis de datos y la "
        "automatización del cuidado infantil. En este portafolio exploramos cómo BAE integra IA, "
        "IoT y Blockchain para crear entornos más seguros y humanos."
    )

    st.markdown("#### 📘 Aprende más")
    st.write("[Ir al sitio oficial de IA](https://sites.google.com/view/aplicacionesdeia/inicio)")

# ======== CONTENIDO PRINCIPAL ========
col1, col2, col3 = st.columns(3)

apps = [
    ("Monitoreo de Temperatura", "https://imultimod.streamlit.app/", "txt_to_audio2.png"),
    ("Análisis de Sueño del Bebé", "https://asistpy-csv.streamlit.app/", "data_analisis.png"),
    ("Reconocimiento de Llanto", "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/", "txt_to_audio.png"),
    ("Conversión de Voz a Texto", "https://traductor-ab0sp9f6fi.streamlit.app/", "OIG8.jpg"),
    ("Detección de Movimiento", "https://vision2-gpt4o.streamlit.app/", "OIG4.jpg"),
    ("Análisis de Video Familiar", "https://transcript-whisper.streamlit.app/", "OIG3.jpg"),
    ("Control de Humedad y Temperatura", "https://chatpdf-cc.streamlit.app/", "Chat_pdf.png"),
    ("Seguimiento del Crecimiento", "https://vision2-gpt4o.streamlit.app/", "OIG6.jpg"),
    ("Predicción de Enfermedades", "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/", "OIG5.jpg"),
    ("Alertas Inteligentes", "https://asistpy-csv.streamlit.app/", "data_analisis.png"),
    ("Generador de Rutinas", "https://imultimod.streamlit.app/", "txt_to_audio2.png"),
    ("Asistente de Lactancia", "https://traductor-ab0sp9f6fi.streamlit.app/", "OIG8.jpg"),
    ("Historias del Bebé (IA)", "https://chatpdf-cc.streamlit.app/", "Chat_pdf.png"),
    ("Visualización de Datos IoT", "https://asistpy-csv.streamlit.app/", "data_analisis.png"),
    ("Panel de Cuidados Blockchain", "https://vision2-gpt4o.streamlit.app/", "OIG4.jpg"),
]

# ======== DISTRIBUCIÓN ========
columns = [col1, col2, col3]

for i, (title, url, img_file) in enumerate(apps):
    with columns[i % 3]:
        st.markdown(f"<div class='app-box'><div class='app-title'>{title}</div>", unsafe_allow_html=True)
        try:
            image = Image.open(Path(img_file))
            st.image(image, use_column_width=True)
        except:
            st.image("https://via.placeholder.com/200x150.png?text=Bae+App", use_column_width=True)
        st.write(f"[Abrir aplicación]({url})")
        st.markdown("</div>", unsafe_allow_html=True)

