import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class VisualizadorGrafo:
    def __init__(self, master, grafo_dict):
        self.figure, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.figure, master=master)
        self.G = nx.Graph(grafo_dict)
        self.pos = nx.spring_layout(self.G, seed=42) # Posición fija para que no salte

    def dibujar(self, visitados=None, ruta=None):
        self.ax.clear()
        
        # Colores por defecto
        node_colors = ['#ADD8E6' for _ in self.G.nodes()] # Celeste
        
        if visitados:
            node_colors = []
            for node in self.G.nodes():
                if ruta and node in ruta:
                    node_colors.append('lightgreen') # Ruta final
                elif node in visitados:
                    node_colors.append('orange') # Visitados
                else:
                    node_colors.append('#ADD8E6')

        nx.draw(self.G, self.pos, with_labels=True, ax=self.ax, 
                node_color=node_colors, node_size=800, font_size=8)
        self.canvas.draw()

    def get_widget(self):
        return self.canvas.get_tk_widget()