#call the file with "python < m.txt"

import sys
import search

class TreasureHuntState:
	pass



class TreasureHuntSearchProblem(search.SearchProblem):
	pass


def modelHeuristic1(state):
	pass

def modelHeuristic2(state):
	pass

def parseInput():
	maze=[]
	m,n= map(int,raw_input().split())

	start=(0,0)
	treasures=[]
	for i in range(m):
		maze.append(list(raw_input()))
		if 's' in maze[-1]:
			start=(i,maze[-1].index('s'))
		if 't' in maze[-1]:
			occurences= [idx for idx, letter in enumerate(maze[-1]) if letter == 't']
			for each in occurences:
				treasures.append((i,each))


	return start, treasures

def main():
	start, treasures = parseInput()
	print start, treasures


if __name__ == "__main__":
	main()
	sys.exit(0)
