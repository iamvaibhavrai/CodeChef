def gcd(m,n):
    while n:
        m,n = n,m%n
    return m

for t in range(int(input())):
    m,n = map(int,input().split(" "))
    g = gcd(m,n)
    res = (m*n)//(g**2)
    print(res)
