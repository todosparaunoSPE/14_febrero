# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:51:26 2025

@author: jperezr
"""

import streamlit as st

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