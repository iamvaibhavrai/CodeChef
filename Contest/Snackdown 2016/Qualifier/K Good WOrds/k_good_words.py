def makeKGoodWord(word,k):
    d = {}
    for letter in word:
        d[letter] = d.get(letter,0) + 1
    value = sorted(d.values())
    setValue = set(value)
    cost = sum(value)
    for x in setValue:
        tempCost = 0
        for y in value:
            if y < x:
                tempCost += y
            elif y > x+k:
                tempCost += y-x-k
        cost = cost if cost<tempCost else tempCost
    return cost

def main():
    t = int(input())
    for i in range(t):
        x = input().split(" ")
        word = list(x[0])
        k = int(x[1])
        result = makeKGoodWord(word,k)
        print(result)

if __name__ == '__main__':
    main()
