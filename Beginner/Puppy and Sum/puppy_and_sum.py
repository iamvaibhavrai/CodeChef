def summation(n):
    return (n*(n+1)//2)

for t in range(int(input())):
    d,n = map(int,input().split(" "))
    s = summation(n)
    for i in range(1,d):
        s = summation(s)
    print(s)
