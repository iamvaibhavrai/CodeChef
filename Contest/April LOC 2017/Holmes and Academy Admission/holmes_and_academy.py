for t in range(int(input())):
    n = int(input())
    x = list(map(int,input().split(' ')))
    x.append(0)
    count,res = 1,0
    for i in range(1,n+1):
        if x[i] == x[i-1]:
            count += 1
        else:
            res += count*(count-1)//2
            res += count
            count = 1
    print(res)
