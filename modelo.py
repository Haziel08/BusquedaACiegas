import collections

class BuscadorCasa:
    def __init__(self):
        # Conexiones de la casa (Grafo)
        self.grafo = {
            'Entrada': ['Sala', 'Garage'], 'Sala': ['Entrada', 'Estudio', 'Comedor', 'Garage', 'Pasillo'],
            'Estudio': ['Sala', 'Oficina'], 'Oficina': ['Estudio', 'Pasillo'],
            'Comedor': ['Sala', 'Cocina', 'Pasillo'], 'Cocina': ['Comedor', 'Patio', 'Lavandería'],
            'Pasillo': ['Sala', 'Comedor', 'Oficina', 'Rec1', 'Rec2', 'Baño1', 'Escaleras'],
            'Rec1': ['Pasillo', 'Lavandería'], 'Rec2': ['Pasillo', 'Baño2'],
            'Baño1': ['Pasillo'], 'Baño2': ['Rec2'], 'Garage': ['Entrada', 'Sala', 'Patio'],
            'Patio': ['Garage', 'Cocina', 'Lavandería', 'Terraza'],
            'Lavandería': ['Cocina', 'Patio', 'Rec1', 'Bodega'], 'Bodega': ['Lavandería'],
            'Escaleras': ['Pasillo', 'Terraza'], 'Terraza': ['Escaleras', 'Patio']
        }

    def bfs_paso_a_paso(self, inicio, meta):
        # Amplitud: Cola (FIFO) -> Sale el de arriba, entran por abajo
        cola = [{'nodo': inicio, 'padre': None, 'ruta': [inicio]}]
        close = []
        historial_open = []
        
        while cola:
            actual = cola.pop(0)
            historial_open.append(actual)
            
            if actual['nodo'] not in close:
                close.append(actual['nodo'])
                if actual['nodo'] == meta:
                    yield historial_open + cola, actual, close, actual['ruta']
                    return

                for s in self.grafo.get(actual['nodo'], []):
                    if s not in close and s not in [n['nodo'] for n in cola]:
                        cola.append({'nodo': s, 'padre': actual['nodo'], 'ruta': actual['ruta'] + [s]})
            
            yield historial_open + cola, actual, close, None

    def dfs_paso_a_paso(self, inicio, meta):
        # Pila (LIFO) -> Sale el de arriba, entran por arriba
        pila = [{'nodo': inicio, 'padre': None, 'ruta': [inicio]}]
        close = []
        historial_open = []
        
        while pila:
            actual = pila.pop()
            historial_open.append(actual)
            
            if actual['nodo'] not in close:
                close.append(actual['nodo'])
                if actual['nodo'] == meta:
                    yield historial_open + pila, actual, close, actual['ruta']
                    return

                # Obtenemos sucesores y los metemos a la pila SOLO si no están en CLOSE ni en la PILA actual
                sucesores = reversed(self.grafo.get(actual['nodo'], []))
                for s in sucesores:
                    nodos_en_pila = [n['nodo'] for n in pila]
                    if s not in close and s not in nodos_en_pila:
                        pila.append({'nodo': s, 'padre': actual['nodo'], 'ruta': actual['ruta'] + [s]})
            
            yield historial_open + pila, actual, close, None