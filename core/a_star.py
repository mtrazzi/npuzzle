import numpy as np

# def reconstruct_path(cameFrom, current):
#   total_path = [current]
#   while current in cameFrom.keys():
#     current = cameFrom[current]
#     total_path.insert(0, current)
#   return total_path

# def find_lowest_fScore(openSet, fScore):
#   # Return str
#   current_state = openSet[0]
#   current_score = fScore[current_state]
#   for state, score in fScore.items():
#     if score < current_score:
#       current_state = state
#   return current_state

# def A_Star(puzzle, hname='tiles-out'):
#   start = puzzle.state
#   goal = puzzle.goal

#   openSet = [start]
#   cameFrom = {}
#   gScore = {}
#   gScore[start] = 0
#   fScore = {}
#   fScore[start] = puzzle.heuristic(hname)

#   while len(openSet) != 0:
#     current = find_lowest_fScore(openSet, fScore)
#     if current == goal:
#       return reconstruct_path(cameFrom, current)

#     openSet.remove(current)
#     for neighbor_puzzle in current.neighbors():
#       neighbor = neighbor_puzzle.state
#       tentative_gScore = gScore[current] + 1
#       if tentative_gScore < gScore.get(neighbor), np.Inf):
#         cameFrom[neighbor] = current
#         gScore[neighbor] = tentative_gScore
#         fScore[neighbor] = gScore[neighbor] + neighbor.heuristic(hname)
#         if neighbor not in openSet:
#           openSet.append(neighbor)

#   return []

def reconstruct_path(cameFrom, current):
  total_path = [current]
  while current in cameFrom.keys():
    current = cameFrom[current]
    total_path.insert(0, current)
  return total_path

def find_lowest_fScore(openSet, fScore):
  # Return str
  current_state = openSet[0]
  current_score = fScore[current_state]
  for state, score in fScore.items():
    if score < current_score:
      current_state = state
  return current_state

def A_Star(start, hname='tiles-out'):
  openSet = [start]
  cameFrom = {}
  gScore = {}
  gScore[start] = 0
  fScore = {}
  fScore[start] = start.heuristic(hname)

  while len(openSet) != 0:
    current = find_lowest_fScore(openSet, fScore)
    if current.state == current.goal:
      return reconstruct_path(cameFrom, current)

    # for idx in range(len(openSet)):
    #   if openSet[idx].state == current.state:
    #     openSet.remove(openSet[idx])

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


# class AStar(object):
#   # cf. pseudocode from https://en.wikipedia.org/wiki/A*_search_algorithm
#   def __init__(self, puzzle, hname='tiles-out'):
#     # maps integers to puzzle states
#     self.states = [puzzle]

#     # special heuristic for h
#     self.hname = hname

#     # utils
#     self.size = puzzle.size
#     self.goal = puzzle.goal

#     # for the output TODO: update those values in _run_
#     self.nb_opened_st = 0
#     self.max_nb_st_mem = 0
#     self.path = []
#     self.open_set = [0]

#     # For node n, came_from[n] is the node immediately preceding it
#     # on the cheapest path from start to n currently known.
#     self.came_from = {}

#     # heuristic maps (g[0] correspond to g(state_0))
#     # IN THE REST OF THE CODE TRIED TO DEAL WITH STATES_ID TO NOT PASS GIGANTIC PUZZLES... MAYBE CONFUSING
#     self.g = [0]
#     self.h = [self.states[0].heuristic()]
#     self.f = [self.h[0]]

#   def run(self):
#     while self.open_set:
#       current = np.argmin(self.f) #id of the state with lowest f score
#       current_state = self.states[current]
#       if self.states[current] == self.goal:
#         return reconstruct_path(self.came_from, current)

#       # remove the state
#       del self.open_set[current]
#       del self.states[current]

#       for neighbor in current_state.neighbors():
#         neighbor_id = self.states.index(neighbor) if neighbor in self.states else len(self.states)
#         if not neighbor in self.states:
#           self.states.append(neighbor)
#         tentative_g = self.g[current] + 1 # weight of edges are 1
#         if tentative_g < self.g[neighbor_id]:
#           self.came_from[neighbor_id] = current
#           self.g[neighbor_id] = tentative_g
#           self.f[neighbor_id] = self.g[neighbor_id] + self.h[neighbor_id]
#           if not neighbor in self.open_set:
#             self.open_set.append(neighbor_id)
