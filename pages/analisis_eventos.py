import streamlit as st
import pandas as pd
from serpapi import GoogleSearch

st.set_page_config(page_title="Análisis de tendencias", page_icon="🟣", layout="wide")

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
            
import streamlit as st
from serpapi import GoogleSearch

# Título de la aplicación
st.image("img/analisis.png", width=500)

# API Key de SerpApi (reemplázala con tu clave real)
API_KEY = "596f9ae7b1bd024900ced0189a2c07e3210b9f24e8cc3098176870aa480b8037"

# Entrada del usuario
st.header("🔍 Parámetros de búsqueda")
ciudad = st.text_input("Introduce el municipio/ciudad/zona", "Madrid")
evento = st.text_input("Introduce el tipo de evento (ej. festival, concierto, feria)", "festival, fiesta")

# Botón de búsqueda
if st.button("Buscar eventos"):
    # Definir la consulta
    query = f"{evento} en {ciudad}"

    # Parámetros de búsqueda
    params = {
        "engine": "google_news",
        "hl": "es",
        "gl": "es",
        "q": query,
        "api_key": API_KEY
    }

    # Ejecutar la búsqueda
    st.write(f"🔍 Buscando noticias sobre **{evento}** en **{ciudad}**...")
    search = GoogleSearch(params)
    results = search.get_dict()

    # Mostrar resultados
    if "news_results" in results:
        for i, news in enumerate(results["news_results"], start=1):
            st.subheader(f"{i}. {news['title']}")
            st.write(f"📰 Fuente: {news.get('source', 'Desconocida')}")
            st.write(f"📅 Fecha: {news.get('date', 'No disponible')}")
            st.write(f"[Leer más]({news['link']})")
            st.write("---")
    else:
        st.error("❌ No se encontraron noticias.")

# Nota: Para ejecutar esta aplicación, instala Streamlit y la API de SerpApi con:
# pip install streamlit go

