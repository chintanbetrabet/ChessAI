from abc import ABCMeta
import util
import copy
fringe=[]
victory_path=[]
level=0
nodes=0
class SearchProblem:
    __metaclass__ = ABCMeta
    def __init__(self):
        self.actions=[]
        self.path=[]
    def getStartState(self):
        return self
    def isGoalState(state):
        if(state.heuristic()==0):
            return True
        else :
            return False
    def getCostOfActions(self,actions):
        total_cost=0
        for x in actions:
            total_cost=total_cost + actions[x]
        print total_cost
    def getSuccessors(self,state,nodes):
        #actions=[]
        return state.legalMoves()
     

def aStarSearch(temp,level=0,nodes=0,victory=0):
    if len(fringe)==0:
        print "fringe is empty"
        cop=copy.deepcopy(temp)
        temp=[]
        temp=[0,cop.heuristic(),cop]   
        fringe.append(temp)
    #victory=0
    '''state1=copy.deepcopy(state)
    state1.del_puz()
    state1.input_puz()
    is_eq=1
    for i in range(9):
        if state1.puzzle[i].val != state.puzzle[i].val:
            is_eq=0
    if is_eq==1:
        print True
    else:
        print False
    raw_input()
   # print state.is_eq(state1)
    #raw_input()
    '''
    
        #raw_input("hI")
        
        #print temp[0]
       # raw_input()
       # moves=state.getSuccessors(state,nodes)
    nodes+=1
    print "expanded:%d"%nodes
    copytemp=temp[:]
    if temp[len(temp)-1].heuristic() == 0 and victory==0:
        victory=1
        #victory_path=temp
        print "done: expanded :%d" % (nodes)
        print "solution is:"
        x=2
        while x <len(temp):
            print
            temp[x].show_puzzle()
            raw_input()
            x+=1
        return 
    #temp[len(temp)-1].()
    #raw_input()
    #level=temp[0]
    
    
    #moves=temp[len(temp)-1].AllMoves()
    moves=['r','u','l','d']
    level=temp[0]
    for y in moves:
                  
        copytemp=temp[:]
        #copyofcopy=copytemp[len(copytemp)-1]
        temp_state=copy.deepcopy(copytemp[len(copytemp)-1])
         #print "found valid moves"
        '''for y in moves:
            print y
        print "moving "
        print x'''
       
        #print "was:"
        #temp_state.show_puzzle()
        #raw_input()
        goahead=temp_state.do_move(y)
        '''is_eq=1
    for i in range(9):
        if state1.puzzle[i].val != temp_state.puzzle[i].val:
            is_eq=0
        if is_eq == 1 :
            print "successors:"
            temp_state.show_puzzle()
           1 raw_input()
       ''' 
        #print "now:"
        #temp_state.show_puzzle()
        #raw_input()
        #print "adding"
        #temp_state
        '''if goahead==1 and is_eq==1:
            temp[len(temp)-1].show_puzzle()
            print "moving%c" % y
            AStarAddToFringe(fringe,copytemp,temp_state,level+1)
            raw_input()
        else:
        '''
        
        if goahead==1:
            AStarAddToFringe(fringe,copytemp,temp_state)
            
            
    
    temp=AStarPopFringe(fringe,level)
    aStarSearch(temp,level,nodes,victory)
    
        
    
                  
def AStarAddToFringe(fringe,path,state):
    path.append(state)
    path[0]+=1
    level=path[0]
    path[1]=state.heuristic()
    fringe.append(path)
            
def AStarPopFringe(fringe,level):
    val_ret=[]
    print "level=%d" % level
    min=999999999999999999999999999999
    for x in fringe:
        '''print "for:"
        x[len(x)-1].show_puzzle()
        print "heuristic + level=%d +%d =%d" % (x[1],x[0],x[0]+x[1])
        raw_input()
        '''
        if int (int(x[1]) + int(x[0])) <min :
            min=x[1]+x[0]
            val_ret=x
        else:
            if (int(x[0])+int(x[1]))==min and int(x[0]) > val_ret[0]:
                min=x[1]+x[0]
                val_ret=x
        
                  
    carry_forward=val_ret
    fringe.remove(val_ret)
    
    return carry_forward
    
    
    
    

        
    
    
    
    
    
    
        
        


