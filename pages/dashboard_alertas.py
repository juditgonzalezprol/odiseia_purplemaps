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

def cargar_datos():
    return pd.read_csv('alertas.csv', parse_dates=['hora_envio'])

df_alertas = cargar_datos()

c1, c2 = st.columns([1.4, 1], gap= "large")  

with c1:
    st.image("img/alertasyavisos.png", width=300)

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
        mapbox_style="carto-positron",
        margin=dict(l=0, r=0, t=0, b=0)
    )

    st.plotly_chart(fig_mapa, use_container_width=True)

with c2:
    
    df_alertas['hora'] = df_alertas['hora_envio'].dt.hour
    df_alertas_hora = df_alertas.groupby('hora').size().reset_index(name='cantidad')

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

    with st.container():
        st.image("img/alertas_por_hora.png", width=300)
        st.plotly_chart(fig_alertas_hora, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)


df_alertas = pd.DataFrame(df_alertas)

def color_violet_text(col):
    return ['color: #6a1b9a; font-weight: bold' for _ in col]

def background_white(col):
    return ['background-color: white' for _ in col]

def hover_effect(col):
    return ['background-color: #6a1b9a; color: white' for _ in col]

header_styles = [
    {'selector': 'th', 'props': [('background-color', 'white'), ('color', 'black'), ('font-weight', 'bold')]}
]

styled_df = (df_alertas.style
            .apply(background_white, subset=df_alertas.columns)  # Fondo blanco
            .apply(color_violet_text, subset=df_alertas.columns)  # Texto violeta
            .set_table_styles(header_styles)  # Estilos de encabezado
            )

st.image("img/alertas_en_tiempo_real.png", width=500)
st.dataframe(styled_df)

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