import folium
from streamlit_folium import st_folium
import streamlit as st

st.set_page_config(page_title="Puntos Violeta", page_icon="🟣", layout="wide")

st.markdown(
    """
    <style>
        /* Fondo blanco */
        .stApp {
            background-color: #a9088e;
        }
        /* Centrar el contenido */
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 90vh;
            text-align: center;
        }
        /* Estilo del título */
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #6a1b9a; /* Morado oscuro */
        }
        /* Estilo del logo */
        .logo {
            width: 200px;
            margin: 20px 0;
        }
        /* Caja de información */
        .info-box {
            background-color: #f3e5f5; /* Lila claro */
            padding: 20px;
            border-radius: 15px;
            width: 60%;
            font-size: 18px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        /* Cambiar el fondo del sidebar a negro */
        [data-testid="stSidebar"] {
            background-color: #c39bd8 !important;
        }
        
        /* Cambiar el color del texto en el sidebar a blanco */
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Centrar y poner margen al logo en el sidebar */
        .sidebar-logo {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px 0;
        }

        /* Ajustar el tamaño del logo */
        .sidebar-logo img {
            width: 180px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("img/searchmap.png", width=500)


# Crear el mapa con un estilo blanco minimalista (CartoDB Positron)
m = folium.Map(
    location=[40.4168, -3.7038], 
    zoom_start=12, 
    tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
    attr="© OpenStreetMap contributors, © CARTO"
)

# Agregar un marcador de ejemplo en Madrid
folium.Marker(
    [40.4168, -3.7038], 
    popup="Punto Violeta en Madrid", 
    tooltip="Haz clic para más info",
    icon=folium.Icon(color="purple")
).add_to(m)

# Mostrar el mapa en Streamlit
st_folium(m, width=1050, height=550)
