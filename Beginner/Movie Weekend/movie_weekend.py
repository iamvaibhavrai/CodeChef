for t in range(int(input())):
    n = int(input())
    length = list(map(int,input().split(" ")))
    rating = list(map(int,input().split(" ")))
    res = 0
    count = 1
    for i in range(1,len(length)):
        if length[res]*rating[res] < length[i]*rating[i]:
            res = i
        elif length[res]*rating[res] == length[i]*rating[i]:
            if rating[i] > rating[res]:
                res = i
    print(res+1)
