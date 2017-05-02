for t in range(int(input())):
    n = int(input())
    s = input()
    for i in s:
        if i == 'I':
            print("INDIAN")
            break
        if i == 'Y':
            print("NOT INDIAN")
            break
    else:
        print("NOT SURE")
