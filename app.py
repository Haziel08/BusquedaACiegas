from flask import Flask, render_template, request, jsonify
from modelo import BuscadorCasa

app = Flask(__name__)
buscador = BuscadorCasa()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nodos', methods=['GET'])
def obtener_nodos():
    # Enviamos los nombres de las habitaciones para llenar los selectores
    return jsonify(sorted(list(buscador.grafo.keys())))

@app.route('/buscar', methods=['POST'])
def buscar():
    data = request.json
    modo = data.get('modo')
    inicio = data.get('inicio')
    meta = data.get('meta')
    
    # Obtenemos todos los pasos del generador de modelo.py
    if modo == "BFS":
        pasos = list(buscador.bfs_paso_a_paso(inicio, meta))
    else:
        pasos = list(buscador.dfs_paso_a_paso(inicio, meta))
    
    return jsonify(pasos)

if __name__ == '__main__':
    app.run(debug=True)