# Tarea 1: Búsqueda a Ciegas - Inteligencia Artificial

<p align="center">
  <img width="100%" alt="Portada" src="https://github.com/user-attachments/assets/tu-banner-ia-aqui.png" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-TERMINADO-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Escuela-UNAM%20FI-002b7a?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
</p>

---

## Índice

- [Descripción del proyecto](#descripción-del-proyecto)
- [Acceso al Proyecto (Demo en Vivo)](#acceso-al-proyecto-demo-en-vivo)
- [Características y Demostración](#características-y-demostración)
- [Algoritmos Implementados](#algoritmos-implementados)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)

---

## Descripción del proyecto

Este simulador interactivo fue desarrollado para la materia de **Inteligencia Artificial** en la Facultad de Ingeniería de la **UNAM**. El objetivo es visualizar y analizar el comportamiento de los algoritmos de búsqueda no informada (BFS y DFS) aplicados al recorrido de una casa inteligente.

El proyecto utiliza una arquitectura donde la lógica de búsqueda reside en **Python** (Backend), mientras que la interfaz gráfica y la gestión del grafo se realizan en el navegador mediante **JavaScript** y **Vis.js** para garantizar una respuesta fluida y dinámica.

---

## Acceso al Proyecto (Demo en Vivo)

Puedes interactuar con la aplicación directamente en el siguiente enlace:

🚀 **[https://busquedaaciegas.onrender.com/](https://busquedaaciegas.onrender.com/)**

> **Nota importante:** Debido a que el proyecto está alojado en una instancia gratuita de Render, el servidor puede tardar entre **30 y 60 segundos** en "despertar" y cargar la página por primera vez. Agradecemos su paciencia en la carga inicial.

---

## Características y Demostración

- **Selección de Nodos**: Permite configurar dinámicamente el punto de inicio y la meta deseada dentro del grafo de la casa.
- **Visualización Dinámica del Grafo**: 
  - 🟡 **Amarillo**: Nodo actualmente bajo análisis.
  - 🟠 **Naranja**: Nodos ya visitados (Lista CLOSE).
  - 🟢 **Verde**: Ruta final encontrada por el algoritmo.
- **Control de Ejecución**: Opción de avance manual paso a paso o ejecución automática con temporizador ajustable.
- **Log de Estados**: Seguimiento visual en tiempo real de las listas OPEN y CLOSE, incluyendo el tachado automático de nodos procesados.

---

## Algoritmos Implementados

1. **Búsqueda en Amplitud (BFS)**: Explora la casa por niveles de profundidad, garantizando encontrar la ruta con el menor número de nodos hasta la meta.
2. **Búsqueda en Profundidad (DFS)**: Prioriza la exploración exhaustiva de cada rama antes de realizar el retroceso (backtracking).

---

## Tecnologías Utilizadas

- **Backend**: Python 3.x y Flask.
- **Frontend**: HTML5, CSS3 (Paleta institucional UNAM) y JavaScript.
- **Librerías Gráficas**: Vis.js para la renderización del grafo dinámico.
- **Despliegue**: Render.

---

## Autor

| [<img src="https://avatars.githubusercontent.com/u/75911106?v=4" width=115><br><sub>Haziel Ibares Sánchez</sub>](https://github.com/Haziel08) |
| :---: |
