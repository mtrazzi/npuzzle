from core.puzzle import neighbors
from core.priority_queue import PriorityQueue
from core.heuristics import heuristic

def reconstruct_AStar(cameFrom, current):
  """Reconstruct path from A*"""
  totalPath = [current]
  while current in cameFrom.keys():
    current = cameFrom[current]
    totalPath.insert(0, current)
  return totalPath

def reconstruct_BFS(start, state):
  """Reconstruct path from BFS"""
  totalPath = []
  current = state[0]
  while current != start:
    totalPath.insert(0, current)
    state = state[1]
    current = state[0]
  return totalPath

def BFS(start, goal, size):
  """Breadth-first search algorithm

  Parameters
  ----------
  state: list
    Current puzzle state
  goal: list
    State we want to achieve
  size: int
    Puzzle size

  Return
  ------
  (totalPath, length, nbOpen, maxOpenSet): (2d-list, int, int, int)
    totalPath: List of state from initial state to goal state
    length: Length of totalPath
    nbOpen: Number of node opened during search
    maxOpenSet: Maximum simultaneously opened node during search
  """
  openSet = [[start,]]
  discovered = [start]
  nbOpen = 1
  maxOpenSet = 1
  while len(openSet) != 0:
    maxOpenSet = max(maxOpenSet, len(openSet))
    state = openSet.pop(0)
    if state[0] == goal:
      totalPath = reconstruct_BFS(start, state)
      return totalPath, len(totalPath), nbOpen, maxOpenSet

    for neighbor in neighbors(state[0], size):
      if neighbor not in discovered:
        discovered.append(neighbor)
        nbOpen += 1
        openSet.append([neighbor, state])
  return [], 0, nbOpen, maxOpenSet

def A_Star(start, goal, size, hname='euclidean'):
  """A* search algorithm

  Parameters
  ----------
  state: list
    Current puzzle state
  goal: list
    State we want to achieve
  size: int
    Puzzle size

  Return
  ------
  (totalPath, length, nbOpen, maxOpenSet): (2d-list, int, int, int)
    totalPath: List of state from initial state to goal state
    length: Length of totalPath
    nbOpen: Number of node opened during search
    maxOpenSet: Maximum simultaneously opened node during search
  """
  openSet = PriorityQueue().add(start, 0, heuristic(goal, start, hname))
  cameFrom = {}
  closedSet = set()

  maxOpenSet = 1
  while openSet.length() != 0:
    maxOpenSet = max(maxOpenSet, openSet.length())
    current = openSet.lowest()
    if current == goal:
      totalPath = reconstruct_AStar(cameFrom, current)
      return totalPath, len(totalPath) - 1, openSet.nbOpen, maxOpenSet

    openSet.remove(current)
    closedSet.add(current)
    for neighbor in neighbors(current, size):
      if neighbor in closedSet:
        continue
      tentative_gScore = openSet.gScore(current) + 1
      if tentative_gScore < openSet.gScore(neighbor):
        cameFrom[neighbor] = current
        if neighbor not in openSet:
          openSet.add(neighbor, tentative_gScore, tentative_gScore + heuristic(goal, neighbor, hname))
  return [], 0, openSet.nbOpen, maxOpenSet
