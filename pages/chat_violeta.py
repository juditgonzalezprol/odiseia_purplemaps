
import streamlit as st
from groq import Groq
import pandas as pd


st.set_page_config(page_title="Chat", page_icon="🟣", layout="wide")


# Configuración del cliente Groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

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
            background-color: #f3e5f5; /* Lila claro */
            padding: 20px;
            border-radius: 15px;
            width: 60%;
            font-size: 18px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }

        .st-emotion-cache-janbn0 {
            background-color: #f3e5f5 !important;
        }

    </style>
    """,
    unsafe_allow_html=True
)

# st.html(
# """
#     <style>
#     .clickable {
#         color: rgb(46, 154, 255);
#         text-decoration: underline;
#     }
    
#     div[data-testid="stChatMessageContent"] {
#         background-color: #cb6ce6;
#         color: white; # Expander content color
#     } 
    
#     div[data-testid="stChatMessage"] {
#         background-color: #cb6ce6;
#         color: white; # Adjust this for expander header color
#     }
#     </style>
# """)



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


# Inicializar estado de la sesión
def init_session_state():
    if "groq_model" not in st.session_state:
        st.session_state["groq_model"] = "llama3-70b-8192"
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "file_content" not in st.session_state:
        st.session_state.file_content = ""
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

info_añadida = """    Guía de Actuación ante la Violencia Machista
                    ¿QUÉ HACER SI ERES TESTIGO DE UNA AGRESIÓN?
                    1. Si la víctima corre peligro inminente:
                    - Llama de inmediato al 112 (Emergencias), 091 (Policía Nacional) o 062 (Guardia Civil).
                    - Usa la app ALERTCOPS para enviar una alerta con tu ubicación.
                    - No te pongas en riesgo, espera a los servicios de emergencia.

                    2. Si la situación no es de riesgo extremo:
                    - Llama a la policía o emergencias.
                    - Graba la situación con tu móvil para aportar pruebas, pero no la compartas en redes sociales.
                    - Si estás en un lugar público, pide ayuda a otras personas y avisen al personal del establecimiento.
                    - Colabora con la policía si llegan al lugar, proporcionando información y pruebas.

                    3. Si la víctima no quiere denunciar:
                    - La denuncia es una decisión personal, pero en casos de violencia de género (pareja/expareja), cualquier persona puede denunciar.

                    ¿QUÉ HACER SI CONOCES A UNA VÍCTIMA?
                    1. Si su vida está en peligro:
                    - Llama al 112, 091 o 062.
                    - Tu llamada es anónima.
                    - Puedes involucrar a vecinos o personas cercanas para brindar apoyo.

                    2. Si la situación no es de riesgo inmediato:
                    - Habla con la víctima en un momento seguro, sin la presencia del agresor.
                    - Escucha sin juzgar y hazle saber que no está sola.
                    - Infórmale sobre los recursos disponibles:
                        - 016 (24h, gratuito y no deja rastro en la factura)
                        - 600 000 016 (WhatsApp)
                        - 016-online@igualdad.gob.es
                    - Si la víctima no quiere actuar, sigue apoyándola y facilitándole información.

                    ¿QUÉ HACER SI TÚ ERES LA VÍCTIMA?
                    1. Si estás en peligro:
                    - Llama al 112, 091 o 062.
                    - Usa la app ALERTCOPS para pedir ayuda.
                    - Acude a una farmacia o Punto Violeta donde pueden ayudarte.

                    2. Si vives con tu agresor:
                    - Infórmate llamando al 016 o contactando por WhatsApp o email.
                    - Hay casas de acogida y centros de emergencia si necesitas salir de tu hogar.

                    3. Si decides romper con la violencia:
                    - Contacta con asociaciones, servicios sociales o profesionales especializados (psicólogas, abogadas, trabajadoras sociales).

                    ¿QUÉ HACER ANTE UNA AGRESIÓN SEXUAL?
                    1. Si acabas de sufrir una agresión:
                    - Acude a un hospital sin lavarte ni cambiarte de ropa para preservar pruebas.
                    - Tienes derecho a asistencia médica, psicológica y jurídica.
                    - Si decides denunciar, informa al personal sanitario.

                    2. Si alguien te cuenta que ha sido agredida:
                    - Escucha con calma y sin juzgar.
                    - Infórmale sobre sus derechos y recursos disponibles (016, hospitales, policía).
                    - No la presiones a denunciar, respeta su decisión.

                    RECURSOS DE AYUDA DISPONIBLES
                    - Emergencias: 112, 091 (Policía), 062 (Guardia Civil).
                    - Información y asesoramiento: 016 (teléfono, WhatsApp y email).
                    - Refugios y casas de acogida: Llama al 016 para más información.
                    - Atención psicológica y jurídica gratuita: Servicios disponibles en cada comunidad autónoma.
                    - Protección a víctimas: Servicio ATENPRO (900 222 292).
                    - Espacios seguros para mascotas: 673 765 330.

                    ¿QUÉ ES UN PUNTO VIOLETA?
                    Un Punto Violeta es un lugar seguro donde las víctimas pueden recibir ayuda e información sobre recursos de apoyo. Se identifican con un distintivo violeta en la puerta.

                    RESUMEN DE CONTACTO RÁPIDO
                    - Emergencias: 112
                    - Asesoramiento: 016 (teléfono, WhatsApp, email)
                    - Refugios y casas de acogida: 016
                    - Atención psicológica y jurídica: 016 o servicios autonómicos
                    - Refugio para mascotas: 673 765 330"""


# st.markdown('<div><h1 class="Chat Punto Violeta" style="color: white;">Chat Violeta</h1></div>', unsafe_allow_html=True)


st.image("img/chatvioleta.png", width=500)
# cols = st.columns([4, 1])
# with cols[0]:
#     st.image("img/chatvioleta.png", width=500)
# with cols[1]:
#     # Convertir los mensajes del chat a un CSV; si no hay mensajes, se genera un CSV con encabezados
#     if st.session_state.messages:
#         df_chat = pd.DataFrame(st.session_state.messages)
#         csv_data = df_chat.to_csv(index=False).encode('utf-8')
#     else:
#         csv_data = "role,content\n".encode("utf-8")
#     st.download_button(
#         label="Guardar Chat",
#         data=csv_data,
#         file_name="chat.csv",
#         mime="text/csv"
#     )

# 🔹 Inicializar variables en `st.session_state`
if "groq_model" not in st.session_state:
    st.session_state["groq_model"] = "llama3-70b-8192"  # Ajusta según el modelo de IA que uses

if "messages" not in st.session_state:
    st.session_state.messages = []

# Ahora puedes acceder a `st.session_state["groq_model"]` sin errores
model = st.session_state["groq_model"]

# Ejemplo de uso en una llamada a la API
st.write(f"Usando el modelo: {model}. Recuerda que esto es un chat generado por inteligencia artificial.")

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada del usuario
if prompt := st.chat_input("💬 ¿Qué quieres preguntar?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("human"):
        st.markdown(prompt)

    # Definir instrucciones estrictas para la IA
    system_message = {
        "role": "system",
        "content": """Eres un asistente de un Punto Violeta, especializado en apoyo contra la violencia machista, agresiones sexuales y acoso.
    
            Solo puedes responder preguntas relacionadas con estos temas o basadas en la información proporcionada. 
            Si la pregunta del usuario no tiene relación con estos temas, responde con: 'No puedo responder esa pregunta'. 

            Sé serio pero ayuda, no exclames nada, usa emojis para hacer la información más clara. 
            Si la persona necesita encontrar un Punto Violeta, dirígela a la pestaña de ubicación.

            Usa toda esta información: {info_añadida}"""}
    

    with st.chat_message("ai"):
        response = client.chat.completions.create(
            model=st.session_state["groq_model"],
            messages=[system_message] + [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
        )
        response_text = response.choices[0].message.content

        # Mostrar advertencia si la pregunta no es válida
        if "No puedo responder esa pregunta" in response_text:
            st.warning("⚠️ Tu pregunta no está relacionada con el documento ni con violencia machista. Reformúlala.")
        else:
            st.markdown(response_text)

    st.session_state.messages.append({"role": "assistant", "content": response_text})
