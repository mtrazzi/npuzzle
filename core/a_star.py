import numpy as np
from core.puzzle import Puzzle

def heuristic_aux(x, y, x_g, y_g, name):
  if name == 'tiles-out':
    return x != x_g or y != y_g
  elif name == 'manhattan':
    return abs(x-x_g) + abs(y-y_g)
  elif name == 'euclidean':
    return np.sqrt((x-x_g) ** 2 + (y-y_g) ** 2)

def heuristic(goal, state, name='manhattan'):
  size = int(np.sqrt(len(goal)))

  coord_goal = np.zeros((size ** 2, 2)) # in index i coordinates of tile i in goal
  coord_state = np.zeros((size ** 2,2)) # in index i coordinates of tile i in state
  for x in range (size):
    for y in range (size):
      coord_goal[goal[x * size + y]] = [x,y]
      coord_state[state[x * size + y]] = [x,y]

  return np.sum([heuristic_aux(coord_state[i][0], coord_state[i][1], coord_goal[i][0], coord_goal[i][1], name) for i in range(size ** 2)])

def reconstruct_path(cameFrom, current):
  totalPath = [current]
  while current in cameFrom.keys():
    current = cameFrom[current]
    totalPath.insert(0, current)
  return totalPath

def find_lowest_fScore(openSet, fScore):
  current_state = openSet[0]
  current_score = fScore[current_state]
  for state, score in fScore.items():
    if score < current_score:
      current_state = state
  return current_state

def A_Star(start, hname='euclidean'):
  state = tuple(start.state)
  goal = tuple(start.goal)
  openSet = [state]
  cameFrom = {}
  gScore = {}
  gScore[state] = 0
  fScore = {}
  fScore[state] = heuristic(goal, state, hname)

  nbOpen = 1
  max_open_set = 1
  while len(openSet) != 0:
    max_open_set = max(max_open_set, len(openSet))
    current = find_lowest_fScore(openSet, fScore)
    if current == goal:
      totalPath = reconstruct_path(cameFrom, current)
      return totalPath, len(totalPath) - 1, nbOpen, max_open_set

    openSet.remove(current)
    del fScore[current]
    for neighbor in Puzzle(current).neighbors():
      tentative_gScore = gScore[current] + 1
      if tentative_gScore < gScore.get(neighbor, np.Inf):
        cameFrom[neighbor] = current
        gScore[neighbor] = tentative_gScore
        fScore[neighbor] = gScore[neighbor] + heuristic(goal, neighbor, hname)
        if neighbor not in openSet:
          openSet.append(neighbor)
          nbOpen += 1

  return [], 0, nbOpen, max_open_set
