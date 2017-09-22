import copy
import sys
import os
import random
max_tile=2
class Square:
    def __init__(self,row,col):
        self.val=0
        self.row=row
        self.col=col
        self.cont=1
        
    def show_piece(self):
        if self.val!=0:
            return "%4d"%self.val
        else :
            return "%4s"%"."
class Board:
    def __init__(self,size_r,size_c,goal):
        self.Puzzle=[]
        self.max_row=size_r
        self.max_col=size_c
        self.score=0
        self.goal=goal
        #self.player=player
        #self.winner=" "
        for i in range(size_r):
            for j in range(size_c):
                add=Square(i,j)
                self.Puzzle.append(add)
        
        x1=random.randint(0,size_r*size_c-1)
        x2=x1
        while x2==x1:
            x2=random.randint(0,size_r*size_c-1)
        self.Puzzle[x1].val=2
        self.Puzzle[x2].val=2
        '''
        self.Puzzle[12].val=4196
        self.Puzzle[0].val=2048
        self.Puzzle[4].val=1024
        self.Puzzle[8].val=512
        '''
    def do_move(self,move,up,down,left,right,maxi='y'):
        effect=0
        global max_tile
        if move==up:
            #i=self.max_row-1
            for i in range(1,self.max_row):
                for c in range(self.max_col):
                    pos1=i*self.max_col+c
                    pos2=pos1                    
                    while pos2>=self.max_col and self.Puzzle[pos2-self.max_col].val==0:
                        pos2-=self.max_col
                    if pos2>=self.max_col and  self.Puzzle[pos1].val==self.Puzzle[pos2-self.max_col].val and self.Puzzle[pos2-self.max_col].cont==1:
                       
                            pos2-=self.max_col
                      

                            
                    if self.Puzzle[pos1].val==self.Puzzle[pos2].val and pos2!=pos1 and self.Puzzle[pos2].cont==1 :
                        self.Puzzle[pos2].val*=2
                        if self.Puzzle[pos2].val>max_tile and maxi=='y':
                            max_tile=self.Puzzle[pos2].val
                        if maxi=='y':
                            self.score+=self.Puzzle[pos2].val
                        if self.Puzzle[pos2].val!=0:
                                
                                self.Puzzle[pos2].cont=0
                                #self.show_board()
                                
                        #self.Puzzle[pos2].cont=0
                                self.Puzzle[pos1].val=0
                        
                        #raw_input()
                        
                    else:
                        if self.Puzzle[pos2].val==0 :
                            self.Puzzle[pos2].val=self.Puzzle[pos1].val
                            #self.show_board()
                            #raw_input()                            
                   # print "pos1=%d pos2=%d"%(pos1,pos2)
                    if pos2!=pos1 and pos2>=0 and pos2<self.max_col*self.max_row:
                        self.Puzzle[pos1].val=0
                        if self.Puzzle[pos2].val!=0:
                                effect+=1
                                #i-=1
                      
        else :
            if move==down:
                i=self.max_row-2
                while i>=0:
                    for c in range(self.max_col):
                        pos1=i*self.max_col+c
                        pos2=pos1
                        while pos2<self.max_col*(self.max_row-1) and self.Puzzle[pos2+self.max_col].val==0:
                            pos2+=self.max_col
                        
                        if pos2<self.max_col*(self.max_row-1) and self.Puzzle[pos1].val==self.Puzzle[pos2+self.max_col].val and self.Puzzle[pos2+self.max_col].cont==1:
                           pos2+=self.max_col
                        if pos2!=pos1  and self.Puzzle[pos1].val==self.Puzzle[pos2].val:
                            self.Puzzle[pos2].val*=2
                            if self.Puzzle[pos2].val>max_tile and maxi=='y':
                                max_tile=self.Puzzle[pos2].val
                            if  maxi=='y':
                                self.score+=self.Puzzle[pos2].val
                            if self.Puzzle[pos2].val!=0:
                                self.Puzzle[pos2].cont=0
                                #self.show_board()
                                #print "cont=0 at %d"%pos2
                                self.Puzzle[pos1].val=0
                            
                        else:
                            if self.Puzzle[pos2].val==0:
                                self.Puzzle[pos2].val=self.Puzzle[pos1].val
                        #print "pos1=%d pos2=%d"%(pos1,pos2)
                        if pos2!=pos1 and pos2>=0 and pos2<self.max_col*self.max_row:
                            if self.Puzzle[pos2].val!=0:
                                effect+=1
                            self.Puzzle[pos1].val=0
                    i-=1
            else:
                if move==left:
                    for c in range(1,self.max_col):
                        for i in range(self.max_row):
                            pos1=i*self.max_col+c
                            pos2=pos1
                            col=c
                            while col>0 and self.Puzzle[pos2-1].val==0:
                                pos2-=1
                                col-=1
                            if col>0 and self.Puzzle[pos2-1].val==self.Puzzle[pos1].val and self.Puzzle[pos2-1].cont==1:
                                pos2-=1

                            if pos2!=pos1  and self.Puzzle[pos1].val==self.Puzzle[pos2].val and self.Puzzle[pos2].cont==1:
                                self.Puzzle[pos2].val*=2
                                if self.Puzzle[pos2].val>max_tile and maxi=='y':
                                    max_tile=self.Puzzle[pos2].val
                                if  maxi=='y':
                                    self.score+=self.Puzzle[pos2].val
                                if self.Puzzle[pos2].val!=0:
                                    
                                    self.Puzzle[pos2].cont=0
                                    #self.show_board()
                                    self.Puzzle[pos1].val=0
                                #self.show_board()
                                
                            else:
                                if self.Puzzle[pos2].val==0:
                                    self.Puzzle[pos2].val=self.Puzzle[pos1].val
                            if pos2!=pos1 and pos2>=0 and pos2<self.max_col*self.max_row:
                                if self.Puzzle[pos2].val!=0:
                                    effect+=1
                                self.Puzzle[pos1].val=0
                else:
                    if move==right:
                        c=self.max_col-2
                        while c>=0:
                            for i in range(self.max_row):
                                pos1=i*self.max_col+c
                                pos2=pos1
                                col=c
                                while col<self.max_col-1 and self.Puzzle[pos2+1].val==0:
                                    pos2+=1
                                    col+=1
                                if col<self.max_col-1 and self.Puzzle[pos2+1].val==self.Puzzle[pos1].val and self.Puzzle[pos2+1].cont==1:
                                    pos2+=1

                                if pos2!=pos1  and self.Puzzle[pos1].val==self.Puzzle[pos2].val and self.Puzzle[pos2].cont==1:
                                    self.Puzzle[pos2].val*=2
                                    if self.Puzzle[pos2].val>max_tile and maxi=='y':
                                        max_tile=self.Puzzle[pos2].val
                                    if  maxi=='y':
                                        self.score+=self.Puzzle[pos2].val
                                    if self.Puzzle[pos2].val!=0:
                                        
                                        self.Puzzle[pos2].cont=0
                                        #self.show_board()
                                        self.Puzzle[pos1].val=0
                                    
                                else:
                                    if self.Puzzle[pos2].val==0:
                                        self.Puzzle[pos2].val=self.Puzzle[pos1].val
                                if pos2!=pos1 and pos2>=0 and pos2<self.max_col*self.max_row:
                                    if self.Puzzle[pos2].val!=0:
                                        effect+=1
                                    self.Puzzle[pos1].val=0
                            c-=1
        self.reset_cont(effect,maxi)
        return effect
    def reset_cont(self,effect,maxi):
        if maxi=='y':
            print "effect=%d"%effect
        for i in range(len(self.Puzzle)):
            self.Puzzle[i].cont=1
        if effect>0:
            x=random.randint(0,self.max_col*self.max_row-1)
            while self.Puzzle[x].val!=0:
                x=random.randint(0,self.max_col*self.max_row-1)
            #print "adding at %d"%x
            ran=random.randint(0,10)
            if ran!=10:
                self.Puzzle[x].val=2
            else:
                self.Puzzle[x].val=4
            #self.show_board()
        else:
            if maxi=='y':
                print " ILLEGAL MOVE"
                #raw_input()
        
            
    #def legal(self):
        
    def show_board(self):
        #print ' '.join(str(j) for j in range(self.max_col))
        for i in range(self.max_row):
                print
                print ' '.join(self.Puzzle[self.max_col*(i)+j].show_piece() for j in range(self.max_col))
    def legal(self,up,down,left,right):
        leg=[up,down,left,right]
        effect=0
        
        for x in leg:
            check=copy.deepcopy(self)
            effect+=check.do_move(x,up,down,left,right,'n')
        return effect

def play(a,up,down,left,right):
    global max_tile
    while a.legal(up,down,left,right)!=0 and max_tile<2048:
        os.system('cls')
        print "score:%d \n Max tile=%d\n GOAL tile:%d"%(a.score,max_tile,a.goal)
        a.show_board()
        print "Enter move: %s,%s,%s,%s:"%(up,down,left,right)
        move=input()
        a.do_move(move,up,down,left,right)
    if max_tile<a.goal:
        print " Thank You for Playing Your score was:%d Max tile:%d"%(a.score,max_tile)
    else:
        print "YOU WON!!!"
    raw_input()
    #a.show_board()
'''
a.do_move('l')
a.show_board()
'''

yes="YES"
print "CHOOSE YOUR CONTROLS:"
controls=[]
up=raw_input("ENTER  KEY FOR UP")
controls.append(up)
down=up
while down in controls:
    down=raw_input("ENTER  KEY FOR DOWN")
controls.append(down)
left=up
while left in controls:
    left=raw_input("ENTER  KEY FOR LEFT")
controls.append(left)
right=up
while right in controls:
    right=raw_input("ENTER  KEY FOR RIGHT")
controls.append(right)
#left=raw_input("ENTER  KEY FOR LEFT")

#right=raw_input("ENTER  KEY FOR RIGHT")
#os.system('cls')
size=-1
while size<2 :
    size=int(raw_input( "ENTER DIMENSION OF SQUARE (2-10) : "))
while(yes=="YES"):
    final=2**(size*2+3)
    a=Board(size,size,final)
    play(a,up,down,left,right)
    yes=raw_input("continue?")
    yes.upper()
    max_tile=2
    

    

                    
                            
                
                        
            
