import streamlit as st

# Configurar la página (debe ser la primera línea)
st.set_page_config(page_title="Home", page_icon="🟣", layout="wide")

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
            background-color: #f3e5f5; /* Lila claro */
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
        <img class="logo" src="https://i.imgur.com/Me7SdDV.png" alt="Logo" style="width: 500px;">
        <h1 class="title" style="color: #a9088e;">¡Bienvenida!</h1>
        <h3 class="title" style="color: #a9088e;">En esta plataforma puedes obtener información, ayuda y recursos sobre los Puntos Violetas</h1>
        <h3 class="title" style="color: #a9088e;">Encuentra los Puntos Violetas cercanos a ti y accede a asistencia especializada.</h1>
        <div class="info-box" style="background-color: #f3e5f5; padding: 20px; border-radius: 15px; width: 60%; font-size: 18px;">
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

# Agregar el logo arriba del menú en el sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-logo"><img src="https://i.imgur.com/UXR930j.png"></div>', unsafe_allow_html=True)


## https://i.imgur.com/Me7SdDV.png
## https://i.imgur.com/UXR930j.png