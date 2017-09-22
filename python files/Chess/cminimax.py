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
    print "size=%d"%len(lis)
    levs=max(a[0] for a in lis)
    #print "leveles=%d"%levs
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
    #print "jumps"
    #print move_jump
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
                    #print "jump"
                    local_min=lis[j][1].evaln()
                    #if j< move_jump[check_level]:
                        #print "j was %d"%j 
                        #j=move_jump[check_level]-1
                        #print "upgrade j=%d"%j
                        #raw_input()
                    check_level+=1
                    min_lis.append(lis[j][1].evaln())
                    local_min=global_min
            else:
                
                #print "check"
                if lis[j][1].evaln()<local_min:
                    local_min=lis[j][1].evaln()
                
        j+=1
                
    if(local_min<global_min):
            min_lis.append(local_min)
    minm=-1*global_min
    #global move1
    #print "len m1=%d len min=%d mover=%d"%(len(move1),len(min_lis),mover)
    minim_lis=[]
    #print "min_lis:"
    #print min_lis
    minim=max(min_lis)
    #raw_input("enter a key")
    for i in range(len(min_lis)):
        if min_lis[i]==minm and i<levs:
            #minim_lis=minim_lis[0:0]
            minim_lis.append(i)
            #minm=min_lis[i]
        else:
            if min_lis[i]==minim :
                 minim_lis.append(i)                

    #lis[min_ind][1].display_board()
    #raw_input("enter a key")
    #print "minim_lis:"
    #print minim_lis
    #print "minimax=%d"%max(min_lis)
    #raw_input("enter a key")
    #print "min_ind=%d time=%d"%(min_ind,time.clock()-t1)
    #raw_input("enter a key")
    #print "original:"
    min_ind=minim_lis[random.randint(0,len(minim_lis)-1)]
    '''for i in range(len(min_lis)):
        if min_lis[i]==minim:
            min_ind=i
            break
    '''
    #move1[min_ind].display_board()
    #print "minimax done min_ind=%d"%min_ind
    print "time=%f minimax=%d"%(time.clock()-t1,minim)
    #raw_input()
    print min_lis
    if minim<-200:
        return -1
    return min_ind        
