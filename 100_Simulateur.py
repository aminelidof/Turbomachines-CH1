import streamlit as st

st.header("🧪 Simulateur de Turbomachines (M1 GPM)")

# Sélection du type de machine avec les nouveaux intitulés
type_machine = st.radio(
    "Sélectionnez le type de machine à simuler :", 
    ["💧 Pompe (Liquide Incompressible)", "💨 Compresseur (Gaz/Air)"]
)

st.divider()

if "Pompe" in type_machine:
    st.subheader("⚙️ Analyse d'une Pompe")
    st.info("Hypothèse : Fluide incompressible (v = constante).")
    
    col1, col2 = st.columns(2)
    with col1:
        m = st.slider("Débit massique $\dot{m}$ (kg/s)", 1.0, 50.0, 35.0)
        dp = st.slider("Élévation de pression $\Delta P$ (bar)", 0.5, 100.0, 40.0)
    
    with col2:
        # Valeur précise pour l'eau à 40 bar (Master 1)
        v = st.number_input("Volume massique $v$ ($m^3/kg$)", value=0.001005, format="%.6f")
        eta = st.slider("Rendement isentropique $\eta_p$ (%)", 50, 100, 85) / 100

    # Calculs
    # Puissance idéale : W = m * v * deltaP
    W_ideal = m * v * (dp * 1e5) / 1000 # kW
    # Puissance réelle : W_reel = W_ideal / rendement
    W_reel = W_ideal / eta

    # Affichage des résultats en métriques
    c1, c2 = st.columns(2)
    c1.metric("Puissance Idéale", f"{W_ideal:.2f} kW")
    c2.metric("Puissance Réelle (Arbre)", f"{W_reel:.2f} kW", delta=f"{W_reel - W_ideal:.2f} kW (Pertes)")

    

else:
    st.subheader("⚙️ Analyse d'un Compresseur d'air")
    st.caption("Modèle basé sur le bilan enthalpique (Système ouvert)")

    col1, col2 = st.columns(2)
    with col1:
        m_air = st.number_input("Débit massique $\dot{m}$ (kg/s)", value=0.02, format="%.3f")
        h1 = st.number_input("Enthalpie entrée $h_1$ (kJ/kg)", value=280.13)
    
    with col2:
        h2 = st.number_input("Enthalpie sortie $h_2$ (kJ/kg)", value=400.98)
        perte_q = st.number_input("Pertes thermiques $q$ (kJ/kg)", value=16.0)

    # Formule Master : W = m * ( (h2 - h1) + q_perte )
    # On considère ici le travail reçu par le fluide
    W_req = m_air * ((h2 - h1) + perte_q)

    st.metric("Puissance mécanique totale requise", f"{W_req:.3f} kW")
    
    st.warning(f"**Interprétation :** Sur les {W_req:.3f} kW fournis, {(m_air*(h2-h1)):.3f} kW servent à augmenter l'énergie du gaz et {(m_air*perte_q):.3f} kW sont dissipés en chaleur.")

    

st.divider()
st.write("👉 *Ce simulateur permet d'appliquer directement les équations du chapitre 1 pour les machines génératrices.*")