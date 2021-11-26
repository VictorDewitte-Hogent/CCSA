def bubble_sort(a):
    teller = 0
    for i in range(0 , len(a)-1):
        for j in range(len(a) -1 , i ,-1):
            teller+=1
            if(a[j-1] > a[j]):
                wissel = a[j]
                a[j] = a[j-1]
                a[j-1]= wissel
                
        print(a)
    print(f"Voor een rij van lengte {len(a)} werd het if-statement {teller} keer uitgevoerd")


a = [int(_) for _ in input().split()]
bubble_sort(a)
