import sys
sys.path.insert(1, "/classes")

from classes.Maze import Maze
from tkinter import Tk


window = Tk()
maze = Maze(window, 8)

maze.generateMaze()
maze.generateCanvase()
maze.colourMaze()

maze.draw(maze.position[0], maze.start_colour)
maze.draw(maze.position[1],maze.goal_colour)

print(maze.layout)

window.mainloop()
