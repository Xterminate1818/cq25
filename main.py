from icmplib import traceroute, NameLookupError, SocketPermissionError
import socket


nodeDict = {}
hostnameNodeDict = {}

def update_node_dict():
    destination = input("Enter a website: ")
    try:
        hops = traceroute(destination)
    except NameLookupError:
        print("Name Look Up Error... try another website T_T")
    except SocketPermissionError:
        print("Please run with elevated privileges!")
    except:
        print("Unknown error conducting traceroute @_@")

    last_distance = 0
    previousAddress = ""
    for hop in hops:
        
        if last_distance + 1 != hop.distance:
            print('Some gateways are not responding')
        else:

            if hop.address not in nodeDict:
                nodeDict[hop.address]= []

            if previousAddress:
                nodeDict[previousAddress].append(hop.address)
            
            previousAddress = hop.address
            

            try:
                name, alias, addresslist = socket.gethostbyaddr(hop.address)
                update_hostname_node_dict(addresslist, name)
            except:
                continue
            
        last_distance = hop.distance
    return nodeDict

def update_hostname_node_dict(ip_address, host_name):
    hostnameNodeDict = nodeDict
    hostnameNodeDict[ip_address, host_name]
    return hostnameNodeDict


if __name__ == "__main__":
    running = True
    while(running):

        update_node_dict()

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
