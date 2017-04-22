def computeHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf

t = int(input())
for i in range(0,t):
	x = list(map(int,input().split()))
	num_elements = x.pop(0)
	if num_elements == 2:
		hcf = computeHCF(x[0],x[1])
		x = [y//hcf for y in x]
	elif num_elements > 2:
		hcf = computeHCF(x[0],x[1])
		for j in range(2,num_elements):
			hcf = computeHCF(x[j],hcf)
		x = [y//hcf for y in x]
	print(' '.join([str(v) for v in x]))
