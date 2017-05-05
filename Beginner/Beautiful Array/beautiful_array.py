for t in range(int(input())):
    n = int(input())
    x = list(map(int,input().split(" ")))
    ones = x.count(1)
    zeros = x.count(0)
    minus = x.count(-1)
    other = n-ones-zeros-minus
    if other > 1:
        print("no")
    elif minus > 1 and ones == 0:
        print("no")
    elif other > 0 and minus > 0:
        print("no")
    else:
        print("yes")
