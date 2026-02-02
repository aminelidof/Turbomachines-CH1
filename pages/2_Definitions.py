# pages/2_Definitions.py

import streamlit as st
from fpdf import FPDF
import os

# 1. Configuration de la page (DOIT être la première commande)
st.set_page_config(page_title="Définitions - Turbomachines", layout="wide")

# --- FONCTION DE GÉNÉRATION DU PDF DYNAMIQUE ---
def generer_pdf_definitions():
    pdf = FPDF()
    pdf.add_page()
    
    # En-tête professionnel
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(31, 73, 125) # Bleu foncé
    pdf.cell(0, 15, "SUPPORT DE COURS : TURBOMACHINES", ln=True, align='C')
    pdf.set_font("Arial", "I", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Chapitre 1 : Fondements et Definitions", ln=True, align='C')
    pdf.ln(10)

    # Section 1 : Classification
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "1. Classification des Machines", ln=True)
    pdf.set_font("Arial", "", 11)
    #
    pdf.multi_cell(0, 7, "- Machine Thermique : Dispositif capable de transformer de l'energie en un travail mecanique utile.")
    pdf.multi_cell(0, 7, "- Turbomachine : Appareil ou un transfert d'energie s'effectue entre un fluide en mouvement continu et un rotor muni d'aubes.")
    pdf.ln(5)

    # Section 2 : Types (Réceptrices vs Motrices)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "2. Types de Turbomachines", ln=True)
    pdf.set_font("Arial", "", 11)
    #
    pdf.multi_cell(0, 7, "- Machines Receptrices : Le rotor fournit du travail au fluide (ex: Pompes, Compresseurs).")
    pdf.multi_cell(0, 7, "- Machines Motrices : Le fluide fournit du travail au rotor (ex: Turbines).")
    pdf.ln(5)

    # Section 3 : Concepts de Systèmes
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "3. Concepts de Systemes et Grandeurs", ln=True)
    pdf.set_font("Arial", "I", 11)
    pdf.set_fill_color(245, 245, 245) # Fond gris pour le Volume de Contrôle
    #
    pdf.multi_cell(0, 7, "Volume de Controle (VC) : Systeme ouvert ou la masse et l'energie traversent les frontieres de la machine en regime permanent.", fill=True)
    pdf.ln(5)
    
    # Grandeurs fondamentales
    pdf.set_font("Arial", "", 11)
    #
    pdf.multi_cell(0, 7, "- Debit massique (m) : Quantite de matiere traversant la section par unite de temps (kg/s).")
    pdf.multi_cell(0, 7, "- Regime Permanent : Les proprietes ne varient pas avec le temps.")

    # Sortie du flux binaire
    return pdf.output(dest='S').encode('latin-1')

# --- BARRE LATÉRALE : TÉLÉCHARGEMENT ---
st.sidebar.subheader("📥 Exportation PDF")
st.sidebar.info("Générez une version PDF de ce chapitre pour vos révisions.")

if st.sidebar.button("🛠️ Préparer le document"):
    try:
        pdf_bytes = generer_pdf_definitions()
        st.sidebar.download_button(
            label="📄 Télécharger le PDF",
            data=pdf_bytes,
            file_name="Definitions_Turbomachines_M1.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.sidebar.error(f"Erreur de génération : {e}")

st.header("📘 Fondements et Définitions")

st.markdown("""
L'étude des turbomachines repose sur une compréhension précise des systèmes thermodynamiques en mouvement. Voici les concepts clés du Chapitre 1 :
""")

# --- Section 1: Classification ---
st.subheader("1. Classification des Machines")
col1, col2 = st.columns(2)

with col1:
    st.write("**⚙️ La Machine Thermique**")
    st.write("""
    Un dispositif capable de transformer de l'énergie (souvent thermique) en un travail mécanique utile $\dot{W}$, ou inversement.
    """)

with col2:
    st.write("**🌀 La Turbomachine**")
    st.write("""
    Appareil où un transfert d'énergie s'effectue entre un fluide en mouvement continu et un élément rotatif (le rotor) muni d'aubes.
    """)

# --- Section 2: Types de Turbomachines ---
with st.expander("🔍 Distinction : Machines Réceptrices vs Motrices", expanded=True):
    st.markdown("""
    * **Machines Réceptrices** : Le rotor fournit du travail au fluide pour augmenter sa pression ou sa vitesse.
        * *Exemples :* Pompes (liquides), Compresseurs et Ventilateurs (gaz).
    * **Machines Motrices** : Le fluide fournit du travail au rotor pour générer une puissance mécanique sur l'arbre.
        * *Exemple :* Turbines (à vapeur, à gaz, ou hydrauliques).
    """)

# --- Section 3: Concepts de Systèmes ---
st.subheader("2. Concepts de Systèmes")

st.warning("""
**Système Ouvert (Volume de Contrôle - VC)** : 
Contrairement à un système fermé, ici la **masse** et l'**énergie** (chaleur et travail) traversent les frontières de la machine. C'est le cadre d'analyse standard pour les turbomachines en régime permanent.
""")

st.markdown(r"""
### 3. Grandeurs Fondamentales
* **Débit massique ($\dot{m}$)** : La quantité de matière traversant la section par unité de temps (kg/s). En régime permanent, $\dot{m}_{entrée} = \dot{m}_{sortie}$.
* **Régime Permanent** : État où les propriétés du fluide en chaque point du système ne varient pas avec le temps ($\frac{dM_{VC}}{dt} = 0$).
* **Fluide de Travail** : 
    * *Incompressible* : Volume massique $v \approx$ constant (Liquides).
    * *Compressible* : $v$ varie fortement avec $P$ et $T$ (Gaz).
""")

# --- Section 4: Note Pédagogique ---
st.divider()
st.info("💡 **Le saviez-vous ?** La distinction entre ventilateur et compresseur dépend uniquement du rapport de pression (le ventilateur déplace l'air avec une compression négligeable).")

st.success("👉 Utilisez le menu à gauche pour passer à la page suivante : **Bilans Énergétiques**.")