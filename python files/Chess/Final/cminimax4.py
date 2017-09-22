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
    # restore this print movejump
    #raw_input()
    return movejump
        
def minimax(lis,color):
    t1=time.clock()
    levs=max(a[0] for a in lis)
               
    global_min=10**5
    check_level=0
    min_ind=0
    minm=-1*global_min
    local_min=global_min
    min_lis=[]
    addToMinPos=[]
    j=0
    move_jump=[]
    move_jump=copy.deepcopy(movejump(lis))
    min_poses=[]
    
    while j < (len(lis)) and check_level<=levs+1:

        if lis[j][1].evaln(check_level,color)==lis[j][1].QuitVal:
            min_lis.append((lis[j][1].QuitVal,check_level))
            #j=move_jump[check_level]-1
            addToMinPos=addToMinPos[0:0]
            addToMinPos.append((check_level,j,lis[j][1].evaln(check_level,color),lis[j][1].tieBreaker(color)))
            check_level+=1
            
        if lis[j][0]>check_level:
            check_level=lis[j][0]

            min_lis.append((local_min,check_level-1))
            if len(addToMinPos)>0:
                  #print addToMinPos
                  #raw_input()
                  min_poses.append(addToMinPos)
                  #print "del as jumped added:"
                  #print addToMinPos
                  #raw_input()
            minm=-1*global_min
            for i in range(len(min_lis)):
                    if min_lis[i][0]>minm:
                            min_ind=i
                            minm=min_lis[i][0]                           
            local_min=global_min            
            addToMinPos=addToMinPos[0:0]
        if lis[j][0]==check_level:
            if lis[j][1].evaln(check_level,color)<minm and lis[j][1].evaln(check_level,color)<lis[j][1].QuitVal:
                    print "JUMP"
                    raw_input()
                    addToMinPos=addToMinPos[0:0]
                    addToMinPos.append((check_level,j,lis[j][1].evaln(check_level,color),lis[j][1].tieBreaker(color)))
                    #print "del as over written localmin from %d to %d add::"%(local_min,lis[j][1].evaln(check_level,color))
                    #print addToMinPos
                    #raw_input()
                    if check_level==0:
                        minm=local_min
                    local_min=global_min
                    #j=move_jump[check_level]-1
                    check_level+=1
                    #jump=1
                    #print "NOW== l=%d minm=" %(check_level)
                    #print minm
                    #raw_input()
                    min_lis.append((lis[j][1].evaln(check_level,color),check_level-1))
                    if len(addToMinPos)>0:
                        #print addToMinPos
                        #raw_input()
                        min_poses.append(addToMinPos)
                        addToMinPos=addToMinPos[0:0]
                    
            else:
                if lis[j][1].evaln(check_level,color)==local_min:
                    addToMinPos.append((check_level,j,lis[j][1].evaln(check_level,color),lis[j][1].tieBreaker(color)))
                    #print "add:"
                    #print addToMinPos
                    #raw_input()
                if lis[j][1].evaln(check_level,color)<local_min:
                    if check_level==0:
                        minm=local_min
                    addToMinPos=addToMinPos[0:0]
                    addToMinPos.append((check_level,j,lis[j][1].evaln(check_level,color),lis[j][1].tieBreaker(color)))
                    #print "del as over written localmin1 from %d to %d add::"%(local_min,lis[j][1].evaln(check_level,color))
                    #print addToMinPos
                    #raw_input()
                    local_min=lis[j][1].evaln(check_level,color)
                    if check_level==0:
                        minm=local_min
        j+=1
                

    minim_lis=[]
    minim=-999999999
    if check_level==levs:
        min_poses.append(addToMinPos)
        if local_min!=global_min:
            min_lis.append((local_min,levs))
        #raw_input()
    for x in min_lis:
        if x[0]>minim:
            minim=x[0]
    #print "doing:%d"%get_index(min_poses,minim)
    #raw_input()
    for i in range(len(min_lis)):
        if min_lis[i][0]==minim and i<=check_level:
            minim_lis.append(i)
    # restore this print "min lis has%d minim=%d"%(len(min_lis),minim)
    #print "min lis:"
    #print min_lis;
    #print "minimax:%d"%minim;
    #raw_input();
    if len(minim_lis)==0:
        print "hopeless"
        return 0,0,-1
    '''
    if len(minim_lis)>=1:
        print "luck"
        min_ind=minim_lis[random.randint(0,len(minim_lis)-1)]
    '''
    '''else:
        print "solo"
        min_ind=minim_lis[0]
        #print min_lis
   # print "color tested was:%s"%color
    #raw_input()
    '''
    if minim<-900:
        print "minim too low"        
        return 0,0,-1
    score,pos=get_index(min_poses,minim)
    return minim,score,pos
def get_index(min_poses,minim):
    #print "minim=%d and min_pos:"%minim
    '''for x in range(len(min_poses)-1):
        print min_poses[x]
    print "INDEX:"
    iny= max(a[0] for a in min_poses)
    print iny
    
    #for cnihwo in range(1000):
    raw_input()
    '''
    
    #pos=-1
    #best_ind=-1
    best_lis=[]
    score=0
    best=-9999999;
    for addToMinPos in min_poses:
        
        for indices in addToMinPos:
            if indices[2]==minim:
                #print "found"
                val=indices[3]+indices[2]
                if val>best:
                    #score=
                    #print "val=%d"%val
                    #raw_input()
                    best=val
                    best_lis=best_lis[0:0]
                    #print "deleting"
                    best_lis.append(indices[0])
                else:
                    if val==best:
                        best_lis.append(indices[0])
    #print "best_lis has:%d"%len(best_lis)
    
    return best,best_lis[random.randint(0,len(best_lis)-1)]
                        

