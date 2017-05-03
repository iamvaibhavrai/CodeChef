for t in range(int(input())):
    s = input()
    counter = 0
    for i in range(1,len(s)):
        if s[i] == '>' and s[i-1] == '<':
            counter += 1
    print(counter)
