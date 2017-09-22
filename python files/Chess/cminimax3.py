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
    return movejump
        
def minimax(lis,color):
    #print "Minimax"
    t1=time.clock()
    #print "size=%d"%len(lis)
    levs=max(a[0] for a in lis)
    #print "leveles=%d"%levs
    global_min=10**5
    check_level=0
    min_ind=0
    minm=-1*global_min
    local_min=minm
    min_lis=[]
    mover=-1
    j=0
    min_poses=[]
    move_jump=[]
    move_jump=copy.deepcopy(movejump(lis))
    #print "jumps"
    #print move_jump
    addToMinPos=[]
        
    while j < (len(lis)) and check_level<=levs:
        mover+=1
        if lis[j][0]>check_level:
            check_level=lis[j][0]
            min_lis.append(local_min)
            min_poses.append(addToMinPos)
            #print "addingz:"
            #print addToMinPos
            #raw_input()
            
            minm=-1*global_min
            for i in range(len(min_lis)):
                    if min_lis[i]>minm:
                            min_ind=i
                            minm=min_lis[i]
                            
            local_min=global_min
            addToMinPos=addToMinPos[0:0]
        if lis[j][0]==check_level:
            if lis[j][1].evaln(check_level,color)<minm:
                    #print "jump"
                    local_min=lis[j][1].evaln(check_level,color)
                    if j< move_jump[check_level]:
                        #print "j was %d"%j 
                        j=move_jump[check_level]-1
                        #print "append j=%d"%j
                        
                    check_level+=1
                    min_lis.append(lis[j][1].evaln(check_level-1,color))
                    min_poses.append(addToMinPos)
                    #print "deleting as Local min was:%d but now is %d"%(local_min,lis[j][1].evaln(check_level,color))
                    #()
                    local_min=global_min
                    addToMinPos=addToMinPos[0:0]
                        
            else:
                
                #print "check"
                if lis[j][1].evaln(check_level,color)==local_min:
                    addToMinPos.append((check_level,j,lis[j][1].evaln(check_level,color),lis[j][1].tieBreaker()))
                    print "now we have:"
                    print addToMinPos
                    
                if lis[j][1].evaln(check_level,color)<local_min and local_min<global_min:
                    print "cl as lm=%d but new=%d"%(local_min,lis[j][1].evaln(check_level,color))
                    local_min=lis[j][1].evaln(check_level,color)
                    addToMinPos=addToMinPos[0:0]
                        
                    
                
        j+=1
                
    #if(local_min<global_min):
    '''min_lis.append(local_min)
    print "finally adding"
    print addToMinPos
    min_poses.append(addToMinPos)
    '''
    minm=-1*global_min
    #global move1
    #print "len m1=%d len min=%d mover=%d"%(len(move1),len(min_lis),mover)
    minim_lis=[]
    #print "min_lis:"
    #print min_lis
    minim=max(min_lis)
    ("enter a key")
    for i in range(len(min_lis)):
        if min_lis[i]==minim and i<=check_level:
            #minim_lis=minim_lis[0:0]
            minim_lis.append(i)
            #minm=min_lis[i]
    print min_lis
    print "min lis has%d minim=%d"%(len(min_lis),minim)
    if len(minim_lis)==0:
        return 0,-1
    if len(minim_lis)>=1:
        min_ind=minim_lis[random.randint(0,len(minim_lis)-1)]
    else:
        min_ind=minim_lis[0]
        print min_lis
   # print "color tested was:%s"%color
    ()
    if minim<-900:
        return 0,-1
    '''luck=random.randint(0,9)
    
    if luck==0:
        print "luck"
        ()
        if check_level>1:
            return minim,random.randint(0,check_level-1)
    '''
    return minim,get_index(min_poses,minim)
def get_index(min_poses,minim):
    #print "minim=%d and min_pos:"%minim
    for x in range(len(min_poses)-1):
        print min_poses[x][2]
        
    raw_input()
    pos=-1
    best_ind=-1
    best_lis=[]
    for addToMinPos in min_poses:
        best=0
        for indices in addToMinPos:
            if indices[2]==minim:
                print "found"
                val=indices[3]+indices[2]
                if val>best:
                    best=val
                    best_lis=best_lis[0:0]
                    #print "deleting"
                    best_lis.append(indices[0])
                else:
                    if val==best:
                        best_lis.append(indices[0])
    return best_lis[random.randint(0,len(best_lis)-1)]
                        
                    
            
            
            
        
