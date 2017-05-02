for t in range(int(input())):
    s1 = input()
    s2 = input()
    minimum = len(s1)
    maximum = len(s1)
    for i,j in zip(s1,s2):
        if i == '?' or j == '?':
            minimum -= 1
        elif i == j:
            maximum -= 1
            minimum -= 1
    print(minimum,maximum)
