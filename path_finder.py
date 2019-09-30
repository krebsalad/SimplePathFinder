# Author: Krebsalad
# date: 30 09 19
# made with : pydroid python3 IDE

class Node:
    
    def __init__ (self, _x, _y, _z=0):
	    self.x = _x
	    self.y = _y
	    self.z = _z
	    self.reset()
    
    def reset(self):
        self.visited = False
        self.walkable = True
        self.adjacent_nodes = []
        self.distance = 0
        self.heuristic = 0
        self.parent = None
   
    def totalCost(self):
	    return self.distance + self.heuristic

class PathFinder:
    
    def __init__ (self, _map):
        self.nodes = _map
        self.path = []
        self.closedList = []
        self.process = []
    
    def getNodeFromProcess(self, _x, _y, _z):
        for n in self.process:
            if(n.x == _x and n.y == _y and n.z == _z):
                return n
        return None
         
    def getNodeFromClosedList(self, _x, _y, _z):
        for n in self.closedList:
            if(n.x == _x and n.y == _y and n.z == _z):
                return n
        return None
    
    def findAdjacentNodes(self, adjacent_val=1.5):
        # find adjacent nodes
        for n1 in self.nodes:
            for n2 in self.nodes:
                if(n1 != n2):
                    if(abs(n1.x - n2.x) <= adjacent_val):
                        if(abs(n1.y - n2.y) <= adjacent_val):
	                        if(abs(n1.z - n2.z) <= adjacent_val):
	                            n1.adjacent_nodes.append(n2)
                    
    def calculateNodeHeuristic(self, n1, n2):
        # pythagoras theorem without sqrt
        a = pow(abs(n1.x - n2.x), 2)
        b = pow(abs(n1.y - n2.y), 2)
        c = pow(abs(n1.z - n2.z), 2)
        return a + b + c
    
    def findPath(self, start, target, range=5):
        # to return nodes
        self.path = []
        
        # non visited list, used to determine to process node
        self.process = []
        self.process.append(start)
        
        # visited list
        self.closedList = []
        
        # pythagoras theorem
        estimated_distance = self.calculateNodeHeuristic(start, target)
        
        # reset node heuristics
        for n in self.nodes:
             n.reset()
        
        # find adjacent nodes up.to 1.5 units
        self.findAdjacentNodes()
       
        print("  finding path from ", start.x, ",", start.y, " to ", target.x, ",",target.y)
        
        # find path
        while(True):
            
            # exit when no nodes left to process
            if(len(self.process) == 0):
                print(" did not find path")
                break
            
            # take lowest cost from process list
            new_i = -1
            lowest_cost = estimated_distance * 2
            for i, n in enumerate(self.process):
                if(n.totalCost() < lowest_cost):
                    lowest_cost  = n.totalCost()
                    new_i = i
            
            # exit if non was found
            if(new_i == -1):
                 print("  did not find path")
                 break
            
            # set current node
            currentNode = self.process.pop(new_i)
            
            # exit if path found
            if(currentNode.x == target.x and currentNode.y == target.y and currentNode.z == target.z):
                print("  found a path")
                break
            
            # add node to closed list
            currentNode.visited = True
            self.closedList.append(currentNode)
            
            # go through adjacent nodes
            for a_n in currentNode.adjacent_nodes:
                # to ignore tiles
                if( a_n.visited or not a_n.walkable):
                    continue
                
                # set heuristics and distance if node not in process yet
                if(self.getNodeFromProcess(a_n.x, a_n.y, a_n.z) == None):
                    a_n.parent = currentNode
                    a_n.distance = currentNode.distance + 1
                    a_n.heuristic = self.calculateNodeHeuristic(a_n, target)
                    self.process.append(a_n)
                    continue
                 
                 # if node is in process, change distance and path if needed
                if(a_n.distance < currentNode.distance):
                     a_n.parent = currentNode
                     a_n.distance = 1 + currentNode.distance
    
        # create path from parent of last tile
        next_n = target
        while not (next_n == None ):
            self.path.append(next_n)
            next_n = next_n.parent
