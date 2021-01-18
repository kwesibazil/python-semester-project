from classes.Search import Search

class Breadth_First(Search):
    def __init__(self, layout, startPos, goalPos):
        Search. __init__(self, layout, startPos, goalPos)
        self.frontier.append(self.start_pos)
######################################################################################################################


########################################################################################################################
    def start(self):

        #if stack is empty then no solution
        if not self.frontier:
            print("stack empty")
            return

        #pop the last node from the Queue
        node = self.frontier.pop(0) 

        #if node contains goal state return solution
        if self.goal == node["pos"]:
            self.explored_set.pop(0)
            return      #return state is access through object variable


        #adds node to the explored set
        self.explored_set.append(node["pos"])

        #expand node by checking if there neighboring nodes anti-clockwise
        self.check(node)

        #recursively call the function till the goal is found or the stack becomes empty
        self.start()
########################################################################################################################


"""
   # if self.goal == node["pos"]:
            #self.explored_set.pop(0)
            #return


"""