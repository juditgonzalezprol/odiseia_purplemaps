import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from datetime import datetime
from geopy.geocoders import Nominatim


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


# Inicializar geolocalizador
geolocator = Nominatim(user_agent="streamlit_app")

# Base de datos de alertas inventadas en el centro de Madrid
initial_alerts = [
    {"Descripción": "Incendio en un edificio", "Tipo": "Emergencia", "Ubicación": "Puerta del Sol, Madrid", "Fecha": "2025-02-21 10:00:00"},
    {"Descripción": "Manifestación en la Gran Vía", "Tipo": "Advertencia", "Ubicación": "Gran Vía, Madrid", "Fecha": "2025-02-21 11:00:00"},
    {"Descripción": "Corte de tráfico por obras", "Tipo": "Información", "Ubicación": "Plaza Mayor, Madrid", "Fecha": "2025-02-21 12:00:00"}
]

# Simulación de almacenamiento de alertas (usando sesión para mantener datos temporalmente)
if 'alerts' not in st.session_state:
    st.session_state.alerts = initial_alerts

# Función para actualizar el mapa
def generate_map():
    m = folium.Map(
        location=[40.4168, -3.7038],  # Ubicación centrada en Madrid
        zoom_start=12,
        tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
        attr="© OpenStreetMap contributors, © CARTO"
    )
    for alert in st.session_state.alerts:
        try:
            location = geolocator.geocode(alert["Ubicación"])
            if location:
                folium.Marker(
                    [location.latitude, location.longitude], 
                    popup=f"{alert['Tipo']}: {alert['Descripción']}",
                    icon=folium.Icon(color="purple", icon="info-sign")
                ).add_to(m)
        except:
            pass  # Ignorar ubicaciones no válidas
    return m


# Mostrar el mapa justo debajo del logo
st.image("img/alertasyavisos.png", width=150)
map_placeholder = st.empty()
map_placeholder.folium_static(generate_map())

# Crear dos columnas
col1, col2 = st.columns([1, 2])

# Formulario para añadir una nueva alerta en la primera columna
with col1:
    st.header("🚨 Nueva Alerta")
    with st.form("new_alert_form"):  # Fondo blanco
        st.markdown("""
            <style>
                div.stForm { 
                    background-color: white; 
                    padding: 15px; 
                    border-radius: 10px; 
                    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                }
            </style>
        """, unsafe_allow_html=True)
        description = st.text_area("Descripción de la alerta")
        alert_type = st.selectbox("Tipo de alerta", ["Emergencia", "Advertencia", "Información"])
        location = st.text_input("Ubicación (Ciudad, Dirección, etc.)")
        submitted = st.form_submit_button("Enviar Alerta")
        
        if submitted and description and alert_type and location:
            new_alert = {
                "Descripción": description,
                "Tipo": alert_type,
                "Ubicación": location,
                "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.alerts.append(new_alert)
            st.success("✅ Alerta enviada con éxito!")
            map_placeholder.folium_static(generate_map())  # Recargar el mapa automáticamente

# Mostrar alertas en forma de galería en la segunda columna
with col2:
    st.header("📌 Alertas Recientes")
    if st.session_state.alerts:
        st.markdown("""
            <style>
                div.alert-box {
                    background-color: white;
                    padding: 10px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                    margin-bottom: 10px;
                }
            </style>
        """, unsafe_allow_html=True)
        alerts_df = pd.DataFrame(st.session_state.alerts)
        for index, row in alerts_df.iterrows():
            with st.expander(f"🔔 {row['Tipo']} - {row['Ubicación']} ({row['Fecha']})"):
                st.markdown("""
                    <style>
                        details {
                            background-color: white;
                            padding: 10px;
                            border-radius: 10px;
                            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                            margin-bottom: 10px;
                        }
                    </style>
                """, unsafe_allow_html=True)
                st.write(f"**Descripción:** {row['Descripción']}")
    else:
        st.info("No hay alertas disponibles. Sé el primero en reportar una!")


with st.sidebar:

    usuario = st.session_state["usuario"]
    permisos = st.session_state["permisos"]


    import pandas as pd
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
    st.subheader("Servicios")
    st.page_link("pages/1_📍Mapa_Violeta.py", label="Mapa Violeta", icon=":material/home_pin:")
    st.page_link("pages/2_ Chat_Violeta.py", label="Chat Violeta", icon=":material/chat:")
    st.page_link("pages/3_⚠️ Alertas_Violeta.py", label="Alertas ", icon=":material/report:")
    if permisos == "administradora":
        st.page_link("pages/dashboard_alertas.py", label="Dashboard Alertas", icon=":material/bar_chart_4_bars:")

    # Botón para cerrar la sesión
    btnSalir=st.button("Salir")
    if btnSalir:
        st.session_state.clear()
        # Luego de borrar el Session State reiniciamos la app para mostrar la opción de usuario y clave
        st.rerun()
