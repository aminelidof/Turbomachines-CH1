import streamlit as st
import pandas as pd

# --- Configuration de la page ---
st.set_page_config(page_title="Simulateur Turbomachines (M1-GM)", layout="wide")

st.header("🧪 Simulateur de Turbomachines (M1-GM)")

st.markdown("""
Ce simulateur applique le **Premier Principe de la Thermodynamique** pour les systèmes ouverts en régime permanent afin d'évaluer les performances des machines hydrauliques et thermiques.
""")

# Choix de la machine (Mise à jour avec Turbine)
type_machine = st.radio(
    "Sélectionnez la machine à simuler :", 
    ["💧 Pompe (Liquide)", "💨 Compresseur (Gaz/Air)", "🌀 Turbine (Vapeur/Gaz)"],
    index=0,
    horizontal=True
)

st.divider()

# ==========================================
# CAS 1 : SIMULATION DE LA POMPE
# ==========================================
if "Pompe" in type_machine:
    st.subheader("⚙️ Paramètres de la Pompe Hydraulique")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown("##### 📥 Paramètres d'Entrée")
        m = st.number_input("Débit massique $\dot{m}$ (kg/s)", value=35.0, step=1.0)
        dp = st.slider("Élévation de pression $\Delta P$ (bar)", 0.5, 100.0, 40.0)
        v = st.number_input("Volume massique $v$ (m³/kg)", value=0.001005, format="%.6f")
        eta_p = st.slider("Rendement isentropique $\eta_p$ (%)", 50, 100, 85) / 100

    # --- Calculs Pompe ---
    # Travail massique idéal : w_s = v * ΔP
    w_ideal_J_kg = v * (dp * 1e5)  # Conversion bar -> Pa
    W_dot_ideal = (m * w_ideal_J_kg) / 1000  # Puissance en kW
    
    # Travail réel absorbé : W_reel = W_ideal / rendement
    W_dot_reel = W_dot_ideal / eta_p
    pertes = W_dot_reel - W_dot_ideal

    with col2:
        st.markdown("##### 📤 Analyse des Puissances")
        c1, c2 = st.columns(2)
        c1.metric("Puissance Idéale", f"{W_dot_ideal:.2f} kW")
        c2.metric("Puissance Réelle (ABS)", f"{W_dot_reel:.2f} kW", 
                  delta=f"{pertes:.2f} kW de pertes", delta_color="inverse")

        # Graphique des pertes (Corrigé pour éviter StreamlitColorLengthError)
        st.write("**Répartition de l'énergie fournie :**")
        chart_data = pd.DataFrame({
            "Désignation": ["Travail Utile (Isentropique)", "Pertes (Irréversibilités)"],
            "Puissance (kW)": [W_dot_ideal, pertes]
        })
        st.bar_chart(chart_data, x="Désignation", y="Puissance (kW)", color="Désignation")

    st.info(r"💡 **Note Master** : Pour une pompe, la puissance réelle est toujours supérieure à la puissance idéale ($\dot{W}_{réel} = \dot{W}_s / \eta_p$).")

# ==========================================
# CAS 2 : SIMULATION DU COMPRESSEUR
# ==========================================
elif "Compresseur" in type_machine:
    st.subheader("⚙️ Paramètres du Compresseur d'Air")
    st.caption("Analyse basée sur le bilan enthalpique avec transfert thermique")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown("##### 📥 Données de l'Écoulement")
        m_air = st.number_input("Débit massique (kg/s)", value=0.02, format="%.3f")
        h1 = st.number_input("Enthalpie entrée $h_1$ (kJ/kg)", value=280.13)
        h2 = st.number_input("Enthalpie sortie $h_2$ (kJ/kg)", value=400.98)
        
        q_type = st.radio("Transfert thermique :", ["Perte (Refroidissement)", "Apport"], horizontal=True)
        q_val = st.number_input("Grandeur du transfert $q$ (kJ/kg)", value=16.0)
        
        # Convention de signe : q < 0 si perte vers l'extérieur
        q_signe = -q_val if "Perte" in q_type else q_val

    # --- Calculs Compresseur ---
    # Bilan : Q - W = m * Δh => W = m * (Δh - q)
    delta_h = h2 - h1
    puissance_h = m_air * delta_h
    puissance_q = m_air * q_signe
    
    # Puissance mécanique totale requise (en valeur absolue pour l'absorption)
    puissance_totale = puissance_h - puissance_q 

    with col2:
        st.markdown("##### 📤 Bilan Énergétique Global")
        st.metric("Puissance mécanique absorbée ($\dot{W}$)", f"{puissance_totale:.3f} kW")
        
        # Détail visuel
        st.write("**Décomposition du besoin énergétique :**")
        detail_data = pd.DataFrame({
            "Composante": ["Variation d'Enthalpie", "Compensation Thermique"],
            "Puissance (kW)": [puissance_h, abs(puissance_q)]
        })
        st.bar_chart(detail_data, x="Composante", y="Puissance (kW)", color="Composante")

    # Correction de l'erreur NameError : utilisation de r""" pour le LaTeX
    st.warning(r"""
    **Interprétation Thermodynamique :** Le compresseur consomme de la puissance mécanique pour deux raisons :
    1. Augmenter l'énergie interne et le travail d'écoulement du gaz ($\Delta h$).
    2. Compenser la chaleur perdue vers l'extérieur ($q < 0$).
    
    Formule : $\dot{W} = \dot{m} [(h_2 - h_1) - q]$.
    """)

# ==========================================
# CAS 3 : SIMULATION DE LA TURBINE (NOUVEAU)
# ==========================================
else:
    st.subheader("⚙️ Paramètres de la Turbine")
    st.caption("Machine motrice : conversion de l'enthalpie du fluide en travail mécanique")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown("##### 📥 Paramètres de Détente")
        m_turb = st.number_input("Débit massique $\dot{m}$ (kg/s)", value=5.0, step=0.5)
        h1_t = st.number_input("Enthalpie d'entrée $h_1$ (kJ/kg)", value=3200.0)
        h2s_t = st.number_input("Enthalpie isentropique sortie $h_{2s}$ (kJ/kg)", value=2400.0)
        eta_t = st.slider("Rendement isentropique $\eta_t$ (%)", 60, 100, 88) / 100

    # --- Calculs Turbine ---
    # Travail isentropique (maximum récupérable) : h1 - h2s
    w_s = h1_t - h2s_t
    # Travail réel récupéré : w_reel = w_s * rendement
    w_reel = w_s * eta_t
    
    puissance_max = m_turb * w_s
    puissance_generee = m_turb * w_reel
    pertes_t = puissance_max - puissance_generee

    with col2:
        st.markdown("##### 📤 Puissance Produite")
        c1, c2 = st.columns(2)
        c1.metric("Puissance Max (Idéale)", f"{puissance_max:.2f} kW")
        c2.metric("Puissance Réelle (Produite)", f"{puissance_generee:.2f} kW", 
                  delta=f"-{pertes_t:.2f} kW dues aux frottements", delta_color="normal")

        st.write("**Répartition de l'énergie disponible :**")
        chart_data_t = pd.DataFrame({
            "Désignation": ["Travail Récupéré", "Énergie perdue (Chaleur/Frottement)"],
            "Puissance (kW)": [puissance_generee, pertes_t]
        })
        st.bar_chart(chart_data_t, x="Désignation", y="Puissance (kW)", color="Désignation")

    st.success(r"💡 **Note Master** : Pour une turbine, le travail réel est inférieur au travail idéal ($\dot{W}_{réel} = \dot{W}_s \cdot \eta_t$).")

# --- Pied de page ---
st.divider()
st.write("📖 *Ce simulateur utilise les méthodologies des exercices 1 , 2 et 3 du module Turbomachines.*")