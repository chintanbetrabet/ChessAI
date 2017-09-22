
#This file contains the general implementation of search algorithms like DFS, BFS, UFS, and A*.
#Adopted from UC Berkeley's PacMan AI Projects.


import util

class SearchProblem:
	"""
	This class outlines the structure of a search problem. This serves as an asbtract class.
	Doesn't implement any methods.
	"""

	def getStartState(self):
		"""
			Returns start state for search problem 
		"""
		util.raiseNotDefined()

	def isGoalState(self, state):
		"""
			Returns whether the given state is goal state or not
		"""
		util.raiseNotDefined()

	def getSuccessors(self, state):
		"""
			For the given search state, this method returns a triplet (nextState, action, stepCost)
		"""
		util.raiseNotDefined()

	def getCostOfActions(self, actions):
		""" 
			actions: a list of legal actions
			Returns the total cost of particular sequence of actions. Must be composed of legal moves.
		"""
		util.raiseNotDefined()



def depthFirstSearch(problem):

	"""
	problem: it is an instance of a class which inherits from SearchProblem class.
	problem object contains all the machinery required to solve the problem. That is,
	this method takes problem as an input and returns a list of legal actions to be
	taken to solve the problem. Since, we are using DFS, it searches the deepest node
	first. 

	Note to self: keeping track of parents of each state doesn't make sense.
	This is the root cause of problems when you were debugging last time.
	pathTree[nextState] = (state, aciton) -> stop doing this if you want a 
	generic implementation of graph_search. Because the same state can have
	two different parents, and when you execute this pathTree[nextState] shit
	the parent gets updated -> it gets correctly updated depending on what 
	condtion you give while adding the state to frontier. you can't have a common
	correct condition for both bfs and dfs. So don't do this.

	If you want to keep track of parents -> have a separate Node class where
	each node is represented by (state, parentState, action). So two states
	with different parents will be treated as two different nodes. You can have
	a generic graph search implementation with this.

	If you don't want to keep track of parents, and you want to directly push
	the state (not node) in the fringe, use the following implementation. 
	"""
	startState = problem.getStartState()
	expandedStates = set([])

	#frontier contains (state, actions) where actions contain a list of actions
	#which lead to that state.
	fringe = util.Stack()
	fringe.push((startState, []))

	while not fringe.isEmpty():
		state, actions = fringe.pop()
		if(problem.isGoalState(state)):
			return actions

		expandedStates.add(state)
		for nextState, action, cost in problem.getSuccessors(state):
			if(nextState not in expandedStates):
				fringe.push((nextState, actions + [action]))


	return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first"""
    visitedStates = set([])
    startState = problem.getStartState()
    expandedStates = set([])

    fringe = util.Queue()
    fringe.push((startState, []))
    visitedStates.add(startState)

    while not fringe.isEmpty():
        state, actions = fringe.pop()

        if(problem.isGoalState(state)):
            return actions

        expandedStates.add(state)
        for nextState, action, cost in problem.getSuccessors(state):
            if(nextState not in visitedStates):
                visitedStates.add(nextState)
                fringe.push((nextState, actions + [action]))

    return []


def uniformCostSearch(problem):
    """Search the least cost nodes in the search tree first"""
    expandedStates = set([])
    startState = problem.getStartState()

    fringe = util.PriorityQueue()
    fringe.push((startState, [], 0), 0)

    while not fringe.isEmpty():
        state, actions, costSoFar = fringe.pop()
        #print state
        if(problem.isGoalState(state)):
            return actions

        if state in expandedStates:
            continue

        expandedStates.add(state)
        for nextState, action, cost in problem.getSuccessors(state):
            #if(nextState not in expandedStates): (Note that this condition alone without
            #the condition in 166, wont't work. Initially, I thought I will eliminate 166 because
            #if I don't add an already expanded state onto to the fringe, why will fringe have
            #an expanded state at the first place leaving condition 166 to be always false.
            #But this is not true. Take the case where you have a state C, which has not been
            #been expanded. Let's say it has come from parent A. Before C is expanded, what if
            #say from a parent B, you add C again onto the fringe. Now you have two unexpanded
            #C's on the fringe. So if you don't have 166, you will expand them twice.)
            totalCost = costSoFar + cost
            fringe.push((nextState, actions + [action], totalCost), totalCost)

    return []

def aStarSearch(problem, heuristic):
	"""Search the least cost nodes in the search tree first"""
	expandedStates = set([])
	startState = problem.getStartState()

	fringe = util.PriorityQueue()
	startHeurisitc = heuristic(startState, problem)
	fringe.push((startState,[], 0), startHeurisitc)

	while not fringe.isEmpty():
		state, actions, costSoFar = fringe.pop()

		if(problem.isGoalState(state)):
			return actions

		if state in expandedStates:
			continue

		expandedStates.add(state)
		for nextState, action, cost in problem.getSuccessors(state):
			totalCost = costSoFar + cost + heuristic(nextState, problem)
			backwardCost = costSoFar + cost
			fringe.push((nextState, actions + [action], backwardCost), totalCost)

	return []