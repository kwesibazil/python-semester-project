import sys
sys.path.insert(0, "/classes")

import json
from tkinter import Label, OptionMenu, StringVar, Tk
from classes.Maze import Maze
from classes.A_Search import A_Search
from classes.Depth_First import Depth_First
from classes.Breadth_First import Breadth_First


########################################################################################################################
def OptionMenuEvent (algo):
    if algo == "Depth first search":
      algorithm.set("Depth first search")
  
      result = Depth_First(mazeOne.layout, mazeOne.start_Pos, mazeOne.goal_Pos, mazeOne.goal_Pos_2)
      mazeOne.displayMaze()
      mazeOne.runMaze(result.explored_set)

      result = Depth_First(mazeTwo.layout, mazeTwo.start_Pos, mazeTwo.goal_Pos, mazeTwo.goal_Pos_2)
      mazeTwo.displayMaze(True)
      mazeTwo.runMaze(result.explored_set)

      result = Depth_First(mazeThree.layout, mazeThree.start_Pos, mazeThree.goal_Pos, mazeThree.goal_Pos_2)
      mazeThree.displayMaze()
      mazeThree.runMaze(result.explored_set)

      result = Depth_First(mazeFour.layout, mazeFour.start_Pos, mazeFour.goal_Pos, mazeFour.goal_Pos_2)
      mazeFour.displayMaze(True)
      mazeFour.runMaze(result.explored_set)
      
    elif algo == "Breadth first search":
      algorithm.set("Breadth first search")

      result = Breadth_First(mazeOne.layout, mazeOne.start_Pos, mazeOne.goal_Pos, mazeOne.goal_Pos_2)
      mazeOne.displayMaze()
      mazeOne.runMaze(result.explored_set)

      result = Breadth_First(mazeTwo.layout, mazeTwo.start_Pos, mazeTwo.goal_Pos, mazeTwo.goal_Pos_2)
      mazeTwo.displayMaze(True)
      mazeTwo.runMaze(result.explored_set)

      result = Breadth_First(mazeThree.layout, mazeThree.start_Pos, mazeThree.goal_Pos, mazeThree.goal_Pos_2)
      mazeThree.displayMaze()
      mazeThree.runMaze(result.explored_set)

      result = Breadth_First(mazeFour.layout, mazeFour.start_Pos, mazeFour.goal_Pos, mazeFour.goal_Pos_2)
      mazeFour.displayMaze(True)
      mazeFour.runMaze(result.explored_set)
      
    else:
      algorithm.set("A* Search")

      result = A_Search(mazeOne.layout, mazeOne.start_Pos, mazeOne.goal_Pos, mazeOne.goal_Pos_2)
      mazeOne.displayMaze()
      #mazeOne.runMaze(result.explored_set)
      mazeOne.runMaze(result.openList)

      result = A_Search(mazeTwo.layout, mazeTwo.start_Pos, mazeTwo.goal_Pos, mazeTwo.goal_Pos_2)
      mazeTwo.displayMaze(True)
      #mazeTwo.runMaze(result.explored_set)
      mazeTwo.runMaze(result.closeList)

      result = A_Search(mazeThree.layout, mazeThree.start_Pos, mazeThree.goal_Pos, mazeThree.goal_Pos_2)
      mazeThree.displayMaze()
      # mazeThree.runMaze(result.explored_set)\
      mazeThree.runMaze(result.closeList)

      result = A_Search(mazeFour.layout, mazeFour.start_Pos, mazeFour.goal_Pos, mazeFour.goal_Pos_2)
      mazeFour.displayMaze(True)
      #mazeFour.runMaze(result.explored_set)
      mazeFour.runMaze(result.closeList)
########################################################################################################################

#file paths
_8x8_with_one_solution = "./mazes/An 8x8 grid with one solution.json"
_8x8_with_two_solution = "./mazes/An 8x8 grid with two solution.json"
_14x14_with_one_solution = "./mazes/An 14x14 grid with one solution.json"
_14x14_with_two_solution = "./mazes/An 14x14 grid with two solution.json"

window = Tk()
window_width = 1000
window_height = 720
window.title("CSE4100 Semester Project")
window.geometry(f'{window_width}x{window_height}')
window.config(bg="white")

algorithm = StringVar()
algorithm.set("Select")
label = Label(window, text="Search Algorithm: ", font="Times 20 italic bold").grid(row=0, column=0, sticky="n", pady=(0,15)) 
option = OptionMenu(window, algorithm, "Depth first search", "Breadth first search", "A* Search", command=OptionMenuEvent)
option.grid(row=0,column=1,sticky="n")


#Generate & Save Random Mazes
#maze.randomMaze()     #rename random maze
#maze.saveMaze(_8x8_with_one_solution)

# 8 *8 Maze with One Solution
mazeOne = Maze(window, 8)
mazeOne.loadMaze(_8x8_with_one_solution)
mazeOne.generateCanvase([4, 0], [3, 0], "Maze: 8x8 with one solution")         #{1st arg = canvas_pos,   2nd arg = label_pos,  3rd arg = label_text):
mazeOne.displayMaze()


# # 8 *8 Maze with two Solution
mazeTwo = Maze(window, 8)
mazeTwo.loadMaze(_8x8_with_two_solution)
mazeTwo.generateCanvase([4, 1], [3, 1], "Maze: 8x8 with two solution")           
mazeTwo.displayMaze()

# # 14 *14 Maze with one Solution
mazeThree = Maze(window, 14)
mazeThree.loadMaze(_14x14_with_one_solution)
mazeThree.generateCanvase([7, 0], [6, 0], "Maze: 14x14 with one solution")   
mazeThree.displayMaze()

# # 14 *14 Maze with one Solution
mazeFour = Maze(window, 14)
mazeFour.loadMaze(_14x14_with_two_solution)
mazeFour.generateCanvase([7, 1], [6, 1], "Maze: 14x14 with two solution")            
mazeFour.displayMaze()

window.mainloop()


