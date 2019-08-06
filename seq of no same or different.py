a=[int(x) for x in input().split()[:3]]
b=set(a)
if(len(a)==len(b)):
    print('all elements are different')
else:
    print('all elements are not different')
