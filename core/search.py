from core.puzzle import neighbors
from core.priority_queue import PriorityQueue
from core.heuristics import heuristic

def reconstruct_path(cameFrom, current):
  """Reconstruct path from A*"""
  totalPath = [current]
  while current in cameFrom.keys():
    current = cameFrom[current]
    totalPath.insert(0, current)
  return totalPath

def BFS(start, goal, size, hname='euclidean'):
  """Greedy Best-First Search algorithm

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
  openSet = PriorityQueue().add_bfs(start, heuristic(goal, start, hname))
  cameFrom = {}
  closedSet = set()

  maxOpenSet = 1
  while openSet.length() != 0:
    maxOpenSet = max(maxOpenSet, openSet.length())
    current = openSet.lowest()
    if current == goal:
      totalPath = reconstruct_path(cameFrom, current)
      return totalPath, len(totalPath) - 1, openSet.nbOpen, maxOpenSet

    openSet.remove(current)
    closedSet.add(current)
    for neighbor in neighbors(current, size):
      if neighbor in closedSet:
        continue
      cameFrom[neighbor] = current
      if neighbor not in openSet:
        openSet.add_bfs(neighbor, heuristic(goal, neighbor, hname))
  return [], 0, openSet.nbOpen, maxOpenSet

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
      totalPath = reconstruct_path(cameFrom, current)
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
