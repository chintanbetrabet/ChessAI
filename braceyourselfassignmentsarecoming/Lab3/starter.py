import copy

class State():

	'''
	basic methods for constructing and proper hashing of State objects
	'''
	def __init__(self, shape):
		self.shape=shape
		self.board=[['.']*shape[1] for i in range(shape[0])]
		
	def __eq__(self, other):
		return tuple(self.board)==tuple(other.board)
		
	def __hash__(self):
		return hash(tuple(map(tuple,self.board)))
	
	def copy(self):
		new_state=State(self.shape)
		new_state.board=copy.deepcopy(self.board)
		return new_state
	
	
	'''
	returns a list of actions that can be taken from the current state
	actions are integers representing the column where a coin can be dropped
	'''
	def getLegalActions(self):
	
		if self.isGoal('X') or self.isGoal('O'):
			return []
	
		top=self.board[0]
		legal_actions=[i for i in range(len(top)) if top[i]=='.']
		return legal_actions
	
	''' 
	returns a State object that is obtained by the agent (parameter)
	performing an action (parameter) on the current state
	'''	
	def generateSuccessor(self, agent, action):
	
		row=0
		while(row<self.shape[0] and self.board[row][action]!=agent):
			row+=1
		
		new_state=self.copy()
		new_state.board[row-1][action]=agent
		return new_state

	'''
	returns True/False if the agent(parameter) has won the game
	by checking all rows/columns/diagonals for a sequence of >=4
	'''
	def isGoal(self, agent):
		
		seq=agent*4
		
		#check rows
		for row in self.board:
			if seq in ''.join(row):
				return True
		
		#check cols
		for col in map(list, zip(*self.board)):
			if seq in ''.join(col):
				return True
			
		#check diagonals
		diags=[]
		pos_right=[(0,j) for j in range(self.shape[1]-4+1)]+[(i,0) for i in range(1,self.shape[0]-4+1)]
		pos_left=[(0,j) for j in range(4-1, self.shape[1])]+[(i,self.shape[1]-1) for i in range(1,self.shape[0]-4+1)]

		for each in pos_right:
			d=''
			start=list(each)
			while(1):				
				if start[0]>=self.shape[0] or start[1]>=self.shape[1]:
					break
				d+=self.board[start[0]][start[1]]
				start[0]+=1
				start[1]+=1
			if seq in d:
				return True

		for each in pos_left:	
			d=''
			start=list(each)
			while(1):
				if start[1]<0 or start[0]>=self.shape[0] or start[1]>=self.shape[1]:
					break
				d+=self.board[start[0]][start[1]]
				start[0]+=1
				start[1]-=1
			
			if seq in d:
				return True
		
		return False
		

	'''
	returns the value of each state for minimax to min/max over at
	zero depth. Right now it's pretty trivial, looking for only goal states.
	(This would be perfect for infinite depth minimax. Not so great for d=2)
	'''	
	def evaluationFunction(self):
		
		if self.isGoal('O'):
			return 1000
		elif self.isGoal('X'):
			return -1000
		
		return 0


	'''
	Print's the current state's board in a nice pretty way
	'''
	def printBoard(self):
		print '-'*self.shape[1]*2
		for row in self.board:
			print ' '.join(row)
		print '-'*self.shape[1]*2




