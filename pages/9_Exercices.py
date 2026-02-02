import streamlit as st

st.set_page_config(page_title="Exercices Turbomachines", layout="wide")
st.header("📝 Travaux Dirigés : Exercices d'Application (M1-GM)")

tabs = st.tabs([
    "Ex 1: Pompe Centrale", 
    "Ex 2: Compresseur Air", 
    "Ex 3: Turbine à Gaz", 
    "Ex 4: Tuyère", 
    "Ex 5: Cycle Rankine"
])

# --- EXERCICE 1 ---
with tabs[0]:
    st.subheader("⚙️ Exercice 1 : Pompe de centrale thermique")
    st.write("""
    **Énoncé :** Une pompe alimente une chaudière avec un débit de $35 \, kg/s$ d'eau liquide saturée à $0.5 \, bar$. 
    L'eau doit être comprimée jusqu'à $60 \, bar$. On suppose la compression isentropique.
    """)
    
    # Correction de l'affichage de la donnée avec \text{} pour les unités
    st.write(r"**Donnée :** $v \approx 0.001005 \text{ m}^3\text{/kg}$")
    
    ans1 = st.number_input("Calculer la puissance consommée (kW) :", key="ex1")
    
    # Calcul rigoureux : P = m * v * (P2 - P1)
    # Conversion : 1 bar = 100 kPa, donc le résultat est directement en kW
    p_ex1 = 35 * 0.001005 * (60 - 0.5) * 100 
    
    if st.button("Vérifier Ex 1"):
        if abs(ans1 - p_ex1) < 2:
            st.success(f"✅ Correct ! Puissance : {p_ex1:.2f} kW")
            st.markdown("---")
            st.markdown(r"**Rappel de la formule :** $\dot{W}_p = \dot{m} \cdot v \cdot (P_2 - P_1)$")
        else:
            st.error(r"❌ Indice : Travail d'une pompe = $v \cdot (P_2 - P_1)$. Vérifiez bien la conversion des bars en Pascals ou kiloPascals.")

# --- EXERCICE 2 ---
with tabs[1]:
    st.subheader("🌀 Exercice 2 : Compresseur d'air industriel")
    st.write("""
    **Énoncé :** De l'air entre dans un compresseur à $100 \, kPa$ et $300 \, K$. Il ressort à $600 \, kPa$ et $520 \, K$. 
    Le débit massique est de $0.2 \, kg/s$. On mesure une perte thermique vers l'extérieur de $10 \, kJ/kg$.
    *Données : $h_1 = 300.19 \, kJ/kg$, $h_2 = 523.63 \, kJ/kg$.*
    """)
    ans2 = st.number_input("Calculer la puissance absorbée sur l'arbre (kW) :", key="ex2")
    # Calcul : W = m * [(h2-h1) + q_perdu] -> W = 0.2 * [(523.63-300.19) + 10]
    p_ex2 = 0.2 * ((523.63 - 300.19) + 10)
    
    if st.button("Vérifier Ex 2"):
        if abs(ans2 - p_ex2) < 0.5:
            st.success(f"✅ Bravo ! La puissance est de {p_ex2:.2f} kW")
        else:
            st.error("❌ Rappel : $\dot{W} = \dot{m} \Delta h + \dot{Q}_{perdue}$.")

# --- EXERCICE 3 ---
with tabs[2]:
    st.subheader("🔥 Exercice 3 : Turbine à gaz (Rendement)")
    st.write("""
    **Énoncé :** Les gaz brûlés entrent dans une turbine à $1200 \, K$ ($h_1 = 1277 \, kJ/kg$) et ressortent à une pression telle que l'enthalpie isentropique serait $h_{2s} = 800 \, kJ/kg$. 
    Le rendement isentropique de la turbine est de $88\%$.
    """)
    ans3 = st.number_input("Calculer le travail réel produit par kg de gaz (kJ/kg) :", key="ex3")
    # Calcul : W_reel = eta * (h1 - h2s) = 0.88 * (1277 - 800)
    p_ex3 = 0.88 * (1277 - 800)
    
    if st.button("Vérifier Ex 3"):
        if abs(ans3 - p_ex3) < 1:
            st.success(f"✅ Correct ! Travail extrait : {p_ex3:.2f} kJ/kg")
        else:
            st.error("❌ Rappel : $\eta_{turbine} = w_{réel} / w_{isentropique}$.")

# --- EXERCICE 4 ---
with tabs[3]:
    st.subheader("🚀 Exercice 4 : Tuyère de propulsion")
    st.write("""
    **Énoncé :** De la vapeur d'eau entre dans une tuyère adiabatique à $h_1 = 3100 \, kJ/kg$ avec une vitesse négligeable. 
    En sortie, l'enthalpie est de $h_2 = 2800 \, kJ/kg$.
    """)
    ans4 = st.number_input("Calculer la vitesse de sortie du fluide (m/s) :", key="ex4")
    # Calcul : V2 = sqrt(2 * (h1 - h2) * 1000)
    p_ex4 = (2 * (3100 - 2800) * 1000)**0.5
    
    if st.button("Vérifier Ex 4"):
        if abs(ans4 - p_ex4) < 5:
            st.success(f"✅ Vitesse de sortie : {p_ex4:.2f} m/s")
        else:
            st.error("❌ Indice : Utilisez le bilan d'énergie cinétique $V_2 = \sqrt{2 \Delta h}$. Attention aux kJ !")

# --- EXERCICE 5 ---
with tabs[4]:
    st.subheader("💡 Exercice 5 : Évaluation d'un Cycle de Rankine")
    st.write("""
    **Énoncé :** Dans une centrale, le travail de la turbine est de $1100 \, kJ/kg$ et le travail de la pompe est de $5 \, kJ/kg$. 
    La chaleur apportée dans la chaudière est de $2800 \, kJ/kg$.
    """)
    ans5 = st.number_input("Calculer le rendement thermique du cycle (%) :", key="ex5")
    # Calcul : (W_turb - W_pompe) / Q_in = (1100 - 5) / 2800 * 100
    p_ex5 = ((1100 - 5) / 2800) * 100
    
    if st.button("Vérifier Ex 5"):
        if abs(ans5 - p_ex5) < 0.1:
            st.success(f"✅ Correct ! Rendement du cycle : {p_ex5:.2f} %")
        else:
            st.error("❌ Rappel : $\eta_{th} = W_{net} / Q_{chaudière}$.")