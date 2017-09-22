import copy
import os
import time
class Square():
    def __init__(self,show,row,col,legal):
        self.show=show
        self.row=row
        self.col=col
        self.legal=copy.deepcopy(legal)
    def update(self):
        if len(self.legal)==1:
            self.show=str(self.legal[0])
        else :
            if self.show!='.':
                self.legal=self.legal[0:0]
                self.legal.append(int(self.show))
class Sudoku():
    def __init__(self,fil):
        self.Puzzle=[]
        pos=0
        univ_legal=[1,2,3,4,5,6,7,8,9]
        f=open(fil,'r')
        for i in range(9):
            line=f.readline()
            for j in range(9):                
                if line[j]=='.':
                    legal=copy.deepcopy(univ_legal)
                else:
                    legal=[line[j]]
                add=Square(line[j],i,j,legal)
                self.Puzzle.append(add)
    def __init__(self,string):
        self.Puzzle=[]
        pos=0
        univ_legal=[1,2,3,4,5,6,7,8,9]
        line=string.split()
        for i in range(9):
            for j in range(9):                
                if line[9*i+j]=='.':
                    legal=copy.deepcopy(univ_legal)
                else:
                    legal=[line[i*9+j]]
                add=Square(line[i*9+j],i,j,legal)
                self.Puzzle.append(add)
    def ret_box(self,i,j):
        start_i=i-i%3
        end_i=start_i+2
        start_j=j-j%3
        end_j=start_j+2
        return self.ret_lis(start_i,end_i,start_j,end_j)        
    def ret_col(self,i,j):
        start_i=0
        end_i=8
        start_j=j
        end_j=j
        return self.ret_lis(start_i,end_i,start_j,end_j)
    def ret_row(self,i,j):
        start_i=i
        end_i=i
        start_j=0
        end_j=8
        return self.ret_lis(start_i,end_i,start_j,end_j)        
    def ret_lis(self,i,i1,j,j1):
        start_i=i
        start_j=j
        lis=[]
        while i<=i1:
            j=start_j
            while j<=j1:
                if self.Puzzle[9*i+j].show!='.' and self.Puzzle[9*i+j].show!='0' :
                   lis.append(int(self.Puzzle[9*i+j].show))
                j+=1
            i+=1
        return lis        
    def upgrade(self,pos):
        if self.Puzzle[pos].show=='.' or self.Puzzle[pos].show=='0' :
            lis=self.ret_col(pos/9,pos%9)
            for x in self.Puzzle[pos].legal:                
                    if x in lis:
                        self.Puzzle[pos].legal.remove(int(x))
            lis=self.ret_row(pos/9,pos%9)
            for x in self.Puzzle[pos].legal:
                if x in lis and len(lis)>1:
                    #x=int(x)
                    self.Puzzle[pos].legal.remove(int(x))
            lis=self.ret_box(pos/9,pos%9)
            for x in self.Puzzle[pos].legal:
                if x in lis and len(lis)>1:
                    self.Puzzle[pos].legal.remove(int(x))
            self.Puzzle[pos].update()            
    def do_move(self,pos):
        if self.Puzzle[pos].show=='.' or self.Puzzle[pos].show=='0':
            self.move_col(pos/9,pos%9)
            self.move_row(pos/9,pos%9)
            self.move_box(pos/9,pos%9)
            self.Puzzle[pos].update()
    def print_legal_on_demand(self,i,i1,j,j1):
        start_j=j
        while i<=i1:
            j=start_j
            while j<=j1:
                print self.Puzzle[9*i+j].legal
                j+=1
            i+=1
    def show_puz(self):
        pos=0
        for i in range(9):
            print
            print ' '.join(self.Puzzle[9*i+j].show for j in range(9))
    def show_puz2(self):
        pos=0
        for i in range(9):
            #print
            print ' '.join(self.Puzzle[9*i+j].show for j in range(9)),
        print
    def move_box(self,i,j):
        start_i=i-i%3
        end_i=start_i+2
        start_j=j-j%3
        end_j=start_j+2
        return self.make_move(start_i,end_i,start_j,end_j)
    def move_col(self,i,j):
        start_i=0
        end_i=8
        start_j=j
        end_j=j
        return self.make_move(start_i,end_i,start_j,end_j)
    def move_row(self,i,j):
        start_i=i
        end_i=i
        start_j=0
        end_j=8
        return self.make_move(start_i,end_i,start_j,end_j)
    def make_move(self,i,i1,j,j1):
        start_i=i
        start_j=j
        special=0
        for num in range(1,10):
            count=0
            move_pos=-1
            i=start_i
            while i<=i1:
                j=start_j
                while j<=j1:
                    pos=9*i+j
                    if len(self.Puzzle[pos].legal)==1 and int(self.Puzzle[pos].show)==num:
                        count=-100000
                    if len(self.Puzzle[pos].legal)!=1:
                        for x in self.Puzzle[pos].legal:
                            if int(x)==num:
                                if count==0:
                                    move_pos=pos
                                count+=1
                    j+=1
                i+=1            
            if count==1 and self.Puzzle[move_pos].show=='.':
                self.Puzzle[move_pos].show=str(num)
                self.Puzzle[move_pos].level=copy.deepcopy([num])
                self.Puzzle[move_pos].update()
                for p in range(81):
                    self.upgrade(p)
                #self.show_puz();
                #raw_input();
                
def fil_count(pu):
    count=0
    for i in range(81):
        if pu.Puzzle[i].show!='.':
            count+=1
    return count
t=input()
while(t>0):
    t-=1
    x=raw_input()
    x1=""
    for i in x:
        if i =='0':
            x1+='.'
        else:
            x1+=i
    #print x1
    #t=time.clock()
    #sud=Sudoku("sud.txt")
    sud=Sudoku(x1)
    #sud.show_puz()
    last=fil_count(sud)
    j=0
    while last!=81:
        #print "last=%d"%last
        for i in range(81):
            sud.upgrade(i)    
        #sud.show_puz()
        if j>0 and last==fil_count(sud):
            for i in range(81):
                sud.do_move(i)
        last=fil_count(sud)
        j+=1
    #t=time.clock()-t1
    #print "after time %f"%t
    sud.show_puz2()

#raw_input("donne")               
                
                
                
