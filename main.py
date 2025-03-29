from icmplib import traceroute
import socket

nodeDict = {}

destination = input("Enter a website:")
hops = traceroute(socket.gethostbyname(destination))

last_distance = 0
for hop in hops:
    print("o3o")
    name, alias, addresslist = socket.gethostbyaddr(hop.address)
    nodeDict[hop.address] = name
    #if last_distance + 1 != hop.distance:
    #    print('Some gateways are not responding')
    last_distance = hop.distance

print(nodeDict)
