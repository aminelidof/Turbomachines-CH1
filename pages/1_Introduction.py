import streamlit as st
from fpdf import FPDF
import os

# 1. Configuration de la page
st.set_page_config(page_title="Introduction - Turbomachines", layout="wide")

# --- FONCTION DE GÉNÉRATION DU PDF ---
def generer_pdf_introduction():
    pdf = FPDF()
    pdf.add_page()
    
    # --- EN-TÊTE ---
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(31, 73, 125)
    pdf.cell(0, 15, "SUPPORT DE COURS : TURBOMACHINES", ln=True, align='C')
    pdf.set_font("Arial", "I", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Chapitre : Introduction et Contexte Industriel", ln=True, align='C')
    pdf.ln(10)

    # --- SECTION 1 : CONTEXTE ---
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "1. Contexte Industriel", ln=True)
    pdf.set_font("Arial", "", 11)
    contexte = (
        "Les turbomachines sont au coeur des procedes industriels modernes : "
        "centrales electriques, petrochimie et propulsion aeronautique. "
        "Contrairement aux machines volumetriques (cylindres/pistons), "
        "les turbomachines fonctionnent en ecoulement continu."
    )
    pdf.multi_cell(0, 7, contexte)
    pdf.ln(5)

    # --- SECTION 2 : VOLUME DE CONTRÔLE ---
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "2. Le Concept de Volume de Controle (VC)", ln=True)
    pdf.set_font("Arial", "", 11)
    vc_text = (
        "En turbomachines, on n'analyse pas une masse fermee mais un espace defini "
        "appele Volume de Controle. \n"
        "- L'echange d'energie resulte de la variation de la quantite de mouvement du fluide.\n"
        "- Le transfert se fait via un rotor (partie mobile) muni d'aubes."
    )
    pdf.multi_cell(0, 7, vc_text)
    
    # --- SECTION 3 : DISTINCTION MAJEURE ---
    pdf.ln(5)
    pdf.set_fill_color(240, 240, 240)
    pdf.set_font("Arial", "B", 11)
    comparaison = (
        "Difference cle : Dans une turbomachine, le fluide n'est jamais prisonnier. "
        "Le passage du fluide est permanent, ce qui permet des debits massiques "
        "bien plus eleves que dans les machines a pistons."
    )
    pdf.multi_cell(0, 7, comparaison, fill=True)

    return pdf.output(dest='S').encode('latin-1')

# --- BARRE LATÉRALE : TÉLÉCHARGEMENT ---
st.sidebar.subheader("📥 Exportation")
try:
    pdf_bytes = generer_pdf_introduction()
    st.sidebar.download_button(
        label="📄 Télécharger l'Introduction (PDF)",
        data=pdf_bytes,
        file_name="Introduction_Turbomachines_M1.pdf",
        mime="application/pdf"
    )
except Exception as e:
    st.sidebar.error(f"Erreur PDF : {e}")

st.header("🔷 Introduction aux Turbomachines")

st.markdown("""
### 🏗️ Contexte Industriel
Les turbomachines sont au cœur des procédés industriels (centrales électriques, pétrochimie, propulsion). 
Contrairement aux **machines volumétriques** (cylindres/pistons) où le fluide est prisonnier, les turbomachines fonctionnent en **écoulement continu**.

### 💡 Le concept de Volume de Contrôle
En Turbomachines, on n'analyse plus un système fermé mais un **Volume de Contrôle (VC)**. 
- L'échange d'énergie se fait par la variation de la quantité de mouvement du fluide.
- Le rotor (partie mobile) interagit avec le fluide via des **aubes**.
""")