t = int(input())
for i in range(0,t):
	a = input()
	a = [i for i in a]
	operator = []
	string = []
	for i in a:
		if i == '(' or i == '+' or i == '-' or i == '*' or i == '/' or i == '^':
			operator.append(i)
		else:
			if i is not ')':
				string.append(i);
		if i == ')':
			j = operator.pop()
			while j is not '(':
				string.append(j)
				j = operator.pop()
	print(''.join(string))