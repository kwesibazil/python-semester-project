from classes.Search import Search

class A_Search(Search):
    def __init__(self, layout, startPos, goalPos):
        Search. __init__(self, layout, startPos, goalPos)
        self.frontier.append(self.start_pos)

    def start(self):

      currentNode = self.start_pos

      #current if current node is goal
      if currentNode == self.goal:
          return self.explored_set

      elif 
