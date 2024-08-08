import math


T =int(input())

for i in range(T):
    n,l = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    low,high = 1,max(arr)
    
    while(low<high):
        mid =(low + high)//2
        count = 0

        for i in range(l):
            count += math.ceil(arr[i]/mid)
        
        if count<=n:
            high = mid 
        
        else:
            low = mid+1 
    print(high)


