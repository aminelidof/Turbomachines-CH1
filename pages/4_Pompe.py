import streamlit as st
from fpdf import FPDF
import os

# 1. Configuration de la page
st.set_page_config(page_title="Étude des Pompes - Master 1 GM", layout="wide")

# --- FONCTION DE GÉNÉRATION DU PDF ---
def generer_pdf_pompe():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    
    # --- EN-TÊTE ---
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(31, 73, 125) 
    pdf.cell(0, 15, "SUPPORT DE COURS : TURBOMACHINES (M1)", ln=True, align='C')
    pdf.set_font("Arial", "I", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Chapitre : Etude des Pompes Hydrauliques", ln=True, align='C')
    pdf.ln(5)
    pdf.line(10, 35, 200, 35) 
    pdf.ln(10)

    # --- SECTION 1 : DÉFINITION ---
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "1. Definition et Role", ln=True)
    pdf.set_font("Arial", "", 11)
    description = (
        "Une pompe est une turbomachine receptrice qui transfert de l'energie mecanique "
        "a un liquide (fluide incompressible) pour augmenter sa pression ou sa hauteur manometrique. "
        "Contrairement aux compresseurs, le volume massique reste constant (v = cte)."
    )
    pdf.multi_cell(0, 7, description)
    pdf.ln(5)

    # --- SECTION 2 : RENDEMENT ET PUISSANCE ---
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "2. Puissance et Rendement global", ln=True)
    pdf.set_font("Arial", "B", 12)
    pdf.set_fill_color(235, 245, 255) 
    pdf.cell(0, 12, "  Phydraulique = m * v * (P2 - P1) = Q * Delta_P  ", ln=True, align='C', fill=True)
    pdf.ln(5)

    return pdf.output(dest='S').encode('latin-1')

# --- BARRE LATÉRALE ---
st.sidebar.subheader("📥 Exportation PDF")
st.sidebar.info("Générez le support de cours pour le chapitre sur les pompes.")

if st.sidebar.button("🛠️ Préparer le document PDF"):
    try:
        pdf_bytes = generer_pdf_pompe()
        st.sidebar.download_button(
            label="📥 Télécharger le Cours Pompes",
            data=pdf_bytes,
            file_name="Cours_Pompes_M1.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.sidebar.error(f"Erreur : {e}")

#################################################################################################################

st.header("💧 Étude des Pompes Hydrauliques")

# --- AJOUT : Illustration Animée ---
st.divider()
col_anim, col_desc = st.columns([1, 1])

with col_anim:
    # Remplacez par votre fichier gif si disponible
    if os.path.exists("pompe_centrifuge.gif"):
        st.image("pompe_centrifuge.gif", caption="Fonctionnement d'une pompe centrifuge", use_container_width=True)
    else:
        st.info("💡 [Schéma : Une pompe centrifuge transforme l'énergie de rotation en énergie cinétique puis en pression]")
        
with col_desc:
    st.markdown("### ⚙️ Particularités des Pompes")
    st.markdown("Dans une pompe (machine hydraulique) :")
    # Utilisez cette syntaxe précise (le 'r' devant les guillemets est crucial)
    st.markdown(r"* **Fluide Incompressible** : Le volume massique $v$ est considéré constant ($v_1 \approx v_2$).")
    st.markdown("* **Transfert d'Énergie** : L'énergie est transmise sous forme de pression.")
    st.markdown("* **Rôle** : Augmenter la charge hydraulique du liquide.")

st.markdown("""
Une pompe est une **turbomachine réceptrice** qui augmente l'énergie d'un liquide. Contrairement au compresseur, les variations de température sont généralement négligeables[cite: 2, 3].
""")

# --- Section 1: Équation d'Euler et Enthalpie ---
st.subheader("📊 Analyse Thermodynamique Simplifiée")

col_text, col_diag = st.columns([1, 1])

with col_text:
    st.markdown(r"""
    Pour un liquide incompressible, le travail isentropique s'écrit simplement :
    
    * **Travail Idéal** : $w_s = v \cdot (P_2 - P_1)$
    * **Point 1** : Aspiration du liquide.
    * **Point 2** : Refoulement.
    * **Irréversibilités** : Les pertes de charge et les frottements augmentent la puissance réelle absorbée sur l'arbre.
    """)

with col_diag:
    st.write("### 📈 Diagramme de Pompe")
    # Utilisation d'une image générique pour illustrer la courbe caractéristique
    st.image("Diagramme de Pompe.jpg", 
             caption="Courbe caractéristique d'une pompe : HMT en fonction du débit", use_container_width=True)

st.divider()

# --- Section 2: Bilans et Rendement (MISE À JOUR) ---
st.subheader("2. Bilans Énergétiques et Rendements")

c1, c2 = st.columns(2)

with c1:
    st.info("**Puissance Hydraulique ($P_h$)**")
    st.write("Énergie transmise au fluide :")
    st.latex(r"P_h = \dot{m} \cdot v \cdot \Delta P = \dot{Q} \cdot \Delta P")

with c2:
    st.error("**Puissance Mécanique ($P_{arbre}$)**")
    st.write("Puissance consommée par le moteur :")
    st.latex(r"P_m = \frac{P_h}{\eta_g}")

st.markdown("### 🔍 Décomposition des Rendements")
st.markdown(r"Le rendement global est le produit des rendements partiels : $\eta_g = \eta_h \cdot \eta_v \cdot \eta_m$")

# Utilisation de colonnes ou d'expanders pour les définitions
col1, col2 = st.columns(2)

with col1:
    st.write(f"**$\eta_g$ (Rendement global)** : Rapport entre la puissance hydraulique utile fournie au fluide et la puissance mécanique absorbée sur l'arbre.")
    st.write(f"**$\eta_h$ (Rendement hydraulique)** : Mesure les pertes d'énergie dues aux frottements du fluide, aux turbulences et aux changements de vitesse.")

with col2:
    st.write(f"**$\eta_v$ (Rendement volumétrique)** : Prend en compte les fuites internes. C'est le rapport entre le débit réel et le débit théorique. Il diminue à haute pression.")
    st.write(f"**$\eta_m$ (Rendement mécanique)** : Représente les pertes par frottements mécaniques entre les pièces mobiles (roulements, joints).")
# --- Section 3: Calculateur Rapide ---
st.divider()
st.subheader("🧮 Calculateur de Puissance de Pompage")

with st.expander("Cliquez pour calculer la puissance nécessaire"):
    col_a, col_b, col_c = st.columns(3)
    
    debit_v = col_a.number_input("Débit volumique (m³/h)", value=10.0)
    delta_p = col_b.number_input("Différence de pression ΔP (bar)", value=2.0)
    eta_pompe = col_c.slider("Rendement de la pompe η", 0.3, 0.95, 0.75)
    
    # Conversion unités SI : 1 m3/h = 1/3600 m3/s | 1 bar = 10^5 Pa
    q_si = debit_v / 3600
    dp_si = delta_p * 100000
    
    p_hyd = q_si * dp_si
    p_elec = p_hyd / eta_pompe
    
    st.write(f"💧 Puissance utile transmise au fluide : **{p_hyd/1000:.2f} kW**")
    st.write(f"🔌 Puissance électrique estimée consommée : **{p_elec/1000:.2f} kW**")

st.success("👉 Ce module complète votre bibliothèque de composants industriels.")