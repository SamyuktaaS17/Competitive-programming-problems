t = int(input())
for i in range(t):
    mn = input()
    mnl = mn.split(" ")
    m = mnl[0]
    n = mnl[1]
    sol =[]
    path = input()
    for i in range(len(path)-1):
        if(path[i]==path[i+1]):
            sol.append(path[i])
    print(max(sol))