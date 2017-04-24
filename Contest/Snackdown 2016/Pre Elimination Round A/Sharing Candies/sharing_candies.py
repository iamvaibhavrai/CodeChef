from fractions import gcd

def main():
    for i in range(int(input())):
        a,b,c,d = map(int,input().split(" "))
        g = gcd(c,d)
        res = min((a-b)%g,(b-a)%g)
        print(res)

if __name__ == '__main__':
    main()
