import main
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
import json

netmap = main.update_node_dict()
netmap = main.update_node_dict()
nodes = []
edges = []

for key, values in netmap.items():
    nodes.append({"data": {"id": key, "label": key}})
    for value in values:
        edges.append({"data": {"id": key+value, "source": key, "target": value}})

json_obj = {
    "nodes": nodes,
    "edges": edges
}

file = open("graph.json", "w")
file.write(json.dumps(json_obj))
print(json.dumps(json_obj))
