# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    current_state = problem.getStartState()
    explored = set()
    path = set()
    stop = 0
    
    def DFS(problem,current_state,path):
        global explored
        global stop
        
        explored |= {current_state[0]}
        path |= {current_state}
        
        if problem.isGoalState(current_state[0])==0:
            stop = 1            
        else:
            for state in problem.getSuccessors(current_state[0]):
                if state[0] not in explored and stop==0:
                    path = DFS(problem,state[0:2],path)
                    
        return path
    
    path = DFS(problem,current_state,path)
    actions = [path[i][1] in range(1,len(path))]
    
    directions = set()
    for i in range(0,len(path)):
        branches = problem.getSuccessors(path[i])
        nodes = [branches[i][0] in range(1,len(branches))]
        actions = [branches[i][1] in range(1,len(branches))]
        directions |= {actions[nodes.index(path[i+1])]}
          

def breadthFirstSearch(problem):
    explored = set()
    fringe = util.Queue()    
    state2parent = {}
    stop = 0
    
    fringe.push(problem.getStartState())
    
    while not fringe.isempty() and stop==0:
        current_state = fringe.pop()

        if current_state[0] not in explored:
            explored |= {current_state[0]}
            
            for state in problem.getSuccessors(current_state):
                state2parent[state] = current_state
                if problem.isGoalState(current_state[0])==1:
                    stop = 1                    
                    break
                else:                                        
                    fringe.push(state[0])
        
            
    
    
    

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
