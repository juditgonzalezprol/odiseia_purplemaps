import streamlit as st
import folium
from streamlit_folium import st_folium 
import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim

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

st.image("img/purplemapsearch.png", width=500)

# Crear el mapa con un estilo blanco minimalista (CartoDB Positron)
m = folium.Map(
    location=[40.4168, -3.7038], 
    zoom_start=12, 
    tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
    attr="© OpenStreetMap contributors, © CARTO"
)

# Leer los puntos desde un archivo CSV
df = pd.read_csv("puntos.csv")

# Iterar sobre cada fila del DataFrame y agregar un marcador con enlace en el popup
for index, row in df.iterrows():
    lat = row["latitud"]
    lon = row["longitud"]
    # Se obtiene el texto del popup o se asigna un valor por defecto
    popup_text = row["popup"] if "popup" in row else "Punto Violeta"
    tooltip_text = row["tooltip"] if "tooltip" in row else "Haz clic para más info"
    
    # Crear enlace HTML para el popup que abra Google Maps en otra pestaña
    html = f'<a href="https://www.google.com/maps?q={lat},{lon}" target="_blank">{popup_text}</a>'
    popup = folium.Popup(html, max_width=300)
    
    # Agregar el marcador con el popup y el tooltip definidos
    folium.Marker(
        [lat, lon],
        popup=popup,
        tooltip=tooltip_text,
        icon=folium.Icon(color="purple")
    ).add_to(m)

# Mostrar el mapa en Streamlit
st_folium(m, width=1500, height=550)

st.markdown(
    """
    <style>
        * { font-family: 'Google Sans', sans-serif; }
        .stApp { background-color: white; }
        [data-testid="stSidebar"] { background-color: #c39bd8 !important; }
        [data-testid="stSidebar"] * { color: white !important; }
        .sidebar-logo { display: flex; justify-content: center; align-items: center; padding: 20px 0; }
        .sidebar-logo img { width: 180px; }
        .container { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 90vh; text-align: center; }
        .title { font-size: 40px; font-weight: bold; color: #6a1b9a; }
        .logo { width: 200px; margin: 20px 0; }
        .info-box { background-color: #db84fa; padding: 20px; border-radius: 15px; width: 60%; font-size: 18px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("img/purplemapsearch.png", width=500)

with st.sidebar:

        st.markdown(
            """
            <style>
                /* Cambiar el fondo del sidebar a morado claro */
                [data-testid="stSidebar"] {
                    background-color: #c39bd8 !important;
                }
                
                /* Cambiar el color del texto en el sidebar a blanco */
                [data-testid="stSidebar"] * {
                    color: white !important;
                }
            </style>
            """,
            unsafe_allow_html=True
        )


        usuario = st.session_state.get("usuario", None)
        permisos = st.session_state.get("permisos", "Usuaria")  # Valor por defecto si no existe


        dfusuarios = pd.read_csv('usuarios.csv')

        # Filtrar usuario
        dfUsuario = dfusuarios[dfusuarios['usuario'] == usuario]

        # ✅ Verificar si dfUsuario no está vacío antes de acceder a valores
        if not dfUsuario.empty:
            nombre = dfUsuario.iloc[0]["nombre"]  # Acceder a la primera fila de forma segura
            permisos = dfUsuario.iloc[0]["permisos"]
        else:
            nombre = "Invitada"
            permisos = "Usuaria"

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
        st.page_link("inicio.py", label="Inicio", icon=":material/home:")
        st.page_link("pages/mapa_violeta.py", label="Mapa Violeta", icon=":material/home_pin:")
        st.page_link("pages/chat_violeta.py", label="Chat Violeta", icon=":material/chat:")
        st.page_link("pages/alertas_violeta.py", label="Alertas ", icon=":material/report:")
        st.page_link("pages/politica_privacidad_terminos_de_uso.py", label="Documentación", icon=":material/contact_support:")
        st.page_link("pages/forms_peticiones.py", label="Solicitud de PV", icon=":material/contact_page:")
        if permisos == "administradora":
            st.subheader("Gestión y administración")
            st.page_link("pages/dashboard_alertas.py", label="Dashboard Alertas", icon=":material/bar_chart_4_bars:")
            st.page_link("pages/modelo_optimizacion_estatal.py", label="Modelo Optimización Estatal", icon=":material/modeling:")
            st.page_link("pages/modelo_optimizacion_local.py", label="Modelo Optimización Local", icon=":material/modeling:")

        st.session_state["usuario"] = usuario
        st.session_state["permisos"] = permisos  # Guardar permisos globalmen

        # Botón para cerrar la sesión
        btnSalir=st.button("Salir")
        if btnSalir:
            st.session_state.clear()
            # Luego de borrar el Session State reiniciamos la app para mostrar la opción de usuario y clave
            st.rerun()