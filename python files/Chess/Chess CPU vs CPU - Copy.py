
'''
check and check mate need working
Computer doesnt understand king-king zone
need better heuristic/evaluation function
'''
#alpha=0.1
#move_jump=[]
move1=[]
move2=[]
check_mate=0
dead=0
import random
import copy
import os
import time
from cminimax4 import minimax
class Piece_def():
    def __init__(self,row=0,col=0,color='G',piece_type="**"):
        self.Color=color
        self.Type=piece_type
        self.Row=row
        self.Col=col
        
    def show_piece(self):
        
        if self.Color!='G':
            return "%s%c |"%(self.Type,self.Color)
        else:
            if (self.Row+self.Col)%2!=0:
                return "*** |"
            else :
                return "    |"
    def show_det(self):
        
        if self.Color!='G':
            return "%s%c |%d %d"%(self.Type,self.Color,self.Row,self.Col)
        else:
            return "*** |"
    def ret_pos(self):
        return self.Col+self.Row*8
        
        
class Square():
    def __init__(self,color,piece):
        self.Color=color
        self.Piece=Piece_def()
        self.Piece=copy.deepcopy(piece)
        
    def show_color(self):
        if self.Color=='B':
            return "*%d%d|"%(self.Piece.Row,self.Piece.Col)
        else :
            return " %d%d|"%(self.Piece.Row,self.Piece.Col)
class Board_State():
    check_mate=0
    alpha=0.1
    Score={'Qu':9,'Kn':4,'Ki':999,'Pn':1,'Bi':3,'Ro':5};
    Weight={'Qu':1,'Kn':1,'Ki':999,'Pn':1,'Bi':1,'Ro':1}
    #Weight={'Qu':9,'Kn':4,'Ki':999,'Pn':1,'Bi':3,'Ro':5}
    symbols=["Qu","Bi","Ki","Kn","Pn","Ro"]
    def Set_reset(self):
        for i in range(63):
            self.Set[i].Piece.Row=i/8
            self.Set[i].Piece.Col=i%8
            
    def reset_square_cols(self):
        for x in self.Set:
            row=x.Piece.Row
            col=x.Piece.Col
            if (row+col)%2==0:
                x.Color='W'
            else :
                x.Color='B'
    
    def __init__(self,fil):
        self.QuitVal=-9999
        self.Set=[]
        self.LastPos=0
        self.NextPos=0
        self.White=[]
        self.Black=[]
        self.univ_leg=set()
        self.LastMoved=' '
        self.PieceNum={'W':{'Qu':1,'Kn':2,'Ki':1,'Pn':8,'Bi':2,'Ro':2},'B':{'Qu':1,'Kn':2,'Ki':1,'Pn':8,'Bi':2,'Ro':2}}
        self.minimaxVal=0
        self.ExpVal=0
        self.NoMoves=0
        self.bcWeight=2
        self.check_state=''
        self.control={'W':0,'B':0}
        f=open(fil,'r')
        #pos=0
        for i in range(8):
            line=f.readline()
            for j in range(8):
                title=line[4*j:4*j+3]
                piece_color=title[2]
                piece_type=title[:2]
                
                color='G'
                if piece_color=='*':
                    piece_color='G'
                if (i+j)%2 !=0:
                    color='B'
                else :
                    color='W'
                new_piece=Piece_def(i,j,piece_color,piece_type)
                sq=Square(color,new_piece)
                if piece_color=='B':
                    self.Black.append(new_piece)
                else :
                    if piece_color=='W':
                        self.White.append(new_piece)
                self.Set.append(sq)
       
        
    def board_control(self,lev,color):
        
        return 0
        return self.control[color]
    def tieBreaker(self,color):
        i=self.NextPos/8
        j=self.NextPos%8
        
        return (-i**2+7*i)*(-j**2+7*j)+self.control[color]*self.bcWeight
        
    def getScore(self,color):
        score=0
        if color=='W':
            opp='B'
        else :
            opp='W'
        for x in self.symbols:
            score+=(self.PieceNum[color][x]-self.PieceNum[opp][x])*self.Score[x]
        return score
    def evaln(self,lev,color):
        score=0
        if color=='W':
            opp='B'
        else :
            opp='W'
        #print "Kings:%s"% self.PieceNum[color]["Ki"]
        if self.PieceNum[color]["Ki"]!=1:
            return self.QuitVal
        #print "Evaluating:%s"%color
        #raw_input()
        
        val=0
        totPieces=0
        for x in self.symbols:
            totPieces+=self.PieceNum[color][x]+self.PieceNum[opp][x]
            val+=(self.PieceNum[color][x]-self.PieceNum[opp][x])*self.Weight[x]
            score+=(self.PieceNum[color][x]-self.PieceNum[opp][x])*self.Score[x]
        if totPieces==2:
            print self.PieceNum[color]
            print self.PieceNum[opp]
            raw_input("Stalemate \nPress a key")
            global check_mate
            check_mate=1
        if self.check_state!=''  or val<-900 or self.PieceNum[color]["Ki"]==0:
            #print "Kings:%d state:%s val:"%(self.PieceNum[color]["Ki"],self.check_state,val)
            #raw_input()
            return self.QuitVal
        
    
        val+= self.board_control(lev,color)*(2)
        #global alpha;
        #self.Weight[self.LastMoved]+=alpha*(val-score)
        
        return val
        #return QuC*9+KnC*4+RoC*5+BiC*3+PnC+KiC*999
        
        #return self.board_control()
    def display_board(self):
        for i in range(8):
            print ' '.join('--- ' for j in range(8))
            print ''.join(self.Set[8*i+j].Piece.show_piece()  for j in range(8))
        #if self.check_state!='':
        #print "CHECK!! for %s"%self.check_state
        #raw_input()
            
    def display_blank_board(self):
        for i in range(8):
            print ' '.join('--- ' for j in range(8))
            print ''.join(self.Set[8*i+j].show_color()  for j in range(8))
        
        
    def bishop_move(self,color='B',move=1,level=0):
        bishop_count=0
        bishops=[]
        
        if color=='B':
            
            for x in self.Black:
                if x.Type=='Bi':
                    bishop_count+=1
                    bishops.append(x)
        else:
            for x in self.White:
                if x.Type=='Bi':
                    bishop_count+=1
                    
                    bishops.append(x)
        if bishop_count==0:
            return 0
        resume=self.bishoplegal(bishops,move,level)
        return resume
    def bishoplegal(self,bishops,move,level,pos_in=-1,player='C'):
        
        leg_pos=[]
        for bis in bishops:
            cont=1
            start_row=bis.Row;start_col=bis.Col
            row=start_row;col=start_col
            pos=row*8+col
            while cont==1 and row<7 and col<7:
                row+=1;col+=1
                pos2=row*8+col
                
                cont=self.move_piece(pos,pos2,bis,move,level)
                if cont>0:
                    leg_pos.append(pos2)
                    self.univ_leg.update({pos2})
                    
            cont=1
            row=start_row;col=start_col;
            while cont==1 and row<7 and col>0:
                row+=1;col-=1
                pos2=row*8+col
                #leg_pos.append(pos2)
                cont=self.move_piece(pos,pos2,bis,move,level)
                if cont>0:
                    leg_pos.append(pos2)
                    self.univ_leg.update({pos2})
            cont=1
            row=start_row;col=start_col;
            
            while cont==1 and row>0 and col>0:
                row-=1;col-=1
                pos2=row*8+col
                cont=self.move_piece(pos,pos2,bis,move,level)
                if cont>0 :
                    self.univ_leg.update({pos2})
                    leg_pos.append(pos2)
            cont=1
            row=start_row;col=start_col;
            while cont==1 and row>0 and col<7:
                row-=1;col+=1
                pos2=row*8+col
                #leg_pos.append(pos2)
                cont=self.move_piece(pos,pos2,bis,move,)
                if cont>0:
                    self.univ_leg.update({pos2})
                    leg_pos.append(pos2)
            
        if player!='C':
            print "legal moves for paw at col"
            print leg_pos
                        
            for check in leg_pos:
                self.univ_leg.update({check})
                if pos_in==check:
                    return 1
            print "illegal in ro at pos_in=%d"%pos_in    
            return -1
        else :
             for check in leg_pos:
                self.univ_leg.update({check})
                                   
        return 1
     #('W',2,level)           
    def knight_move(self,color='B',move=1,level=0):
        knight_count=0
        knights=[]
        if color=='B':
        
            for x in self.Black:
                if x.Type=='Kn':
                    knight_count+=1
                    knights.append(x)
        else:
            for x in self.White:
                if x.Type=='Kn':
                    knight_count+=1
                    knights.append(x)
        if knight_count==0:
            return 0
        resume=self.knightlegal(knights,move,level)
        return resume
    def knightlegal(self,knights,move,level,pos_in=-1,player='C'):
        leg_pos=[]
        for kn in knights:
            cont=1
            start_row=kn.Row;start_col=kn.Col
            row=start_row;col=start_col
            pos=row*8+col
            if row>0:
                
                if col>1:
                    pos2=(row-1)*8+col-2
                    
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0  :
                        self.univ_leg.update({pos2})
                        leg_pos.append(pos2)
                        
                if col<6:
                    pos2=(row-1)*8+col+2
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0  :
                        self.univ_leg.update({pos2})
                        leg_pos.append(pos2)
                        
            if row>1:
                
                if col>0:
                    pos2=(row-2)*8+col-1
                    
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0  :
                        self.univ_leg.update({pos2})
                        leg_pos.append(pos2)
                if col<7:
                    pos2=(row-2)*8+col+1
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0  :
                        self.univ_leg.update({pos2})
                        leg_pos.append(pos2)
                        
                    
                    
            if row<6:
               
                if col>0:
                    pos2=(row+2)*8+col-1
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0:
                        self.univ_leg.update({pos2})
                        leg_pos.append(pos2)
                        
                    
                if col<7:
                    pos2=(row+2)*8+col+1
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0  :
                        self.univ_leg.update({pos2})
                        leg_pos.append(pos2)
                        
                    
                    
            if row<7:
                
                if col>1:
                    pos2=(row+1)*8+col-2
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0:
                        self.univ_leg.update({pos2})
                        leg_pos.append(pos2)
                        
                    
                    
                         
                if col<6:
                    pos2=(row+1)*8+col+2
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0:
                        self.univ_leg.update({pos2})
                        leg_pos.append(pos2)
                        
                    
            

        if player!='C':
            '''print "legal moves for paw at col:%d and row:%d" % (kn.Col,kn.Row)
            print leg_pos
            raw_input("enter a key")
            '''
            
            for check in leg_pos:
                self.univ_leg.update({check})
                if pos_in==check:
                    return 1
            print "illegal knight move to pos_in=%d"%pos_in
            raw_input()
            return -1
        else :
             for check in leg_pos:
                self.univ_leg.update({check})
        
        return 1
                    
                    
     #('W',2,level)       
    def rook_move(self,color='B',move=1,level=0):
        rook_count=0
        rooks=[]
        
        if color=='B':
            
            for x in self.Black:
                if x.Type=='Ro':
                    rook_count+=1
                    rooks.append(x)
        else:
            for x in self.White:
                if x.Type=='Ro':
                    rook_count+=1
                    rooks.append(x)
        if rook_count==0:
            return 0
        resume=self.rooklegal(rooks,move,level)
        return resume
    def rooklegal(self,rooks,move,level,pos_in=-1,player='C'):
        leg_pos=[]
        for ro in rooks:
            cont=1
            start_row=ro.Row;start_col=ro.Col
            row=start_row;col=start_col
            pos=row*8+col
            
            while row>0 and cont==1:
                row-=1
                pos2=(row)*8+col
                cont=self.move_piece(pos,pos2,ro,move,level)
                
                if cont>0:
                    self.univ_leg.update({pos2})
                    leg_pos.append(pos2)
            cont=1    
            row=start_row;col=start_col;
            while row<7 and cont==1:
                row+=1
                pos2=(row)*8+col
                cont=self.move_piece(pos,pos2,ro,move,level)
                if cont>0:
                    self.univ_leg.update({pos2})
                    leg_pos.append(pos2)
                
            row=start_row;col=start_col;
            cont=1
            while col<7 and cont==1:
                col+=1
                pos2=(row)*8+col
                cont=self.move_piece(pos,pos2,ro,move,level)
                if cont>0:
                    self.univ_leg.update({pos2})
                    leg_pos.append(pos2)
                
            row=start_row;col=start_col;
            cont=1
            while col>0 and cont==1:
                col-=1
                pos2=(row)*8+col
                cont=self.move_piece(pos,pos2,ro,move,level)
                if cont>0:
                    self.univ_leg.update({pos2})
                    leg_pos.append(pos2)
                
            row=start_row;col=start_col;
        if player!='C':
            
            for check in leg_pos:
                self.univ_leg.update({check})
                if pos_in==check:
                    return 1
            print "illegal rook move to pos_in=%d"%pos_in
            raw_input("Press a key");
            return -1
        else :
             for check in leg_pos:
                self.univ_leg.update({check})
        
        return 1
    def queen_move(self,color='B',move=1,level=0):
        queen_count=0
        queens=[]
        
        if color=='B':
            
            for x in self.Black:
                if x.Type=='Qu':
                    queen_count+=1
                    queens.append(x)
        else:
            for x in self.White:
                if x.Type=='Qu':
                    queen_count+=1
                    queens.append(x)
        
        if queen_count==0:
            return 0
        
        resume=self.queenlegal(queens,move,level)
        return resume
    def queenlegal(self,queens,move=1,level=0,pos_in=-1,player='C'):
        for qn in queens:
            lis=[qn]
            check1=self.bishoplegal(lis,move,level,pos_in,player)
            check2=self.rooklegal(lis,move,level,pos_in,player)
            if check1>0 or check2>0:
                return 1
            else:
                print "illegal Queen move to pos_in=%d"%pos_in
                raw_input()
                return -1
    def king_move(self,color='B',move=1,level=0):
        king_count=0
        kings=[]
        if color=='B':
            
            for x in self.Black:
                if x.Type=='Ki':
                    king_count+=1
                    kings.append(x)
        else:
            for x in self.White:
                if x.Type=='Ki':
                    king_count+=1
                    kings.append(x)
        if king_count==0:
            return 0
        resume=self.kinglegal(kings,move,level)
        return resume
    def kinglegal(self,king,move=1,level=0,pos_in=-1,player='C'):
        add=[1,-1,8,-8,-7,7,-9,9]
        ret=-1
        #color=king.Color
        start_row=king[0].Row;start_col=king[0].Col
        row=start_row;col=start_col
        pos=row*8+col
        for a in add:
            pos2=pos+a
            if pos2==pos_in:
                ret=1
            if pos2>=0 and pos2<64 :
                #self.univ_leg.update({pos2})
                cont=self.move_piece(pos,pos2,king[0],move,level,pos_in)
                if cont>0:
                    self.univ_leg.update({pos2})
                    self.univ_leg.update({pos2})
                
        return ret
            
    def pawn_move(self,color='B',move=1,level=0):
        pawn_count=0
        pawns=[]
        if color=='B':
            
            for x in self.Black:
                if x.Type=='Pn':
                    pawn_count+=1
                    pawns.append(x)
        else:
            for x in self.White:
                if x.Type=='Pn':
                    pawn_count+=1
                    pawns.append(x)
        if pawn_count==0:
            return 0
        resume=self.pawnlegal(pawns,move,level)
        return resume
    def pawnlegal(self,pawns,move=1,level=0,pos_in=-1,player='C'):
        leg_pos=[]
        att_pos=[]
        opp=' '
                    
        for paw in pawns:
            start_row=paw.Row;start_col=paw.Col
            row=start_row;col=start_col
            pos=row*8+col
            color=paw.Color
            if color=='B':
                mulp=1
                opp='W'
            else :
                mulp=-1
                opp='B'
            
            
            if row==6 and color=='W':
                pos2=pos+mulp*16
                if pos2>=0 and pos2<64 and((self.Set[pos2].Piece.Type=='**' or self.Set[pos2].Piece.Type=='  ') and (self.Set[pos2-mulp*8].Piece.Type=='**' or self.Set[pos2-mulp*8].Piece.Type=='  ')):
                    cont=self.move_piece(pos,pos2,paw,move,level)
                    if cont>0:
                        self.univ_leg.update({pos2})
                        leg_pos.append(pos2)
                        
                        
            if row==1 and color=='B':
               
                pos2=pos+mulp*16
                
                if (pos2>0 and pos2<64 )and ((self.Set[pos2].Piece.Type=='**' or self.Set[pos2].Piece.Type=='  ') )and ((self.Set[pos2-mulp*8].Piece.Type=='**' or self.Set[pos2-mulp*8].Piece.Type=='  ')):
                    cont=self.move_piece(pos,pos2,paw,move,level)
                    
                    if cont>0:
                        
                        self.univ_leg.update({pos2})
                        leg_pos.append(pos2)
                        
            pos2=pos+mulp*8
            if pos2>=0 and pos2<63 and ((self.Set[pos2].Piece.Type=='**' or self.Set[pos2].Piece.Type=='  ' )):
                cont=self.move_piece(pos,pos2,paw,move,level)
                if cont>0:
                    self.univ_leg.update({pos2})
                    leg_pos.append(pos2)
                    
                    
            pos2=pos+mulp*7
            if pos2>=0 and pos2 <64 and self.Set[pos2].Piece.Color == opp:
                cont=self.move_piece(pos,pos2,paw,move,level)
                if self.Set[pos].Piece.Col==0 and color=='B':
                    cont=-1
                if self.Set[pos].Piece.Col==7 and color=='W':
                    cont=-1
                if cont>0:
                    self.univ_leg.update({pos2})
                    leg_pos.append(pos2)
                    att_pos.append(pos2)
                    

                    
            pos2=pos+mulp*9
            if pos2>=0 and pos2 <64 and self.Set[pos2].Piece.Color == opp:
                cont=self.move_piece(pos,pos2,paw,move,level)
                
                if self.Set[pos].Piece.Col==0 and color=='W':
                    cont=-1
                if self.Set[pos].Piece.Col==7 and color=='B':
                    cont=-1
                if cont>0:
                    self.univ_leg.update({pos2})
                    leg_pos.append(pos2)
                    att_pos.append(pos2)
                    

                    
        if player!='C':
            for check in leg_pos:
                if check in att_pos:
                    self.univ_leg.update({check})
                if pos_in==check:
                    Board_show=copy.deepcopy(self)
                    os.system('cls')
                    os.system('cls')
                    global move1
                    Board_show.LastMoved='Pn'
                    move1.append(Board_show)
                    return 1
            print "illegal Pawn move at pos_in=%d"%pos_in
            raw_input()
            return -1
        else :
             for check in leg_pos:
                self.univ_leg.update({check})
        
        return 1
    
    def Black_details(self):
        print "BD"
        for x in self.Black:
            print x.show_det()
        raw_input("enter a key")
    def White_details(self):
        print "WD"
        for x in self.White:
            print x.show_det()
        raw_input("enter a key")
        
    def move_piece(self,pos,pos2,piece,move=1,level=0,pos_in=-1):
        if pos2<0 or pos2>63:
            
            return -1
        kill=0
        sam=0
        color=piece.Color
        opp=''
        if color=='B':
            opp='W'
        else :
            if color=='W':
                opp='B'
            else :
                self.reset_square_cols()
                print "Empty Square"
                raw_input()
                return -1
        Board1=copy.deepcopy(self)
        if move==1:
            Board1.LastMoved=piece.Type
            Board1.LastPos=pos
            Board1.NextPos=pos2
        if Board1.Set[pos2].Piece.Color==color:
            sam=1
        if Board1.Set[pos2].Piece.Color==opp:
                found=0
                kill=1
                Board1.PieceNum[opp][Board1.Set[pos2].Piece.Type]-=1
            #if Board1.Set[pos2].Piece.Type!='  ':#k=ki
                if Board1.Set[pos2].Piece.Type=='Ki' :#and move==2:
                    Board1.check_state=opp
                    global dead;
                    dead+=1
                    print "DEAD %d for %s now"%(dead,opp);
                    Board1.PieceNum[opp]["Ki"]=0
                    print "DEAD %d for %s now check:%s kings:%s"%(dead,opp,Board1.check_state,Board1.PieceNum[opp]["Ki"]);
                    
                    
                    
                
                if opp=='B':
                    i=0
                    for p in Board1.Black:
                        
                        if p.ret_pos()==pos2:                          
                            Board1.Black.remove(p)
                            found=1
                        i+=1
                    if found==0:
                        print "not found"
                    
                if opp =='W':
                    for p in Board1.White:
                        rem=Piece_def()
                        
                        if p.ret_pos()==pos2:
                            
                            Board1.White.remove(p)

        if Board1.Set[pos2].Piece.Color ==color:
            
            return -1
        
        
        Board1.Set[pos2].Piece=copy.deepcopy(Board1.Set[pos].Piece)
        
        Board1.Set[pos].Piece.Color='G'
        Board1.Set[pos].Piece.Type='**'
        piece_type=piece.Type
        col=piece.Col
        row =piece.Row
        row1=pos2/8;col1=pos2%8
        Board1.Set[pos2].Piece.Row=row1;
        Board1.Set[pos2].Piece.Col=col1
        
        found=0
        if color=='B':
            for i in range(len(Board1.Black)):
                if Board1.Black[i].ret_pos()==pos:
                    
                    Board1.Black.remove(Board1.Black[i])
                    add=Piece_def(pos2/8,pos2%8,color,piece_type)
                    
                    Board1.Black.append(add)
                    Board1.reset_square_cols()
                    found=1
                    
        if color=='W':
            
            for i in range(len(Board1.White)):
                
                if Board1.White[i].ret_pos()==pos:
                    
                    Board1.White.remove(Board1.White[i])
                    add=Piece_def(pos2/8,pos2%8,color,piece_type)
                    Board1.White.append(add)
                    Board1.reset_square_cols()
                    found=1
         
        if pos_in==pos2 :
            global move1
            
            move1=move1[0:0]
            Board1.reset_square_cols()
            if move==1:
                Board1.LastMoved=piece.Type
            
            print "moved:%s from %d to %d"%(Board1.LastMoved,Board1.LastPos,Board1.NextPos)
            
            move1.append(Board1)
        else :
            if move==2 :
                if Board1.PieceNum['B']["Ki"]<1:
                    print "WRITING DEAD with val:%d"%Board1.evaln(0,opp);
                best_pos=[27,28,35,36]              
                if pos in best_pos:
                    Board1.control[piece.Color]-=1
                if pos2 in best_pos:
                    Board1.control[piece.Color]+=1
                    
                move2.append([level,Board1])
                
                
            else:
                if move==1:
                    best_pos=[27,28,35,36]
                    if pos2 in best_pos:
                        Board1.control[piece.Color]+=1
                    if pos in best_pos:
                        Board1.control[piece.Color]-=1
                    Board1.LastMove=piece.Type
                    move1.append(Board1)
                    
                    
                Board1.reset_square_cols()
        if sam==0 and kill==0:
            return 1
        else :
            if kill!=0:
                return 0.5
            else:
                return -1
      

    
def find_legal_u(pos,pos2,piece,board):
    typ=piece.Type
    piece.Row=pos/8
    piece.Col=pos%8
    move=1
    level=0
    if typ=='Pn':
        lis=[piece]
        return board.pawnlegal(lis,move,level,pos2,'U')
        
    if typ=='Kn':
        lis=[piece]
        return board.knightlegal(lis,move,level,pos2,'U')
    if typ=='Bi':
        lis=[piece]
        return board.bishoplegal(lis,move,level,pos2,'U')
    if typ=='Qu':
        lis=[piece]
        return board.queenlegal(lis,move,level,pos2,'U')
    if typ=='Ro':
        lis=[piece]
        return board.rooklegal(lis,move,level,pos2,'U')
    if typ=='Ki':
        lis=[piece]
        return board.kinglegal(lis,move,level,pos2,'U')
def make_move1(board,color):
    print
    global move1
    move1=move1[0:0]
    move=1
    level=0
    t1=time.clock()
    board.univ_leg=set()
    board.bishop_move(color)
    board.queen_move(color)
    board.rook_move(color)
    board.knight_move(color)
    board.pawn_move(color)
    board.king_move(color)
    board.NoMoves=len(board.univ_leg)
    i=0
    t1=time.clock()
    cn=0
    
    if color=='W':
        color='B'
    else:
        color='W'
    
    for x in move1:
        
        make_move2(x,i,color,board.NoMoves)
        i+=1
          
def make_move2(board,level,color,NoMoves):
    board.NoMoves=NoMoves
    board.bishop_move(color,2,level)
    board.queen_move(color,2,level)
    board.rook_move(color,2,level)
    board.knight_move(color,2,level)
    board.pawn_move(color,2,level)
    board.king_move(color,2,level)
    
def Play_CPU(board,color):
    t1=time.clock()
    print "CPU Thinking...."
    make_move1(board,color)
    minimaxVal,score,pos=minimax(move2,color)
    #print "Minimax val was;%d"%minimaxVal
    #raw_input()
    if pos ==-1:
        print "check mate as pos=%d"%pos
        raw_input()
        global check_mate
        check_mate=1
        pos=0
    move1[pos].ExpVal=minimaxVal
    move1[pos].score=score
    move1[pos].val=minimaxVal
    board=copy.deepcopy(move1[pos])
    board.Weight[board.LastMoved]+=board.alpha*(board.getScore(color)-board.val)
    #print "BC:%d"%board.bcWeight
    board.bcWeight+=board.alpha*(board.getScore(color)-board.val)*board.control[color]
    return move1[pos]
    
def check_move1(board,color):
    lis=[]
    lis.append(board.bishop_move(color))  
    lis.append(board.queen_move(color))
    lis.append(board.rook_move(color))
    lis.append(board.knight_move(color))
    lis.append(board.king_move(color))
    lis.append(board.pawn_move(color))
    return min(lis)
    
def Play_user(board,color):
    os.system('cls')
    board.display_board()
    pos=int(raw_input("Enter Start position"))
    level=0
    pos2=int(raw_input("Enter Final position"))
    if pos not in range(0,64) or pos2 not in range(0,64):
        raw_input("Out of range Position!\n Press any key to continue")
        return board,-1
    pie=copy.deepcopy(board.Set[pos].Piece)
    board1=copy.deepcopy(board)
    lis_res=find_legal_u(pos,pos2,pie,board)
    if lis_res==1:
        print"yo"
        global move1
        board.move_piece(pos,pos2,pie,1,level,pos2)
        board1=copy.deepcopy(move1[len(move1)-1])
        os.system('cls')
        cont=1
        board1.display_board()
        print "cont=%d"%cont
        if cont==-2:
            print "Illegal Move"
            raw_input("enter a key")
            os.system('cls')
            return board1,-1
    else :
        print "Invalid Move"
        raw_input("enter a key")
        os.system('cls')
        return board1,-1
    return board1,1
def Play(player,board):
    if player=='U':
        Play_user(board)
        print "After play \n"
        os.system('cls')
        global move1
        Play('C',move1[0])
    if player=='C':
        global move2
        board=copy.deepcopy(Play_CPU(board))
        if check_mate==0:
            print "After CPU play \n"
            os.system('cls')
            print
        
            move1=move1[0:0]
            move2=move2[0:0]
        #raw_input("enter a key")
            Play('U',board)
        else :
            print "Check Mate for CPU"        
        
def Play1(player,board,color) :
    if player=='C':
        board=copy.deepcopy(Play_CPU(board,color))
    else:
        board,rep=Play_user(board,color)
        while rep==-1:
            board,rep=Play_user(board,color)
    #print board.NoMoves
    return board  
        
def game():
    os.system("cls")
    Chess=Board_State('board.txt')
    '''print "Choose Your color(W/B): "
    playerColor=raw_input()
    if playerColor=='W' or playerColor=='w':
        WhitePlayer='U'
        BlackPlayer='C'
    else:
        if playerColor=='B' or playerColor== 'b':
            WhitePlayer='C'
            BlackPlayer='U'
        else:
            game()
    '''
    board=copy.deepcopy(Chess)    
    i=0
    WhitePlayer='C'
    BlackPlayer='C'
    #print "USER is %s"%playerColor
    while check_mate==0 and i<500:
        os.system("cls")
        print "moves:%d"%i
        color='W'
        board=copy.deepcopy(Play1(WhitePlayer,board,'W'))
        #print "%sMoved %s from %d to %d val is %d difference is:%d"%(color,board.LastMoved,board.LastPos,board.NextPos,board.evaln(0,color),(board.ExpVal-board.evaln(0,color)))
        if board.PieceNum[color]['Ki']==0:
            print "OVER LOSER %s"%color
            raw_input()
        color='B'
        board=copy.deepcopy(Play1(BlackPlayer,board,'B'))
        #print "%sMoved %s from %d to %d val is %d difference is:%d"%(color,board.LastMoved,board.LastPos,board.NextPos,board.evaln(0,color),(board.ExpVal-board.evaln(0,color)))
        global move1
        global move2
        move1=move1[0:0]
        move2=move2[0:0]
        i+=1
        if i%2==0:
            print board.Weight
            raw_input()
        board.check_state==''
    if check_mate!=0:
        print "Check Mate"
        raw_input()    
    print "done with %d moves"%i
    raw_input()  
game()            
                
                
                    
                
        

            
                
        
