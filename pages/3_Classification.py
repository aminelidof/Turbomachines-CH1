# pages/3_Classification.py
import streamlit as st
from fpdf import FPDF

# 1. Configuration de la page
st.set_page_config(page_title="Classification - Turbomachines", layout="wide")

# --- FONCTION DE GÉNÉRATION DU PDF ---
def generer_pdf_classification():
    pdf = FPDF()
    pdf.add_page()
    
    # En-tête professionnel
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(31, 73, 125)
    pdf.cell(0, 15, "SUPPORT DE COURS : TURBOMACHINES", ln=True, align='C')
    pdf.set_font("Arial", "I", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Chapitre : Classification des Machines", ln=True, align='C')
    pdf.ln(10)

    # Section 1 : Sens du transfert
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "1. Classification selon le Sens de l'Energie", ln=True)
    pdf.set_font("Arial", "", 11)
    texte_sens = (
        "- Machines Receptrices (Pompes, Compresseurs) : Recoivent du travail pour "
        "augmenter la pression du fluide.\n"
        "- Machines Motrices (Turbines) : Extraient l'energie du fluide pour produire "
        "une puissance mecanique."
    )
    pdf.multi_cell(0, 7, texte_sens)
    pdf.ln(5)

    # Section 2 : Nature du fluide et Ecoulement
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "2. Nature du Fluide et Ecoulement", ln=True)
    pdf.set_font("Arial", "", 11)
    texte_nature = (
        "- Machines Hydrauliques : Fluide incompressible (eau).\n"
        "- Machines Thermiques : Fluide compressible (gaz, vapeur).\n"
        "- Direction : Axiale (grand debit) ou Radiale/Centrifuge (forte pression)."
    )
    pdf.multi_cell(0, 7, texte_nature)
    pdf.ln(5)

    # Section 3 : Critères 
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "3. Criteres Techniques", ln=True)
    pdf.set_font("Arial", "B", 11)
    pdf.set_fill_color(240, 240, 240)
    criteres = (
        "- Action vs Reaction : Chute de pression dans le stator uniquement (Action) "
        "ou repartie entre stator et rotor (Reaction).\n"
        "- Nombre d'etages : Monocellulaire ou Multicellulaire.\n"
        "- Vitesse Specifique (Ns) : Choix de la machine optimale."
    )
    pdf.multi_cell(0, 7, criteres, fill=True)

    return pdf.output(dest='S').encode('latin-1')

# --- BARRE LATÉRALE : TÉLÉCHARGEMENT ---
st.sidebar.subheader("📥 Exportation PDF")
if st.sidebar.button("🛠️ Preparer le PDF Classification"):
    try:
        pdf_content = generer_pdf_classification()
        st.sidebar.download_button(
            label="📥 Telecharger le document",
            data=pdf_content,
            file_name="Classification_Turbomachines_M1.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.sidebar.error(f"Erreur : {e}")

########################################################################################################################################################################

st.header("🧭 Classification des Turbomachines")

st.markdown("""
Les turbomachines sont classées selon plusieurs critères fondamentaux qui déterminent leur conception, leur équation de transfert d'énergie et leur domaine d'application.
""")

# --- Section 1: Sens du transfert d'énergie ---
st.subheader("1. Classification selon le Sens de l'Énergie")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### ⚙️ Machines Réceptrices (Génératrices)
    Elles reçoivent de l'énergie mécanique sur l'arbre pour augmenter l'énergie du fluide (pression, vitesse).
    * **Pompes** : Pour les fluides incompressibles (liquides).
    * **Compresseurs** : Pour les fluides compressibles (gaz), avec rapport de pression élevé.
    * **Ventilateurs** : Pour déplacer de grands volumes de gaz avec une faible compression.
    """)

with col2:
    st.markdown("""
    #### 🌀 Machines Motrices (Réceptrices de fluide)
    Elles extraient l'énergie du fluide pour la transformer en travail mécanique sur l'arbre.
    * **Turbines Hydrauliques** : Utilisent l'énergie de l'eau.
    * **Turbines à Vapeur/Gaz** : Utilisent l'enthalpie des gaz en expansion.
    """)



# --- Section 2: Nature du Fluide et Écoulement ---
st.subheader("2. Nature du Fluide et Type d'Écoulement")

tab1, tab2 = st.tabs(["💧 Nature du Fluide", "🔄 Direction de l'Écoulement"])

with tab1:
    st.markdown(r"""
    * **Machines Hydrauliques** : Le fluide est pratiquement incompressible (eau, huile). Les variations de température sont souvent négligées.
    * **Machines Thermiques** : Le fluide est compressible (air, vapeur, gaz de combustion). Le volume massique $v$ varie fortement, nécessitant l'usage de l'enthalpie $h$.
    """)

with tab2:
    st.markdown("""
    * **Axiale** : Le fluide traverse la machine parallèlement à l'axe de rotation. (Idéal pour de grands débits).
    * **Radiale (Centrifuge)** : Le fluide entre axialement et ressort perpendiculairement à l'axe. (Idéal pour de fortes pressions).
    * **Mixte** : Combinaison des deux modes.
    """)



# --- Section 3: Critères de Conception Avancés ---
st.subheader("3. Critères Techniques")

with st.expander("🛠️ Détails des critères de conception"):
    st.markdown(r"""
    * **Action vs Réaction** :
        * **Action** : La chute de pression s'effectue uniquement dans les aubages fixes (distributeur).
        * **Réaction** : La pression diminue à la fois dans le distributeur et dans la roue mobile.
    * **Nombre d'étages** :
        * **Monocellulaire (mono-étage)** : Une seule roue (ex: pompe domestique).
        * **Multicellulaire (multi-étage)** : Plusieurs roues en série pour atteindre des pressions très élevées (ex: compresseur de réacteur).
    * **Vitesse Spécifique ($N_s$)** : Paramètre adimensionnel utilisé pour choisir le type de machine optimal selon le débit et la hauteur.
    """)

# --- Section 4: Résumé ---
st.divider()
st.info("💡 **Rappel Master** : Le choix entre une machine axiale ou radiale se fait souvent sur la base du diagramme de Cordier, reliant le coefficient de débit au coefficient de pression.")

st.success("👉 Prochaine étape : Consultez les **Bilans Énergétiques** pour quantifier ces transferts.")
