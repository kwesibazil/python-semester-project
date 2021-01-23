from classes.Search import Search

class A_Search(Search):
    def __init__(self, layout, startPos, goalPos,  goalPos_2):
        Search. __init__(self, layout, startPos, goalPos, goalPos_2)
        self.frontier.append(self.start_pos)

    def search(self, x,y):
        currentPos = [x, y]
        kwesi = self.layout[x]

        if currentPos == self.goal:
            self.explored_set.pop(0)
            return True

        elif self.layout[x][y] == 'wall':
            return False

        elif  self.visitable(currentPos):
            return False

        self.explored_set.append(currentPos)

        if((x< len(self.layout) - 1 and self.search(x+1, y))
            or (y > 0 and self.search(x, y-1))
            or (x > 0 and self.search(x-1, y))
            or (y < len(self.layout)-1 and self.search(x, y+1))):
            return True

        return False
#checks to see if the node has been visited before



########################################################################################################################
    def visitable(self, node):
        if node in self.explored_set:
            return True
########################################################################################################################
