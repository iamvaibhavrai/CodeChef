for t in range(int(input())):
    n = int(input())
    xor = 1
    for j in range(n):
        x = input()
        if j == 0:
            continue
        xor ^= (j+1)
    print(xor)
