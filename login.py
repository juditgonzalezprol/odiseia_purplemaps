import streamlit as st
import pandas as pd

def validarUsuario(usuario, clave):
    try:
        dfusuarios = pd.read_csv('usuarios.csv', dtype={'clave': str})
        dfusuarios = dfusuarios.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    except FileNotFoundError:
        st.error("⚠️ Error: Archivo 'usuarios.csv' no encontrado")
        return False

    if not dfusuarios.empty and ((dfusuarios['usuario'] == usuario) & (dfusuarios['clave'] == clave)).any():
        return True
    else:
        return False

def generarLogin():
    st.markdown(
        """
        <style>
            * { font-family: 'Google Sans', sans-serif; }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("img/purple_blanco_PNG.png", width=500)

    # Si ya hay usuario en sesión, mostramos el menú (o lo que corresponda)
    if 'usuario' in st.session_state:
        # Aquí llamas a la función que genera el menú, por ejemplo: generarMenu()
        pass
    else:
        st.markdown(
            """
            <style>
                /* Estilos para el formulario */
                div[data-testid="stForm"] {
                    background-color: #ffffff;
                    padding: 30px;
                    border-radius: 15px;
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
                    width: 400px;
                    margin: auto;
                    text-align: center;
                }
                /* Otros estilos... */
            </style>
            """,
            unsafe_allow_html=True
        )

        # Bloque de formulario para el login
        with st.form('frmLogin'):
            parUsuario = st.text_input('Usuaria')
            parPassword = st.text_input('Contraseña', type='password')
            btnLogin = st.form_submit_button('Entrar', type='primary')
            if btnLogin:
                if validarUsuario(parUsuario, parPassword):
                    st.session_state['usuario'] = parUsuario

                    # Asignar permisos (ejemplo, extraerlos del CSV)
                    try:
                        dfusuarios = pd.read_csv('usuarios.csv')
                        dfUsuario = dfusuarios[dfusuarios['usuario'] == parUsuario]
                        if not dfUsuario.empty:
                            st.session_state['permisos'] = dfUsuario.iloc[0]['permisos']
                        else:
                            st.session_state['permisos'] = "usuaria"
                    except FileNotFoundError:
                        st.error("⚠️ Error: Archivo 'usuarios.csv' no encontrado")
                        st.stop()

                    st.rerun()
                else:
                    st.error("Usuario o clave inválidos", icon=":material/gpp_maybe:")

if __name__ == "__main__":
    generarLogin()
