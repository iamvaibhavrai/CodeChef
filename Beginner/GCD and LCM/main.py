def gcd(a,b):
	while b:
		a,b = b,a%b
	return a

for t in range(int(input())):
    a,b = map(int,input().split(" "))
    res = gcd(a,b)
    m = a*b
    print(res,m//res)
