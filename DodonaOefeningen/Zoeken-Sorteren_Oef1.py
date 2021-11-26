def zoekBinair(a, zoekItem):
    l = 0
    r = len(a) -1
    while(l != r):
        m = (l+r)//2
        print(f"{l}, {r}")
        if (a[m] < zoekItem):
            l = m + 1
        else:
            r =m
    if(a[l]== zoekItem):
        index = l
    else:
        index = -1
    return index
