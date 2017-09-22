'''
All good but computer is too defensive
check and check mate need working
PAwn kills even head on
need better heuristic/evaluation function
'''
move_jump=[]
move1=[]
move2=[]
move=1
index=0
level=0
univ_leg=[]
board_control=0
rein_leg_pos=1
cop='Y'
import copy
import os
import time
class Piece_def():
    def __init__(self,row=0,col=0,color='G',piece_type="**"):
        self.Color=color
        self.Type=piece_type
        self.Row=row
        self.Col=col
        #self.Protected=[]
    def show_piece(self):
        #print self.Pos
        if self.Color!='G':
            return "%s%c |"%(self.Type,self.Color)
        else:
            if (self.Row+self.Col)%2!=0:
                return "*** |"
            else :
                return "   |"
    def show_det(self):
        #self.Pos=self.Row*8+self.Col
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
        self.Set=[]
        self.White=[]
        self.Black=[]
        pos=0
        self.control=0
        f=open(fil,'r')
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
        '''print "Black:"
        for pie in self.White:
            print pie.show_piece()
            raw_input("enter a key")
        '''
        '''for x in self.White:
            print "%s,%d,%d,%d"%(x.show_piece(),x.Row,x.Col,x.Pos)
            raw_input("enter a key")
        '''
    def all_legal(self):
        univ_leg=[]
        cop='N'
        self.bishop_move()
        self.queen_move()
        self.rook_move()
        self.knight_move()
        self.pawn_move()
        self.king_move()
        cop='Y'
    def board_control(self):
        self.all_legal()
        best_pos=[27,28,35,36]
        control=0
        
        for c in best_pos:
            for b in univ_leg:
                if b==c:
                    control+=1
        #self.display_board()
        #print "control=%d"%control
        #raw_input("enter a key")

        return control
    def evaln(self):
        #print "evaluaing"
        #raw_input("enter a key")
        QuC=0;KnC=0;RoC=0;PnC=0;BiC=0;KiC=0;
        for x in self.Black:
            if x.Type=='Qu':
                QuC+=1
            if x.Type=='Bi':
                BiC+=1
            if x.Type=='Kn':
                KnC+=1
            if x.Type=='Pn':
                PnC+=1
            if x.Type=='Ro':
                RoC+=1
            if x.Type=='Ki':
                KiC+=1
        for x in self.White:
            if x.Type=='Qu':
                QuC-=1
            if x.Type=='Bi':
                BiC-=1
            if x.Type=='Kn':
                KnC-=1
            if x.Type=='Pn':
                PnC-=1
            if x.Type=='Ro':
                RoC-=1
            if x.Type=='Ki':
                KiC-=1
            
        return self.board_control()*20+QuC*9+KnC*4+RoC*5+BiC*3+PnC+KiC*999
    def display_board(self):
        for i in range(8):
            print ' '.join('--- ' for j in range(8))
            print ''.join(self.Set[8*i+j].Piece.show_piece()  for j in range(8))
        
    def display_blank_board(self):
        for i in range(8):
            print ' '.join('--- ' for j in range(8))
            print ''.join(self.Set[8*i+j].show_color()  for j in range(8))
        
        
    def bishop_move(self,color='B',move=1,level=0):
        bishop_count=0
        bishops=[]
        #print "looking for color:%c"%color
        if color=='B':
            
            for x in self.Black:
                if x.Type=='Bi':
                    bishop_count+=1
                    bishops.append(x)
        else:
            for x in self.White:
                if x.Type=='Bi':
                    bishop_count+=1
                    #print "bis count=%d"%bishop_count
                    bishops.append(x)
        if bishop_count==0:
            return 0
        resume=self.bishoplegal(bishops,move,level)
        return resume
    def bishoplegal(self,bishops,move,level,pos_in=-1,player='C'):
        #print "BIS_leg"
        #raw_input("enter a key")
        leg_pos=[]
        for bis in bishops:
            cont=1
            start_row=bis.Row;start_col=bis.Col
            row=start_row;col=start_col
            pos=row*8+col
            while cont==1 and row<7 and col<7:
                row+=1;col+=1
                pos2=row*8+col
                #leg_pos.append(pos2)
                cont=self.move_piece(pos,pos2,bis,move,level)
                if cont>0:
                    leg_pos.append(pos2)
            cont=1
            row=start_row;col=start_col;
            while cont==1 and row<7 and col>0:
                row+=1;col-=1
                pos2=row*8+col
                #leg_pos.append(pos2)
                cont=self.move_piece(pos,pos2,bis,move,level)
                if cont>0:
                    leg_pos.append(pos2)
            cont=1
            row=start_row;col=start_col;
            
            while cont==1 and row>0 and col>0:
                row-=1;col-=1
                pos2=row*8+col
                cont=self.move_piece(pos,pos2,bis,move,level)
                if cont>0 :
                    
                    leg_pos.append(pos2)
            cont=1
            row=start_row;col=start_col;
            while cont==1 and row>0 and col<7:
                row-=1;col+=1
                pos2=row*8+col
                #leg_pos.append(pos2)
                cont=self.move_piece(pos,pos2,bis,move,)
                if cont>0:
                    leg_pos.append(pos2)
            
        if player!='C':
            print "legal moves for paw at col"
            print leg_pos
            raw_input("enter a key")
            
            for check in leg_pos:
                univ_leg.append(check)
                if pos_in==check:
                    return 1
            print "illegal in ro at pos_in=%d"%pos_in    
            return -1
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
                    #leg_pos.append(pos2)
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0  :
                        leg_pos.append(pos2)
                if col<6:
                    pos2=(row-1)*8+col+2
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0  :
                        leg_pos.append(pos2)
            if row>1:
                #print "tone"
                if col>0:
                    pos2=(row-2)*8+col-1
                    
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0  :
                        leg_pos.append(pos2)
                if col<7:
                    pos2=(row-2)*8+col+1
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0  :
                        leg_pos.append(pos2)
                    
                    
            if row<6:
                #print "othne"
                if col>0:
                    pos2=(row+2)*8+col-1
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0 :
                        leg_pos.append(pos2)
                    
                if col<7:
                    pos2=(row+2)*8+col+1
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0  :
                        leg_pos.append(pos2)
                    
                    
            if row<7:
                #print "fone"
                if col>1:
                    pos2=(row+1)*8+col-2
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0:
                        leg_pos.append(pos2)
                    
                    
                         
                if col<6:
                    pos2=(row+1)*8+col+2
                    cont=self.move_piece(pos,pos2,kn,move,level)
                    if cont>0:
                        leg_pos.append(pos2)
                    
            

        if player!='C':
            print "legal moves for paw at col:%d and row:%d" % (kn.Col,kn.Row)
            print leg_pos
            raw_input("enter a key")
            
            for check in leg_pos:
                univ_leg.append(check)
                if pos_in==check:
                    return 1
            print "illegal in kn at pos_in=%d"%pos_in
            return -1
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
            #print "pos=%d row=%d col=%d"%(pos,row,col)
            while row>0 and cont==1:
                row-=1
                pos2=(row)*8+col
                cont=self.move_piece(pos,pos2,ro,move,level)
                #print "cont=%d"%(cont)
                if cont>0:
                    leg_pos.append(pos2)
            cont=1    
            row=start_row;col=start_col;
            while row<7 and cont==1:
                row+=1
                pos2=(row)*8+col
                cont=self.move_piece(pos,pos2,ro,move,level)
                if cont>0:
                    leg_pos.append(pos2)
                
            row=start_row;col=start_col;
            cont=1
            while col<7 and cont==1:
                col+=1
                pos2=(row)*8+col
                cont=self.move_piece(pos,pos2,ro,move,level)
                if cont>0:
                    leg_pos.append(pos2)
                
            row=start_row;col=start_col;
            cont=1
            while col>0 and cont==1:
                col-=1
                pos2=(row)*8+col
                cont=self.move_piece(pos,pos2,ro,move,level)
                if cont>0:
                    leg_pos.append(pos2)
                
            row=start_row;col=start_col;
        if player!='C':
            '''print "legal moves for paw at col:" 
            print leg_pos
            #raw_input("enter a key")
            '''
            for check in leg_pos:
                univ_leg.append(check)
                if pos_in==check:
                    return 1
            print "illegal in ro at pos_in=%d"%pos_in
            return -1
        return 1
    def queen_move(self,color='B',move=1,level=0):
        queen_count=0
        queens=[]
        '''if move==2:
            print "in queens:"
            self.Black_details()
            self.White_details()
        '''
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
        '''if move==2:
            print "we have: %d queens"%queen_count
            raw_input("enter a key")
        '''
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
                print "illegal in qu at pos_in=%d"%pos_in
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
        
        start_row=king[0].Row;start_col=king[0].Col
        row=start_row;col=start_col
        pos=row*8+col
        for a in add:
            pos2=pos+a
            if pos2==pos_in:
                ret=1
            if pos2>=0 and pos2<64:
                univ_leg.append(pos2)
                cont=self.move_piece(pos,pos2,king[0],move,level,pos_in)
                
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
        #print "pc=%d"%pawn_count
        #raw_input("enter a key")
        resume=self.pawnlegal(pawns,move,level)
        return resume
    def pawnlegal(self,pawns,move=1,level=0,pos_in=-1,player='C'):
        leg_pos=[]
        opp=' '
        for paw in pawns:
            
            #print "pc=%d"%len(pawns)
            #raw_input("enter a key")
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
                leg_pos.append(pos2)
            if row==1 and color=='B':
                pos2=pos+mulp*16
                self.move_piece(pos,pos2,paw,move,level)
                leg_pos.append(pos2)
            
            pos2=pos+mulp*8
            self.move_piece(pos,pos2,paw,move,level)
            leg_pos.append(pos2)
            pos2=pos+mulp*7
            
            if pos2>=0 and pos <64 and self.Set[pos2].Piece.Color == opp:
                self.move_piece(pos,pos2,paw,move,level)
                leg_pos.append(pos2)
            pos2=pos+mulp*9
            if pos2>=0 and pos <64 and self.Set[pos2].Piece.Color == opp:
                self.move_piece(pos,pos2,paw,move,level)
                leg_pos.append(pos2)
        if player!='C':
            '''
            print "legal moves for paw at col:"  
            print leg_pos
            raw_input("enter a key")
            '''
            for check in leg_pos:
                univ_leg.append(check)
                if pos_in==check:
                    Board_show=copy.deepcopy(self)
                    os.system('cls')
                    #print "moved:"
                    #self.display_board()
                    os.system('cls')
                    #print "added:"
                    #Board_show.display_board()
                    global move1
                    move1.append(Board_show)
                    return 1
            print "illegal in pw at pos_in=%d"%pos_in
            return -1
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
            #print "range"
            return -1
        kill=0
        sam=0
        #print "move=%d"%move
        #print piece.show_piece()
        #print self.Set[pos].Piece.show_piece()
        #print self.Set[pos2].Piece.show_piece()
        #print "pos=%d pos2=%d pos_in=%d"%(pos,pos2,pos_in)
        
        color=piece.Color
        opp=''
        if color=='B':
            opp='W'
        else :
            if color=='W':
                opp='B'
            else :
                self.reset_square_cols()
                #self.display_blank_board()
                print "Empty Square"
                return -1
        Board1=copy.deepcopy(self)
        if Board1.Set[pos2].Piece.Color==color:
            sam=1
        if Board1.Set[pos2].Piece.Color==opp:
            
            found=0
            kill=1
            
            if Board1.Set[pos2].Piece.Type!='Ki':
                if opp=='B':
                    
                    #print Board1.Set[pos2].Piece.show_piece()
                    i=0
                    for p in Board1.Black:
                        #print p.show_piece()
                        #rem=Piece_def()
                        #print p.show_piece()
                        if p.ret_pos()==pos2:
                           
                            #print "found at i=%d "%i
                            #print p.show_piece() 
                            Board1.Black.remove(p)
                            found=1
                        i+=1
                    if found==0:
                        print "noooooooooo"
                    
                      
                    
                if opp =='W':
                    for p in Board1.White:
                        rem=Piece_def()
                        #print p.show_piece()
                        if p.ret_pos()==pos2:
                            
                            #print "eliminate one of:%d" %(len(Board1.White))
                            #print p.show_piece()
                            Board1.White.remove(p)
                            #raw_input("enter a key")
                    
                        
                        
                    #print "white is now"
                    #print ' '.join(Board1.White[i].show_piece() for i in range(len(Board1.White)))
                
                #Board1.display_board()
                    
                          
            else :
                Board1.reset_square_cols()
                #Board1.display_blank_board()
                print "CHECK"
                return -2
        if Board1.Set[pos2].Piece.Color ==color:
            #Board1.reset_square_cols()
            #Board1.display_blank_board()
            #print "Own piece Blocked at pos2=%d"%pos2
            return -1
        
        '''if pos_in!=-1:
            print "square color of destination is:%c"%Board1.Set[pos].Color
            raw_input("enter a key")
        '''
        Board1.Set[pos2].Piece=copy.deepcopy(Board1.Set[pos].Piece)
        
        Board1.Set[pos].Piece.Color='G'
        Board1.Set[pos].Piece.Type='**'
        piece_type=piece.Type
        col=piece.Col
        row =piece.Row
        row1=pos2/8;col1=pos2%8
        Board1.Set[pos2].Piece.Row=row1;
        Board1.Set[pos2].Piece.Col=col1
        '''if pos_in!=-1:
            print " now square color of destination is:%c"%Board1.Set[pos].Color
            raw_input("enter a key")
        '''
        found=0
        if color=='B':
            #Board1.Black_details()
            #print "pos=%d"%pos
            #raw_input("enter a key")
            for i in range(len(Board1.Black)):
                #if pos_in==-1:
                    #print "for :%s its pos=%d"%(Board1.Black[i].show_piece(),Board1.Black[i].ret_pos())
                if Board1.Black[i].ret_pos()==pos:
                    #print "removing:"
                    #print Board1.Black[i].show_piece()
                    
                    #print "after rem Black is now"
                    #print ' '.join(Board1.Black[i].show_det() for i in range(len(Board1.Black)))
                    #Board1.Black_details()
                    #raw_input("enter a key")
                    
                    #print "after add Black is now"
                    #print ' '.join(Board1.Black[i].show_det() for i in range(len(Board1.Black)))
                    #Board1.Black_details()
                    #raw_input("enter a key")
                    #print "removing:%s"%Board1.Black[i].show_det()
                    #print "adding:%s"%add.show_det()
                    
                    Board1.Black.remove(Board1.Black[i])
                    add=Piece_def(pos2/8,pos2%8,color,piece_type)
                    
                    Board1.Black.append(add)
                    Board1.reset_square_cols()
                    found=1
                    #Board1.Black_details()
                    #Board1.Black_details()
                    #raw_input("enter a key")
        if color=='W':
            #Board1.White_details()
            #print "pos=%d"%pos
            #raw_input("enter a key")
            #print "source=%d,%d"%(row,col)
            #raw_input("enter a key")
            for i in range(len(Board1.White)):
                #print Board1.White[i].Row
                #raw_input("enter a key")
                #if pos_in==-1:
                    #print "for :%s its pos=%d"%(Board1.White[i].show_piece(),Board1.White[i].ret_pos())
                    #raw_input("enter a key")
                if Board1.White[i].ret_pos()==pos:
                    '''print "removing:"
                    print Board1.White[i].show_piece()
                    print "after rem white is now"
                    #print ' '.join(Board1.White[i].show_piece() for i in range(len(Board1.White)))
                    Board1.White_details()
                    raw_input("enter a key")
                 
                    print "after add white is now"
                    Board1.White_details()
                    raw_input("enter a key")
                    '''
                    Board1.White.remove(Board1.White[i])
                    add=Piece_def(pos2/8,pos2%8,color,piece_type)
                    Board1.White.append(add)
                    Board1.reset_square_cols()
                    found=1
                    
        if found==0:
            print "noooooo you are at %d"%pos
            #Board1.White_details()
            for count in range(len(Board1.White)):
                
                print Board1.White[count].ret_pos()
                if Board1.White[count].ret_pos()==pos:
                    print "YAAAAAAAAAAAAAAY"
                    raw_input("enter a key")
            raw_input("enter a key")
        
        if pos_in==pos2 :
            global move1
            #print "level1"
            #raw_input("enter a key")
            for x in range(len(move1)):
                move1.pop()
            Board1.reset_square_cols()
            move1.append(Board1)
        else :
            if move==2 :
                #print piece.Type
                move2.append([level,Board1])
                
                
            else:
                if move==1:
                    #print "move=%d"%(len(move1))
                    move1.append(Board1)
                Board1.reset_square_cols()
        if sam==0 and kill==0:
            return 1
        else :
            if kill!=0:
                #print "kill at %d"%pos2
                return 0.5
            else:
                print "same "
                return -1
        #raw_input("enter a key")

    
def find_legal_u(pos,pos2,piece,board):
    typ=piece.Type
    #board.White_details()
    '''raw_input("enter a key")
    print "find legal user"
    print "%s%d"%(piece.show_piece(),piece.ret_pos())
    '''
    piece.Row=pos/8
    piece.Col=pos%8
    global move
    global level
    #print "FL"
    #board.Black_details()
    if typ=='Pn':
        lis=[piece]
        #self,pawns,move=1,level=0,pos_in=-1,player='C'
        
        return board.pawnlegal(lis,move,level,pos2,'U')
        #board.display_board()
        #print "i=%d"%i
        #raw_input("enter a key")
        #return i
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

    
    
def make_move1(board):
   
    print
    for x in range(len(move1)):
        move1.pop()
    move=1
    level=0
    
    board.bishop_move()
    board.queen_move()
    board.rook_move()
    board.knight_move()
    board.pawn_move()
    board.king_move()
    i=0  
    for x in move1:
        print i
        print x.display_board()
        
        #raw_input("enter a key")
        make_move2(x,i)
        move_jump.append(len(move2))
        i+=1
        
def make_move2(board,level):
    global univ_leg
    for x in univ_leg:
        univ_leg.pop()
    #univ_leg.trunc()
    #print "move2:"
    #board.display_board()
    #raw_input("enter a key")
    #board.Black_details()
    #board.White_details()    
    #print "bis"
    board.bishop_move('W',2,level)
    #print "qui"
    board.queen_move('W',2,level)
    #print "rook"
    board.rook_move('W',2,level)
    #print "knight"
    board.knight_move('W',2,level)
    #print "pawn"
    board.pawn_move('W',2,level)
    #print "majesty"
    board.king_move('W',2,level)
    
    
def Play_CPU(board):
    print "CPU Thinking...."
    make_move1(board)
    
    pos=minimax(move2)
    #print "RET POS+%d"%pos
    #hminiraw_input("enter a key")
    os.system('cls')
    return move1[pos]
def minimax(lis):
    #print "Minimax"
    t1=time.clock()
    print "size=%d"%len(move2)
    print "leveles=%d"%max(a[0] for a in move2)
    #raw_input("enter a key")
    #for x in lis:
        #x.display_board()
    #raw_input("enter a key")
    
    global_min=10**5
    check_level=0
    min_ind=0
    minm=-1*global_min
    local_min=global_min
    min_lis=[]
    mover=-1
    #print "i=%d"%mover
    j=0
    print "jumpers:"
    print move_jump
    raw_input()
    while j < (len(lis)):
        mover+=1
        print time.clock()-t1
        #print "mover=%d j=%d lev=%d"%(mover,j,check_level)
        if lis[j][0]>check_level:
            #print "next"
            #print "level=%d"%x[0]
            #x[1].display_board()
            #raw_input("enter a key")
            #os.system('cls')
            #print "has blacks:"
            #x[1].Black_details()
            #raw_input("enter a key")
            #lyfyyfyyffyfyfjffhhvhjhvjhvjvvvjvjjfjffhffhfjhjhjhjhfhfjjjhfjfjfjhfjjhjhhfj
            #x[1].display_board()
            #print "has evaln:%d"%(x[1].evaln())
            #raw_input("enter a key")
            check_level=lis[j][0]
            #print "at:%d"%x[0]
            min_lis.append(local_min)
            minm=-1*global_min
            #print "min:%d"%local_min
            for i in range(len(min_lis)):
                    if min_lis[i]>minm:
                            min_ind=i
                            minm=min_lis[i]
                            
            local_min=global_min
        if lis[j][0]==check_level:
            #print "level"
            #os.system('cls')
            #print "level=%d"%x[0]
            #x[1].display_board()
            #raw_input("enter a key")
            #print "has blacks:"
            #x[1].Black_details()
            #raw_input("enter a key")
            
            #print "has evaln:%d"%(x[1].evaln())
            #raw_input("enter a key")
            #print "scan:%d"%x[1].evaln().evaln()
            if lis[j][1].evaln()<minm:
                    #print "jump"
                    local_min=lis[j][1].evaln()
                    if j< move_jump[check_level]:
                        print "j was %d"%j 
                        j=move_jump[check_level]-1
                        print "upgrade j=%d"%j
                        raw_input()
                        check_level+=1
                    min_lis.append(lis[j][1].evaln())
                    local_min=global_min
            else:
                
                #print "check"
                if lis[j][1].evaln()<local_min:
                    local_min=lis[j][1].evaln()
                    
                '''if j==move_jump[check_level]-1:
                    #print "upgrade"
                    check_level+=1
                    min_lis.append(
                    #raw_input()
                '''
                
        j+=1
                
    if(local_min<global_min):
            min_lis.append(local_min)
    minm=-1*global_min
    global move1
    print "len m1=%d len min=%d mover=%d"%(len(move1),len(min_lis),mover)
    raw_input("enter a key")
    for i in range(len(min_lis)):
        if min_lis[i]>minm:
            min_ind=i
            minm=min_lis[i]
    #lis[min_ind][1].display_board()
    #raw_input("enter a key")
    print min_lis
    raw_input("enter a key")
    print "min_ind=%d time=%d"%(min_ind,time.clock()-t1)
    raw_input("enter a key")
    return min_ind        
def check_move1(board):
    lis=[]
    print "CM!:"
    lis.append(board.bishop_move())  
    lis.append(board.queen_move())
    lis.append(board.rook_move())
    lis.append(board.knight_move())
    lis.append(board.king_move())
    lis.append(board.pawn_move())
    return min(lis)
    
def Play_user(board):
    os.system('cls')
    #board.reset_square_cols()
    #board.Set_reset()
    #board.display_blank_board()
    #raw_input("enter a key")
    board.display_board()
    pos=int(raw_input("Enter Start position"))
    pie=copy.deepcopy(board.Set[pos].Piece)
    pos2=int(raw_input("Enter Final position"))
    #print "pos is =%d"%pos
    #board.White_details()
    raw_input("enter a key")
    lis_res=find_legal_u(pos,pos2,pie,board)
    if lis_res==1:
        print"yo"
        print "pos is =%d pos2=%d"%(pos,pos2)
        raw_input("enter a key")
        global move1
        board.move_piece(pos,pos2,pie,move,level,pos2)
        board1=copy.deepcopy(move1[len(move1)-1])
        os.system('cls')
        #move1[len(move1)-1].display_board()
        #raw_input("enter a key")
        cont=check_move1(board1)
        print "cont=%d"%cont
        if cont==-2:
            print "Illegal Move"
            raw_input("enter a key")
            os.system('cls')
            Play_user(board)
        
                
        
    else :
        print "Invalid Move"
        raw_input("enter a key")
        os.system('cls')
        Play_user(board)
def Play(player,board):
    if player=='U':
        Play_user(board)
    
        print "After play \n"
        os.system('cls')
        global move1
        Play('C',move1[0])
    if player=='C':
        
        board=copy.deepcopy(Play_CPU(board))
        print "After CPU play \n"
        os.system('cls')
        print
        #board.Black_details()
        
        #board.reset_square_cols()
        #board.Set_reset()
        #board.display_board()
        for x in range(len(move1)):
            move1.pop()
        for x in range(len(move2)):
            move2.pop()
        #raw_input("enter a key")
        Play('U',board)
        
        
    
        
Chess=Board_State('board.txt')
Play('U',Chess)

            
            
            
                
            
    

        
            
    
