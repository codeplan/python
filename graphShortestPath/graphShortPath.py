###################################################
# Shortest path problem using Dijkistra Algorithm,
# -- By Avdesh kr Singh, singh.avdesh.k@gmail.com
###################################################

import math
from collections import namedtuple
from collections import defaultdict

constants = namedtuple('constants', 'radius')
CONST = constants(radius=4000)

class CloudTravel:

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
  
    def addNodes(self, count):
        for i in range(count):
            self.nodes.add(i)
  
    def addEdge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
#        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
#        self.distances[(from_node, to_node)] = distance


    def latLonArc(self, latLong1=(), latLong2=()):
        
        lat1 = math.radians(float(latLong1[0]))
        lon1 = math.radians(float(latLong1[1]))
        lat2 = math.radians(float(latLong2[0]))
        lon2 = math.radians(float(latLong2[1]))

        arc = CONST.radius * \
    math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * \
                    math.cos(lon1 - lon2))
        return int(arc)

    ## Dijkistra Algorithm ##
    def getDist(self, initial, dest):
        visited = {initial: 0}
        nodes = set(self.nodes)
    
        while nodes: 
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node
      
            if min_node is None:
                break
      
            nodes.remove(min_node)
            current_weight = visited[min_node]
      
            if min_node == dest: break
      
            for edge in self.edges[min_node]:
                try:  
                    weight = current_weight + self.distances[(min_node, edge)]
                except:
                    continue
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
      
        return visited
    
    def shortestTrip(self, latitude, longitude, canTravel, origin, destination):
        canTravel = [ i.split(' ') for i in canTravel  ]
        canTravel = [ list(map(int, j)) for j in canTravel  ]
        latitude = list(latitude)
        longitude = list(longitude)
        self.makeNetwork(canTravel, latitude, longitude)
        d = self.getDist(origin, destination)
        
        if destination in d:
            return d[destination]
        else:
            return -1
    			
    def makeNetwork(self, canTravel, latitude, longitude):
        self.addNodes(len(canTravel)+1)
        
        for nodeFrom in range(len(canTravel)):
            for nodeTo in canTravel[nodeFrom]:
                dis = self.latLonArc((latitude[nodeFrom], longitude[nodeFrom]), \
                        (latitude[nodeTo], longitude[nodeTo]))
                self.addEdge(nodeFrom, nodeTo, dis)
                
if __name__ == "__main__":
    c = CloudTravel()

    ###### Change the inputs of line below #########
    #dist = c.shortestTrip(lat,lon,canTravel,origin,destination)
    dist = c.shortestTrip([0, 0, 70], [90, 0, 45],  ["2", "0 2", "0 1"], 0, 1)
    #dist = c.shortestTrip([0, 30, 60], [25, -130, 78],  ["1 2", "0 2", "1 2"], 0, 0)
    #dist = c.shortestTrip([0, 20, 55], [-20, 85, 42],  ["1", "0", "0"], 0, 2)

    if dist != -1:
        print("The distance from origin to destination is: %d"% dist)
    else:
        print("No available routes.")
