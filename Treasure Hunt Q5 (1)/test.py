def minimax(lis):
    #print "Minimax"
    print "size=%d"%len(lis)
    #for x in lis:
        #x.display_board()
    raw_input()
    
    global_min=10**399
    check_level=0
    min_ind=0
    min_pos=0
    minm=-1*global_min
    local_min=global_min
    min_lis=[]
    for x in lis:
        if x[0]>check_level:
            check_level=x[0]
            #print "at:%d"%x[0]
            min_lis.append(local_min)
            minm=-1*global_min
            #print "min:%d"%local_min
            for i in range(len(min_lis)):
                    if min_lis[i]>minm:
                            min_ind=i
                            minm=min_lis[i]
            local_min=global_min
        if x[0]==check_level:
            #print "scan:%d"%x[1]
            if x[1]<minm:
                    check_level+=1
                    min_lis.append(x[1])
            else:
                if x[1]<local_min:
                    local_min=x[1]
    if(local_min<global_min):
            min_lis.append(local_min)
    minm=-1*global_min
    for i in range(len(min_lis)):
        if min_lis[i]>minm:
            min_ind=i
            minm=min_lis[i]
    print min_ind
m=[(0,4),(1,5),(1,8),(2,5),(2,10),(3,7),(3,6)]
minimax(m)

