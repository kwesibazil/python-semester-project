from tkinter import Button, Canvas, Frame, Label, OptionMenu, StringVar, Tk
from random import randint
import json
import time

class Maze:
    def __init__(self, window, grid, cell_size =25):
        self.speed = 0.2                            #movement speed of the maze  
        self.grid = grid                            #size of the maze(e.g 8*8/14*14)  - datatype int
        self.cell_size = cell_size                         #size of each cell - datatype int

        self.path = []
        self.layout = []                            #the layout (postion of every individual wall and passage in the maze)  - datatype multi array [[][][]...]
        self.start_Pos = []                         #the starting point of the maze -- data-type list[x,y]
        self.goal_Pos = []                          #the first target point of the maze -- data-type list[x,y]                  
        self.goal_Pos_2 = []                        #the second target point of the maze -- data-type list[x,y]  
    
        #utilities properties 
        self.position = []
        self.goal_colour = "red"
        self.wall_colour = "blue"
        self.background = "white"
        self.start_colour = "yellow"
        self.passage_colour = "white"

        #Tkinter 
        self.label = []
        self.canvas = []   
        self.window = window

#Generates a Random Maze
########################################################################################################################
    def randomMaze(self):
        stack_empty = False
        visited_cells = []
        
        row = randint(0, self.grid-1)
        col= randint(0, self.grid-1)
        
        self.layout = [['wall' for _ in range(self.grid)] for _ in range(self.grid)]     
        self.layout[row][col] = 'clear'
        self.position.append([row, col])
        
        while not stack_empty:
            adj_sides = self.findSides(row, col)

            if len(adj_sides) != 0:
                rand = randint(1, len(adj_sides))-1
                row, col = adj_sides[rand]
                self.layout[row][col] = 'clear'
                visited_cells.append([row, col])

            else:
                try:
                    row, col = visited_cells.pop()
                    self.position.append([row, col])
                except IndexError:
                    stack_empty = True

        self.position = self.position[0:2] 
        self.start_Pos = self.position[0]
        self.goal_Pos = self.position[1]
        self.layout[self.start_Pos[0]][self.start_Pos[1]] = 'start'
        #self.layout[self.goal_Pos[0]][self.goal_Pos[1]] = 'goal'
########################################################################################################################

#maps out the passsages and walls of the maze
########################################################################################################################
    def findSides(self, row, col):
        adj_sides = []  
        sides = [
                [row, col-1, row-1, col-2, row, col-2, row+1, col-2, row-1, col-1, row+1, col-1], #left
                [row, col+1, row-1, col+2, row, col+2, row+1, col+2, row-1, col+1, row+1, col+1], #right
                [row-1, col, row-2, col-1, row-2, col, row-2, col+1, row-1, col-1, row-1, col+1], #top
                [row+1, col, row+2, col-1, row+2, col, row+2, col+1, row+1, col-1, row+1, col+1]  #bottom
        ] 

        for side in sides:  
            if side[0] > 0 and side[0] < (self.grid-1) and side[1] > 0 and side[1] < (self.grid-1):
                if self.layout[side[2]][side[3]] == 'clear' or self.layout[side[4]][side[5]] == 'clear' or self.layout[side[6]][side[7]] == 'clear' or self.layout[side[8]][side[9]] == 'clear' or self.layout[side[10]][side[11]] == 'clear':
                    pass
                else:
                    adj_sides.append(side[0:2])

        return adj_sides
########################################################################################################################

#creates a tkinter canvas
########################################################################################################################
    def generateCanvase(self, canvas_pos, label_pos, label_text):
        self.canvas = Canvas(self.window, width=(self.grid * self.cell_size), height=(self.grid * self.cell_size), bg=self.background )
        self.canvas.grid(row=canvas_pos[0], column = canvas_pos[1], pady=(0,20), padx=(10,10))
        self.label = Label(self.window, text=label_text, font="Times 16 italic bold").grid(row=label_pos[0], column=label_pos[1], sticky="n")
        
#########################################################################################################################

#########################################################################################################################
    def displayMaze(self, option=False):  
        self.layout[self.goal_Pos[0]][self.goal_Pos[1]] = 'goal'
        if option:
            self.layout[self.goal_Pos_2[0]][self.goal_Pos_2[1]] = 'goal'

        for row in range(self.grid):
            for col in range(self.grid):
                if self.layout[row][col] == 'clear':
                    colour = self.passage_colour
                elif self.layout[row][col] == 'wall':
                    colour = self.wall_colour
                elif self.layout[row][col] == 'start':
                    colour = self.start_colour
                else:
                    colour = self.goal_colour
                    self.layout[row][col] = 'clear'
                pos = []
                pos.append([row, col])
                self.draw(pos[0], colour)
#########################################################################################################################

########################################################################################################################
    def draw(self, pos, colour):
        x1 = pos[1] * self.cell_size
        y1 = pos[0] * self.cell_size
        x2 = x1 +  self.cell_size
        y2 = y1 +  self.cell_size
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=colour)
########################################################################################################################
########################################################################################################################
    def runMaze(self, path):
        for node in path:
            self.draw(node, "green")
            self.window.update()
            time.sleep(self.speed)
#########################################################################################################################

#########################################################################################################################
    def saveMaze(self, path):
        maze ={
            "start_Pos": self.start_Pos,
            "goal_Pos": self.goal_Pos,
            "goal_Pos_2": self.goal_Pos_2,
            "layout": self.layout
        }
        with open(path, 'wt') as maze_write:
            json.dump(maze, maze_write, )
#########################################################################################################################

######################################################################################################################### 
    def loadMaze(self, path):
        with open(path, 'r') as maze_read:
            attrib = json.load(maze_read)
            self.start_Pos = attrib['start_Pos']
            self.goal_Pos = attrib['goal_Pos']
            self.goal_Pos_2 = attrib['goal_Pos_2']
            self.layout = attrib['layout']
#########################################################################################################################
