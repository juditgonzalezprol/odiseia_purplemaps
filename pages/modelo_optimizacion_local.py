import streamlit as st
import requests
import folium
from streamlit_folium import folium_static
from serpapi import GoogleSearch
from streamlit_folium import st_folium
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# Configuración de la página
st.set_page_config(page_title="Buscador de Lugares", layout="wide")


# Estilos personalizados
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
        .stApp { background-color: white; }
        .st-emotion-cache-janbn0 { background-color: #db84fa !important; }
        [data-testid="stSidebar"] { background-color: #222 !important; }
        [data-testid="stSidebar"] * { color: white !important; }

        /* 🔥 Corrección del borde de los gráficos */
        .stPlotlyChart, .stMap {
            background-color: white;
            border: 2px solid #6a1b9a;
            border-radius: 30px;
            padding: 10px; /* Se cambia de -4px a 10px */
            overflow: hidden; /* Evita que la imagen sobresalga */
            margin-bottom: 20px; /* Espaciado para evitar que se encime */
        }

        /* 🔥 Corrección del mapa */
        .stMap {
            height: 500px; /* Ajusta la altura */
            width: 100%; /* Evita que sobresalga */
        }

        /* Estilo del encabezado */
        h2, h3, h4 {
            color: #6a1b9a;
        }

    </style>
    """,
    unsafe_allow_html=True
)

# Título

# API Key de SerpApi (reemplázala con la tuya)
API_KEY = "596f9ae7b1bd024900ced0189a2c07e3210b9f24e8cc3098176870aa480b8037"
ubicacion = "@40.417031, -3.683458,14z"

params_policia = {
  "engine": "google_maps",
  "q": "Policia",
  "ll": ubicacion,
  "api_key": "596f9ae7b1bd024900ced0189a2c07e3210b9f24e8cc3098176870aa480b8037"
}
search_policia = GoogleSearch(params_policia)
results_policia = search_policia.get_dict()

coordenadas_policia = [
    (lugar["gps_coordinates"]["latitude"], lugar["gps_coordinates"]["longitude"])
    for lugar in results_policia["local_results"]
]

params_discoteca = {
  "engine": "google_maps",
  "q": "Discoteca",
  "ll": ubicacion,
  "api_key": "596f9ae7b1bd024900ced0189a2c07e3210b9f24e8cc3098176870aa480b8037"
}
search_discoteca = GoogleSearch(params_discoteca)
results_discoteca = search_discoteca.get_dict()

coordenadas_discoteca = [
    (lugar["gps_coordinates"]["latitude"], lugar["gps_coordinates"]["longitude"])
    for lugar in results_discoteca["local_results"]
]

params_club = {
  "engine": "google_maps",
  "q": "Club de noche",
  "ll": ubicacion,
  "api_key": "596f9ae7b1bd024900ced0189a2c07e3210b9f24e8cc3098176870aa480b8037"
}
search_club = GoogleSearch(params_club)
results_club = search_club.get_dict()

coordenadas_club = [
    (lugar["gps_coordinates"]["latitude"], lugar["gps_coordinates"]["longitude"])
    for lugar in results_club["local_results"]
]


params_bar = {
  "engine": "google_maps",
  "q": "Bar de noche",
  "ll": ubicacion,
  "api_key": "596f9ae7b1bd024900ced0189a2c07e3210b9f24e8cc3098176870aa480b8037"
}
search_bar = GoogleSearch(params_bar)
results_bar = search_bar.get_dict()

coordenadas_bar = [
    (lugar["gps_coordinates"]["latitude"], lugar["gps_coordinates"]["longitude"])
    for lugar in results_bar["local_results"]
]

# Crear el mapa centrado en un punto medio
mapa = folium.Map(location=[40.42, -3.69], zoom_start=12)

# Agregar los puntos al mapa con diferentes colores y categorías
for coord in coordenadas_bar:
    folium.Marker(coord, popup="Bar", icon=folium.Icon(color="red")).add_to(mapa)

for coord in coordenadas_club:
    folium.Marker(coord, popup="Club", icon=folium.Icon(color="red")).add_to(mapa)

for coord in coordenadas_discoteca:
    folium.Marker(coord, popup="Discoteca", icon=folium.Icon(color="red")).add_to(mapa)

for coord in coordenadas_policia:
    folium.Marker(coord, popup="Policía", icon=folium.Icon(color="blue")).add_to(mapa)


# 📌 Unir coordenadas de bares, clubes y discotecas como puntos prioritarios
coordenadas_prioritarias = np.array(coordenadas_bar + coordenadas_club + coordenadas_discoteca)
coordenadas_policia = np.array(coordenadas_policia)  # Para referencias de zonas cubiertas

# 📌 Función para calcular los puntos violeta óptimos evitando zonas de policía
def calcular_puntos_violeta(n_puntos):
    """
    Calcula los puntos óptimos usando K-Means en bares, discotecas y clubes,
    pero evitando que los puntos caigan en zonas ya cubiertas por la policía.
    """
    kmeans = KMeans(n_clusters=n_puntos, random_state=42, n_init=10)
    kmeans.fit(coordenadas_prioritarias)

    puntos_violeta = kmeans.cluster_centers_

    # Filtrar puntos que no estén demasiado cerca de la policía
    distancia_minima = 0.003  # Aproximadamente 300m de distancia
    puntos_finales = []
    
    for punto in puntos_violeta:
        if all(np.linalg.norm(punto - pol) > distancia_minima for pol in coordenadas_policia):
            puntos_finales.append(punto)
    
    # Si todos los puntos fueron filtrados, al menos devuelve los originales
    if not puntos_finales:
        puntos_finales = puntos_violeta

    return np.array(puntos_finales)

# 📌 Función para generar el mapa
def mostrar_mapa(n_puntos):
    """
    Genera y muestra el mapa con las discotecas, bares, clubes y los puntos violeta.
    """
    puntos_violeta = calcular_puntos_violeta(n_puntos)

    # Centrar el mapa en la media de las coordenadas
    lat_centro = np.mean(coordenadas_prioritarias[:, 0])
    lon_centro = np.mean(coordenadas_prioritarias[:, 1])
    mapa = folium.Map(location=[lat_centro, lon_centro], zoom_start=13)

    # Añadir bares
    for lat, lon in coordenadas_bar:
        folium.Marker([lat, lon], icon=folium.Icon(color="red"), popup="Bar").add_to(mapa)

    # Añadir clubes
    for lat, lon in coordenadas_club:
        folium.Marker([lat, lon], icon=folium.Icon(color="red"), popup="Club").add_to(mapa)

    # Añadir discotecas
    for lat, lon in coordenadas_discoteca:
        folium.Marker([lat, lon], icon=folium.Icon(color="red"), popup="Discoteca").add_to(mapa)

    # Añadir estaciones de policía
    for lat, lon in coordenadas_policia:
        folium.Marker([lat, lon], icon=folium.Icon(color="blue"), popup="Policía").add_to(mapa)

    # Añadir puntos violeta óptimos
    for lat, lon in puntos_violeta:
        folium.Marker([lat, lon], icon=folium.Icon(color="purple", icon="heart"), popup="Punto Violeta").add_to(mapa)

    # Mostrar el mapa en Streamlit
    st_folium(mapa, width=1600, height=500)

# 📌 Interfaz de Streamlit
st.image("img/optimizador_local.png", width=600)
n_puntos = st.slider("Número de Puntos Violetas que se quieren poner", min_value=1, max_value=8, value=3, step=1)
mostrar_mapa(n_puntos)

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