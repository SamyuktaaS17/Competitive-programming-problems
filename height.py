t = int(input())
for i in range(t):
    n = int(input())
    l = input()
    h = l.split(" ")
    h = [int(i) for i in h]
    if(h == sorted(h)):
        print("L")
    elif(h == sorted(h,reverse = True)):
        print("R")
    else:
        print("N")
