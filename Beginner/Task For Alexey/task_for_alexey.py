def lcm(a,b):
    return (a*b)//gcd(a,b)

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

for t in range(int(input())):
    n = int(input())
    x = list(map(int,input().split(" ")))
    res = lcm(x[0],x[1])
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            l = lcm(x[i],x[j])
            res = min(l,res)
    print(res)
