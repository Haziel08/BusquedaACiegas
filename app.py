import streamlit as st
from modelo import BuscadorCasa
import networkx as nx
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Tarea: Búsqueda a Ciegas", layout="wide")
st.title("Simulador de IA - Búsqueda a Ciegas")
st.write("Autor: Haziel Ibares Sánchez - UNAM FI")

# Inicializar el modelo en la sesión de Streamlit
if 'modelo' not in st.session_state:
    st.session_state.modelo = BuscadorCasa()
    st.session_state.iterador = None
    st.session_state.logs = ""

# --- BARRA LATERAL (CONTROLES) ---
with st.sidebar:
    st.header("Configuración")
    nodos = sorted(list(st.session_state.modelo.grafo.keys()))
    inicio = st.selectbox("Nodo de Inicio", nodos, index=nodos.index("Entrada"))
    meta = st.selectbox("Nodo Meta", nodos, index=nodos.index("Bodega"))
    
    col1, col2 = st.columns(2)
    if col1.button("Amplitud (BFS)"):
        st.session_state.iterador = st.session_state.modelo.bfs_paso_a_paso(inicio, meta)
        st.session_state.logs = ">>> MODO AMPLITUD <<<\n"
        
    if col2.button("Profundidad (DFS)"):
        st.session_state.iterador = st.session_state.modelo.dfs_paso_a_paso(inicio, meta)
        st.session_state.logs = ">>> MODO PROFUNDIDAD <<<\n"

    if st.button("Siguiente Paso >"):
        if st.session_state.iterador:
            try:
                # Obtener el siguiente estado de tu lógica original
                estructura, actual, visitados, ruta = next(st.session_state.iterador)
                
                # Actualizar Log
                log_actual = f"\n--- OPEN ---\n"
                for est in estructura:
                    log_actual += f"| {est['nodo']}({est['padre'] or 'Root'})\n"
                log_actual += f"\n--- CLOSE ---\n{', '.join(visitados)}\n"
                
                if ruta:
                    log_actual += f"\n✔ RUTA: {' -> '.join(ruta)}"
                
                st.session_state.logs = log_actual
                st.session_state.visitados = visitados
                st.session_state.ruta_final = ruta
            except StopIteration:
                st.warning("Búsqueda terminada.")

# --- CUERPO PRINCIPAL ---
col_grafo, col_log = st.columns([2, 1])

with col_log:
    st.subheader("Seguimiento (OPEN/CLOSE)")
    st.text_area("Log de estados", value=st.session_state.logs, height=500)

with col_grafo:
    st.subheader("Mapa de la Casa")
    # Lógica de dibujo similar a tu visualizador
    fig, ax = plt.subplots()
    G = nx.Graph(st.session_state.modelo.grafo)
    pos = nx.spring_layout(G, seed=42)
    
    visitados = getattr(st.session_state, 'visitados', [])
    ruta = getattr(st.session_state, 'ruta_final', None)
    
    colores = []
    for nodo in G.nodes():
        if ruta and nodo in ruta: colores.append('lightgreen')
        elif nodo in visitados: colores.append('orange')
        else: colores.append('skyblue')
        
    nx.draw(G, pos, with_labels=True, node_color=colores, node_size=800, font_size=8, ax=ax)
    st.pyplot(fig)