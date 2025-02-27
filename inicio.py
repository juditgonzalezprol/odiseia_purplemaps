import streamlit as st
import login
import pandas as pd
from groq import Groq 

login.generarLogin()

if 'usuario' in st.session_state:

    permisos = st.session_state["permisos"]

    if permisos == "usuaria":

        # Aplicar estilos CSS para centrar contenido y personalizar la página
        st.markdown(
            """
            <style>
                /* Fondo blanco */
                .stApp {
                    background-color: white;
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
                    background-color: black !important;
                }
                
                /* Cambiar el color del texto en el sidebar a blanco */
                [data-testid="stSidebar"] * {
                    color: #c39bd8 !important;
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

            <div class="container">
                <h1 class="title" style="color: #a9088e;">¡Bienvenida!</h1>
                <h3 class="title" style="color: #a9088e;">En esta plataforma puedes obtener información, ayuda y recursos sobre los Puntos Violetas</h1>
                <h3 class="title" style="color: #a9088e;">Encuentra los Puntos Violetas cercanos a ti y accede a asistencia especializada.</h1>
                <div class="info-box" style="background-color: #db84fa; padding: 20px; border-radius: 15px; width: 60%; font-size: 18px;">
                    <p>📞 <strong>Teléfono de Atención a Víctimas de Violencia de Género: 016</strong></p>
                    <p>🚨 <strong>Emergencias: 112</strong></p>
                    <p>👮‍♀️ <strong>Policía Nacional:</strong> 091</p>
                    <p>🛡️ <strong>Guardia Civil:</strong> 062</p>
                    <p>✉️ <strong>Email de atención:</strong> <a href="mailto:016-online@igualdad.gob.es">016-online@igualdad.gob.es</a></p>
                    <p>📍 <strong>App ALERTCOPS:</strong> Envío de alertas con geolocalización a las fuerzas de seguridad.</p>
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    if permisos == "administradora":

        # Configurar la API de Groq
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])

        # Inicializar estado de sesión
        if "groq_model" not in st.session_state:
            st.session_state["groq_model"] = "llama3-70b-8192"

        if "alert_summary" not in st.session_state:
            st.session_state["alert_summary"] = "Aún no se ha generado el resumen."

        # 📌 Cargar el CSV de alertas
        @st.cache_data
        def load_alerts():
            try:
                df = pd.read_csv("alertas.csv")
                return df
            except FileNotFoundError:
                st.error("⚠️ No se encontró el archivo 'alertas.csv'. Asegúrate de que el archivo existe.")
                return pd.DataFrame()

        # Generar resumen de alertas con la API de Groq
        def generate_alert_summary(df):
            if df.empty:
                return "No hay alertas disponibles para analizar."

            # Formatear los datos del CSV para enviarlos a la API
            alert_text = df.to_string()

            # 📌 Prompt para la IA
            prompt = f"""
            Analiza la siguiente lista de alertas y genera un resumen indicando:
            - Los **lugares más críticos** que requieren atención inmediata.
            - Qué tipos de alertas son más frecuentes.
            - Si hay algún **patrón o tendencia** en la ubicación y tipo de alerta.
            - Recomendaciones para la respuesta a emergencias.

            Lista de alertas:
            {alert_text}

            Genera el resumen en un formato claro y fácil de leer.
            """

            # Llamar a la API de Groq
            response = client.chat.completions.create(
                model=st.session_state["groq_model"],
                messages=[{"role": "system", "content": prompt}]
            )

            return response.choices[0].message.content

        st.image("img/resumen_alertas.png", width=500)
        # Botón para generar el resumen
        # Agregar estilos personalizados
        st.markdown("""
            <style>
                /* Estilo personalizado para el botón */
                div.stButton > button {
                    background-color: white !important;  /* Fondo blanco */
                    color: #a9088e !important;  /* Letras en violeta */
                    border: 2px solid #a9088e !important;  /* Borde violeta */
                    border-radius: 8px !important;
                    padding: 10px 15px !important;
                    font-size: 16px !important;
                    font-weight: bold !important;
                    transition: all 0.3s ease-in-out !important;
                    cursor: pointer !important;
                }

                /* Hover: Cambia a fondo violeta y letras blancas */
                div.stButton > button:hover {
                    background-color: #a9088e !important;
                    color: white !important;
                }
            </style>
        """, unsafe_allow_html=True)

        # Botón con estilo modificado
        if st.button("🔍 Analizar Alertas"):
            df_alerts = load_alerts()
            if not df_alerts.empty:
                summary = generate_alert_summary(df_alerts)
                st.session_state["alert_summary"] = summary


        # 📌 Mostrar el resumen en un recuadro
        st.markdown(f"""
            <div style="background-color: #f9f9f9; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
                <p style="color: #a9088e; font-weight: bold;">{st.session_state['alert_summary']}</p>
            </div>
        """, unsafe_allow_html=True)
        
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
            st.page_link("pages/analisis_eventos.py", label="Analisis de eventos", icon=":material/modeling:")

        st.session_state["usuario"] = usuario
        st.session_state["permisos"] = permisos  # Guardar permisos globalmen

        # Botón para cerrar la sesión
        btnSalir=st.button("🔙")
        if btnSalir:
            st.session_state.clear()
            # Luego de borrar el Session State reiniciamos la app para mostrar la opción de usuario y clave
            st.rerun()