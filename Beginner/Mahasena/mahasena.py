n = int(input())
x = list(map(int,input().split(' ')))
even,odd = 0,0
for i in x:
    if i&1 == 0:
        even += 1
    else:
        odd += 1
if even>odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
