import copy
import time
import random
def movejump(move2):
    movejump=[]
    lev=0
    for i in range(len(move2)):
        if lev<move2[i][0]:
            lev+=1
            movejump.append(i)
    print movejump
    #raw_input()
    return movejump
        
def minimax(lis,color):
    #print "Minimax"
    t1=time.clock()
    #print "size=%d"%len(lis)
    levs=max(a[0] for a in lis)
    #print "leveles=%d"%levs
    global_min=10**5
    check_level=1
    min_ind=0
    minm=-1*global_min
    local_min=global_min
    min_lis=[]
    mover=-1
    j=0
    move_jump=[]
    move_jump=copy.deepcopy(movejump(lis))
    #print "jumps"
    #print move_jump
    while j < (len(lis)) and check_level<=levs:
        mover+=1
        
        if lis[j][0]>check_level:
            check_level=lis[j][0]
            min_lis.append((local_min,check_level-1))
            minm=-1*global_min
            for i in range(len(min_lis)):
                    if min_lis[i]>minm:
                            min_ind=i
                            minm=min_lis[i]
                            
            local_min=global_min
        if lis[j][0]==check_level:
            if lis[j][1].evaln(check_level,color)<minm:
                    #print "jump"
                    local_min=lis[j][1].evaln(check_level,color)
                    if j< move_jump[check_level-1]:
                        #print "j was %d"%j 
                        j=move_jump[check_level-1]-1
                        #print "upgrade j=%d"%j
                        #raw_input()
                    check_level+=1
                    min_lis.append((lis[j][1].evaln(check_level,color),check_level-1))
                    #local_min=global_min
            else:
                
                #print "check"
                if lis[j][1].evaln(check_level,color)<local_min:
                    local_min=lis[j][1].evaln(check_level,color)
                
        j+=1
                
    '''#if(local_min<global_min):
    print "check=%d"%check_level  
    min_lis.append((local_min,check_level))
    minm=-1*global_min
    '''
    #global move1
    #print "len m1=%d len min=%d mover=%d"%(len(move1),len(min_lis),mover)
    minim_lis=[]
    #print "min_lis:"
    #print min_lis
    minim=-999999999
    for x in min_lis:
        if x[0]>minim:
            minim=x[0]
    #raw_input("enter a key")
    for i in range(len(min_lis)):
        if min_lis[i][0]==minim and i<=check_level:
            #minim_lis=minim_lis[0:0]
            minim_lis.append(i)
            #minm=min_lis[i]
    #print min_lis
    print "min lis has%d minim=%d"%(len(min_lis),minim)
    if len(minim_lis)==0:
        print "hopeless"
        return 0,-1
    if len(minim_lis)>=1:
        print "luck"
        min_ind=minim_lis[random.randint(0,len(minim_lis)-1)]
    else:
        print "solo"
        min_ind=minim_lis[0]
        #print min_lis
   # print "color tested was:%s"%color
    #raw_input()
    if minim<-900:
        print "minim too low"
        
        return 0,-1
    '''luck=random.randint(0,9)
    
    if luck==0:
        print "luck"
        #raw_input()
        if check_level>1:
            return minim,random.randint(0,check_level-1)
    '''
    return minim,min_ind        
