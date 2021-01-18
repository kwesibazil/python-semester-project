import sys
sys.path.insert(0, "/classes")

from tkinter import Tk
from classes.Maze import Maze
from classes.Depth_First import Depth_First



window = Tk()
maze = Maze(window, 8)
maze.generateMaze()

dfs = Depth_First(maze.layout, maze.start_Pos, maze.goal_Pos)

dfs.start()

layout = dfs.layout
expore = dfs.explored_set
kwesi = dfs.path
print(type(kwesi))
print(type(expore))

maze.generateWindow()
maze.generateCanvase()
maze.solveMaze(dfs.explored_set)

window.mainloop()

