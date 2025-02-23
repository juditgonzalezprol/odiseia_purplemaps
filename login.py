import streamlit as st
import pandas as pd

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
          
    with st.sidebar:

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
        st.page_link("pages/alerta_mensajeria.py", label="mensajeria", icon=":material/chat:")
        st.page_link("pages/3_⚠️ Alertas_Violeta.py", label="Alertas ", icon=":material/report:")
        if permisos == "administradora":
            st.page_link("pages/dashboard_alertas.py", label="Dashboard Alertas", icon=":material/bar_chart_4_bars:")
    
        st.session_state["usuario"] = usuario
        st.session_state["permisos"] = permisos  # Guardar permisos globalmen

        # Botón para cerrar la sesión
        btnSalir=st.button("Salir")
        if btnSalir:
            st.session_state.clear()
            # Luego de borrar el Session State reiniciamos la app para mostrar la opción de usuario y clave
            st.rerun()

def generarLogin():
    st.image("img/pulpleblanco.png", width=500)
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
                    background-color: #cb6ce6; /* Color lila claro */
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

                /* Campos de entrada */
                input[type="text"], input[type="password"] {
                    background-color: #f3e5f5;
                    border: 1px solid #6a1b9a;
                    color: #4a148c;
                    padding: 10px;
                    border-radius: 5px;
                    width: 100%;
                }

                /* Botón de ingreso */
                div[data-testid="stFormSubmitButton"] button {
                    background-color: #cb6ce6 !important;
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
                    background-color: #f3e5f5;
                    border: 2px solid #6a1b9a;  /* Borde violeta normal */
                    color: #4a148c;
                    padding: 10px;
                    border-radius: 5px;
                    width: 100%;
                    outline: none; /* Elimina el borde azul predeterminado */
                }

                /* Cambio de borde al seleccionar el campo */
                input[type="text"]:focus, input[type="password"]:focus {
                    border: 2px solid #cb6ce6 !important; /* Borde violeta claro al enfocar */
                    box-shadow: 0px 0px 8px #cb6ce6 !important; /* Efecto de brillo violeta */
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