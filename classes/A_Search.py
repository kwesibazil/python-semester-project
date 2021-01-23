from tkinter.constants import X
from classes.Search import Search
from classes.Cell import Cell

class A_Search(Search):
    def __init__(self, layout, startPos, goalPos,  goalPos_2):
        self.goal = goalPos
        self.goal_2 = goalPos_2
        self.layout = layout

        self.cell = Cell(startPos[0], startPos[1])
        self.openList = []
        self.closeList = []
        self.openList.append(self.cell)
        self.search()
        self.explored_set = []


    def search (self):
        if not self.openList:  # if stack is empty then no solution
            return

        self.closeList.append(self.openList.pop(0))
        #node = self.closeList[0].x
        node = self.closeList[0]        # node = [node.x, node.y]
      
        if self.goal == node or self.goal_2 == node:
          return self.closeList

        self.check(node) 


    def check (self, node):
        node = self.validNode(node)
        neighb = node.neighb

        if ('left' in neighb.keys() and self.layout[neighb["left"][0]][neighb["left"][1]] == 'clear'):
            adj =  Cell(neighb["left"][0], neighb["left"][1])            #self.layout[neighb["left"][0]][node["left"][1]]
            if adj in self.closeList:
              self.check(adj)
            else:
              if adj in self.openList:
                self.shortestpath(adj, node)
              else:
                self.openList.append(adj)
                self.update_cell_obj(adj, node)
                self.check(adj)

       # if 'bottom' in neighb.keys()  and self.layout[neighb["bottom"][0]][node["bottom"][1]] == 'clear':
        if 'bottom' in neighb.keys() and self.layout[neighb["bottom"][0]][neighb["bottom"][1]] == 'clear':

            adj =  Cell(neighb["bottom"][0], neighb["bottom"][1])                     #self.layout[neighb["bottom"][0]][neighb["bottom"][1]]

            if adj in self.closeList:
              self.check(adj)
            else:
              if adj in self.openList:
                self.shortestpath(adj, node)
              else:
                self.openList.append(adj)
                self.update_cell_obj(adj, node)
               
        if 'right' in neighb.keys() and self.layout[neighb["right"][0]][neighb["right"][1]] == 'clear':
            
            adj =  Cell(neighb["right"][0], neighb["right"][1])                                                                      #self.layout[neighb["right"][0]][neighb["right"][1]]

            if adj in self.closeList:
              self.check(adj)
            else:
              if adj in self.openList:
                self.shortestpath(adj, node)
              else:
                self.openList.append(adj)
                self.update_cell_obj(adj, node)
                


        if 'top' in neighb.keys() and self.layout[neighb["top"][0]][neighb["top"][1]] == 'clear': 
          adj = Cell(neighb["top"][0], neighb["top"][1])               #self.layout[neighb["top"][0]][neighb["top"][1]]
          if adj in self.closeList:
            self.check(adj)
          else:
            if adj in self.openList:
              self.shortestpath(adj, node)
            else:
              self.openList.append(adj)
              self.update_cell_obj(adj, node)
              


    def update_cell_obj(self, adj, cell_obj):
          adj.g = cell_obj.g + 10
          adj.h = self.get_heuristic(adj)
          adj.parent = cell_obj
          adj.f = adj.h + adj.g

# Calculate the heuristic value
########################################################################################################################
    def get_heuristic(self, node):
       # h1 = 10 * (abs(self.start_pos.x - self.goal.x) + abs(self.start_pos.y - self.goal.y))
        h1 = 10 * (abs(node.pos[0] - self.goal[0]) + abs(node.pos[1] - self.goal[1]))
        # if self.goal_2 is not None:
        #     h2 = 10 * (abs(node.x - self.goal_2[0]) + abs(node.y - self.goal_2[1]))
        # if (h2 is not None and h2 < h1):
        #     return h2
       # else:
        return h1


    def shortestPath(self, adj, cell_obj):
          if adj.g > cell_obj.g + 10:
              self.update_cell_obj(adj, cell_obj)
          else:
              self.update_cell_obj(adj, cell_obj)



    def validNode(self, pos):

        node = {"pos": [pos.pos[0], pos.pos[1]]}

        if (pos.pos[0] - 1) >= 0:
            node.update({"top": [pos.pos[0]-1, pos.pos[1]]})

        if (pos.pos[0] - 1) >= 0:
            node.update({"top": [pos.pos[0]-1, pos.pos[1]]})

        if(pos.pos[0] + 1) < len(self.layout):
            node.update({"bottom": [pos.pos[0]+1, pos.pos[1]]})
        
        if(pos.pos[1] + 1) < len(self.layout[0]):
            node.update( {"right":[pos.pos[0], pos.pos[1]+1]})
        
        if(pos.pos[1] - 1) >= 0:
            node.update({"left": [pos.pos[0], pos.pos[1]-1 ]})
        
        pos.neighb = node
        return pos


        """

  def validNode(self, pos):

        node = {"pos": [pos.x, pos.y]}

        if (pos.x - 1) >= 0:
            node.update({"top": [pos.x-1, pos.y]})

        if(pos.x + 1) < len(self.layout):
            node.update({"bottom": [pos.x+1, pos.y]})
        
        if(pos.y + 1) < len(self.layout[0]):
            node.update( {"right":[pos.x, pos.y+1]})
        
        if(pos.y - 1) >= 0:
            node.update({"left": [pos.X, pos.y-1 ]})
        
        pos.neighb = node
        return pos

        """""


        # h= self.frontier.pop(0)

        # node = self.frontier.pop(0)  # pop the last node from the Queue

        # if self.goal == node["pos"] or self.goal_2 == node["pos"]:  # if node contains goal state return solution
        #     self.explored_set.pop(0)
        #     return

        # self.explored_set.append(node["pos"])  # adds node to the explored set
        # self.check(node)  # expand node by checking if there neighboring nodes anti-clockwise
        # self.search()  # recursively call the function till the goal is found or the stack becomes empty
