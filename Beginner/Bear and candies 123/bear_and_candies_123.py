for t in range(int(input())):
    a,b = map(int,input().split(" "))
    count,x,y = 1,0,0
    while(True):
        x += count
        if x > a:
            print("Bob")
            break
        count += 1
        y += count
        if y > b:
            print("Limak")
            break
        count += 1
