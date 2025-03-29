import main
import json

# Takes a dictionary of {hosts: edges} and returns a cytoscape json blob
def make_json_blob(dict):
    nodes = []
    edges = []
    for key, values in dict.items():
        nodes.append({"data": {"id": key, "label": key}})
        for value in values:
            edges.append({"data": {"id": key+value, "source": key, "target": value}})

    return json.dumps({
        "nodes": nodes,
        "edges": edges
    })

if __name__ == "__main__":
    netmap = main.update_node_dict({})
    netmap = main.update_node_dict(netmap)
    json = make_json_blob(netmap)
    print(json)
    file = open("./graph.json", "w")
    file.write(json)
