from flask import Flask
from flask import request
from icmplib import traceroute, NameLookupError, SocketPermissionError
import socket
import json

app = Flask(__name__, static_folder = "./")

if __name__ == "__main__":
    app.run(debug=False)

@app.route("/", methods = ['GET', 'POST'])
def index():
    return open("index.html").read()

@app.route("/api/<request_name>", methods = ['GET', 'POST'])
def getRoute(request_name):
    if request.method == 'GET':
        print(request_name)
        nodeDict = {}

        try:
            hops = traceroute(request_name)
        except NameLookupError:
            print("Name Look Up Error... try another website T_T")
            return
        except SocketPermissionError:
            print("Please run with elevated privileges!")
            return
        except Exception as e:
            print(e)

        last_distance = 0
        previousKey = ""
        for hop in hops:
            if last_distance + 1 != hop.distance:
                continue
            else:

                try:
                    name, _, _ = socket.gethostbyaddr(hop.address)
                except:
                    if hop.address not in nodeDict:
                        nodeDict[hop.address]= []

                    if previousKey:
                        nodeDict[previousKey].append(hop.address)
                    previousKey = hop.address
                else:
                    if name not in nodeDict:
                        nodeDict[name]= []

                    if previousKey:
                        nodeDict[previousKey].append(name)
                    previousKey = name

            last_distance = hop.distance
        netmap = nodeDict
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

        return json.dumps(json_obj)
