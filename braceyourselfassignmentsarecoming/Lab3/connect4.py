import copy
import os
from minimax import minimax
import time
class Square():
    def __init__(self,row,col,show):
        self.row=row
        self.col=col
        self.show=show
class Connect():
    def __init__(self,size_r,size_c,player):
        self.Puzzle=[]
        self.max_row=size_r
        self.max_col=size_c
        self.player=player
        self.winner=" "
        for i in range(size_r):
            for j in range(size_c):
                add=Square(i,j,'.')
                self.Puzzle.append(add)
    def successor(self,col,symbol):
        cont=1
        i=0
        while cont==1:
            if self.Puzzle[self.max_col*i+col].show=='.':
                cont=0
            else:
                i+=1
        self.Puzzle[self.max_col*i+col].show==symbol
    def evaln(self):
        if self.heur('O')>3:
                return -1000
        else:
            if self.heur('X')>3:
                return 10000
            else:
                return self.heur('X')-self.heur('O')
    def heur(self,play):
        t1=time.clock()
        count=0
        if play=='X':
            opp='O'
        else:
            opp='X'
        vals={0}
        max_lis=set()
        begin=0
        i=0
        j=0
        for cols in range(self.max_col):
            i=0
            count=0
            prev=-1
            begin=0
            while i<self.max_row:              
                pos=i*self.max_col+cols
                if begin==0 and self.Puzzle[pos].show==play:
                    begin=1
                if begin==1:
                    if self.Puzzle[pos].show==opp:
                        if prev<0 or prev>self.max_row*self.max_col-1:
                            if count > 3:
                                winner=play
                        else:
                            if self.Puzzle[prev].show=='.':                            
                                vals.update({count})                            
                        count=0
                        begin=0
                        vals.update({count})                     
                        
                    if self.Puzzle[pos].show==play:
                        if count==0:
                            prev=(i-1)*self.max_col+cols
                        count+=1
                    if self.Puzzle[pos].show=='.':
                        vals.update({count})
                        count=0
                        begin=0               
                i+=1
        max_lis.update({max(vals)})
        vals={0}
        count=0
        #row search
        for rows in range(self.max_row):
            i=0
            prev=-1
            count=0
            begin=0
            while i<self.max_col:
                pos=rows*self.max_col+i
                if begin==0 and self.Puzzle[pos].show==play:
                    begin=1
                if begin==1:
                    if self.Puzzle[pos].show==opp:
                        if prev<0 or prev>self.max_row*self.max_col-1:
                            if count > 3:
                                winner=play
                        else:
                            if self.Puzzle[prev].show=='.':                            
                                 vals.update({count})
                        count=0
                        begin=0
                    if self.Puzzle[pos].show==play:
                    
                        if count==0:
                            prev=rows*self.max_col+i-1
                        count+=1
                    if self.Puzzle[pos].show=='.':
                        vals.update({count})
                        count=0
                        begin=0

                    
                i+=1
        max_lis.update({max(vals)})
        vals={0}
        count=0
        #diagonal search1

        for x in range(self.max_col):
            curr_row=0
            curr_col=x
            count=0
            prev=-1
            begin=0
            while curr_row<self.max_row and curr_col<self.max_col:
                pos=curr_row*self.max_col+curr_col
                if begin==0 and self.Puzzle[pos].show==play:
                    begin=1
                if begin==1:
                    #print "IN diag:%d count=%d"%(curr_row,count)
                        
                    if self.Puzzle[pos].show==opp:
                        if prev<0 or prev>self.max_row*self.max_col-1:
                            if count >=4:
                                #print "victory for %c"%play
                                winner=play
                        else:
                            if self.Puzzle[prev].show=='.':                            
                                '''if count>=3:
                                    print "for play:%s in prev= %dcol:%d count=%d"%(play,prev,cols,count)
                                    #raw_input()
                                '''
                                vals.update({count})
                        count=0
                        begin=0
                    
                    if self.Puzzle[pos].show==play:
                        if count==0:
                            prev=(curr_row-1)*self.max_col+(curr_col-1)
                        count+=1
                    if self.Puzzle[pos].show=='.':
                        vals.update({count})
                        count=0
                        begin=0
                curr_row+=1
                curr_col+=1
        
        max_lis.update({max(vals)})
        vals={0}
        #diagonal search2
        count=0        
        for x in range(self.max_col):
            curr_row=0
            curr_col=x
            prev=-1
            count=0
            begin=0
            while curr_row<self.max_row and curr_col>=0:
                pos=curr_row*self.max_col+curr_col
                if begin==0 and self.Puzzle[pos].show==play:
                    begin=1
                if begin==1:
                    #print "IN diag:%d count=%d"%(curr_row,count)
                        
                    if self.Puzzle[pos].show==opp:
                        if prev<0 or prev>self.max_row*self.max_col-1:
                            if count >=4:
                                winner=play
                        else:
                            if self.Puzzle[prev].show=='.':                            
                                vals.update({count})
                        count=0
                        vals.update({0})
                        begin=0                    
                    if self.Puzzle[pos].show==play:
                        if count==0:
                            prev=(curr_row-1)*self.max_col+(curr_col+1)
                        count+=1
                    if self.Puzzle[pos].show=='.':
                        vals.update({count})
                        count=0
                        begin=0
                curr_row+=1
                curr_col-=1        
        max_lis.update({max(vals)}) 
        
        if max(max_lis)>3:
            self.winner=play
        #print "iteration time:%f"%(time.clock()-t1)
        #raw_input()
        return (max(max_lis))    
    def show_board(self):
            print ' '.join(str(j) for j in range(self.max_col))
            for i in range(self.max_row):
                print
                print ' '.join(self.Puzzle[self.max_col*(self.max_row-i-1)+j].show for j in range(self.max_col))
    def move(self,symbol,col):
        i=0
        pos_m=-1
        cont=1
        while cont==1 and i<self.max_row:
            pos=i*self.max_col+col
            if self.Puzzle[pos].show=='.':
                self.Puzzle[pos].show=symbol
                cont=0
                pos_m=pos
            i+=1
        if pos_m==-1:
            print "Invalid Entry"
        return pos_m
move2=[]
def move1_do(puz,symbol):
    move1=[]
    move2=[]
    for i in range(puz.max_col):
        puz1=copy.deepcopy(puz)
        do=puz1.move(symbol,i)
        if do !=-1:
            move1.append(puz1)
    ind=0
    if symbol=='X':
        symbol='O'
    else :
        symbol='X'
    for x in move1:
        
        move2_do(move2,x,symbol,ind)
        ind+=1
    ret_ind=minimax(move2)
    return(move1[ret_ind])
def move2_do(move2,puz,symbol,ind):
    
    for i in range(puz.max_col):
        puz1=copy.deepcopy(puz)
        do=puz1.move(symbol,i)
        if do !=-1:
            move2.append([ind,puz1])
def get_play():
    x=raw_input("Enter your symbol: X or O:")
    if x=='X' or x== 'x':
        x='X'
        opp='O'
    else:
        if x=='O' or x=='o':
            x='O'
            opp='X'
        else:
            print "invalid entry "
            raw_input("Press any key to continue")
            get_play()
    return x,opp
connect=Connect(10,10,'X')
player='O'
opp='X'
print "YOU are:%c"%player
connect.show_board()
while(connect.heur(player)!=4 and connect.heur(opp)!=4):
    os.system('cls')
    connect.show_board()
    print "streak for %s is:%d"%(player,connect.heur(player))
    print "streak for %s is:%d"%(opp,connect.heur(opp))
    #raw_input()
    print "%s enter col"%player
    col=int(raw_input())
    x=-1
    while x==-1:
        x=connect.move(player,col)
    connect.show_board()
    if connect.winner==" ":
        connect=copy.deepcopy(move1_do(connect,opp))
    #raw_input()
    os.system('cls')
    connect.show_board()
    print "winner is %s"%connect.winner
connect.show_board()
print "streak for %s is:%d"%(player,connect.heur(player))
print "streak for %s is:%d"%(opp,connect.heur(opp))
print "winner is %s"%connect.winner
raw_input()
