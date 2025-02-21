# Función para mostrar un mapa con posibles ubicaciones de Puntos Violetas
# Función de login para acceder a la administración
import folium
import streamlit as st

# ❗ `set_page_config()` debe ser lo primero en el script
st.set_page_config(page_title="LogIn Admin", page_icon="🟣", layout="wide")

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

        .st-emotion-cache-janbn0 {
            background-color: #f3e5f5 !important;
        }

    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔐 Acceso Administrativo")

username = st.text_input("👤 Usuario", key="username")
password = st.text_input("🔑 Contraseña", type="password", key="password")

# Credenciales predefinidas (se pueden modificar o almacenar en variables seguras)
if st.button("Iniciar sesión"):
    if username == "admin" and password == "1234":
        st.session_state["authenticated"] = True
        st.success("✅ Inicio de sesión exitoso. Accediendo al panel administrativo...")
    else:
        st.error("❌ Usuario o contraseña incorrectos")

