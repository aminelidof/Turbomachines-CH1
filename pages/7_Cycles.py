# pages/6_Cycles.py
import sys
import os

# Ajoute le dossier parent au chemin de recherche de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.diagrams import brayton, rankine

import streamlit as st
from utils.diagrams import brayton, rankine

st.header("🔄 Cycles thermodynamiques")

st.subheader("Cycle de Brayton")
st.plotly_chart(brayton(), use_container_width=True)

st.subheader("Cycle de Rankine")
st.plotly_chart(rankine(), use_container_width=True)

