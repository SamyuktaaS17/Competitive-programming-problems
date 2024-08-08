T =int(input())

for i in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    flag = 0
    sort_arr = sorted(arr)
    max = 0
    for i in range(n):
        if(arr[i] == sort_arr[i]):
            max+=1 
            if(flag==1):
                max+=1
                flag = 0
        else:
            flag = 1
            if(i==n-1):
                max+=1
                break
            
    print(max)
