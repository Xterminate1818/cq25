import matplotlib.pyplot as plt

edges = []
for key, values in nodeDict.items():
    for value in values:
        edges.append((key, value))
G = nx.Graph()
G.add_edges_from(edges)
nx.draw_networkx(G)
plt.show()
