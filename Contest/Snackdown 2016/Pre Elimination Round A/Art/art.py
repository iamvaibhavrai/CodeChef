def finishPainting(p,n):
    if n < 3:
        return False
    count = 1
    prev = p[0]
    for i in range(1,n):
        curr = p[i]
        if curr == prev:
            count += 1
        else:
            count = 1
            prev = curr
        if count == 3:
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
