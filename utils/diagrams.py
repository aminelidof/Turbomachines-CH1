import plotly.graph_objects as go
import numpy as np

def brayton():
    # Simulation des courbes isobares réelles (Gaz Parfait)
    s_range = np.linspace(1, 2.2, 100)
    # Courbes exponentielles pour les pressions constantes
    t_iso_p1 = 300 * np.exp(0.4 * (s_range - 1))  
    t_iso_p2 = 600 * np.exp(0.4 * (s_range - 1.2)) 
    
    fig = go.Figure()
    
    # Ajout des lignes de pression (Isobares)
    fig.add_trace(go.Scatter(x=s_range, y=t_iso_p1, name="P1 (Basse Pression)", line=dict(color='blue', dash='dash')))
    fig.add_trace(go.Scatter(x=s_range, y=t_iso_p2, name="P2 (Haute Pression)", line=dict(color='red', dash='dash')))
    
    # Points du cycle : 1->2 (Compression), 2->3 (Chauffe), 3->4 (Détente), 4->1
    S_cycle = [1.0, 1.15, 1.9, 2.05, 1.0] 
    T_cycle = [300, 650, 1300, 900, 300]
    
    fig.add_trace(go.Scatter(x=S_cycle, y=T_cycle, mode="lines+markers+text", 
                             text=["1", "2", "3", "4", ""], textposition="top center",
                             name="Cycle Réel", line=dict(color='black', width=3)))
    
    fig.update_layout(title="Cycle de Brayton (T-s) - Niveau Master", 
                      xaxis_title="Entropie (s)", yaxis_title="Température (T)")
    return fig

def rankine():
    # Tracé de la cloche de saturation de l'eau (Approximation Master)
    s_dome = np.linspace(0.4, 8.5, 100)
    t_dome = 374 * np.exp(-0.05 * (s_dome - 4.4)**2) + 20

    # Points du cycle Rankine (Pompe -> Chaudière -> Turbine -> Condenseur)
    S_cycle = [1.5, 1.5, 6.5, 6.5, 1.5]  # Entropie
    T_cycle = [45, 50, 550, 160, 45]     # Température

    fig = go.Figure()

    # Ajout du dôme de vapeur
    fig.add_trace(go.Scatter(x=s_dome, y=t_dome, name="Cloche de saturation", line=dict(color='gray')))

    # Ajout du tracé du cycle
    fig.add_trace(go.Scatter(x=S_cycle, y=T_cycle, mode="lines+markers+text",
                             text=["1", "2", "3", "4", "1"],
                             textposition="top center",
                             name="Cycle de Rankine", line=dict(color='blue', width=3)))

    fig.update_layout(title="Cycle de Rankine (T-s) - Niveau Master",
                      xaxis_title="s (kJ/kg.K)", yaxis_title="Température T (°C)")
    return fig
