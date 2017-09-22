#temperature is Anneal.temp
import os
import sys
import copy
import time
import random
global bias
global lm
global lim
global cn
cn=0
temp=1
max_val=0
lim=20000
lm=0
bias=2

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
    global temp
    #print state.colors
    begin=state.get_temp()
    #if cn%50==0:
        #print "begin:%d cn=%d"%(state.get_temp(),cn)
    
        #raw_input()
    if state.temp==0:
        print "OVER at%d in cn=%d"%(state.temp,cn)
        state.win_display()
        #raw_input()
        return state
    #moves=[]
    test=copy.deepcopy(state)
    
        #state1=copy.deepcopy(state)
    i=random.randint(0,len(state.colors)-1)
    colo=random.randint(0,state.color_num-1)
    while colo==test.colors[i]:
        colo=random.randint(0,state.color_num-1)        
    test.colors[i]=colo
        #moves.append(state1)
    '''
       for x in moves:
       print x.colors
       raw_input()
    '''
    cn+=1
    #print "temp=%d"%state.get_temp()
    #ind=random.randint(0,len(moves)-1)
    #test=moves[ind]
    if test.get_temp()>state.get_temp():
        global max_val
        global best
        if test.get_temp()>max_val:
            #print "found best"
            #raw_input()
            max_val=test.get_temp()
            best=copy.deepcopy(test)
        #print " cool:%d"%(test.get_temp())
        temp+=1
        return test
    else:
        if state.get_temp()==max_val:
            #print "losing best"
            ran=random.randint(0,cn)
        else:
            ran=random.randint(0,cn/bias)
        
        if ran<100:
            #print "ran=%d chance was:%lf"%(ran,float(test.get_temp())/(test.get_temp()**2))
            #raw_input()
            return test
        else:
            return state
'''s=" qwtertyutiop\nf"
print s
x=s.split('\n')
print x
 '''   

lis=[]
for i in range(5):
    #global cn
    cn=0
    a=Anneal('map.txt')
    best=copy.deepcopy(a)
    #a.disp()
    #print "links=%d"%a.links
    #raw_input()
    t1=time.clock()
    while a.temp!=0 and cn<lim:
        a=copy.deepcopy(Local_Move(a))
        #Local_Move(a)
    #print "OVER at%d in cn=%d best was %d"%(a.temp,cn,max_val)
    #raw_input()
    #print "time=%f"%float(time.clock()-t1)
    #a.win_display()
    lis.append([(time.clock()-t1),cn])
print lis
raw_input() 

    
    
