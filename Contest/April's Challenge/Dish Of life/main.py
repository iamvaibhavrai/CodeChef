def main():
    t = int(input())
    for i in range(t):
        n,k = map(int,input().split(" "))
        ingridients = [0 for i in range(k)]
        printed = 1
        f_continue = 0
        for j in range(n):
            x = input().split(" ")
            for k in range(1,len(x)):
                ingridients[int(x[k])-1] = 1
            for ingridient in ingridients:
                if ingridient == 0:
                    f_continue = 1
                    break
        for ingridient in ingridients:
            if ingridient == 0:
                printed = 0
                print("sad")
                break
        if printed:
            if f_continue:
                print("all")
            else:
                print("some")

if __name__ == '__main__':
    main()
