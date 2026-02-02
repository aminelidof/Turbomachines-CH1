import streamlit as st
from fpdf import FPDF
import os

# 1. Configuration de la page
st.set_page_config(page_title="Étude des Compresseurs - Master 1 GM", layout="wide")

# --- FONCTION DE GÉNÉRATION DU PDF ---
def generer_pdf_compresseur():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    
    # --- EN-TÊTE ---
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(31, 73, 125) # Bleu professionnel
    pdf.cell(0, 15, "SUPPORT DE COURS : TURBOMACHINES (M1)", ln=True, align='C')
    pdf.set_font("Arial", "I", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Chapitre : Etude des Compresseurs", ln=True, align='C')
    pdf.ln(5)
    pdf.line(10, 35, 200, 35) 
    pdf.ln(10)

    # --- SECTION 1 : DÉFINITION ---
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "1. Definition et Role", ln=True)
    pdf.set_font("Arial", "", 11)
    description = (
        "Un compresseur est une turbomachine receptrice qui augmente la pression d'un fluide "
        "en lui fournissant un travail mecanique. "
        "L'analyse repose sur la comparaison entre le travail reel et le travail ideal."
    )
    pdf.multi_cell(0, 7, description)
    pdf.ln(5)

    # --- SECTION 2 : ANALYSE THERMODYNAMIQUE ---
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "2. Analyse sur le Diagramme de Mollier (h-s)", ln=True)
    pdf.set_font("Arial", "", 11)
    analyse = (
        "- Point 1 : Admission du fluide a basse pression (P1).\n"
        "- Trajet 1 -> 2s : Compression Isentropique (ideale, s constant).\n"
        "- Trajet 1 -> 2 : Compression Reelle avec augmentation d'entropie (s2 > s1).\n"
        "- Impact : Le travail reel absorbe (h2 - h1) est superieur au travail ideal (h2s - h1)."
    )
    pdf.multi_cell(0, 7, analyse)
    pdf.ln(5)
    
    # Insertion de l'image (Compresseur)
    img_path = "mollier_compresseur.png"
    if os.path.exists(img_path):
        pdf.image(img_path, x=35, w=140)
        pdf.ln(5)

    # --- SECTION 3 : RENDEMENT ISENTROPIQUE ---
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "3. Rendement Isentropique (nc)", ln=True)
    pdf.set_font("Arial", "B", 12)
    pdf.set_fill_color(255, 235, 235) # Fond léger rouge/rose pour compresseur
    pdf.cell(0, 12, "  nc = (h2s - h1) / (h2_reel - h1)  ", ln=True, align='C', fill=True)
    pdf.ln(5)

    # --- SECTION 4 : NOTE MASTER 1 ---
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "4. Observations Techniques", ln=True)
    pdf.set_font("Arial", "", 11)
    note = (
        "Plus le rendement est faible, plus le fluide s'echauffe inutilement. "
        "Cela necessite souvent un refroidissement entre deux etages de compression pour "
        "se rapprocher d'une compression isotherme plus econome en energie."
    )
    pdf.multi_cell(0, 7, note)

    return pdf.output(dest='S').encode('latin-1')

# --- BARRE LATÉRALE ---
st.sidebar.subheader("📥 Exportation PDF")
st.sidebar.info("Générez le support de cours pour ce chapitre (Texte + Diagrammes).")

if st.sidebar.button("🛠️ Préparer le document PDF"):
    try:
        pdf_bytes = generer_pdf_compresseur()
        st.sidebar.download_button(
            label="📥 Télécharger le Cours Compresseurs",
            data=pdf_bytes,
            file_name="Cours_Compresseurs_M1.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.sidebar.error(f"Erreur : {e}")

#################################################################################################################

# 1. Configuration de la page
st.set_page_config(page_title="Étude des Compresseurs - Master 1 GM", layout="wide")

st.header("🌀 Étude Thermodynamique des Compresseurs")

# --- AJOUT : Illustration Animée ---
st.divider()
col_anim, col_desc = st.columns([1, 1])

with col_anim:
    # On utilise l'une de vos deux animations identiques
    if os.path.exists("Axial_compressor.gif"):
        st.image("Axial_compressor.gif", caption="Cinématique d'un compresseur axial", use_container_width=True)
    else:
        st.warning("Animation 'Axial_compressor.gif' introuvable.")

with col_desc:
    st.markdown("""
    ### ⚙️ Fonctionnement Mécanique
    L'animation ci-contre illustre la rotation des aubes :
    * **Rotor** : Accélère le fluide et lui transmet l'énergie mécanique.
    * **Stator** : Transforme l'énergie cinétique en pression (diffusion).
    * Chaque étage augmente progressivement la pression du fluide.
    """)
# -----------------------------------

st.markdown("""
Un compresseur est une **turbomachine réceptrice** qui augmente la pression d'un fluide en lui fournissant un travail mécanique. 
L'analyse repose sur la comparaison entre le travail réel et le travail idéal sur le diagramme de Mollier ($h-s$).
""")

# --- Section 1: Le Diagramme de Mollier (h-s) ---
st.subheader("📊 Diagramme Mollier (h-s) et Évolution")

col_text, col_diag = st.columns([1, 1])

with col_text:
    st.markdown(r"""
    **Analyse thermodynamique :**
    
    * **Point 1** : Admission du fluide à basse pression ($P_1$).
    * **Trajet 1 → 2s** : Compression **Isentropique** (idéale). C'est une verticale ($s_1 = s_2$). Elle représente le travail minimal nécessaire.
    * **Trajet 1 → 2** : Compression **Réelle**. À cause des irréversibilités (frottements), l'entropie augmente ($s_2 > s_1$).
    * **Impact Enthalpique** : L'écart vertical $(h_2 - h_1)$ est plus grand que $(h_{2s} - h_1)$. On dépense donc plus d'énergie que prévu.
    """)

with col_diag:
    st.write("### 📈 Représentation de la Compression")
    
    # Vérification et affichage de votre image enregistrée
    img_path = "mollier_compresseur.png"
    
    if os.path.exists(img_path):
        st.image(img_path, caption="Évolution réelle (1-2) vs isentropique (1-2s)", use_container_width=True)
    else:
        st.error(f"⚠️ L'image '{img_path}' est introuvable dans le dossier racine.")
        # Secours via URL si l'image locale est absente
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Mollier_h-s_diagram_compression.svg/500px-Mollier_h-s_diagram_compression.svg.png", 
                 caption="Schéma de secours (Wikimedia)", use_container_width=True)

st.divider()

# --- Section 2: Bilans et Rendement ---
st.subheader("2. Bilans Énergétiques et Rendement")

c1, c2 = st.columns(2)

with c1:
    st.info("**Travail Isentropique ($w_s$)**")
    st.write("Travail minimum théorique :")
    st.latex(r"w_{s} = h_{2s} - h_1")

with c2:
    st.error("**Travail Réel ($w_{réel}$)**")
    st.write("Travail réellement absorbé :")
    st.latex(r"w_{réel} = h_{2,réel} - h_1")

st.markdown("### Formule du Rendement Isentropique ($\eta_c$)")
st.latex(r"\eta_{c} = \frac{h_{2s} - h_1}{h_{2,réel} - h_1}")

# --- Section 3: Outil de Calcul (Nouveauté Master) ---
st.divider()
st.subheader("🧮 Calculateur Rapide (Cas de l'Air)")

with st.expander("Cliquez pour calculer les températures de sortie"):
    col_a, col_b, col_c = st.columns(3)
    
    t1 = col_a.number_input("Température Entrée T1 (K)", value=293.15)
    pi = col_b.number_input("Rapport de pression (P2/P1)", value=5.0)
    eta = col_c.slider("Rendement Isentropique ηc", 0.5, 1.0, 0.85)
    
    # Calcul pour gaz parfait (gamma air = 1.4)
    gamma = 1.4
    t2s = t1 * (pi**((gamma-1)/gamma))
    t2r = t1 + (t2s - t1) / eta
    
    st.write(f"✅ Température de sortie idéale ($T_{{2s}}$) : **{t2s:.2f} K**")
    st.write(f"🔥 Température de sortie réelle ($T_{{2,réel}}$) : **{t2r:.2f} K**")

st.warning(r"⚠️ **Note Master** : Plus le rendement est faible, plus le fluide s'échauffe inutilement. C'est pourquoi un refroidissement est souvent nécessaire entre deux étages de compression.")

st.success("👉 Ce module est prêt pour l'analyse des exercices de thermodynamique appliquée.")