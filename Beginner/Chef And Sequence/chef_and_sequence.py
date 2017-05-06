for t in range(int(input())):
    n = int(input())
    s = set(list(map(str,input().split(" "))))
    m = int(input())
    ss = set(list(map(str,input().split(" "))))
    j = 0
    print('Yes' if(s&ss == ss) else 'No')
