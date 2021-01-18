import sys
sys.path.insert(0, "/classes")

from tkinter import Tk
from classes.Maze import Maze
from classes.Depth_First import Depth_First
from classes.Breadth_First import Breadth_First


window = Tk()

maze = Maze(window, 8)
maze.generateMaze()
dfs = Depth_First(maze.layout, maze.start_Pos, maze.goal_Pos)
dfs.start()
maze.generateWindow()
maze.generateCanvase("Depth first Maze")
maze.solveMaze(dfs.explored_set)


bfs = Breadth_First(maze.layout, maze.start_Pos, maze.goal_Pos)
bfs.start()
maze.generateWindow()
maze.generateCanvase("Breath first Maze")
maze.solveMaze(bfs.explored_set)
window.mainloop()

