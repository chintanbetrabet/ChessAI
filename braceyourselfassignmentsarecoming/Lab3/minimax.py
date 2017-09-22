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
    return movejump
        
def minimax(lis):
    #print "Minimax"
    t1=time.clock()
    levs=max(a[0] for a in lis)
    global_min=10**5
    check_level=0
    min_ind=0
    minm=-1*global_min
    local_min=global_min
    min_lis=[]
    mover=-1
    j=0
    move_jump=[]
    move_jump=copy.deepcopy(movejump(lis))
    while j < (len(lis)) and check_level<levs:
        mover+=1
        
        if lis[j][0]>check_level:
            check_level=lis[j][0]
            min_lis.append(local_min)
            minm=-1*global_min
            for i in range(len(min_lis)):
                    if min_lis[i]>minm:
                            min_ind=i
                            minm=min_lis[i]
                            
            local_min=global_min
        if lis[j][0]==check_level:
            if lis[j][1].evaln()<minm:
                    local_min=lis[j][1].evaln()
                    check_level+=1
                    min_lis.append(lis[j][1].evaln())
                    local_min=global_min
            else:
                if lis[j][1].evaln()<local_min:
                    local_min=lis[j][1].evaln()
        j+=1
                
    if(local_min<global_min):
            min_lis.append(local_min)
    minm=-1*global_min
    minim_lis=[]
    minim=max(min_lis)
    for i in range(len(min_lis)):
        if min_lis[i]==minm and i<levs:
            #minim_lis=minim_lis[0:0]
            minim_lis.append(i)
            #minm=min_lis[i]
        else:
            if min_lis[i]==minim :
                 minim_lis.append(i)                
    min_ind=minim_lis[random.randint(0,len(minim_lis)-1)]
    print "time=%f"%(time.clock()-t1)
    return min_ind        
