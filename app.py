from flask import Flask, render_template, request, jsonify
from modelo import BuscadorCasa

app = Flask(__name__)
buscador = BuscadorCasa()

@app.route('/')
def index():
    # Carga la página principal
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    data = request.json
    modo = data.get('modo')
    inicio = data.get('inicio')
    meta = data.get('meta')
    
    # Ejecutamos el algoritmo de tu modelo.py
    if modo == "BFS":
        generador = buscador.bfs_paso_a_paso(inicio, meta)
    else:
        generador = buscador.dfs_paso_a_paso(inicio, meta)
    
    # Convertimos todos los pasos del generador a una lista para enviarla a la web
    pasos = list(generador)
    return jsonify(pasos)

if __name__ == '__main__':
    app.run(debug=True)