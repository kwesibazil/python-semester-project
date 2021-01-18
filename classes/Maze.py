from tkinter import Canvas, Tk
from random import randint
import time

class Maze:
    def __init__(self, window, grid, ):
        self.grid = grid
        self.layout = []   
        self.position = []
        self.start_Pos = []   
        self.goal_Pos = [] 
        self.goal_Pos2 = []
        self.cell_size = 5
        self.window_width = 1260
        self.window_height = 720
        self.goal_colour = "red"
        self.wall_colour = "blue"
        self.background = "grey"
        self.start_colour = "yellow"
        self.passage_colour = "white"
        self.speed = 0.01
        self.canvas = [] 
        self.window = window

########################################################################################################################
    def generateMaze(self):
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

#########################################################################################################################
    def generateWindow(self,title = "CSE4100 Semester Project"):
        self.window.title(title)
        self.window.geometry(f'{self.window_width}x{self.window_height}')
########################################################################################################################

########################################################################################################################
    def generateCanvase(self, heading):
        self.canvas = Canvas(self.window, width=((self.grid * self.cell_size)), height=(self.grid * self.cell_size), bg=self.background )
        self.canvas.pack()
        self.canvas.create_text(1160,100,fill="darkblue",font="Times 16 italic bold",text=heading)
#########################################################################################################################

#########################################################################################################################
    def colourMaze(self):   
        for row in range(self.grid):
            for col in range(self.grid):
                if self.layout[row][col] == 'clear':
                    colour = self.passage_colour
                elif self.layout[row][col] == 'wall':
                    colour = self.wall_colour
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
    def solveMaze(self, path):

        self.colourMaze()
        self.draw(self.start_Pos, self.start_colour)
        self.draw(self.goal_Pos, self.goal_colour)

        for node in path:
            self.draw(node, "green")
            self.window.update()
            time.sleep(0.2)
#########################################################################################################################