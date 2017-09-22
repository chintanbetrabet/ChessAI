for i in range(8):
    #for j in range(8):
    r=i
    #c=j-4
    print ' '.join(str((-r**2+7*r)*(-j**2+7*j)) for j in range(8))
    
