class Search:

    def __init__(self, layout, startPos, goalPos, goalPos_2):
        self.path = []
        self.frontier = []
        self.explored_set = []
        self.goal = goalPos
        self.goal_2 = goalPos_2
        self.layout = layout
        self.start_pos = self.validNode(startPos)
        
#adds the position of the top, bottom,left, right to the current node as item in a dict
######################################################################################################################
    def validNode(self, pos):
        node = {"pos": [pos[0], pos[1]]}

        if (pos[0] - 1) >= 0:
            node.update({"top": [pos[0]-1, pos[1]]})

        if(pos[0] + 1) < len(self.layout):
            node.update({"bottom": [pos[0]+1, pos[1]]})
        
        if(pos[1] + 1) < len(self.layout[0]):
            node.update({"right": [pos[0], pos[1]+1 ]})
        
        if(pos[1] - 1) >= 0:
            node.update({"left": [pos[0], pos[1]-1 ]})

        return node
########################################################################################################################


#checks to see if the node has been visited before
########################################################################################################################
    def visitable(self, node):
        if node not in self.explored_set:
            node = self.validNode(node)
            self.frontier.append(node)
########################################################################################################################


# explore neighbors anti-clockwise starting by the one on the left
########################################################################################################################
    def check (self, node):
        if ('left' in node.keys() and self.layout[node["left"][0]][node["left"][1]] == 'clear'):
            self.visitable(node["left"])

        if 'bottom' in node.keys()  and self.layout[node["bottom"][0]][node["bottom"][1]] == 'clear':
            self.visitable(node["bottom"])

        if 'right' in node.keys() and self.layout[node["right"][0]][node["right"][1]] == 'clear':
            self.visitable(node["right"])

        if 'top' in node.keys() and self.layout[node["top"][0]][node["top"][1]] == 'clear': 
            self.visitable(node["top"])



# Calculate the heuristic value
########################################################################################################################
    def get_heuristic(self):
        h1 = 10 * (abs(self.start_pos.x - self.goal.x) + abs(self.start_pos.y - self.goal.y))
        if self.goal_2 is not None:
            h2 = 10 * (abs(self.start_pos.x - self.goal_2.x) + abs(self.start_pos.y - self.goal_2.y))
        if (h2 is not None and h2 < h1):
            return h2
        else:
            return h1


            
########################################################################################################################

    def update_cell_obj(self, adj, cell_obj):
        adj.g = cell_obj.g + 10
        adj.h = self.get_heuristic()
        adj.parent = cell_obj
        adj.f = adj.h + adj.g

########################################################################################################################

    def shortestPath(self, adj, cell_obj):
        if adj.g > cell_obj.g + 10:
            self.update_cell_obj(adj, cell_obj)
        else:
            self.update_cell_obj(adj, cell_obj)

########################################################################################################################

class cell_block(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0




