import streamlit as st
from fpdf import FPDF
import os

# 1. Configuration initiale
st.set_page_config(page_title="Étude des Turbines - Master 1 GM", layout="wide")

def generer_cours_complet():
    # Utilisation de 'P' pour Portrait et 'mm' pour millimètres
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    
    # --- EN-TÊTE ---
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(31, 73, 125) # Bleu foncé professionnel
    pdf.cell(0, 15, "SUPPORT DE COURS : TURBOMACHINES (M1)", ln=True, align='C')
    pdf.set_font("Arial", "I", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Chapitre : Etude Approfondie des Turbines", ln=True, align='C')
    pdf.ln(5)
    pdf.line(10, 35, 200, 35) # Ligne de séparation
    pdf.ln(10)

    # --- SECTION 1 : DÉFINITION ---
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "1. Definition et Role", ln=True)
    pdf.set_font("Arial", "", 11)
    description = (
        "Une turbine est une turbomachine motrice qui extrait l'energie d'un fluide "
        "(vapeur, gaz ou eau) pour produire une puissance mecanique sur l'arbre. "
        "A l'inverse du compresseur, le fluide subit ici une detente."
    )
    pdf.multi_cell(0, 7, description)
    pdf.ln(5)

    # --- SECTION 2 : ANALYSE THERMODYNAMIQUE ---
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "2. Analyse sur le Diagramme de Mollier (h-s)", ln=True)
    pdf.set_font("Arial", "", 11)
    analyse = (
        "- Point 1 : Admission (Haute Pression P1, Haute Temperature).\n"
        "- Trajet 1 -> 2s : Detente Isentropique ideale (entropie constante).\n"
        "- Trajet 1 -> 2 : Detente Reelle avec augmentation d'entropie (s2 > s1) due aux frottements.\n"
        "- Consequences : Le travail reel recupere est inferieur au travail isentropique."
    )
    pdf.multi_cell(0, 7, analyse)
    pdf.ln(5)
    
    # Insertion du schéma technique (Mollier)
    img_path = "mollier_turbine.png"
    if os.path.exists(img_path):
        # Centrage de l'image
        pdf.image(img_path, x=35, w=140)
        pdf.ln(5)

    # --- SECTION 3 : RENDEMENT ISENTROPIQUE ---
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "3. Rendement Isentropique (nt)", ln=True)
    pdf.set_font("Arial", "B", 12)
    pdf.set_fill_color(230, 240, 255)
    # Formule mathématique simplifiée pour le PDF
    pdf.cell(0, 12, "  nt = (h1 - h2_reel) / (h1 - h2s)  ", ln=True, align='C', fill=True)
    pdf.ln(5)

    # --- SECTION 4 : VAPEUR HUMIDE & CLASSIFICATION ---
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "4. Specificites Techniques (Master 1)", ln=True)
    pdf.set_font("Arial", "", 11)
    
    # Titre en vapeur
    vapeur = (
        "Dans les turbines a vapeur, la detente finit souvent en zone humide. "
        "Le titre x2 doit rester superieur a 0.85 pour eviter l'erosion des aubes par les gouttelettes."
    )
    pdf.multi_cell(0, 7, vapeur)
    pdf.ln(3)

    # Classification
    classification = (
        "Classification : \n"
        "- Action : La chute de pression a lieu uniquement dans le stator.\n"
        "- Reaction : La pression chute a la fois dans le stator et le rotor."
    )
    pdf.multi_cell(0, 7, classification)

    # Sortie sécurisée pour Streamlit
    return pdf.output(dest='S').encode('latin-1')

# --- INTERFACE DE TÉLÉCHARGEMENT ---
st.sidebar.subheader("📥 Exportation du Cours")
st.sidebar.info("Générez un PDF contenant les schémas, les formules de rendement et les analyses thermodynamiques.")

if st.sidebar.button("🛠️ Préparer le document PDF"):
    try:
        pdf_bytes = generer_cours_complet()
        st.sidebar.download_button(
            label="📥 Télécharger le Cours (PDF)",
            data=pdf_bytes,
            file_name="Cours_Approfondi_Turbines_M1.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.sidebar.error(f"Erreur lors de la génération : {e}")

################################################################################################################################################################


st.header("🌪️ Étude Approfondie des Turbines")
# --- AJOUT : Illustration Animée ---
st.divider()
col_anim, col_desc = st.columns([1, 1])

with col_anim:
    if os.path.exists("turbine.gif"):
        st.image("turbine.gif", caption="Architecture d'une turbine axiale", use_container_width=True)
    else:
        st.warning("Animation 'turbine.gif' introuvable.")

with col_desc:
    st.markdown("""
    ### ⚙️ Architecture Axiale
    Dans une turbine axiale :
    * Le fluide haute pression entre et se détend à travers les aubes.
    * L'énergie thermique et de pression est convertie en **couple mécanique** sur l'arbre.
    * Contrairement au compresseur, le fluide fournit le travail à la machine.
    """)
# -----------------------------------

st.markdown("""
Une turbine est une **turbomachine motrice** qui extrait l'énergie d'un fluide (vapeur, gaz ou eau) pour produire une puissance mécanique $\dot{W}$ sur l'arbre.
À l'inverse du compresseur, le fluide subit ici une **détente**.
""")

# --- Section 1: Le Diagramme de Mollier (h-s) ---
st.subheader("📊 Diagramme Mollier (h-s) de Détente")

col_text, col_diag = st.columns([1, 1])

with col_text:
    st.markdown(r"""
    Sur le diagramme Enthalpie-Entropie, la détente s'effectue vers les pressions décroissantes :
    
    * **Point 1** : Admission (Haute Pression $P_1$, Haute Température).
    * **Trajet 1 → 2s** : Détente **Isentropique** (idéale). C'est le maximum de travail extractible ($w_s = h_1 - h_{2s}$).
    * **Trajet 1 → 2** : Détente **Réelle**. Les frottements internes génèrent de la chaleur, donc l'entropie augmente ($s_2 > s_1$).
    * **Conséquence** : On récupère moins de travail que prévu car l'enthalpie de sortie réelle $h_2$ est plus élevée que $h_{2s}$.
    """)

with col_diag:
    st.write("### 📈 Représentation de la Détente")
    
    # Affichage de votre image enregistrée
    img_path = "mollier_turbine.png"
    
    if os.path.exists(img_path):
        st.image(img_path, caption="Détente réelle (1-2) vs isentropique (1-2s)", use_container_width=True)
    else:
        st.error(f"⚠️ L'image '{img_path}' est introuvable.")
        # Schéma de secours au cas où
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Mollier_h-s_diagram_expansion.svg/500px-Mollier_h-s_diagram_expansion.svg.png", 
                 caption="Schéma de secours : Détente dans le diagramme h-s", use_container_width=True)



st.divider()

# --- Section 2: Bilans et Rendement ---
st.subheader("2. Rendement Isentropique de Détente ($\eta_t$)")

c1, c2 = st.columns(2)

with c1:
    st.info("**Travail Réel ($w_{réel}$)**")
    st.write("C'est l'énergie effectivement récupérée :")
    st.latex(r"w_{réel} = h_1 - h_{2,réel}")

with c2:
    st.success("**Travail Isentropique ($w_s$)**")
    st.write("C'est le maximum théorique extractible :")
    st.latex(r"w_{s} = h_1 - h_{2s}")

st.markdown("#### Formule finale du rendement")
st.latex(r"\eta_t = \frac{w_{réel}}{w_{s}} = \frac{h_1 - h_2}{h_1 - h_{2s}}")

# --- Section 3: Spécificité Master 1 : Vapeur Humide ---
st.divider()
st.subheader("💧 Cas de la Vapeur d'eau (Titre x)")

st.warning("""
Dans les turbines à vapeur, la détente finit souvent sous la courbe de saturation. 
Il est impératif de calculer le **titre en vapeur** $x_2$ pour s'assurer qu'il reste supérieur à 0.85-0.90 afin de protéger les aubes contre l'érosion.
""")

with st.expander("🔍 Formule du Titre"):
    st.write("L'enthalpie au point 2 (mélange liquide-vapeur) s'écrit :")
    st.latex(r"h_2 = h_f + x_2 \cdot (h_g - h_f)")
    st.write("Où $h_f$ est l'enthalpie du liquide saturé et $h_g$ celle de la vapeur saturée à la pression $P_2$.")

# --- Section 4: Classification ---
st.subheader("⚙️ Classification par Principe")
col_a, col_b = st.columns(2)

with col_a:
    st.write("**Turbines à Action**")
    st.write("La chute de pression a lieu uniquement dans le distributeur (stator).")
    st.write("*Exemple : Turbine Pelton, Curtis.*")
    

with col_b:
    st.write("**Turbines à Réaction**")
    st.write("La pression chute à la fois dans le stator et dans le rotor.")
    st.write("*Exemple : Turbine Francis, Kaplan.*")
    

st.divider()
st.success("👉 Ce module clôture l'étude individuelle des composants. Vous pouvez maintenant passer à l'étude des cycles combinés.")