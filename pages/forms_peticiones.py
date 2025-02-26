import streamlit as st
import os
import csv
from datetime import datetime
import pandas as pd

# Inyectar CSS para usar Google Sans y texto en color blanco
st.markdown(
    """
    <style>
    * {
        font-family: 'Google Sans', sans-serif;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True
)

# Asegurarse de que exista la carpeta "peticiones"
if not os.path.exists("peticiones"):
    os.makedirs("peticiones")

csv_file_path = "peticiones/peticiones.csv"

# Si el CSV no existe, se crea y se escribe la cabecera
if not os.path.exists(csv_file_path):
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["timestamp", "nombre", "apellidos", "correo", "telefono", "experiencia"])

st.title("Petición para Atender un Punto Violeta")
st.write("Completa tus datos y describe tu experiencia relacionada con la gestión de puntos violeta o atención al ciudadano para enviar la petición al gobierno.")

# Creación del formulario
with st.form("form_peticion"):
    st.subheader("Datos Personales")
    nombre = st.text_input("Nombre")
    apellidos = st.text_input("Apellidos")
    correo = st.text_input("Correo Electrónico")
    telefono = st.text_input("Teléfono")
    
    st.subheader("Experiencia")
    experiencia = st.text_area("Experiencia relacionada con la gestión de puntos violeta o atención al ciudadano")
    
    submit_button = st.form_submit_button("Enviar Petición")

# Procesar la información del formulario al hacer clic en el botón de envío
if submit_button:
    if not (nombre and apellidos and correo and telefono and experiencia):
        st.error("⚠️ Por favor, completa todos los campos y describe tu experiencia.")
    else:
        # Generar un identificador único usando la fecha y hora actual
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Guardar los datos del formulario en el archivo CSV
        with open(csv_file_path, mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([timestamp_str, nombre, apellidos, correo, telefono, experiencia])
        
        st.success("¡Tu petición ha sido enviada y guardada correctamente!")

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
            st.page_link("pages/modelo_optimizacion.py", label="Algoritmo Optimización", icon=":material/modeling:")

        st.session_state["usuario"] = usuario
        st.session_state["permisos"] = permisos  # Guardar permisos globalmen

        # Botón para cerrar la sesión
        btnSalir=st.button("Salir")
        if btnSalir:
            st.session_state.clear()
            # Luego de borrar el Session State reiniciamos la app para mostrar la opción de usuario y clave
            st.rerun()