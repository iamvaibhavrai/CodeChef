t = int(input())
for i in range(0,t):
	sal = int(input())
	if sal<1500:
		sal *= 2
	else:
		sal = 2*sal + 500 - (sal/50)

	print("0.1f" %sal)