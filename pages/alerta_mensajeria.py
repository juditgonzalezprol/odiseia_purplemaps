import streamlit as st
from twilio.rest import Client

# 📌 Configurar credenciales de Twilio
TWILIO_ACCOUNT_SID = "AC3abe2648b578b8dcfe2f642d3ad75844"  # 🔥 Tu Twilio Account SID
TWILIO_AUTH_TOKEN = "SK33aba97adb6029f644e3356bacdfafee"  # 🔥 Reemplázalo con tu Auth Token
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Número de Twilio habilitado para WhatsApp
TO_WHATSAPP_NUMBER = "whatsapp:+34655566823"  # 📌 Número destino

# 📌 Contenido del mensaje
CONTENT_SID = "HX229f5a04fd0510ce1b071852155d3e75"  # 🔥 ID del contenido predefinido en Twilio
CONTENT_VARIABLES = '{"1":"AVISO PELIGRO DE CONTACTO"}'  # Variables personalizadas

# 📌 Función para enviar mensaje de WhatsApp
def enviar_mensaje_whatsapp():
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            content_sid=CONTENT_SID,
            content_variables=CONTENT_VARIABLES,
            to=TO_WHATSAPP_NUMBER
        )

        st.success(f"✅ Mensaje enviado con éxito! SID: {message.sid}")

    except Exception as e:
        st.error(f"⚠️ Error al enviar mensaje: {e}")

# 📌 UI en Streamlit
st.title("📲 Enviar Mensaje de WhatsApp con Twilio")

if st.button("🚀 Enviar Mensaje de WhatsApp"):
    enviar_mensaje_whatsapp()
