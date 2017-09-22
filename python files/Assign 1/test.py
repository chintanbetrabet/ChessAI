from search import aStarSearch
from search import SearchProblem
import copy
class MapObj:
    def __init__(self,x,y,val):
        self.x=x
        self.y=y
        self.val=val
    def show_val(self):
        return self.val
    def show_x(self):
        return self.x
    def show_y(self):
        return self.y
    def show_state(self):
        print "in show_state()"
        print"%d %d %c" % (self.x,self.y,self.val)
class Map(SearchProblem):
    def __init__(self):
        self.treasures=[]
        self.puzzle=[]
        self.xsize=20
        self.ysize=20
        
    def all_moves(self):
        return ['u','l','d','r']
    def find_curr(self):
    
        for i in range(self.xsize*self.ysize):
            if self.puzzle[i].val=='s':
                #print "found"
                pos=i
                return pos
        print "missing"
        #raw_input()
           
    def is_up(self):
        pos=self.find_curr()
        x=pos/self.ysize
        y=pos%self.ysize
        if ( x >0 ):
            new_pos=(x-1)*self.ysize+(y)
            if self.puzzle[new_pos].val !='#':
                return True
            else :
                return False
        else :
            return False
    
    def is_down(self):
        pos=self.find_curr()
        x=pos/self.ysize
        y=pos%self.ysize
        #print "in is down pos=%d x=%d y=%d" % (pos,x,y)
        if ( x < self.xsize-1 ):
            pos1=(x+1)*self.ysize+(y)
            #print "in is down pos2=%d" % pos1
            if self.puzzle[pos1].val !='#':
                return True
            else :
                return False
        else :
            return False
    
            
    def is_left(self):
        pos=self.find_curr()
        x=pos/self.ysize
        y=pos%self.ysize
        
        if ( y > 0 ):
            pos1=x*self.ysize+(y-1)
            if self.puzzle[pos1].val !='#':
                return True
            else :
                return False
        else :
            return False
    
    def set_curr(self):
        for x in self.puzzle:
            if x.val=='s':
                x.show_state()
                
    def is_right(self):
        pos=self.find_curr()
        x=pos/self.ysize
        y=pos%self.ysize
        
        if ( y < self.ysize-1):
            pos1=x*self.ysize+(y+1)
            if self.puzzle[pos1].val !='#':
                return True
            else :
                return False
        else :
            return False
    
    
    def legalMoves(self):
        actions=[]
       # print "legalMoves Called"
        if self.is_up():
            actions.append('u')
        if self.is_down():
            #print "legalMoves Called is d"
            actions.append('d')
        if self.is_left():
            actions.append('l')
        if self.is_right():
            actions.append('r')
        pos=self.find_curr()
        # "Legal at pos=%d x,y =%d,%d:" %(pos,pos//self.ysize,pos%self.ysize)
        #print actions
        
        return actions
    def do_move(self,move):
        present=0
        pos=self.find_curr()
        lis=self.legalMoves()
        for x1 in lis:
            if x1==move:
                present=1
                pos=self.find_curr()
                #print "pos: indo is %d" %pos
            #self.puzzle[pos].show_state()          
        pos2=-1
        if(present==1):
            #print "pos= %d moving:%c" % move          
            if move=='u':
                pos2=(self.puzzle[pos].x-1)*self.ysize+self.puzzle[pos].y
            else :
                if move=='d':
                    #print "pos=%d x=%d y=%d " % (pos,self.puzzle[pos].x,self.puzzle[pos].y)
                    pos2=(self.puzzle[pos].x+1)*self.ysize+self.puzzle[pos].y
                    #print "pos2=%d" %pos2
                else:
                    if move=='l': 
                        pos2=(self.puzzle[pos].x)*self.ysize+self.puzzle[pos].y-1
                    else:
                        if move=='r':
                            pos2=(self.puzzle[pos].x)*self.ysize+self.puzzle[pos].y+1
        else :
            return 0
        #found=0
        #print "pos= %d moving:%c to pos2=%d" % (pos,move,pos2)
        #print "swapping pos2=%d"%pos2
        #print "maze size: %d" % (len(self.puzzle))
        #self.puzzle[pos].show_state()
        #self.puzzle[pos2].show_state()
        ##raw_input()
        for pr in self.treasures:    
            if pos2==pr:                               
                self.treasures.remove(pos2)
                print "found treasure"
                self.puzzle[pos2].val='.'
                #self.show_puzzle()
                #raw_input()
            
                
            #if self.puzzle[pos].val=='t':
           # #raw_input()
        #temp=' '
        
        self.puzzle[pos].val='.'
        self.puzzle[pos2].val='s'

        #print "pos= %d moving:%c to pos2=%d" % (pos,move,pos2)
        #self.puzzle[pos2].show_state()
        #print "current:"
        #print self.find_curr()
        #self.puzzle[self.find_curr()].show_state()
        #print "left: %d" % len(self.treasures)
        '''if (len(self.treasures)) ==5 :
            raw_input()
        #self.show_puzzle()
        #raw_input()
        '''
        return 1
        
        

        
    def show_puzzle(self):
        #print "treasures at"
        #print self.treasures
        #print self.find_curr()
        for j in range(self.xsize):
            #print "range:%d"%(self.xsize)
            #print"x=%d"%j
            print ''.join(self.puzzle[j*self.xsize+i].val for i in range(self.ysize))
    def heuristic(self):
        count=0
        dis=[]
        if len(self.treasures)==0:
            count=0
        else:
            #dis=[]
            pos=self.find_curr()
            for tre in self.treasures:
                x=self.puzzle[tre].x
                y=self.puzzle[tre].y
                x1=self.puzzle[pos].x
                y1=self.puzzle[pos].y
                add=abs(x-x1)+abs(y-y1)
                dis.append(add)
                count=sum(dis)
        #return sum(dis)*len(self.treasures)
        return count
                
                
        
        return count
    def input_puz(self,fil):
        f=open(fil,'r')
        x=f.readline()
        tot=0
        print x
        
        i=0
        while x[i]!=' ':            
            i+=1
            #print "loop1"
        y=x[:i]
        #print "hi"
        self.xsize=int(y)
        i+=1
        j=i
        while j<len(x):            
            j+=1
        y=x[i:j]
        self.ysize=int(y)
        print "xs: %d  ys:%d"%(self.xsize,self.ysize)
        #i=0
        #j=0
        for line in f:
            #j=0
            for y in line:
                i=tot/self.ysize
                j=tot%self.ysize
                
                a=MapObj(i,j,y)
                if y =='t':
                    #print "treasure:"
                    #a.show_state()
                    ##raw_input()
                    self.treasures.append(i*self.ysize+j)
                if y!=' ' and y!='\n':
                    self.puzzle.append(a)
                    tot+=1
                                    
                
        self.set_curr()
        print self.find_curr()
        #self.puzzle[self.find_curr()].show_state()
        

   

TreasureMap=Map()
TreasureMap.input_puz('m.txt')
print TreasureMap.puzzle[20].show_state()
print "maze size: %d" % (len(TreasureMap.puzzle))
TreasureMap.show_puzzle()
#print TreasureMap.find_curr()

#TreasureMap.puzzle[1].show_state()
#TreasureMap.show_puzzle()
aStarSearch(TreasureMap)
        
    
    
        
