for t in range(int(input())):
    n,m,k = list(map(int,input().split(" ")))
    x = n-m if n>m else m-n
    if x < k:
        print("0")
    else:
        print(x-k)
