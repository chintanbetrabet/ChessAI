import copy
def minimax(lis):
    #print "Minimax"
    #print "size=%d"%len(lis)
    #for x in lis:
        #x.display_board()
    #raw_input()
    
    global_min=10**5
    check_level=0
    min_ind=0
    minm=-1*global_min
    local_min=global_min
    min_lis=[]
    mover=0
    #print "i=%d"%mover
    i=0
    j=0
    cont=0
    run=0
    print len(lis)
    while i<len(lis) and j<len(lis[i]):
        run+=1
        #print "i=%d j=%d"%(i,j)
        #print "run=%d check:%d"%(run,lis[i][j])
        #raw_input()
        if j==0:
            local_min=lis[i][j]
            #print "lm=%d"%local_min
        if lis[i][j]<minm:
            print 
            min_lis.append(lis[i][j])
            minm=max(min_lis)
           # print "cut after%d"%lis[i][j]
           # print "mini=%d"%minm
            i+=1
            j=0
            
            
        else:
            if lis[i][j]<local_min:
                local_min=lis[i][j]
                
                
            j+=1           
        if j==len(lis[i]):
            #print "rest"
            min_lis.append(local_min)
            minm=max(min_lis)
            #print "mini=%d"%minm
            if(i<len(lis)):
                i+=1
                j=0
        
    #print min_lis
    min_ind=0
    minm=-1*global_min
    i=0
    while i<len(lis):
        if min_lis[i]>minm:
            minm=min_lis[i]
        i+=1
    #print "ran:%d"%run
    return i-1
        

             
             
             
             
    
                    

