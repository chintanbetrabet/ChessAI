from abc import ABCMeta
import util
import copy
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
    def getSuccessors(self,state):
        #actions=[]
        return state.all_moves()
        

def aStarSearch(state):
    fringe=[]
    level=0
    nodes=0
    fringe.insert(len(fringe),[level,state.heuristic(),state])
    victory=0
    while victory==0:
        temp=AStarPopFringe(fringe,level,state)
        moves=temp[len(temp)-1].getSuccessors(temp[len(temp)-1])
        nodes+=1
        if nodes%100 ==0:
            print "expanded:%d  now at:"%nodes
        #temp[len(temp)-1].puzzle[temp[len(temp)-1].find_curr()].show_state()
        #temp[len(temp)-1].show_puzzle()
        #raw_input()
        copytemp=temp[:]
        if temp[len(temp)-1].heuristic() == 0 :
            victory=1
            print "done: expanded :%d" % (nodes)
            print "solution is:"
            x=2
            while x <len(temp):
                print
                temp[x].show_puzzle()
                raw_input()
                x+=1
            return 1
        level=temp[0]
        
        
        for y in moves:
            copytemp=temp[:]
            copyofcopy=copytemp[len(copytemp)-1]
            temp_state=copy.deepcopy(copytemp[len(copytemp)-1])
            goahead=temp_state.do_move(y)
            
            if goahead==1:
                '''print "moved %c"% y
                temp_state.show_puzzle()
                raw_input()
                '''
                #print "move %c is done" % y
                AStarAddToFringe(fringe,copytemp,temp_state,level+1)
    
        
    
                  
def AStarAddToFringe(fringe,path,state,level):
    path.append(state)
    path[0]=level
    path[1]=state.heuristic()
    fringe.insert(len(fringe)+1,path)
            
def AStarPopFringe(fringe,level,state):
    val_ret=[]
    #print "level=%d" % level
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
#def BFS(state):
        
    
    
    
    

        
    
    
    
    
    
    
        
        


