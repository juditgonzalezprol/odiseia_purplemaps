import streamlit as st
import folium
from streamlit_folium import st_folium 
import pandas as pd

st.set_page_config(page_title="Puntos Violeta", page_icon="🟣", layout="wide")

st.markdown(
    """
    <style>

        * {
            font-family: 'Google Sans', sans-serif;
        }
        /* Fondo blanco */
        .stApp {
            background-color: white;
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
            background-color: #db84fa; /* Lila claro */
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

with st.sidebar:

    usuario = st.session_state.get("usuario", None)

    dfusuarios = pd.read_csv('usuarios.csv')
    dfUsuario = dfusuarios[dfusuarios['usuario'] == usuario]
    
    if not dfUsuario.empty:
        nombre = dfUsuario['nombre'].values[0]
        permisos = dfUsuario['permisos'].values[0]
    else:
        nombre = "Invitada"

    # usuario = st.session_state["usuario"]
    # permisos = st.session_state["permisos"]

    st.image("img/Purple_Maps.png", width=100)
    # Cargamos la tabla de usuarios
    dfusuarios = pd.read_csv('usuarios.csv')
    # Filtramos la tabla de usuarios
    dfUsuario =dfusuarios[(dfusuarios['usuario']==usuario)]
    # Cargamos el nombre del usuario
    nombre= dfUsuario['nombre'].values[0]
    permisos= dfUsuario['permisos'].values[0]
    #Mostramos el nombre del usuario
    st.write(f"Hola **:blue-background[{nombre}]** ")
    # Mostramos los enlaces de páginas
    st.subheader("Funcionalidades")
    st.page_link("pages/1_📍Mapa_Violeta.py", label="Mapa Violeta", icon=":material/home_pin:")
    st.page_link("pages/2_ Chat_Violeta.py", label="Chat Violeta", icon=":material/chat:")
    st.page_link("pages/3_⚠️ Alertas_Violeta.py", label="Alertas ", icon=":material/report:")
    if permisos == "administradora":
        st.subheader("Gestión y administración")
        st.page_link("pages/dashboard_alertas.py", label="Dashboard Alertas", icon=":material/bar_chart_4_bars:")

    st.session_state["usuario"] = usuario
    st.session_state["permisos"] = permisos  # Guardar permisos globalmen

    # Botón para cerrar la sesión
    btnSalir=st.button("Salir")
    if btnSalir:
        st.session_state.clear()
        # Luego de borrar el Session State reiniciamos la app para mostrar la opción de usuario y clave
        st.rerun()