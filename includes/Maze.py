from tkinter import Canvas, Tk
from random import randint

grid = 8   
cellSize = 55               #width in pixel
adj_sides = []              #number of rows and column in maze
visited_cells = []

end_colour = "red"
wall_colour = 'blue'
background = 'purple'       #background colour
start_colour = 'Green'
passage_colour = "white"

#########################################################################################################################
def generate_maze():
    colour = []
    stack_empty = False
    start_row = randint(0, grid-1)
    start_col= randint(0, grid-1)
    row, col = start_row, start_col
    colour.append([start_row, start_col])
    
    global layout
    layout = [['wall' for _ in range(grid)] for _ in range(grid)]     #maze layout multiarray
    layout[start_row][start_col] = 'clear'
    
    while not stack_empty:
        adj_sides = find_sides(row, col)
    
        if len(adj_sides) != 0:
            rand = randint(1, len(adj_sides))-1
            current_row, current_col = adj_sides[rand]
            layout[current_row][current_col] = 'clear'
            visited_cells.append([current_row, current_col])
            col = current_col
            row = current_row

        if len(adj_sides) == 0:
            try:
                row, col = visited_cells.pop()
                colour.append([row, col])
            except IndexError:
                stack_empty = True
    
    return colour[0:2]
#########################################################################################################################

#########################################################################################################################
def find_sides(row, col):
    adj_sides = []  
    sides = [
            [row, col-1, row-1, col-2, row, col-2, row+1, col-2, row-1, col-1, row+1, col-1], #left
            [row, col+1, row-1, col+2, row, col+2, row+1, col+2, row-1, col+1, row+1, col+1], #right
            [row-1, col, row-2, col-1, row-2, col, row-2, col+1, row-1, col-1, row-1, col+1], #top
            [row+1, col, row+2, col-1, row+2, col, row+2, col+1, row+1, col-1, row+1, col+1]  #bottom
    ] 

    for side in sides:  
        if side[0] > 0 and side[0] < (grid-1) and side[1] > 0 and side[1] < (grid-1):
            if layout[side[2]][side[3]] == 'clear' or layout[side[4]][side[5]] == 'clear' or layout[side[6]][side[7]] == 'clear' or layout[side[8]][side[9]] == 'clear' or layout[side[10]][side[11]] == 'clear':
                pass
            else:
                adj_sides.append(side[0:2])

    return adj_sides
#########################################################################################################################

#########################################################################################################################
def get_dimension():
    dim = int(input("\n\tMaze Dimension\n \t    1 = 8 * 8\n\t    2 = 14 * 14\n\n\tEnter your Choice:"))
    while dim not in (1 , 2):
        dim = int(input("\n\tInvalid Please input a choice [1 or 2]:"))
    return 8 if dim == 1 else 14
#########################################################################################################################

#########################################################################################################################
def generate_canvase(option):
    global grid, window, canvas
    grid = get_dimension() if option else grid
    window = Tk()
    window.title('CSE4100 Semester Project')
    canvas = Canvas(window, width=(grid * cellSize), height=(grid * cellSize), bg=background)
    canvas.pack()
#########################################################################################################################

#########################################################################################################################
def colour_maze():
    global layout
    for row in range(grid):
        for col in range(grid):
            if layout[row][col] == 'clear':
                colour = passage_colour
            elif layout[row][col] == 'wall':
                colour = wall_colour

            draw(row, col, colour)
#########################################################################################################################

########################################################################################################################
def draw(row, col, colour):
    x1 = col*cellSize
    y1 = row*cellSize
    x2 = x1+cellSize
    y2 = y1+cellSize
    canvas.create_rectangle(x1, y1, x2, y2, fill=colour)
#########################################################################################################################

#########################################################################################################################


colour = generate_maze()
generate_canvase(False)         
colour_maze();
print(colour)
draw(colour[0][0], colour[0][1], start_colour)
draw(colour[1][0], colour[1][1], end_colour)

window.mainloop()






