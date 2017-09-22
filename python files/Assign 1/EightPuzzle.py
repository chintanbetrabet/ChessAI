from search import SearchProblem
from search import aStarSearch
import math
import copy
class ProblemState():
    def __init__(self,x,y,val):
        self.x=x
        self.y=y
        self.val=val
        #self.goal=[]
    def show_state(self):
        print"%d %d %d" % (self.x,self.y,self.val)
    def show_val(self):
        return self.val
    def show_x(self):
        return self.x
    def show_y(self):
        return self.y
    def disp(self):
        return self.val
     
class EightPuzzle(SearchProblem):
  
    def __init__(self):
        self.puzzle=[]
        #self.move=' '
    def make_goal(self):
        for x in range(3):
            for y in range(3):
                a=ProblemState(x,y,3*x+y)
                self.puzzle.append(a)
    def all_moves(self):
        return ['d','u','l','r']
        
        
                    
    def input_puz(self):
        size=0;i=0;
        print "enter the start position line wise(3 nums per line), enter zero for blank and no space b/w numbers"
        while size<9 :
            cont=1;k=0
            #print "size:%d" % size
            input=raw_input()
            while k <3 and cont==1 :
                val=input[k]
                val=int(val)
                cont=self.check_puz(val,size)
                if(cont ==True):
                    #print "passing: x=%d y=%d val=%d"%(size/3,k,val)
                    a=ProblemState(size/3,k,val)
                    #print "wrote: x=%d y=%d val=%d"%(a.x,a.y,a.val)
                    
                    self.puzzle.append(a)
                    size+=1
                    k+=1
                else :
                    print "failed due to invalid entry, re-enter line" ;
                    cont=0
                    for x in range(size%3):
                        self.puzzle.pop()
                        size-=size%3
                    k=0
    def check_puz(self,val,size):
        #print "size=%d"%size
        if size==0:
           #print "pity"
           return True
        if val>8 :
            print" value out of range(only enter 0-8)"
            return False
        else :
            for x in range(size):
                #print "%d checked at index:%d value = %d"%(val,x,self.puzzle[x].disp())
                if self.puzzle[x].disp()== val :
                    print "%d already exists at index:%d"%(val,x)
                    return False
        return True
    
    def is_eq(self,state):
        for x in range(9):
            if self.puzzle[x].disp()!=state.puzzle[x].disp():
                return False
            else:
                return True 
    def find_bl(self):
        for i in range(9):
            if self.puzzle[i].disp()==0:
                return i
            
    def is_up(self):
        pos=self.find_bl()
        if (self.puzzle[pos].show_x()!=0):
            #print "allowed up as x=%d" % self.puzzle[pos].x
            return True
        else:
            return False
    def is_down(self):
        pos=self.find_bl()
        if (self.puzzle[pos].show_x()!=2):
            #print "allowed down as x=%d" % self.puzzle[pos].x
            return True
        else:
            return False
    def is_left(self):
        pos=self.find_bl()
        if (self.puzzle[pos].show_y()!=0):
            #print "allowed lefft as y=%d" % self.puzzle[pos].y
            return True
        else:
            return False
    def is_right(self):
        pos=self.find_bl()
        if (self.puzzle[pos].show_y()!=2):
            #print "allowed up as y=%d" % self.puzzle[pos].y
            return True
        else:
            return False
    def null_heur(self):
        goal=EightPuzzle()
        count=0
        goal.make_goal()
        for i in range(9):
             if goal.puzzle[i].val!=self.puzzle[i].val:
                 count=1
        return count
    def heuristic(self):
        count=0
        goal=EightPuzzle()
        goal.make_goal()
        for source in self.puzzle:
           
           x=source.show_x()
           y=source.show_y()
           for perf in goal.puzzle:
               if perf.disp()==source.disp():
                   pos=perf
           add=0
           xg=int(pos.show_x())
           yg=int(pos.show_y())
           add+=pow(((x-xg)**2+(y-yg)**2),.5)
           #print "xg=%d x=%d yg=%d y=%d h+=%d for val:%d"%(xg,x,yg,y,add,source.disp())
           #raw_input()
           count+=add
        return self.null_heur()
    def move_up(self):
        pos=self.find_bl()
        x=self.puzzle[pos].show_x()
        y=self.puzzle[pos].show_y()
        if x>0:
            x-=1
        else:
            x+=1
        new_pos=3*x+y
        temp=self.puzzle[pos].disp()
        self.puzzle[pos].val=self.puzzle[new_pos].disp()
        self.puzzle[new_pos].val=temp
    def move_down(self):
        pos=self.find_bl()
        x=self.puzzle[pos].show_x()
        y=self.puzzle[pos].show_y()
        if x<2:
            x+=1
        else:
            x-=1
        new_pos=3*x+y
        temp=self.puzzle[pos].val
        self.puzzle[pos].val=self.puzzle[new_pos].val
        self.puzzle[new_pos].val=temp
        
    def move_left(self):
        pos=self.find_bl()
        x=self.puzzle[pos].show_x()
        y=self.puzzle[pos].show_y()
        if y>0:
            y-=1
        else :
            y+=1
        new_pos=3*x+y
        temp=self.puzzle[pos].disp()
        self.puzzle[pos].val=self.puzzle[new_pos].disp()
        self.puzzle[new_pos].val=temp
        
    def move_right(self):
        pos=self.find_bl()
        x=self.puzzle[pos].show_x()
        y=self.puzzle[pos].show_y()
        if(y<2):
            y+=1
        else:
            y-=1
        new_pos=3*x+y
        temp=self.puzzle[pos].disp()
        self.puzzle[pos].val=self.puzzle[new_pos].disp()
        self.puzzle[new_pos].val=temp
    def AllMoves():
        return ['u','l','r','d']
        
    def do_move(self,move):
        #print "i am::"
        #self.show_puzzle()
        #print "0 at: (%d,%d)" % (self.puzzle[self.find_bl()].x,self.puzzle[self.find_bl()].y)
        lis=self.legalMoves()
        #print "l moves in do_move are:"
        present=0
        '''for x in lis:
            if move==x:
                present=1
        if present==0:
            return 0
        '''
        #raw_input
        if move=='u' and self.is_up :
           # print "0 at: (%d,%d)" % (self.puzzle[self.find_bl()].x,self.puzzle[self.find_bl()].y)
           # print "allowed move up"
            self.move_up()
        else :
            if move=='d':
                #print "0 at: (%d,%d)" % (self.puzzle[self.find_bl()].x,self.puzzle[self.find_bl()].y)
                #print "allowed move down"
                self.move_down()
            else:
                if move=='l':
                   # print "0 at: (%d,%d)" % (self.puzzle[self.find_bl()].x,self.puzzle[self.find_bl()].y)
                   # print "allowed move left"
                    self.move_left()
                else:
                    if move=='r':
                        #print "0 at: (%d,%d)" % (self.puzzle[self.find_bl()].x,self.puzzle[self.find_bl()].y)
                        #print "allowed move right"
                        self.move_right()
        return 1
        
         
        
    def legalMoves(self):
        actions=[]
        
        if self.is_up():
            actions.append('u')
        if self.is_down():
            actions.append('d')
        if self.is_left():
            actions.append('l')
        if self.is_right():
            actions.append('r')
        return actions
    def explain_legal(self):
        if self.is_up():
            print " upa as y=%d" % self.puzzle[self.find_bl()].y
        if self.is_down():
            print " dn as y=%d" % self.puzzle[self.find_bl()].y
        if self.is_left():
           print " left as x=%d" % self.puzzle[self.find_bl()].x

        if self.is_right():
            print " right as x=%d" % self.puzzle[self.find_bl()].x

        #print "for this"
            
        #self.show_puzzle()
        #
        '''print "returning this"
        for x in actions:
            print x
        
        raw_input()'''
        #return actions
    def show_puzzle(self,x=3):
        for i in range(x):
                print "%d %d %d" % (self.puzzle[3*i].disp(),self.puzzle[3*i+1].disp(),self.puzzle[3*i+2].disp())

   
        
            
    def del_puz(self):
        while len(self.puzzle)>0:
            self.puzzle.pop()
        print "size now is:%d" %(len(self.puzzle))
    def make_goal(self):
        for x in self.puzzle:
            self.puzzle.pop()
        for i in range(3):
            for j in range(3):
                a=ProblemState(i,j,3*i+j)
                self.puzzle.append(a)
        #print "goal:"
        #self.show_puzzle()
        #print "heur:=%d"%(self.heuristic())
    def show_puzzle_details(self,x=3):
        for i in self.puzzle:
            print "%d (%d,%d)" % (i.val,i.x,i.y)
            #raw_input

    
    
fin=EightPuzzle()
fin.input_puz()
test1=EightPuzzle()
fin.show_puzzle()
aStarSearch(fin)
#temp=EightPuzzle()
#temp.copy_state(fin)
#temp.show_puzzle()




