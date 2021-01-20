from classes.Search import Search

class Depth_First(Search):
    def __init__(self, layout, startPos, goalPos, goal_Pos_2):
        Search. __init__(self, layout, startPos, goalPos, goal_Pos_2)
        self.frontier.append(self.start_pos)
        self.search()

######################################################################################################################

########################################################################################################################
    def search(self):
        if not self.frontier:                                   #if stack is empty then no solution
            return

        node = self.frontier.pop()                              #pop the last node from the stack

        if self.goal == node["pos"] or self.goal_2 == node["pos"] :                            #if node contains goal state return solution
            return self.explored_set.pop(0)

        self.explored_set.append(node["pos"])                   #adds node to the explored set
        self.check(node)                                        #expand node by checking if there neighboring nodes anti-clockwise
        self.search()                                            #recursively call the function till the goal is found or the stack becomes empty
########################################################################################################################
