import numpy as np

class PriorityQueue(object):
  """Priority Queue Data Structure

  Attributes
  ----------
  states: list
    The set of discovered nodes
  gScores: dict
    For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
  fScores: dict
    For node n, fScore[n] := gScore[n] + h(n). Where h() is an admissible heuristic function.
  """
  def __init__(self):
    self.states = []
    self.gScores = {}
    self.fScores = {}
    self.nbOpen = 0

  def add(self, state, gScore=np.Inf, fScore=np.Inf):
    self.states.append(state)
    self.gScores[state] = gScore
    self.fScores[state] = fScore
    self.nbOpen += 1
    return self

  def lowest(self):
    """Return the state for the lowest fScore"""
    current_state = self.states[0]
    current_score = self.fScores[current_state]
    for state, score in self.fScores.items():
      if score < current_score:
        current_state = state
    return current_state

  def length(self):
    return len(self.states)

  def remove(self, _T):
    self.states.remove(_T)
    self.fScores[_T] = np.Inf
    return self

  def gScore(self, _T):
    return self.gScores.get(_T, np.Inf)

  def fScore(self, _T):
    return self.fScores.get(_T, np.Inf)

  def __contains__(self, _T):
    return _T in self.states
