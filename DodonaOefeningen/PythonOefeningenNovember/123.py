def evenOneven(getal):
    even= 0
    onevne=0
    for i in str(getal):
        if(int(i)% 2) == 0:
            even +=1
        else:
            onevne+=1  
    return even, onevne
    # """
    # >>> evenOneven(886328712442992)
    # (10, 5)
    # >>> evenOneven(10515)
    # (1, 4)
    # >>> evenOneven(145)
    # (1, 2)
    # """

def volgende(getal):
    tupel = evenOneven(getal)
    string = ""
    int2 = 0
    for i in tupel:
        string+=(str(i))
        int2+= i
    string += (str(int2))
    return int(string)
    # """
    # >>> volgende(886328712442992)
    # 10515
    # >>> volgende(10515)
    # 145
    # >>> volgende(145)
    # 123
    # """

def stappen(getal):
    if getal == 123:
        return 0
    teller = 0
    condition =True
    getal1 = getal
    while(condition==True):
        getal1 = volgende(getal1)
        if getal1==123:
            condition=False
        teller+=1
    return teller
    # """
    # >>> stappen(886328712442992)
    # 3
    # >>> stappen(1217637626188463187643618416764317864)
    # 4
    # >>> stappen(0)
    # 2
    # >>> stappen(1)
    # 5
    # >>> stappen(2)
    # 2
    # >>> stappen(3)
    # 5
    # """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
