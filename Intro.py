import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(
    page_title="BAE | Baby App Especializada",
    page_icon="👶",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILO PERSONALIZADO (colores BAE) ---
st.markdown("""
    <style>
        body {
            background-color: #F8FAFC;
            color: #2E2E2E;
        }
        [data-testid="stSidebar"] {
            background-color: #F0F7FF;
            border-right: 1px solid #CCE0FF;
        }
        h1, h2, h3, h4 {
            color: #5271FF;
            font-family: 'Poppins', sans-serif;
        }
        .stButton>button {
            background-color: #5271FF;
            color: white;
            border-radius: 10px;
            height: 2.5em;
            width: 100%;
            border: none;
        }
        .stButton>button:hover {
            background-color: #6F8BFF;
        }
        .small-text {
            font-size: 15px;
            color: #666;
        }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("👶 BAE | Portafolio de Experiencias Inteligentes")
st.markdown(
    "### Una aplicación diseñada para el **cuidado y desarrollo de tu bebé**, "
    "donde la tecnología se combina con el amor y la ciencia para ofrecer bienestar desde los primeros días de vida."
)

# --- SIDEBAR ---
with st.sidebar:
    st.image("bebeFeliz.png", width=120)
    st.subheader("Sobre BAE 💧")
    st.write(
        "BAE (Baby Ambient Environment) integra sensores IoT, inteligencia artificial y blockchain "
        "para ofrecer un monitoreo ambiental seguro, ético y trazable que ayuda a cuidar la salud "
        "de los bebés en sus primeros meses de vida."
    )

    st.markdown("---")
    st.write("**Explora nuestras experiencias digitales:**")
    st.markdown(
        "- 🔊 Interacción por voz y sonido\n"
        "- 🌡️ Análisis ambiental inteligente\n"
        "- 💬 Comunicación emocional asistida\n"
        "- 📊 Visualización de datos y desarrollo"
    )

# --- SECCIÓN PRINCIPAL DE CONTENIDO ---
st.subheader("🌱 Experiencias Inteligentes")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🍼 Monitoreo Ambiental")
    image = Image.open('bebeFrio.png')
    st.image(image, width=220)
    st.write("Sensores inteligentes que analizan la temperatura y humedad del entorno del bebé en tiempo real.")
    st.button("Explorar función")

    st.subheader("💤 Detección de Estado Emocional")
    image = Image.open('bebeCalor.png')
    st.image(image, width=220)
    st.write("Mediante IA, el sistema identifica patrones en el llanto y comportamiento para anticipar necesidades.")
    st.button("Probar modelo")

with col2:
    st.subheader("💧 Salud y Bienestar")
    image = Image.open('thermometer.png')
    st.image(image, width=220)
    st.write("BAE ayuda a detectar variaciones ambientales que podrían afectar la salud del bebé.")
    st.button("Simular lectura")

    st.subheader("📊 Dashboard de Desarrollo")
    image = Image.open('data_analisis.png')
    st.image(image, width=220)
    st.write("Visualiza los datos recolectados por los sensores y recibe alertas preventivas personalizadas.")
    st.button("Ver dashboard")

with col3:
    st.subheader("🤖 Blockchain y Seguridad")
    image = Image.open('OIG4.jpg')
    st.image(image, width=220)
    st.write("Toda la información es encriptada y registrada en Polkadot, garantizando trazabilidad y privacidad.")
    st.button("Conocer más")

    st.subheader("🎵 Comunicación Natural")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=220)
    st.write("Convierte sonidos, palabras y emociones en interacciones seguras y cálidas con tu bebé.")
    st.button("Explorar demo")

# --- PIE DE PÁGINA ---
st.markdown("---")
st.markdown(
    "<p class='small-text' style='text-align:center;'>BAE © 2025 | Baby Ambient Environment • "
    "Innovación para un futuro más saludable.</p>",
    unsafe_allow_html=True
)


