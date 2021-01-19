"""
maze.generateCanvase("A* Search")

layout =   [
  ['wall',  'clear',  'clear',  'clear',  'clear',  'clear',   'clear',   'clear',  'clear',  'clear',  'clear',  'clear'],
  ['wall',  'clear',  'wall',   'wall',   'wall',   'wall',     'wall',   'wall',   'wall',   'wall',   'wall',  'clear'],
  ['wall',  'clear',  'wall',   'clear',  'clear',  'clear',    'clear',   'clear', 'clear',  'clear',  'wall',  'clear'],
  ['wall',  'clear',  'wall',   'clear',  'wall',    'wall',     'wall',   'wall',   'wall',   'clear',  'wall',  'clear'],
  ['wall',  'clear',  'clear',  'clear',  'wall',    'clear',    'clear',  'clear',  'clear',  'clear',  'wall', 'clear'],
  ['wall',  'wall',   'wall',   'clear',  'wall',    'clear',     'wall',   'wall',   'wall',   'wall',   'wall', 'clear'],
  ['start', 'clear',  'clear',  'clear',  'wall',    'clear',     'clear',  'clear',  'clear',  'clear', 'clear', 'clear'],
  ['wall',  'wall',   'wall',   'wall',   'wall',   'wall',     'wall',   'wall',   'wall',   'wall',   'wall',  'wall'],
  ['wall',  'wall',   'wall',   'wall',   'wall',   'wall',     'wall',   'wall',   'wall',   'wall',   'wall',  'wall'],
  ['wall',  'wall',   'wall',   'wall',   'wall',   'wall',     'wall',   'wall',   'wall',   'wall',   'wall',  'wall'],
  ['wall',  'wall',   'wall',   'wall',   'wall',   'wall',     'wall',   'wall',   'wall',   'wall',   'wall',  'wall']
]

start = [6,0]
goal = [0, 11]

maze.layout = layout
maze.start_Pos = start
maze.goal_Pos = goal

a_search = A_Search(layout, start, goal)
a_search.search(maze.start_Pos[0], maze.start_Pos[1])
kwesi = a_search.explored_set
maze.displayMaze(a_search.explored_set)"""
