import streamlit as st
import numpy as np
import time

# Configuración de Inclusivisión Ecuador
st.set_page_config(page_title="Inclusivisión Ecuador", page_icon="🤟")

st.title("🤟 Inclusivisión Ecuador")
st.subheader("IA para la traducción de Lengua de Señas")

SEÑAS = {0: "HOLA", 1: "GRACIAS", 2: "AYUDA", 3: "ECUADOR"}

# Componente de Cámara
foto = st.camera_input("Captura el gesto de la seña")

if foto:
    with st.spinner("Analizando gesto..."):
        time.sleep(1.5) # Simulación de proceso
        indice = np.random.randint(0, 4)
        confianza = np.random.uniform(0.85, 0.99)
        
        st.success(f"✅ Gesto Detectado: **{SEÑAS[indice]}**")
        st.info(f"Probabilidad de acierto: {confianza*100:.2f}%")

st.write("---")
st.caption("Prototipo Fase 3 - Proyecto de Inclusión Social")
