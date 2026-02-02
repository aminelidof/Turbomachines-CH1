import streamlit as st

st.header("✔️ Corrigés Méthodologiques")

# --- CORRECTION 1 ---
with st.expander("Solution Exercice 1 (Pompe)"):
    st.markdown(r"""
    **Méthodologie :**
    1. Pour un liquide incompressible : $w_p = \int v dP \approx v(P_2 - P_1)$.
    2. Conversion : $1 \, bar = 10^5 \, Pa$.
    3. Calcul :
       - $\Delta P = (60 - 0.5) \times 10^5 = 59.5 \times 10^5 \, Pa$.
       - $w_p = 0.001005 \times 59.5 \times 10^5 = 5979.75 \, J/kg = 5.98 \, kJ/kg$.
       - $\dot{W} = \dot{m} \times w_p = 35 \times 5.98 = \mathbf{209.29 \, kW}$.
    """)

# --- CORRECTION 2 ---
with st.expander("Solution Exercice 2 (Compresseur)"):
    st.markdown(r"""
    **Méthodologie :**
    1. Bilan d'énergie : $\dot{Q} - \dot{W} = \dot{m}(h_2 - h_1)$.
    2. Attention : $\dot{W}$ est le travail reçu par le fluide, si on cherche le travail *absorbé*, on prend la valeur absolue.
    3. Calcul :
       - $\dot{Q} = \dot{m} \times q_{perte} = 0.2 \times (-10) = -2 \, kW$.
       - $\dot{m}(h_2 - h_1) = 0.2 \times (523.63 - 300.19) = 44.69 \, kW$.
       - $\dot{W} = 44.69 - (-2) = \mathbf{46.69 \, kW}$.
    """)

# --- CORRECTION 3 ---
with st.expander("Solution Exercice 3 (Turbine)"):
    st.markdown(r"""
    **Méthodologie :**
    1. Travail isentropique (maximum possible) : $w_s = h_1 - h_{2s}$.
    2. Travail réel : $w_{réel} = \eta_t \times w_s$.
    3. Calcul :
       - $w_s = 1277 - 800 = 477 \, kJ/kg$.
       - $w_{réel} = 0.88 \times 477 = \mathbf{419.76 \, kJ/kg}$.
    """)

# --- CORRECTION 4 ---
with st.expander("Solution Exercice 4 (Tuyère)"):
    st.markdown(r"""
    **Méthodologie :**
    1. Bilan d'énergie pour une tuyère : $h_1 + \frac{V_1^2}{2} = h_2 + \frac{V_2^2}{2}$.
    2. Si $V_1 \approx 0$, alors $V_2 = \sqrt{2(h_1 - h_2)}$.
    3. **Attention aux unités :** Convertir $kJ/kg$ en $J/kg$ ($\times 1000$).
    4. Calcul :
       - $\Delta h = 3100 - 2800 = 300 \, kJ/kg = 300,000 \, J/kg$.
       - $V_2 = \sqrt{2 \times 300,000} = \sqrt{600,000} \approx \mathbf{774.6 \, m/s}$.
    """)

# --- CORRECTION 5 ---
with st.expander("Solution Exercice 5 (Cycle)"):
    st.markdown(r"""
    **Méthodologie :**
    1. Travail net du cycle : $W_{net} = W_{turbine} - W_{pompe}$.
    2. Rendement thermique : $\eta_{th} = \frac{W_{net}}{Q_{in}}$.
    3. Calcul :
       - $W_{net} = 1100 - 5 = 1095 \, kJ/kg$.
       - $\eta_{th} = \frac{1095}{2800} = 0.391 = \mathbf{39.1 \%}$.
    """)