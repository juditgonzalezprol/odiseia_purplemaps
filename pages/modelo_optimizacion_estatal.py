import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
from sklearn.preprocessing import MinMaxScaler
import joblib
from io import StringIO
import json
import requests

# Estilos personalizados
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
        .stApp { background-color: white; }
        .st-emotion-cache-janbn0 { background-color: #db84fa !important; }
        [data-testid="stSidebar"] { background-color: #222 !important; }
        [data-testid="stSidebar"] * { color: white !important; }

        /* 🔥 Corrección del borde de los gráficos */
        .stPlotlyChart, .stMap {
            background-color: white;
            border: 2px solid #6a1b9a;
            border-radius: 30px;
            padding: 10px; /* Se cambia de -4px a 10px */
            overflow: hidden; /* Evita que la imagen sobresalga */
            margin-bottom: 20px; /* Espaciado para evitar que se encime */
        }

        /* 🔥 Corrección del mapa */
        .stMap {
            height: 500px; /* Ajusta la altura */
            width: 100%; /* Evita que sobresalga */
        }

        /* Estilo del encabezado */
        h2, h3, h4 {
            color: #6a1b9a;
        }

    </style>
    """,
    unsafe_allow_html=True
)
# 📌 Cargar modelo previamente entrenado (ajusta la ruta si es necesario)
modelo = joblib.load("modelo_entrenado.pkl")  # Asegúrate de tener este modelo guardado

# 📌 Función proporcionada
def funcion(csv, modelo):
    # Convertimos el csv en DataFrame
    df = pd.DataFrame(csv)

    # Eliminamos las variables no relevantes
    try:
        df = df.drop(['municipio', 'codigo_postal'], axis=1) 
    except:
        pass

    # Convertimos a porcentaje las siguientes variables
    df["num_sin_estudios"] = df["num_sin_estudios"] / df["poblacion"]
    df["num_secundaria"] = df["num_secundaria"] / df["poblacion"]
    df["num_superior"] = df["num_superior"] / df["poblacion"]

    # Predecimos la variable objetivo
    predict_random = modelo.predict(df)
    predict_random = predict_random

    # Convertimos las predicciones en un DataFrame
    resultados = pd.DataFrame({"DelitosLibSex": predict_random})

    # Normalizamos la columna de predicción entre 0 y 1
    scaler = MinMaxScaler()
    resultados["Score"] = scaler.fit_transform(resultados[["DelitosLibSex"]])

    # Agregamos el ranking (1 es el más alto)
    resultados["Ranking"] = resultados["DelitosLibSex"].rank(ascending=False, method="min").astype(int)

    return resultados

# 📌 Título de la aplicación
st.title("Optimización Estatal: Predicción y Mapa de Riesgo")

# 📌 Cargar archivo CSV
uploaded_file = st.file_uploader("Sube un archivo CSV con datos municipales", type=["csv"])

if uploaded_file is not None:
    # Leer el archivo
    df = pd.read_csv(uploaded_file)

    # Ejecutar la función con el modelo
    resultados = funcion(df, modelo)

    # Unir los resultados con las coordenadas del CSV original
    df_resultado = pd.concat([df, resultados], axis=1)

    # Mostrar tabla con los resultados
    st.write("Resultados del modelo:")
    st.dataframe(df_resultado)

    # Crear el mapa minimalista
    st.write("### Mapa de Riesgo por Municipio")

    # Obtener la latitud y longitud de cada municipio
    coordenadas = df_resultado[["latitud", "longitud", "Score"]].dropna()

    # Crear mapa centrado en la zona media de los municipios
    map_center = [coordenadas["latitud"].mean(), coordenadas["longitud"].mean()]
    mapa = folium.Map(location=map_center, zoom_start=6, tiles="cartodbpositron")

    # Añadir marcadores de colores basados en la puntuación de riesgo
    for _, row in coordenadas.iterrows():
        color = f"#{int((1-row['Score'])*255):02x}{int(row['Score']*255):02x}00"  # Gradiente de rojo a verde
        folium.CircleMarker(
            location=[row["latitud"], row["longitud"]],
            radius=6,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.8,
            popup=f"Puntuación de Riesgo: {row['Score']:.2f}"
        ).add_to(mapa)

    # Mostrar el mapa en Streamlit
    st_folium(mapa, width=900, height=500)

    # 📌 Texto a enviar a Groq para explicación automática
    texto_para_groq = """
    La optimización estatal se basa en un modelo de regresión entrenado con datos públicos
    para predecir la necesidad de intervención en municipios con alto riesgo de delitos de 
    libertad sexual. Utilizando variables como densidad poblacional, nivel educativo y tasas
    de criminalidad, el modelo genera un ranking y normaliza los valores para una mejor
    comparación. Posteriormente, los resultados se representan en un mapa, donde el color
    varía de rojo (mayor riesgo) a verde (menor riesgo), facilitando la toma de decisiones
    en la asignación de recursos.
    """

    # 📌 Enviar el texto a Groq para explicación
    st.write("### Explicación Generada por IA")
    
    response = requests.post(
        "https://api.groq.com/v1/completions",  # Endpoint de Groq
        headers={"Authorization": "Bearer TU_API_KEY", "Content-Type": "application/json"},
        data=json.dumps({
            "model": "gpt-4",
            "prompt": texto_para_groq,
            "max_tokens": 150
        })
    )

    if response.status_code == 200:
        resultado_groq = response.json()["choices"][0]["text"]
        st.write(resultado_groq)
    else:
        st.error("Error al obtener la respuesta de Groq")

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