import numpy as np

def find_coord_in_list(l, elt):
  size = int(np.sqrt(len(l)))
  for i in range(size):
    for j in range(size):
      if l[i * size + j] == elt:
        return i, j

def heuristic(goal, state, name='tiles-out'):
  s = 0
  size = int(np.sqrt(len(goal)))
  for x in range (size):
    for y in range (size):
      x_g, y_g = find_coord_in_list(goal, state[x * size + y])
      if name == 'tiles-out':
        s += x != x_g or y != y_g
      elif name == 'manhattan':
        s += abs(x-x_g) + abs(y-y_g)
      elif name == 'euclidean':
        s += np.sqrt((x-x_g) ** 2 + (y-y_g) ** 2)
  return s

def reconstruct_path(cameFrom, current):
  total_path = [current]
  while current in cameFrom.keys():
    current = cameFrom[current]
    total_path.insert(0, current)
  return total_path

def find_lowest_fScore(openSet, fScore):
  current_state = openSet[0]
  current_score = fScore[current_state]
  for state, score in fScore.items():
    if score < current_score:
      current_state = state
  return current_state

def A_Star(start, hname='euclidean'):
  openSet = [start]
  cameFrom = {}
  gScore = {}
  gScore[start] = 0
  fScore = {}
  fScore[start] = start.heuristic(hname)

  iteration = 0
  while len(openSet) != 0:
    iteration += 1
    if (iteration % 100 == 0):
      print(f'iteration #{iteration}')
    current = find_lowest_fScore(openSet, fScore)
    if current.state == current.goal:
      return reconstruct_path(cameFrom, current)

    openSet.remove(current)
    fScore[current] = np.Inf
    for neighbor in current.neighbors():
      tentative_gScore = gScore[current] + 1
      if tentative_gScore < gScore.get(neighbor, np.Inf):
        cameFrom[neighbor] = current
        gScore[neighbor] = tentative_gScore
        fScore[neighbor] = gScore[neighbor] + neighbor.heuristic(hname)
        if neighbor not in openSet:
          openSet.append(neighbor)

  return []