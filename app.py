# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:51:26 2025

@author: jperezr
"""

import streamlit as st

# Estilo de fondo
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background:
radial-gradient(black 15%, transparent 16%) 0 0,
radial-gradient(black 15%, transparent 16%) 8px 8px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
background-color:#282828;
background-size:16px 16px;
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Título de la aplicación
st.title("Día del Amor y la Amistad - PENSIONISSSTE")

# Subtítulo
st.header("Videos para mis compañeros y compañeras")

# Cargar y mostrar el primer video
st.subheader("Video 1")
video_file_1 = open('video1.mp4', 'rb')
video_bytes_1 = video_file_1.read()
st.video(video_bytes_1)

# Cargar y mostrar el segundo video
st.subheader("Video 2")
video_file_2 = open('video2.mp4', 'rb')
video_bytes_2 = video_file_2.read()
st.video(video_bytes_2)
