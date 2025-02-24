import streamlit as st
import pandas as pd
import os

# Validación simple de usuario y clave con un archivo csv


def validarUsuario(usuario, clave):    
    """Permite la validación de usuario y clave
    
    Args:
        usuario (str): Usuario a validar
        clave (str): Clave del usuario
    
    Returns:
        bool: True si el usuario es válido, False si no
    """    
    try:
        dfusuarios = pd.read_csv('usuarios.csv', dtype={'clave': str})  # Forzar claves como texto
        dfusuarios = dfusuarios.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  # Quitar espacios
    except FileNotFoundError:
        st.error("⚠️ Error: Archivo 'usuarios.csv' no encontrado")
        return False
    
    # 📌 Validación de usuario y clave
    if not dfusuarios.empty and ((dfusuarios['usuario'] == usuario) & (dfusuarios['clave'] == clave)).any():
        return True
    else:
        return False

def generarMenu(usuario):
    
    """Genera el menú dependiendo del usuario

    Args:
        usuario (str): usuario utilizado para generar el menú
    """

    # 📌 Archivo donde se guarda la sesión del usuario
    SESSION_FILE = "session.txt"

    # 🔄 **Al iniciar la app, cargar la sesión**
    def cargar_sesion():
        if os.path.exists(SESSION_FILE):
            with open(SESSION_FILE, "r") as f:
                lines = f.readlines()
                if len(lines) >= 2:
                    return lines[0].strip(), lines[1].strip()  # Retorna usuario y permisos
        return None, None  # Si no hay sesión, retorna None

    # 📝 **Función para guardar el usuario en archivo**
    def guardar_sesion(usuario, permisos):
        with open(SESSION_FILE, "w") as f:
            f.write(f"{usuario}\n{permisos}")

    # 📂 **Función para eliminar la sesión**
    def eliminar_sesion():
        if os.path.exists(SESSION_FILE):
            os.remove(SESSION_FILE)

    # 📌 **Intentar cargar la sesión al inicio**
    usuario, permisos = cargar_sesion()

    # **Si el usuario no está autenticado, detener la ejecución**
    if usuario is None:
        st.warning("⚠️ No has iniciado sesión. Redirigiendo al login...")
        st.stop()

    # 🔍 **Cargar la base de datos de usuarios**
    dfusuarios = pd.read_csv('usuarios.csv')
    dfUsuario = dfusuarios[dfusuarios['usuario'] == usuario]

    if dfUsuario.empty:
        nombre = "Invitada"
        permisos = "Usuaria"
    else:
        nombre = dfUsuario.iloc[0]["nombre"]
        permisos = dfUsuario.iloc[0]["permisos"]

    # 🔹 **SIDEBAR**
    with st.sidebar:
        st.image("img/Purple_Maps.png", width=100)
        st.write(f"Hola **:blue-background[{nombre}]** ")

        st.subheader("Funcionalidades")
        st.page_link("pages/1_📍Mapa_Violeta.py", label="Mapa Violeta", icon=":material/home_pin:")
        st.page_link("pages/2_ Chat_Violeta.py", label="Chat Violeta", icon=":material/chat:")
        st.page_link("pages/3_⚠️ Alertas_Violeta.py", label="Alertas ", icon=":material/report:")

        if permisos == "administradora":
            st.subheader("Gestión y administración")
            st.page_link("pages/dashboard_alertas.py", label="Dashboard Alertas", icon=":material/bar_chart_4_bars:")

        # 🔴 **Botón para cerrar sesión**
        if st.button("Salir"):
            eliminar_sesion()  # Borra sesión
            st.rerun()


    # with st.sidebar:

    #     import pandas as pd
    #     st.image("img/Purple_Maps.png", width=100)
    #     # Cargamos la tabla de usuarios
    #     dfusuarios = pd.read_csv('usuarios.csv')
    #     # Filtramos la tabla de usuarios
    #     dfUsuario =dfusuarios[(dfusuarios['usuario']==usuario)]
    #     # Cargamos el nombre del usuario
    #     nombre= dfUsuario['nombre'].values[0]
    #     permisos= dfUsuario['permisos'].values[0]
    #     #Mostramos el nombre del usuario
    #     st.write(f"Hola **:blue-background[{nombre}]** ")
    #     # Mostramos los enlaces de páginas
    #     st.subheader("Funcionalidades")
    #     st.page_link("pages/1_📍Mapa_Violeta.py", label="Mapa Violeta", icon=":material/home_pin:")
    #     st.page_link("pages/2_ Chat_Violeta.py", label="Chat Violeta", icon=":material/chat:")
    #     st.page_link("pages/3_⚠️ Alertas_Violeta.py", label="Alertas ", icon=":material/report:")
    #     if permisos == "administradora":
    #         st.subheader("Gestión y administración")
    #         st.page_link("pages/dashboard_alertas.py", label="Dashboard Alertas", icon=":material/bar_chart_4_bars:")
    
    #     st.session_state["usuario"] = usuario
    #     st.session_state["permisos"] = permisos  # Guardar permisos globalmen

    #     # Botón para cerrar la sesión
    #     btnSalir=st.button("Salir")
    #     if btnSalir:
    #         st.session_state.clear()
    #         # Luego de borrar el Session State reiniciamos la app para mostrar la opción de usuario y clave
    #         st.rerun()

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

    col1, col2, col3 = st.columns([1, 2, 1])  # Columnas para centrar la imagen
    with col2:  # Columna central
        st.image("img/purple_blanco_PNG.png", width=500)

    """Genera la ventana de login o muestra el menú si el login es valido
    """    
    # Validamos si el usuario ya fue ingresado    
    if 'usuario' in st.session_state:
        generarMenu(st.session_state['usuario']) # Si ya hay usuario cargamos el menu        
    else: 
        # Aplicar estilos personalizados con CSS
        st.markdown(
            """
            <style>
                /* Fondo general de la aplicación */
                .stApp {
                    background-color: #c39bd8; /* Color lila claro */
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

                /* Campos de entrada (usuario y contraseña) */
                input[type="text"], input[type="password"] {
                    background-color: #c39bd8;
                    border: 2px solid #6a1b9a;  /* Borde violeta normal */
                    color: white !important;  /* 🔹 Texto en blanco */
                    padding: 10px;
                    border-radius: 5px;
                    width: 100%;
                    outline: none; /* Elimina el borde azul predeterminado */
                }


                /* Cambio de borde al seleccionar el campo */
                input[type="text"]:focus, input[type="password"]:focus {
                    border: 2px solid #db84fa !important; /* Borde violeta claro al enfocar */
                    box-shadow: 0px 0px 8px #db84fa !important; /* Efecto de brillo violeta */
                    outline: none !important;
                }

            </style>
            """,
            unsafe_allow_html=True
        )

        with st.form('frmLogin'):
            parUsuario = st.text_input('Usuaria')
            parPassword = st.text_input('Contraseña',type='password')
            btnLogin=st.form_submit_button('Entrar',type='primary')
            if btnLogin:
                if validarUsuario(parUsuario,parPassword):
                    st.session_state['usuario'] =parUsuario
                    st.rerun()
                else:
                    st.error("Usuario o clave inválidos",icon=":material/gpp_maybe:")      

        # Crear columnas para alinear los botones en fila
        # Aplicar estilos personalizados con CSS para los botones
        st.markdown(
            """
            <style>
                /* Contenedor de los botones de registro */
                .registro-container {
                    display: flex;
                    width: 200px;  /* Mismo ancho que el formulario */
                    margin: auto;
                }

                /* Estilos generales para los botones */
                .registro-btn {
                    background-color: #c39bd8 !important;
                    color: white !important;
                    border: 2px solid white !important;
                    border-radius: 8px !important;
                    padding: 10px !important;
                    width: 30% !important; /* Distribuir los botones equitativamente */
                    font-size: 14px !important;
                    font-weight: bold !important;
                    text-align: center !important;
                    cursor: pointer !important;
                    transition: 0.3s !important;
                }

                /* Hover: Fondo violeta más oscuro */
                .registro-btn:hover {
                    background-color: #a26bcf !important;
                    border-color: #ffffff !important;
                }

            </style>
            """,
            unsafe_allow_html=True
        )

        # Crear un contenedor para alinear los botones en fila
        col1, col2, col3 = st.columns(3)

        # Botón 1: Registrarse con DNI-Electrónico
        with col1:
            if st.button("🆔 DNI-Electrónico", key="dni", help="Registrarse con DNI-Electrónico"):
                st.success("Registro con DNI-Electrónico seleccionado")

        # Botón 2: Registrarse con Clave365
        with col2:
            if st.button("🔑 Clave365", key="clave365", help="Registrarse con Clave365"):
                st.success("Registro con Clave365 seleccionado")

        # Botón 3: Registrarse con otro método
        with col3:
            if st.button("📄 Otro Método", key="otro", help="Registrarse con otro método"):
                st.success("Registro con otro método seleccionado")

              