# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 10:33:33 2023

@author: Gadiel Jimenez
"""

def prim(graph):
    mst = set()
    visited = set()
    node = list(graph.keys())[0]
    visited.add(node)
    while visited != set(graph.keys()):
        candidates = []
        
        for n in visited:
            for m, weight in graph[n].items():
                if m not in visited:
                    candidates.append((n, m, weight))
        edge = min(candidates, key=lambda x: x[2])
        mst.add(edge)
        visited.add(edge[1])
        print(f"Seleccionamos la arista {edge[0]}-{edge[1]} de peso {edge[2]}")
    return mst

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1}
}
mst = prim(graph)
print("El árbol de expansión mínima es:")
print(mst)
