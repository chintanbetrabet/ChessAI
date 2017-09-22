#Treasure Hunt Solver
#AUTHOR - Srinath
#email - srinath132@gmail.com

#run as 'python treasureHunt.py m.txt'

import sys,os
import search
import util, time
import pickle

class TreasureHuntState:
	"""
	State representation for the problem. {(x,y)->current position, [position of remaining
	treasures]}
	"""
	maze = [[]]
	dim  = ()

	@classmethod
	def setMaze(cls, m):
		cls.maze = m
		cls.dim = (len(m), len(m[0]))

	def __init__(self, pos, treasures):
		"""

		Initialises the state with position of agent and positions of
		remaining treasures

		"""
		self.pos = pos
		self.treasures = treasures

	def isGoal(self):
		"""
		Checks whether the current instance state is goal state.
		Goal state is when no more treasures are left.
		"""
		return len(self.treasures) == 0

	def legalMoves(self):
		"""
		Returns a list of legal moves from current position 
		"""
		pos, treasures, maze = self.pos, self.treasures, TreasureHuntState.maze
		dim = TreasureHuntState.dim
		

		#[up, down, left, right]
		possiblePos = [(pos[0]-1, pos[1]), (pos[0]+1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1)]

		legal = lambda (x,y): x >= 0 and y >= 0 and x < dim[0] and y < dim[1] and maze[x][y] != '#'

		moves = []

		if(legal(possiblePos[0])):
			moves.append("up")

		if(legal(possiblePos[1])):
			moves.append("down")

		if(legal(possiblePos[2])):
			moves.append("left")

		if(legal(possiblePos[3])):
			moves.append("right")

		return moves

	def result(self, move):
		"""
		Returns a new state which will be the result of applying the 
		given action on current state
		"""
		newX, newY = 0,0
		oldX, oldY = self.pos

		if(move == "up"):
			newX = oldX - 1
			newY = oldY

		elif(move == "down"):
			newX = oldX + 1
			newY = oldY

		elif(move == "left"):
			newX = oldX
			newY = oldY - 1

		elif(move == "right"):
			newX = oldX
			newY = oldY + 1

		else:
			raise "Illegal Move"


		newTreasures = set(self.treasures)
		newTreasures.discard((newX, newY))

		newState = TreasureHuntState((newX, newY), newTreasures)
		return newState


	def __eq__(self, otherState):
		return (self.pos == otherState.pos and self.treasures == otherState.treasures)

	def __hash__(self):
		return hash(tuple(self.pos)+tuple(self.treasures))


class TreasureHuntSearchProblem(search.SearchProblem):
	expandedStates = 0

	def __init__(self, initialState):
		self.initialState = initialState

	def getStartState(self):
		return self.initialState

	def isGoalState(self, state):
		return state.isGoal()

	def getSuccessors(self, state):
		succ = []
		for move in state.legalMoves():
			succ.append((state.result(move), move, 1))

		TreasureHuntSearchProblem.expandedStates += 1

		return succ

	def getCostOfActions(self, actions):
		return len(actions)

	@classmethod
	def getNoExpandedStates(cls):
		return cls.expandedStates


def distanceToTreasure(state, problem, func):
	"""
	Returns the closest/farthest (depending upon on func) treasure distance
	"""
	treasures = set(state.treasures)
	pos = state.pos[:]

	if not treasures:
		return 0

	distToClosestTreasure = func([util.manhattanDistance(pos, t) for t in treasures])

	return distToClosestTreasure	



def modelHeuristic1(state, problem):
	"""
	Returns number of remaining treasures from current state
	"""
	return len(state.treasures)

def modelHeuristic2(state, problem):
	"""
	Returns the closest treasure distance
	"""
	return distanceToTreasure(state, problem, min)

def modelHeuristic3(state, problem):
	"""
	Returns the farthest treasure distance
	"""
	return distanceToTreasure(state, problem, max)

def modelHeuristic4(state, problem):
	"""
	Returns the manhattan tour - covering all treasures from current pos.

	CAVEAT: Not always admissible.
	"""
	treasures = list(state.treasures)
	pos = state.pos[:]

	if not treasures:
		return 0

	current = pos
	manhattanTour = 0
	while treasures:
		closestTreasure, distToClosestTreasure = min([(t,util.manhattanDistance(current, t)) for t in treasures], key = lambda x: x[1])

		manhattanTour += distToClosestTreasure
		current = closestTreasure
		treasures.remove(closestTreasure)

	return manhattanTour


def executeAStar(problem):
	print '\nSolution using A* Search\n'

	heuristics = {}
	heuristics['modelHeuristic1'] = "Remaining treasures left."
	heuristics['modelHeuristic2'] = "Distance to closest treasure."
	heuristics['modelHeuristic3'] = "Distance to farthest treasure."
	heuristics['modelHeuristic4'] = "Total manhattan tour of all remaining treasures."

	remarks = {}
	try:
		with open("heuristicRemarks.pickle") as f:
			remarks = pickle.load(f)
	except IOError as e:
		raise IOError("Hey put the file in same directory as your code!")
	except:
		raise Exception("Some shit happened.")


	base = "modelHeuristic"
	for i in range(1, 5):
		heuristicName = base + str(i)
		heuristic = globals()[heuristicName]

		print "Running A* using heuristic: " + heuristics[heuristicName]
		TreasureHuntSearchProblem.expandedStates = 0
		start = time.clock()
		solution = search.aStarSearch(problem, heuristic)
		timeTaken = time.clock() - start

		print "No. of nodes expanded: ", TreasureHuntSearchProblem.getNoExpandedStates()
		print "Time Taken: ", str(timeTaken)+"s"
		print '\n' + remarks[heuristicName] + '\n'
		print "No of steps: ", problem.getCostOfActions(solution)

		if i == 1:
			print "Solution: "
			for s in solution:
				print s,

		print '\n'
		if i != 4:
			raw_input("Press Enter for results of next heuristic:")
			if os.name == 'nt':
				os.system('cls')
			else:
				os.system('clear')

		print 

def parseInput(filename):
	f = open(filename, 'r')
	maze=[]
	m,n= map(int,f.readline().strip().split())

	start=(0,0)
	treasures=[]
	for i in range(m):
		maze.append(list(f.readline().strip()))
		if 's' in maze[-1]:
			start=(i,maze[-1].index('s'))
		if 't' in maze[-1]:
			occurences= [idx for idx, letter in enumerate(maze[-1]) if letter == 't']
			for each in occurences:
				treasures.append((i,each))


	f.close()
	return start, treasures, maze

def main():
	start, treasures, maze = parseInput(sys.argv[1])

	startState = TreasureHuntState(start, set(treasures))
	TreasureHuntState.setMaze(maze)

	problem = TreasureHuntSearchProblem(startState)
	start = time.clock()
	solution = search.breadthFirstSearch(problem)
	timeTaken = time.clock() - start

	print "Solution using UCS"
	print "No. of nodes expanded: ", TreasureHuntSearchProblem.getNoExpandedStates()
	print "Time Taken: ", str(timeTaken) + "s"

	print "No of steps: ", problem.getCostOfActions(solution)
	print "Solution: "
	for s in solution:
		print s,


	print '\n\n'

	executeAStar(problem)



if __name__ == "__main__":
	main()
	sys.exit(0)