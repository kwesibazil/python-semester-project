from tkinter import Canvas, Tk
from random import randint

class Maze:
    def __init__(self, window, grid):
        self.grid = grid
        self.layout = []   
        self.position = []    
        self.cell_size = 55
        self.window = window
        self.goal_colour = "red"
        self.wall_colour = "blue"
        self.background = "white"
        self.start_colour = "green"
        self.passage_colour = "white"

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
    def generateCanvase(self, title = "CSE4100 Semester Project"):
        self.window.title(title)
        global canvas
        canvas = Canvas(self.window, width=(self.grid * self.cell_size), height=(self.grid * self.cell_size), bg=self.background )
        canvas.pack()
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
        canvas.create_rectangle(x1, y1, x2, y2, fill=colour)
########################################################################################################################
