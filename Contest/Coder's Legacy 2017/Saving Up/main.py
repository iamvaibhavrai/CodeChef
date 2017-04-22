test_cases = int(input())
for i in range(test_cases):
	no_of_expenditures,salary = map(int, input().split(" "))
	x = input()
	x = x.split(" ")
	sum_of_expenditures = 0
	for j in x:
		j = int(j)
		sum_of_expenditures += j
	if sum_of_expenditures <= salary/2:
		print("Yes")
	else:
		print("No")