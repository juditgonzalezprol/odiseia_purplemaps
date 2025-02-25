import streamlit as st
import os
import csv
from datetime import datetime

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
