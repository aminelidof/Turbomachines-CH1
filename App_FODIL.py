import streamlit as st
from fpdf import FPDF
import os

# 1. Configuration de la page (DOIT être la toute première commande)
st.set_page_config(
    page_title="Thermodynamique Appliquée – Turbomachines",
    page_icon="⚙️",
    layout="wide"
)

# --- FONCTION DE GÉNÉRATION DU PDF (PRÉSENTATION DU MODULE) ---
def generer_pdf_accueil(theme_name):
    pdf = FPDF()
    pdf.add_page()
    
    # En-tête institutionnel
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(31, 73, 125)
    pdf.cell(0, 10, "CENTRE UNIVERSITAIRE DE MAGHNIA", ln=True, align='C')
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, "Departement de Genie Mecanique - Master 1 GM", ln=True, align='C')
    pdf.ln(10)

    # Titre du Module
    pdf.set_font("Arial", "B", 20)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 15, "Thermodynamique Appliquee aux Turbomachines", ln=True, align='C')
    pdf.set_font("Arial", "I", 12)
    pdf.cell(0, 10, "Support de cours interactif - Dr FODIL", ln=True, align='C')
    pdf.ln(10)

    # Objectifs Pédagogiques
    pdf.set_font("Arial", "B", 14)
    pdf.set_fill_color(230, 240, 255)
    pdf.cell(0, 10, " Objectifs du Chapitre :", ln=True, fill=True)
    pdf.set_font("Arial", "", 11)
    objectifs = (
        "- Analyse Systemique : Volumes de Controle (VC).\n"
        "- Bilans Rigoureux : Masse et Energie (h = u + Pv).\n"
        "- Performance : Etude des compresseurs, pompes et turbines.\n"
        "- Cycles Complexes : Brayton et Rankine reels.\n"
        "- Expertise : Application sur cas industriels (Exercices 1 a 5)."
    )
    pdf.multi_cell(0, 8, objectifs)
    pdf.ln(10)

    # Infos Additionnelles
    pdf.set_font("Arial", "I", 10)
    pdf.cell(0, 10, f"Document genere avec le theme : {theme_name}", ln=True, align='R')

    return pdf.output(dest='S').encode('latin-1')

# 2. Gestion des Thèmes (Initialisation et Sélection UNIQUE)
if 'theme_choice' not in st.session_state:
    st.session_state.theme_choice = "Sombre (Pro)"

st.sidebar.title("🎨 Personnalisation")
# Suppression du doublon ici pour éviter l'erreur DuplicateElementKey
theme = st.sidebar.selectbox(
    "Choisir l'environnement :",
    ["Sombre (Pro)", "Clair (Lecture)", "Ingénierie (Bleu)"],
    key="theme_choice" 
)

# 3. Export PDF dans la barre latérale
st.sidebar.divider()
st.sidebar.subheader("📥 Documents")
try:
    pdf_bytes = generer_pdf_accueil(theme)
    st.sidebar.download_button(
        label="📄 Télécharger le Syllabus (PDF)",
        data=pdf_bytes,
        file_name="Presentation_Turbomachines_M1.pdf",
        mime="application/pdf"
    )
except Exception as e:
    st.sidebar.error(f"Erreur PDF : {e}")

# 4. Fonction d'application dynamique du style
def apply_theme(theme_name):
    if theme_name == "Sombre (Pro)":
        bg_color, box_bg, text_color, title_color, border_color = "#0e1117", "#1d2129", "#c9d1d9", "#58a6ff", "#30363d"
    elif theme_name == "Clair (Lecture)":
        bg_color, box_bg, text_color, title_color, border_color = "#f4f6fa", "#ffffff", "#31333F", "#0b5394", "#d1d5db"
    else:  # Ingénierie (Bleu)
        bg_color, box_bg, text_color, title_color, border_color = "#001529", "#002140", "#ffffff", "#1890ff", "#003a8c"

    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{ background-color: {bg_color}; }}
    .box {{
        background-color: {box_bg};
        padding: 25px;
        border-radius: 12px;
        border-left: 5px solid {title_color};
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
        font-size: 18px;
        color: {text_color};
        margin-bottom: 20px;
    }}
    h1, h2, h3 {{ color: {title_color} !important; }}
    p, li, span {{ color: {text_color}; }}
    hr {{ border-color: {border_color}; }}
    
    /* Style spécifique pour la main-box du corps de page */
    .main-box {{
        padding: 20px;
        border-radius: 10px;
        border-left: 6px solid {title_color};
        background-color: {box_bg};
        margin-bottom: 20px;
        border: 1px solid {border_color};
    }}
    </style>
    """, unsafe_allow_html=True)

# Application du thème choisi
apply_theme(theme)

# 5. Corps de la page d'accueil
st.title("⚙️ Thermodynamique Appliquée")
st.subheader("Chapitre 1 : Les Turbomachines – Master 1 GM - Dr FODIL")

# Construction de la boîte d'objectifs
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown(f'<div style="color:{st.session_state.theme_choice}; font-weight:bold; font-size:1.2em; margin-bottom:15px;">🎯 Objectifs du Chapitre (M1-GM)</div>', unsafe_allow_html=True)

st.markdown("✅ **Analyse Systémique** : Comprendre les turbomachines en tant que Volumes de Contrôle (VC).")
st.markdown(r"✅ **Bilans Rigoureux** : Maîtriser les bilans de masse et d'énergie ($h = u + Pv$).")
st.markdown("✅ **Performance** : Analyser les compresseurs, pompes et turbines.")
st.markdown("✅ **Cycles Complexes** : Étudier les cycles de Brayton et Rankine réels.")
st.markdown("✅ **Expertise** : Appliquer les calculs sur des cas industriels (Exercices 1 à 5).")
st.markdown('</div>', unsafe_allow_html=True)



# --- INSERTION DE L'IMAGE / GIF CORRIGÉE ---
st.write("### 🌀 Visualisation du Cycle Thermodynamique")

# Utilisation de st.image pour afficher le GIF ou l'image
# Remplacez "turbine_a_vapeur.gif" par le chemin réel de votre fichier sur votre PC
try:
    # Si le fichier est dans le même dossier que votre script :
    st.image("turbine_a_vapeur.gif", caption="Cycle de fonctionnement d'une turbine à vapeur", use_container_width=True)
except:
    # Image de secours si le fichier n'est pas trouvé localement
    st.info("💡 [Schéma technique : Cycle de Rankine / Turbine à vapeur]")

# Statistiques du cours
c1, c2 = st.columns(2)
c1.metric("Niveau Académique", "Master 1 GM")
c2.metric("Support", "CU Maghnia")

c3, c4 = st.columns(2)
c3.metric("Présenté Par", "Dr FODIL")
c4.metric("Statut", "Interactif")

st.success(f"👉 Thème '{theme}' appliqué avec succès.")