import streamlit as st
from PIL import Image
from pathlib import Path

# ===== CONFIGURACIÓN GENERAL =====
st.set_page_config(page_title="Portafolio BAE", page_icon="👶", layout="wide")

# ===== COLORES BAE =====
COLOR_PRIMARIO = "#DD8E6B"  # melocotón
COLOR_SECUNDARIO = "#F0D192"  # fondo crema
COLOR_ACENTO = "#FFF2C3"  # amarillo pálido
COLOR_SUAVE = "#C6E2E3"  # azul agua

# ===== ESTILOS CSS =====
st.markdown(f"""
    <style>
        body {{
            background-color: {COLOR_SECUNDARIO};
            color: #2E2E2E;
            font-family: 'Poppins', sans-serif;
        }}
        .header {{
            text-align: center;
            padding: 30px 0 10px 0;
        }}
        .header h1 {{
            font-size: 2.8em;
            font-weight: 700;
            color: {COLOR_PRIMARIO};
            margin-bottom: 5px;
        }}
        .header h3 {{
            font-size: 1.3em;
            color: #5A5A5A;
            margin-bottom: 25px;
        }}
        .app-box {{
            background: #FFF8EA;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.05);
            margin-bottom: 25px;
            border-left: 10px solid {COLOR_PRIMARIO};
            transition: all 0.25s ease;
        }}
        .app-box:hover {{
            transform: scale(1.02);
            box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        }}
        .app-title {{
            color: {COLOR_PRIMARIO};
            font-size: 1.3em;
            font-weight: 600;
            margin-bottom: 10px;
        }}
        .stMarkdown a {{
            color: {COLOR_SUAVE};
        }}
        .sidebar .sidebar-content {{
            background-color: {COLOR_ACENTO};
        }}
    </style>
""", unsafe_allow_html=True)

# ===== ENCABEZADO =====
with st.container():
    st.markdown('<div class="header">', unsafe_allow_html=True)
    # Aquí puedes reemplazar el nombre del archivo por tu logo real
    st.image("logo_bae.png", width=140)  
    st.markdown("""
        <h1>Portafolio BAE</h1>
        <h3>Aplicaciones para el cuidado y desarrollo de tu bebé</h3>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ===== SIDEBAR =====
with st.sidebar:
    st.image("logo_bae.png", width=120)
    st.markdown(f"### 🌸 Aplicaciones con Inteligencia Artificial")
    st.write(
        "BAE combina inteligencia artificial, IoT y blockchain para crear entornos más seguros, "
        "humanos y adaptativos para los bebés. Aquí encontrarás las herramientas que impulsan el "
        "cuidado inteligente desde los primeros días de vida."
    )

    st.markdown(f"#### 💡 Aprende más")
    st.write("[Explora más herramientas IA](https://sites.google.com/view/aplicacionesdeia/inicio)")

# ===== CONTENIDO PRINCIPAL =====
col1, col2, col3 = st.columns(3)

apps = [
    ("Introducción a Bae", "https://n3qduxtjtgbzxps9vdppnw.streamlit.app/", "1.png"),
    ("Audios con cuentos para Bebé", "https://texto-a-voz-36cpsnzbwwjklgy9kjvhta.streamlit.app/", "2.png"),
    ("Reconocimiento de Diagnostico", "https://b4xnfch5ocmgrjdhz3grjs.streamlit.app/", "3.png"),
    ("Conversión de Voz a Texto", "https://chatpdf-crxyojkks8b3scte2r4aml.streamlit.app/", "4.png"),
    ("Detección de Movimiento", "https://characters-brpc4s4yb04.streamlit.app/", "5.png"),
    ("Análisis por voz", "https://znfsrrvdas34igywkpvasm.streamlit.app/", "6.png"),
    ("Aprendiendo los Numeros", "https://nele77pi8emynduggzai45.streamlit.app/", "7.png"),
    ("BAE OCR Audio", "https://ocr-audio-f2rmevcnhuomksuamepdjm.streamlit.app/", "8.png"),
    ("Predicción de Enfermedades", "https://recepmqtt-hhs6p59arcbxmww82fyab9.streamlit.app/", "9.png"),
    ("Alertas Inteligentes", "https://tdfesp-oe3hp9zkmc4qhst8plnoda.streamlit.app/", "10.png"),
    ("Generador de Rutinas", "https://imultimod.streamlit.app/", "11.png"),
    ("Asistente de Lactancia", "https://traductor-ab0sp9f6fi.streamlit.app/", "12.png"),
    ("Tablero de historias Bae", "https://tactil-bgolrmbhdgvokrtstuvmvc.streamlit.app/", "13.png"),
    ("Visualización IoT", "https://yolov5-54fvqmwgbihxqpptfp75ml.streamlit.app/", "14.png"),
    ("Panel Blockchain BAE", "https://vision2-gpt4o.streamlit.app/", "15.png"),
]
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
