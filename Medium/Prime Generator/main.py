import math

def prime(x):
 	y = math.sqrt(x)
 	if y == int(y):
 		return 0
 	for i in range(3,int(y)+1):
 		if x % i == 0:
 			return 0
 	return 1

def main():
	t = int(input())
	for i in range(t):
		x,y = map(int,input().split(" "))
		count = 0
		if x < 3:
			print(2)
		if x % 2 == 0:
			x += 1
		for i in range(x,y+1,2):
			if prime(i):
				print(i)

if __name__ == '__main__':
	main()