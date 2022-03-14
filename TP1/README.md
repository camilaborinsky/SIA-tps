# TP1: Métodos de búsqueda

### Problema a resolver: Rompecabezas de números

8 números en una grilla de 3x3

## Dependencias

- Python 3+
- pip

## Ejecución

```
pip install -r requirements.txt
python number_puzzle_solver.py
```

## Parámetros

Las configuraciones de ejecución pueden realizarse en el archivo _config.json_ que se encuentra en la raíz del tp 1. \
Este archivo tiene la siguiente estructura:

```
{
  "board": [
    [2, 5, 3],
    [1, 7, 4],
    [0, 8, 6]
  ],
  "algorithm": "LGS",
  "heuristic": "inversions"
}
```

### Tablero

El campo _board_ del archivo de configuración de ejecución se corresponde con el tablero del estado inicial del problema.\
Consiste en una matriz de 3x3 (un array de arrays de long. 3) donde cada número representa la ficha que contiene a ese número y el 0 representa el espacio vacío.

### Algoritmos

A continuación las posibilidades para el campo _algorithm_ correspondiente a la estrategia de búsqueda que se va a emplear

**No informados**

- DFS : depth-first search (primero en profundidad)
- BFS : breath-first search (primero en anchura)
- VDS : variable-depth search (primero en profundidad con cota variable)

**Informados**

- A\* :
- LGS : local greedy search (heurística local)
- GGS : global greedy search (heurística global)

### Heurísticas

A continuación se mencionan las heurísticas elegidas, es decir las opciones posibles para el campo _heuristic_ del archivo de configuración

**Admisible**

- _manhattan_
- _hamming_

**No Admisible**

- _inversions_
