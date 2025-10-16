import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(
    page_title="BAE | Aplicaciones de IA",
    page_icon="👶",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILO VISUAL DE BAE ---
st.markdown("""
    <style>
        /* Fondo general */
        body {
            background-color: #F8FAFC;
            color: #2E2E2E;
            font-family: "Poppins", sans-serif;
        }

        /* Encabezados */
        h1, h2, h3 {
            color: #5271FF;
            font-weight: 600;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #F0F7FF;
            border-right: 2px solid #D6E4FF;
        }

        /* Botones */
        .stButton>button {
            background-color: #5271FF;
            color: white;
            border-radius: 10px;
            height: 2.5em;
            width: 100%;
            border: none;
            font-weight: 500;
        }
        .stButton>button:hover {
            background-color: #6F8BFF;
        }

        /* Enlaces */
        a {
            color: #5271FF !important;
            text-decoration: none;
            font-weight: 500;
        }
        a:hover {
            color: #3857E0 !important;
            text-decoration: underline;
        }

        /* Subtítulos */
        .stMarkdown p {
            font-size: 16px;
            color: #4A4A4A;
        }

        /* Imágenes */
        img {
            border-radius: 12px;
            box-shadow: 0px 2px 8px rgba(82, 113, 255, 0.15);
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 2em;
            color: #888;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# --- CONTENIDO PRINCIPAL ---
st.title("👶 Portafolio BAE | Aplicaciones de Inteligencia Artificial")
st.markdown(
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, "
    "lo que resulta en una mayor eficiencia y precisión en diversos campos."
)

# --- SIDEBAR ---
with st.sidebar:
    st.image("bebeFeliz.png", width=150)
    st.subheader("🌱 Aplicaciones con Inteligencia Artificial")
    parrafo = (
        "Explora cómo la inteligencia artificial puede integrarse con el monitoreo de bebés, "
        "creando experiencias seguras, humanas y adaptadas al entorno."
    )
    st.write(parrafo)

    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.markdown("**Páginas y ejercicios prácticos:**")
    st.write(f"[Haz clic aquí para explorar]({url_ia})")

# --- CONTENEDORES DE APLICACIONES ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🎙️ Conversión de texto a voz")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=190)
    st.write("En el siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial.") 
    url = "https://imultimod.streamlit.app/"
    st.write(f"[Texto a voz]({url})")

    st.subheader("🧠 Reconocimiento de Objetos")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos cómo se detectan objetos en imágenes.") 
    url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    st.write(f"[YOLO]({url})")

    st.subheader("⚙️ Entrenando Modelos")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos cómo puedes usar tu modelo entrenado.") 
    url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    st.write(f"[Modelo YOLO]({url})")

with col2:
    st.subheader("🗣️ Conversión de voz a texto")
    image = Image.open('OIG8.jpg')
    st.image(image, width=200)
    st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
    url = "https://traductor-ab0sp9f6fi.streamlit.app/"
    st.write(f"[Voz a texto]({url})")

    st.subheader("📈 Análisis de Datos")
    image = Image.open('data_analisis.png')
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo se pueden analizar datos usando agentes.") 
    url = "https://asistpy-csv.streamlit.app/"
    st.write(f"[Análisis de Datos]({url})")

    st.subheader("🎧 Transcriptor Audio y Video")
    image = Image.open('OIG3.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos cómo realizamos transcripciones de audio y video.") 
    url = "https://transcript-whisper.streamlit.app/"
    st.write(f"[Transcriptor]({url})")

with col3:
    st.subheader("📄 Generación en Contexto")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento PDF.") 
    url = "https://chatpdf-cc.streamlit.app/"
    st.write(f"[RAG PDF]({url})")

    st.subheader("🖼️ Análisis de Imagen")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos la capacidad de análisis en imágenes.") 
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"[Visión]({url})")

    st.subheader("🤖 Sistema Ciberfísico")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"[Ciberfísico]({url})")

# --- FOOTER ---
st.markdown("<div class='footer'>BAE © 2025 | Baby Ambient Environment</div>", unsafe_allow_html=True)

