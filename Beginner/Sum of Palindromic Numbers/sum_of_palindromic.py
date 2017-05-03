def palindrome(n):
    i = str(n)
    l = len(i)
    if l == 1:
        return True
    for j in range(l//2):
        if i[j] != i[l-j-1]:
            return False
    return True

for t in range(int(input())):
    l,r = map(int,input().split(" "))
    res = 0
    for i in range(l,r+1):
        if palindrome(i):
             res += i
    print(res)
