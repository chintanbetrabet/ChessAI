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
    def getSuccessors(self,state,nodes):
        #actions=[]
        return state.legalMoves()
        

def aStarSearch(state):
    fringe=[]
    victory_path=[]
    level=0
    nodes=0
    fringe.insert(len(fringe),[level,state.heuristic(),state])
    victory=0
    state1=copy.deepcopy(state)
    state1.del_puz()
    state1.input_puz()
    '''is_eq=1
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
    while victory==0:
        #raw_input("hI")
        temp=AStarPopFringe(fringe,level,state,state1)
        #print temp[0]
       # raw_input()
       # moves=state.getSuccessors(state,nodes)
        nodes+=1
        print "expanded:%d"%nodes
        copytemp=temp[:]
        if temp[len(temp)-1].heuristic() == 0 :
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
            return 1
        #temp[len(temp)-1].()
        #raw_input()
        level=temp[0]
        
        #raw_input("eioohgoiheoigheogih")
        moves=['u','l','d','r']
        for y in moves:
            '''if nodes == 92:
                print y
                temp[len(temp)-1].explain_legal()
            '''
            
            copytemp=temp[:]
            copyofcopy=copytemp[len(copytemp)-1]
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
                raw_input()
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
                AStarAddToFringe(fringe,copytemp,temp_state,level+1)
    
        
    
                  
def AStarAddToFringe(fringe,path,state,level):
    path.append(state)
    path[0]=level
    path[1]=state.heuristic()
    fringe.insert(len(fringe)+1,path)
            
def AStarPopFringe(fringe,level,state,state1):
    val_ret=[]
    print "level=%d" % level
    #print "fringe has %d elements:" % (len(fringe))
    #raw_input()
    min=999999999999999999999999999999
    for x in fringe:
        ##print "for:"
        #x[len(x)-1].show_puzzle()
        #print "cost =%d(%d) + %d = %d" % (x[0],len(x)-2,x[1],x[0]+x[1])
        #
        
        if int (int(x[1]) + int(x[0])) <min :
            min=x[1]+x[0]
            val_ret=x
        else:
            if (int(x[0])+int(x[1]))==min and int(x[0]) > val_ret[0]:
                min=x[1]+x[0]
                val_ret=x
    #print "level returned=%d" % val_ret[0]
    
    #raw_input()
        
                  
    carry_forward=val_ret
    #print "fringe has%d" %(len(fringe))
    fringe.remove(val_ret)
    #print "fringe has%d" %(len(fringe))
    #print "current  best state:(%d,%d)"%(carry_forward[0],carry_forward[1])
    '''=1
    for x in range(9):
        if state1.puzzle[x].val==carry_forward[len(carry_forward)-1].puzzle[x].val:
            is_eq=0
    '''
    '''if level == 8 :
        print "stop"
        raw_input()
    '''
    
    return carry_forward
#def BFS(state):
        
    
    
    
    

        
    
    
    
    
    
    
        
        


