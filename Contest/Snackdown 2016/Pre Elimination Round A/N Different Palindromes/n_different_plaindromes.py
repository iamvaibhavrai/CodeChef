for t in range(int(input())):
    n = int(input())
    res = []
    j = 0
    while n > 0:
        i = 1
        x = i*(i+1)//2
        while x <= n:
            i += 1
            x = i*(i+1)//2
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
        for m in range(i-1):
            res.append(letters[j])
        j += 1
        x = i*(i-1)//2
        n -= x
    print(''.join(res))
