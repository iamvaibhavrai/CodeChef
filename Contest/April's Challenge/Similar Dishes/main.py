def main():
    t = int(input())
    for i in range(t):
        counter = 0
        x = input().split(" ")
        y = input().split(" ")
        for i in x:
            if i in y:
                counter += 1
        if counter <2:
            print("dissimilar")
        else:
            print("similar")

if __name__ == '__main__':
    main()
