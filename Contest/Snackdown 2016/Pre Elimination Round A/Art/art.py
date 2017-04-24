def finishPainting(p,n):
    if n < 3:
        return False
    prev = p[0]
    flag1 = 1
    flag2 = 1
    for i in range(n):
        curr = p[i]
        if curr != prev:
            if n-i < 3:
                flag1 = 0
        prev = p[i] if curr != prev else prev
    for i in range(n-1,-1,-1):
        curr = p[i]
        if curr != prev:
            if i-2 < 0:
                flag2 = 0
        prev = p[i] if curr != prev else prev
    if flag1 or flag2:
        return True
    return False


def main():
    for t in range(int(input())):
        n = int(input())
        p = list(map(int,input().split(" ")))
        if(finishPainting(p,n)):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
