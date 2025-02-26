import streamlit as st
import pandas as pd
from datetime import datetime
from geopy.geocoders import Nominatim
import geocoder
import folium
from streamlit_folium import folium_static

# **Configuración de estilos globales**
st.markdown("""
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

        /* Borde del mapa en violeta */
        .stDeckGlJsonChart, .folium-map {
            border: 6px solid #db84fa !important;
            border-radius: 15px !important;
            padding: 5px !important;
        }

        /* Aumentar borde del formulario */
        div.stForm {
            border: 3px solid #db84fa !important;
            border-radius: 10px !important;
            padding: 20px !important;
        }

        /* Aumentar borde de las alertas recientes */
        div.stExpander {
            border: 2px solid #db84fa !important;
            border-radius: 8px !important;
            padding: 10px !important;
        }

        /* Campos de texto SIEMPRE con borde violeta */
        div[data-baseweb="input"] {
            border: 2px solid #db84fa !important;
            border-radius: 6px !important;
            padding: 8px !important;
        }
        div[data-baseweb="input"] input, 
        textarea.stTextArea {
            color: black !important;
            border: none !important;
            outline: none !important;
        }

        /* Botones personalizados SOLO para "Usar mi ubicación actual" y "Enviar" */
        div.stButton > button:first-of-type, /* Primer botón en la página */
        div.stForm button {  /* Botón dentro de un formulario */
            background-color: white !important;
            color: #db84fa !important;
            border: 2px solid #db84fa !important;
            border-radius: 8px !important;
            padding: 10px 15px !important;
            font-size: 16px !important;
            font-weight: bold !important;
            transition: all 0.3s ease-in-out !important;
            cursor: pointer !important;
        }

        /* Hover: Fondo violeta y letras blancas SOLO para "Usar mi ubicación actual" y "Enviar" */
        div.stButton > button:first-of-type:hover,
        div.stForm button:hover {
            background-color: #db84fa !important;
            color: black !important;
        }

        /* Estilos para los radio buttons */
        div[data-baseweb="radio"] {
            display: flex;
            justify-content: center;
            gap: 15px;
        }
        div[data-baseweb="radio"] label {
            background-color: #ffffff;
            border: 2px solid #db84fa;
            border-radius: 8px;
            padding: 8px 12px;
            font-size: 16px;
            font-weight: bold;
            color: #db84fa !important;
            transition: all 0.3s ease-in-out;
            cursor: pointer;
        }
        div[data-baseweb="radio"] label:hover {
            background-color: #db84fa;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)


# **Inicializar geolocalizador**
geolocator = Nominatim(user_agent="streamlit_app")

# **Función para cargar datos del CSV**
@st.cache_data
def load_data():
    try:
        return pd.read_csv("alertas.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["tipo", "latitude", "longitude", "ubicación", "descripción", "status", "hora_envio"])

# **Cargar alertas en sesión**
if "alerts" not in st.session_state:
    st.session_state.alerts = load_data()

# **Mostrar Mapa con puntos de alerta y borde violeta**
st.image("img/alertasyavisos.png", width=400)

map_placeholder = st.empty()  # Contenedor para el mapa

def generate_map():
    m = folium.Map(
        location=[40.4168, -3.7038],  # Ubicación centrada en Madrid
        zoom_start=12,
        tiles="CartoDB Positron"  # Mapa blanco minimalista
    )
    for _, row in st.session_state.alerts.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=10,  # Radio del punto de alerta
            color="#db84fa",  # Borde violeta
            fill=True,
            fill_color="#db84fa",
            fill_opacity=0.4,  # Transparencia del punto de alerta
            popup=f"{row['tipo']}: {row['descripción']}"
        ).add_to(m)
    return m

with map_placeholder:
    if not st.session_state.alerts.empty:
        folium_static(generate_map())  # Renderiza el mapa con los puntos de alerta
    else:
        st.warning("No hay alertas disponibles para mostrar.")

# **Obtener ubicación actual del usuario**
def get_current_location():
    g = geocoder.ip('me')  # Detectar ubicación por IP
    if g.latlng:
        latitude, longitude = g.latlng
        location = geolocator.reverse((latitude, longitude), language="es")  # Convertir a dirección
        return latitude, longitude, location.address if location else "Ubicación desconocida"
    return None, None, "Ubicación no encontrada"

# **Formulario para añadir alerta**
st.image("img/nueva_alerta.png", width=250)

col1, col2 = st.columns(2)

with col1:
    use_current_location = st.button("📍 Usar mi ubicación actual")

with col2:
    manual_location = st.text_input("📌 O ingresar una dirección manual")

latitude, longitude, location_name = None, None, None

if use_current_location:
    latitude, longitude, location_name = get_current_location()
    if latitude and longitude:
        st.success(f"Ubicación detectada: {location_name}")
    else:
        st.error("⚠️ No se pudo obtener la ubicación actual.")

if manual_location:
    location = geolocator.geocode(manual_location)
    if location:
        latitude, longitude, location_name = location.latitude, location.longitude, location.address
        st.success(f"Dirección detectada: {location_name}")
    else:
        st.error("⚠️ No se pudo obtener la ubicación de la dirección ingresada.")

# **Formulario**
with st.form("new_alert_form"):
    description = st.text_area("Descripción de la alerta")
    alert_type = st.selectbox("Tipo de alerta", ["Emergencia", "Advertencia", "Información", "Acoso Callejero"])
    
    submitted = st.form_submit_button("Enviar Alerta")

    if submitted and description:
        if latitude is not None and longitude is not None:
            new_alert = {
                "tipo": alert_type,
                "latitude": latitude,
                "longitude": longitude,
                "ubicación": location_name,
                "descripción": description,
                "status": "activa",
                "hora_envio": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            # **Actualizar estado en sesión**
            st.session_state.alerts = pd.concat([st.session_state.alerts, pd.DataFrame([new_alert])], ignore_index=True)
            # **Guardar en CSV**
            st.session_state.alerts.to_csv("alertas.csv", index=False)
            # **Actualizar el mapa**
            with map_placeholder:
                folium_static(generate_map())  # Recargar mapa con la nueva alerta
            st.success("✅ Alerta enviada con éxito!")
        else:
            st.error("⚠️ Debes seleccionar una ubicación antes de enviar la alerta.")

# **Filtro para mostrar solo alertas activas o inactivas con botones**
st.image("img/consullta_alertas_recientes.png", width=500)

# Agregar radio buttons para filtrar entre alertas activas o inactivas
status_filter = st.radio(
    "Filtrar alertas por estado:", 
    ["Todas", "Activas", "Inactivas"], 
    horizontal=True  # 🔹 Esto hace que los botones estén en línea
)

# Aplicar el filtro sobre las alertas
if status_filter == "Activas":
    filtered_alerts = st.session_state.alerts[st.session_state.alerts["status"] == "activa"]
elif status_filter == "Inactivas":
    filtered_alerts = st.session_state.alerts[st.session_state.alerts["status"] == "inactiva"]
else:
    filtered_alerts = st.session_state.alerts  # Mostrar todas las alertas

# **Mostrar alertas filtradas**
if not filtered_alerts.empty:
    for _, row in filtered_alerts.iterrows():
        with st.expander(f"🔔 {row['tipo']} - ({row['hora_envio']})"):
            st.write(f"**Descripción:** {row['descripción']}")
            st.write(f"📍 **Ubicación:** {row['ubicación']}")
            st.write(f"📌 **Estado:** {row['status'].capitalize()}")
else:
    st.info("No hay alertas disponibles en este estado.")


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
            st.page_link("pages/modelo_optimizacion.py", label="Algoritmo Optimización", icon=":material/modeling:")

        st.session_state["usuario"] = usuario
        st.session_state["permisos"] = permisos  # Guardar permisos globalmen

        # Botón para cerrar la sesión
        btnSalir=st.button("Salir")
        if btnSalir:
            st.session_state.clear()
            # Luego de borrar el Session State reiniciamos la app para mostrar la opción de usuario y clave
            st.rerun()