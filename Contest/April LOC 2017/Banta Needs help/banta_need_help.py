class Node:
    def __init__(self):
        self.prev = None
        self.prevprev = None

for t in range(int(input())):
    n = int(input())
    res = 0
    node = Node()
    for i in range(1,n+1):
        if i == 1:
            res += i
            temp = 1
            node.prev = 1
            node.prevprev = 0
        else:
            curr = node.prev + node.prevprev
            node.prevprev = node.prev
            node.prev = curr
            res = (res + i*curr) % 1000000007
    print(res)
