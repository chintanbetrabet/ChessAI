def minimax(lis):
    #print "Minimax"
    #t1=time.clock()
    print "size=%d"%len(move2)
    levs=max(a[0] for a in move2)
    print "leveles=%d"%levs
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
    #print "jumpers:"
    print move_jump
    #raw_input()
    while j < (len(lis)) and check_level<levs:
        mover+=1
        
        #print time.clock()-t1
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
                        #raw_input()
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
    minim_lis=[minm]
    #raw_input("enter a key")
    for i in range(len(min_lis)):
        if min_lis[i]>minm and i<levs:
            minim_lis=minim_lis[0:0]
            minim_lis.append(i)
            minm=min_lis[i]
        else:
            if min_lis[i]==minm and i<levs:
                 minim_lis.append(i)                
    #lis[min_ind][1].display_board()
    #raw_input("enter a key")
    print min_lis
    #raw_input("enter a key")
    print "min_ind=%d "%(min_ind)
    #raw_input("enter a key")
    print "original:"
    min_lis=minim_lis[random.randint(0,len(minim_lis)-1)]
    move1[min_ind].display_board()
    return min_ind        
