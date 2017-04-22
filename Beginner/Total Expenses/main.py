t = int(input())
for i in range(0,t):
	q,p = map(int,input().split())
	expense = q*p
	if q>1000:
		expense -= expense/10
	print(float(expense))