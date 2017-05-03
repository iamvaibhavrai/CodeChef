for t in range(int(input())):
        counter = 0
        n = int(input())
        a = list(map(int,input().split(" ")))
        b = list(map(int,input().split(" ")))
        for j in range(n):
            if j == 0:
                time=a[j]
            else:
                time=a[j]-a[j-1]
            if time>=b[j]:
                counter += 1
        print(counter)
