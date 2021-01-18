class Depth_First:
    def __init__(self, layout, startPos, goalPos):
        self.path = []
        self.stack = []
        self.explored_set = []
        self.goal = goalPos
        self.layout = layout
        self.start_pos = self.validNode(startPos)
        self.stack.append(self.start_pos)
######################################################################################################################

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

########################################################################################################################
    def start(self):
        
        if not self.stack:
            print("stack empty")
            return

        node = self.stack.pop()

        if self.layout[node["pos"][0]][node["pos"][1]] == 'goal':
            print("goal found")
            return

        self.explored_set.append(node["pos"])

        if ('left' in node.keys() and self.layout[node["left"][0]][node["left"][1]] == 'clear'):
            self.check(node["left"])

        if 'bottom' in node.keys()  and self.layout[node["bottom"][0]][node["bottom"][1]] == 'clear':
                    self.check(node["bottom"])

        if 'right' in node.keys() and self.layout[node["right"][0]][node["right"][1]] == 'clear':
            self.check(node["right"])

        if 'top' in node.keys() and self.layout[node["top"][0]][node["top"][1]] == 'clear': 
                    self.check(node["top"])


        self.start()
########################################################################################################################

########################################################################################################################
    def check(self, node):
        if node not in self.explored_set:
            node = self.validNode(node)
            self.stack.append(node)
            self.path.append(node)


