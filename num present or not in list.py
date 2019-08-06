a=[int(x) for x in input().split() [:5]]
b=int(input())
if b in a:
    print(b,"is present")
else:
    print(b,"is not present")
