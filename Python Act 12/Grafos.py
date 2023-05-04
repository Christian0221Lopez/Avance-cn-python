# Librerías
# ======================================================================================
import networkx as nx
import numpy as np
import pandas as pd
import warnings
import scipy as sp
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

G = nx.Graph()
print(G)

G.is_directed()

Grafos = pd.read_csv(
    "C:\\Users\\USER\\Documents\\UdeG\\Seminario Estructuras de Datos 2\\Python Act 12\\Lineas de CDMX.txt",
    header=None,
    sep=",",
    names=["Nodo", "Relacion"],
)

relaciones = np.zeros((len(Grafos), 2), dtype=int)

for i, row in Grafos.iterrows():
    relaciones[i][0] = int(row["Nodo"])
    relaciones[i][1] = int(row["Relacion"])

print("Arreglo Bidimencional")

for i in relaciones:
    print(i)

print(Grafos)
# Añadir multiples nodos
# ======================================================================================
for i in range(len(relaciones)):
    nodo_1 = relaciones[i][0]
    nodo_2 = relaciones[i][1]
    G.add_node(nodo_1)
    G.add_node(nodo_2)
    G.add_edge(nodo_1, nodo_2)

fig, ax = plt.subplots(figsize=(1, 1))
nx.draw(G, with_labels=True, ax=ax)
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])

print(G)

adjM = nx.adjacency_matrix(G)
IncM = nx.incidence_matrix(G)

with open("C:\\Users\\USER\\Documents\\UdeG\\Seminario Estructuras de Datos 2\\Python Act 12\\Lineas de CDMX Matriz de Adyacencia.txt"
          ,"w") as archivo:
  for i in range(adjM.shape[0]):
    for j in range(adjM.shape[1]):
        archivo.write(f"{int(adjM[i,j])} ")
    archivo.write("\n")


with open("C:\\Users\\USER\\Documents\\UdeG\\Seminario Estructuras de Datos 2\\Python Act 12\\Lineas de CDMX Matriz de Incidencia.txt"
          ,"w") as archivo:
    for i in range(IncM.shape[0]):
        for j in range(IncM.shape[1]):
            archivo.write(f"{int(IncM[i,j])} ")
        archivo.write("\n")

plt.show()