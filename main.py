from icmplib import traceroute
import socket

nodeDict = {}
running = True
while(running):

    destination = input("Enter a website: ")
    hops = traceroute(socket.gethostbyname(destination))

    last_distance = 0
    previousAddress = ""
    for hop in hops:
        #name, alias, addresslist = socket.gethostbyaddr(hop.address)
        
        if last_distance + 1 != hop.distance:
            print('Some gateways are not responding')
        else:
            if not nodeDict[hop.address]:
                nodeDict[hop.address]= []
            
            if previousAddress:
                nodeDict[previousAddress].append(hop.address)
            previousAddress = hop.address

        last_distance = hop.distance

    correctInput = False
    while(not correctInput):
        keepGoing = ""
        keepGoing = input("Input Another?(y/N)").lower()
        if(keepGoing == "n"):
            correctInput = True
            running = False
        elif(keepGoing == "y"):
            correctInput = True
        else:
            continue



print(nodeDict)
