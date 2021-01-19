import sys
sys.path.insert(0, "/classes")

from tkinter import Tk
from classes.Maze import Maze
from classes.A_Search import A_Search
from classes.Depth_First import Depth_First
from classes.Breadth_First import Breadth_First

window = Tk()
maze = Maze(window, 8)
maze.generateMaze()
maze.generateWindow()

maze.generateCanvase("Depth first Maze")
dfs = Depth_First(maze.layout, maze.start_Pos, maze.goal_Pos)
maze.displayMaze(dfs.explored_set)


maze.generateCanvase("Breath first Maze")
bfs = Breadth_First(maze.layout, maze.start_Pos, maze.goal_Pos) 
maze.displayMaze(bfs.explored_set)
#print(maze.layout)

window.mainloop()

