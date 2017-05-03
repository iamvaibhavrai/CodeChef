for t in range(int(input())):
    w,p = map(int,input().split(' '))
    words = list(input().split(' '))
    phrases = []
    for m in range(p):
        x = list(input().split(' '))
        for n in range(1,len(x)):
            phrases.append(x[n])
    counter = 0
    for i in range(len(words)):
        if words[i] in phrases:
            print("YES",end=" ")
        else:
            print("NO",end=" ")
    print()
