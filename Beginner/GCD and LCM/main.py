def computeHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf
def computeLCM(x, y):
   lcm = (x*y)//computeHCF(x,y)
   return lcm

t = int(input())
for i in range(0,t):
	a,b = map(int,input().split())
	print(str(computeHCF(a,b)) + " " + str(computeLCM(a,b)))