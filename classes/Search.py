class Search:

    def __init__(self, layout, startPos, goalPos):
        self.path = []
        self.frontier = []
        self.explored_set = []
        self.goal = goalPos
        self.layout = layout
        self.start_pos = self.validNode(startPos)
        #self.stack.append(self.start_pos)


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


#checks to see if the current node has a valid neighbour and if that neighbour is 'clear'
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
########################################################################################################################
      
