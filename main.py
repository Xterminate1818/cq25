from icmplib import traceroute, NameLookupError, SocketPermissionError
import socket


def update_node_dict(nodeDict):
    destination = input("Enter a website: ")
    try:
        hops = traceroute(destination)
    except NameLookupError:
        print("Name Look Up Error... try another website T_T")
        return
    except SocketPermissionError:
        print("Please run with elevated privileges!")
        exit
    except:
        print("Unknown error conducting traceroute @_@ Try again?")
        return

    last_distance = 0
    previousKey = ""
    for hop in hops:
        
        if last_distance + 1 != hop.distance:
            continue
        else:

            try:
                name, alias, addresslist = socket.gethostbyaddr(hop.address)
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
    return nodeDict



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
