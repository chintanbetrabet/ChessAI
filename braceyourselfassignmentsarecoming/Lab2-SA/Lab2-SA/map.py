#temperature is Anneal.temp
import os
import sys
import copy
import math
import random
cn=0
class Anneal:
    def __init__(self,name):
        fil=open(name,'r')
        self.Set=[]
        self.colors=[]
        self.color_num=0
        self.links=0
        self.temp=0
        x=fil.readline()
        
        self.color_num=int(x)
        for x in fil:
            part=x.split(':')
            #print part
            ind=int(part[0])
            div=part[1].split(',')
            las=div[len(div)-1]
            new_las=las[0:-1]
            #print "las=%ss"%new_las
            div[len(div)-1]=(new_las)
            #print div
            #raw_input()
            self.Set.append([])
            for add in div:
                if add.isdigit() and int(add)!=part[0]:
                    self.Set[ind-1].append(int(add))
                    self.links+=1
            #self.Set.insert(ind,x[2:int(len(x))-1])
            #print self.Set
        self.init_color()
    def init_color(self):
        for x in self.Set:
            self.colors.append(0)
        self.temp=self.links
    def disp(self):
        for x in self.Set:
            print ','.join(str(y) for y in x)
    def get_temp(self):
        prev=-1
        self.temp=0
        good=0
        for i in range(len(self.colors)):
            for x in self.Set[i]:
                if self.colors[i]==self.colors[x-1]:
                    self.temp+=1
                else:
                    good+=1
        return good
    def win_display(self):
        i=1
        for x in self.colors:
            print "%d:%d"%(i,x)
            i+=1
                
def Local_Move(state):
    global cn
    #print state.colors
    begin=state.get_temp()
    if cn%50==0:
        print "begin:%d cn=%d"%(state.get_temp(),cn)
    
        #raw_input()
    if state.temp==0 or cn>950:
        print "OVER at%d in cn=%d"%(state.temp,cn)
        state.win_display()
        return state
    moves=[]
    for i in range(1,len(state.colors)):
        for col in range(1,state.color_num):
            state1=copy.deepcopy(state)
            state1.colors[i]=col
            moves.append(state1)
    '''
       for x in moves:
       print x.colors
       raw_input()
    '''
    cn+=1
    #print "temp=%d"%state.get_temp()
    ind=random.randint(0,len(moves)-1)
    test=moves[ind]
    if test.get_temp()>state.get_temp():
        #print " cool:%d"%(test.get_temp())
        Local_Move(test)
    else:
        #print "temp activated at %d"%(test.get_temp())
        #raw_input()
        ran=random.randint(0,test.get_temp()**2)
        if ran<test.get_temp():
            #print "ran=%d chance was:%lf"%(ran,float(test.get_temp())/(test.get_temp()**2))
            #raw_input()
            Local_Move(test)
        else:
            Local_Move(state)
'''s=" qwtertyutiop\nf"
print s
x=s.split('\n')
print x
    
'''
a=Anneal('map.txt')
a.disp()
print "links=%d"%a.links


a=copy.deepcopy(Local_Move(a))
raw_input()
        
