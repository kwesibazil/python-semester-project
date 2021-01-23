from classes.Search import Search

class A_Search(Search):
    def __init__(self, layout, startPos, goalPos):
        Search. __init__(self, layout, startPos, goalPos)
        self.frontier.append(self.start_pos)
        self.search()

########################################################################################################################
    def search(self):
        if not self.frontier:  # if stack is empty then no solution
            return

        node = self.frontier.pop(0)  # pop the last node from the Queue
        
        if self.goal == node["pos"] or self.goal_2 == node["pos"]:  # if node contains goal state return solution
            self.explored_set.pop(0)
            return

        self.explored_set.append(node["pos"])  # adds node to the explored set
        self.check(node)  # expand node by checking if there neighboring nodes anti-clockwise
        self.search()  # recursively call the function till the goal is found or the stack becomes empty

########################################################################################################################

    # def search(self, x,y):
    #     currentPos = [x, y]
    #     kwesi = self.layout[x]
    #
    #     if currentPos == self.goal:
    #         self.explored_set.pop(0)
    #         return True
    #
    #     elif self.layout[x][y] == 'wall':
    #         return False
    #
    #     elif  self.visitable(currentPos):
    #         return False
    #
    #     self.explored_set.append(currentPos)
    #
    #     if((x< len(self.layout) - 1 and self.search(x+1, y))
    #         or (y > 0 and self.search(x, y-1))
    #         or (x > 0 and self.search(x-1, y))
    #         or (y < len(self.layout)-1 and self.search(x, y+1))):
    #         return True
    #
    #     return False
#checks to see if the node has been visited before



########################################################################################################################
    def visitable(self, node):
        if node in self.explored_set:
            return True
########################################################################################################################
