import streamlit as st
from fpdf import FPDF
import os

# 1. Configuration de la page (DOIT être la première commande)
st.set_page_config(page_title="Analyse Énergétique", page_icon="⚖️", layout="wide")

# --- FONCTION DE GÉNÉRATION DU PDF DYNAMIQUE ---
def generer_pdf_bilans(m, h1, h2, puissance):
    pdf = FPDF()
    pdf.add_page()
    
    # --- EN-TÊTE ---
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(31, 73, 125)
    pdf.cell(0, 15, "SUPPORT DE COURS : TURBOMACHINES", ln=True, align='C')
    pdf.set_font("Arial", "I", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Chapitre : Bilans Energetiques et Premier Principe", ln=True, align='C')
    pdf.ln(10)

    # --- SECTION 1 : THEORIE ---
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "1. Le Premier Principe en Systeme Ouvert", ln=True)
    pdf.set_font("Arial", "", 11)
    theorie = (
        "L'analyse repose sur le Volume de Controle (VC). L'equation generale est :\n"
        "Q - W = m * [ Delta_h + Delta_Ec + Delta_Ep ]\n\n"
        "Hypotheses pour les turbomachines :\n"
        "- Transformation adiabatique (Q = 0)\n"
        "- Energies cinetique et potentielle negligeables.\n"
        "Equation simplifiee : W = m * (h1 - h2)"
    )
    pdf.multi_cell(0, 7, theorie)
    pdf.ln(5)

    # --- SECTION 2 : RESULTATS DU CALCULATEUR ---
    pdf.set_font("Arial", "B", 14)
    pdf.set_fill_color(230, 240, 255)
    pdf.cell(0, 10, "2. Rapport de Calcul Personnalise", ln=True, fill=True)
    pdf.set_font("Courier", "B", 12)
    pdf.ln(2)
    pdf.cell(0, 10, f"- Debit massique : {m} kg/s", ln=True)
    pdf.cell(0, 10, f"- Enthalpie d'entree (h1) : {h1} kJ/kg", ln=True)
    pdf.cell(0, 10, f"- Enthalpie de sortie (h2) : {h2} kJ/kg", ln=True)
    pdf.set_text_color(200, 0, 0)
    pdf.cell(0, 10, f"==> PUISSANCE CALCULEE : {puissance} kW", ln=True)

    # Utilisation de 'latin-1' pour éviter les erreurs de caractères spéciaux
    return pdf.output(dest='S').encode('latin-1')

# --- CONTENU DE LA PAGE ---
st.header("⚖️ Analyse Énergétique des Systèmes Ouverts")

# 🧮 LE CALCULATEUR (Premier Bloc)
st.subheader("🧮 Calculateur de Puissance")
with st.container(border=True):
    col_a, col_b, col_c = st.columns(3)
    # Ajout de 'key' pour différencier les widgets du premier bloc
    m_test = col_a.number_input("Débit (kg/s)", value=1.0, key="m_1")
    h1_test = col_b.number_input("h entrée (kJ/kg)", value=3000.0, key="h1_1")
    h2_test = col_c.number_input("h sortie (kJ/kg)", value=2500.0, key="h2_1")
    
    p_calc = m_test * (h1_test - h2_test)
    st.write(f"**Puissance calculée :** `{p_calc} kW` ({'Turbine' if p_calc > 0 else 'Compresseur/Pompe'})")

# --- BARRE LATÉRALE : GÉNÉRATION ET TÉLÉCHARGEMENT ---
st.sidebar.subheader("📥 Exportation PDF")

try:
    # Le PDF utilise les données du premier calculateur
    pdf_data = generer_pdf_bilans(m_test, h1_test, h2_test, p_calc)
    
    st.sidebar.download_button(
        label="📄 Télécharger le Bilan PDF",
        data=pdf_data,
        file_name="Bilan_Energetique_M1.pdf",
        mime="application/pdf",
        key="download_bilan"
    )
except Exception as e:
    st.sidebar.error(f"Erreur de génération : {e}")

# --- RESTE DE LA THÉORIE ---
st.subheader("1. La notion d'Enthalpie ($h$)")

st.latex(r"h = u + Pv")

# --- Section Secondaire (Répétition demandée du bloc information) ---
st.divider()
st.header("⚖️ Analyse Énergétique des Systèmes Ouverts (Détails)")

st.markdown("""
L'analyse d'une turbomachine repose sur le concept de **Volume de Contrôle (VC)**. 
Contrairement aux systèmes fermés, ici la matière transporte de l'énergie (Enthalpie) à travers les frontières. 
""")



# --- Section 1: Fondamentaux ---
st.subheader("1. La notion d'Enthalpie ($h$)")
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    Pour entrer dans une machine, le fluide doit "pousser" la masse déjà présente.  
    Ce travail d'écoulement ($P \cdot v$) s'ajoute à l'énergie interne ($u$). 
    """)
    st.latex(r"h = u + Pv")
with col2:
    st.info("**Unité :** kJ/kg ")

# --- Section 2: Premier Principe ---
st.subheader("2. Premier Principe en Régime Permanent")
st.markdown("C'est l'équation maîtresse pour tout ingénieur en énergétique : ")
st.latex(r"\dot{Q} - \dot{W}_{sh} = \dot{m} \left[ \Delta h + \Delta e_c + \Delta e_p \right]")

# --- Section 3: Hypothèses et Simplification ---
with st.expander("🔍 Voir les hypothèses de simplification", expanded=True):
    st.markdown(r"""
    En pratique, pour les turbomachines : 
    * **Adiabatique ($\dot{Q} \approx 0$)** : Les transformations sont si rapides que la chaleur n'a pas le temps de s'échapper. 
    * **Énergies macroscopiques négligeables** : $\Delta \frac{V^2}{2} \approx 0$ et $g\Delta z \approx 0$. 
    """)
    
    st.divider()
    st.markdown("**La relation de travail technique devient : **")
    st.latex(r"\dot{W}_{sh} = \dot{m}(h_1 - h_2)")

# --- Section 4: Convention de Signes ---
st.subheader("3. Interprétation des résultats")
c1, c2 = st.columns(2)

with c1:
    st.success("🌀 **Machine Motrice (Turbine)**")
    st.markdown("$h_1 > h_2 \implies \dot{W} > 0$ ")
    st.caption("Le fluide cède de l'énergie au rotor. ")

with c2:
    st.error("⚙️ **Machine Réceptrice (Pompe/Comp)**")
    st.markdown("$h_1 < h_2 \implies \dot{W} < 0$ ")
    st.caption("Le rotor fournit du travail au fluide. ")

# --- Section 5: Petit Calculateur Rapide (Deuxième Bloc) ---
st.divider()
st.subheader("🧮 Vérificateur Rapide de Puissance (Copie)")
with st.container(border=True):
    col_a2, col_b2, col_c2 = st.columns(3)
    # Ajout de 'key' différents ("_2") pour éviter l'erreur DuplicateElementId
    m_test2 = col_a2.number_input("Débit (kg/s)", value=1.0, key="m_2")
    h1_test2 = col_b2.number_input("h entrée (kJ/kg)", value=3000.0, key="h1_2")
    h2_test2 = col_c2.number_input("h sortie (kJ/kg)", value=2500.0, key="h2_2")
    
    p_calc2 = m_test2 * (h1_test2 - h2_test2)
    st.write(f"**Puissance calculée :** `{p_calc2} kW` ({'Turbine' if p_calc2 > 0 else 'Compresseur/Pompe'})")