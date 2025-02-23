import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_autorefresh import st_autorefresh  # Para auto-recarga

# Configuración de la aplicación
st.set_page_config(
    page_title="Dashboard de Alertas",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Auto-recarga cada 2 segundos
st_autorefresh(interval=2000, key="data_refresh")

# Estilos personalizados
st.markdown(
    """
    <style>
        .stApp { background-color: white; }
        .st-emotion-cache-janbn0 { background-color: #f3e5f5 !important; }
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

# Carga de datos desde un archivo local **sin caché**
def cargar_datos():
    return pd.read_csv('alertas.csv', parse_dates=['hora_envio'])

df_alertas = cargar_datos()

# Creación de columnas para dividir la pantalla
c1, c2 = st.columns([1.4, 1], gap= "large")  # Ajuste para hacer el mapa más grande y la tabla más pequeña

# 📍 **Mapa interactivo con fondo blanco y zoom más alejado**
with c1:
    st.subheader("📍 Ubicación de Alertas")

    fig_mapa = px.scatter_mapbox(
        df_alertas,
        lat="latitude",
        lon="longitude",
        hover_name="tipo",
        hover_data=["descripción", "status", "hora_envio"],
        color_discrete_sequence=["#6a1b9a"],
        size_max=10,
        zoom=9,  # Zoom más alejado
        height=600,
        width=200  # Tamaño más grande
    )

    fig_mapa.update_layout(
        mapbox_style="carto-positron",  # Fondo blanco minimalista
        margin=dict(l=0, r=0, t=0, b=0)
    )

    st.plotly_chart(fig_mapa, use_container_width=True)

# 📊 **Tabla de alertas con filtro y tamaño reducido**
with c2:
    
    df_alertas['hora'] = df_alertas['hora_envio'].dt.hour
    df_alertas_hora = df_alertas.groupby('hora').size().reset_index(name='cantidad')

    # Gráfico de alertas por hora con fondo blanco y borde violeta
    fig_alertas_hora = px.line(
        df_alertas_hora,
        x='hora',
        y='cantidad',
        markers=True,
        title="Alertas por Hora",
        color_discrete_sequence=['#6a1b9a']
    )

    fig_alertas_hora.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#6a1b9a"),
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="lightgray")
    )

    # Mostrar gráfico con estilo **SIN caché**
    with st.container():
        st.markdown('<div class="stPlotlyChart">', unsafe_allow_html=True)
        st.plotly_chart(fig_alertas_hora, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)




df_alertas = pd.DataFrame(df_alertas)

# 🔥 Función para cambiar el color del texto a violeta
def color_violet_text(col):
    return ['color: #6a1b9a; font-weight: bold' for _ in col]

# 🔥 Función para el fondo blanco
def background_white(col):
    return ['background-color: white' for _ in col]

# 🔥 Función para hover: fondo violeta y letras blancas
def hover_effect(col):
    return ['background-color: #6a1b9a; color: white' for _ in col]

# 🔥 Estilos para los encabezados
header_styles = [
    {'selector': 'th', 'props': [('background-color', 'white'), ('color', 'black'), ('font-weight', 'bold')]}
]

# Aplicamos estilos con `pandas Styler`
styled_df = (df_alertas.style
            .apply(background_white, subset=df_alertas.columns)  # Fondo blanco
            .apply(color_violet_text, subset=df_alertas.columns)  # Texto violeta
            .set_table_styles(header_styles)  # Estilos de encabezado
            )

# st.table(styled_df)
st.image("img/alertas_en_tiempo_real.png", width=500)
st.dataframe(styled_df)

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