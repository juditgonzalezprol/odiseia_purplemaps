import streamlit as st
import pandas as pd

def validarUsuario(usuario, clave):    
    """Permite la validación de usuario y clave

    Args:
        usuario (str): Usuario a validar
        clave (str): Clave del usuario

    Returns:
        bool: True si el usuario es válido, False si no
    """    
    try:
        dfusuarios = pd.read_csv('usuarios.csv', dtype={'clave': str})
        dfusuarios = dfusuarios.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    except FileNotFoundError:
        st.error("⚠️ Error: Archivo 'usuarios.csv' no encontrado")
        return False

    # Validación de usuario y clave
    if not dfusuarios.empty and ((dfusuarios['usuario'] == usuario) & (dfusuarios['clave'] == clave)).any():
        return True
    else:
        return False

def generarMenu():
    """Genera el menú dependiendo del usuario autenticado"""
    
    # Verifica si la sesión está activa
    if 'usuario' not in st.session_state:
        st.warning("⚠️ No has iniciado sesión. Redirigiendo al login...")
        st.stop()
    
    usuario = st.session_state['usuario']
    
    # Cargar la base de datos de usuarios
    dfusuarios = pd.read_csv('usuarios.csv')
    dfUsuario = dfusuarios[dfusuarios['usuario'] == usuario]

    if dfUsuario.empty:
        nombre = "Invitada"
        permisos = "Usuaria"
    else:
        nombre = dfUsuario.iloc[0]["nombre"]
        permisos = dfUsuario.iloc[0]["permisos"]

    # SIDEBAR
    with st.sidebar:
        st.image("img/Purple_Maps.png", width=100)
        st.write(f"Hola **:blue-background[{nombre}]** ")
        st.subheader("Funcionalidades")
        st.page_link("pages/1_📍Mapa_Violeta.py", label="Mapa Violeta", icon=":material/home_pin:")
        st.page_link("pages/2_ Chat_Violeta.py", label="Chat Violeta", icon=":material/chat:")
        st.page_link("pages/3_⚠️ Alertas_Violeta.py", label="Alertas", icon=":material/report:")

        if permisos == "administradora":
            st.subheader("Gestión y administración")
            st.page_link("pages/dashboard_alertas.py", label="Dashboard Alertas", icon=":material/bar_chart_4_bars:")

        # Botón para cerrar sesión
        if st.button("Salir"):
            st.session_state.clear()
            st.rerun()

def generarLogin():
    st.markdown(
        """
        <style>
            * {
                font-family: 'Google Sans', sans-serif;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Centrar imagen de logo
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("img/purple_blanco_PNG.png", width=500)

    # Si ya hay usuario en sesión, mostramos el menú
    if 'usuario' in st.session_state:
        generarMenu()
    else: 
        st.markdown(
            """
            <style>
                /* Fondo general */
                .stApp {
                    background-color: #c39bd8;
                }
                /* Estilo del formulario */
                div[data-testid="stForm"] {
                    background-color: #ffffff;
                    padding: 30px;
                    border-radius: 15px;
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
                    width: 400px;
                    margin: auto;
                    text-align: center;
                }
                /* Botón de ingreso */
                div[data-testid="stFormSubmitButton"] button {
                    background-color: #c39bd8 !important;
                    color: white !important;
                    border-radius: 8px !important;
                    padding: 10px !important;
                    width: 100% !important;
                    border: none !important;
                }
                /* Mensajes de error */
                div[data-testid="stAlert"] {
                    background-color: #ffebee;
                    color: #b71c1c;
                    border-radius: 8px;
                    padding: 10px;
                }
                /* Campos de entrada */
                input[type="text"], input[type="password"] {
                    background-color: #c39bd8;
                    border: 2px solid #6a1b9a;
                    color: white !important;
                    padding: 10px;
                    border-radius: 5px;
                    width: 100%;
                    outline: none;
                }
                /* Cambio de borde al enfocar */
                input[type="text"]:focus, input[type="password"]:focus {
                    border: 2px solid #db84fa !important;
                    box-shadow: 0px 0px 8px #db84fa !important;
                    outline: none !important;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        with st.form('frmLogin'):
            parUsuario = st.text_input('Usuaria')
            parPassword = st.text_input('Contraseña', type='password')
            btnLogin = st.form_submit_button('Entrar', type='primary')
            if btnLogin:
                if validarUsuario(parUsuario, parPassword):
                    st.session_state['usuario'] = parUsuario
                    st.rerun()
                else:
                    st.error("Usuario o clave inválidos", icon=":material/gpp_maybe:")

        st.markdown(
            """
            <style>
                .registro-container {
                    display: flex;
                    width: 200px;
                    margin: auto;
                }
                .registro-btn {
                    background-color: #c39bd8 !important;
                    color: white !important;
                    border: 2px solid white !important;
                    border-radius: 8px !important;
                    padding: 10px !important;
                    width: 30% !important;
                    font-size: 14px !important;
                    font-weight: bold !important;
                    text-align: center !important;
                    cursor: pointer !important;
                    transition: 0.3s !important;
                }
                .registro-btn:hover {
                    background-color: #a26bcf !important;
                    border-color: #ffffff !important;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Botones de registro en fila
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🆔 DNI-Electrónico", key="dni", help="Registrarse con DNI-Electrónico"):
                st.success("Registro con DNI-Electrónico seleccionado")
        with col2:
            if st.button("🔑 Clave365", key="clave365", help="Registrarse con Clave365"):
                st.success("Registro con Clave365 seleccionado")
        with col3:
            if st.button("📄 Otro Método", key="otro", help="Registrarse con otro método"):
                st.success("Registro con otro método seleccionado")

if __name__ == "__main__":
    generarLogin()
