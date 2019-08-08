t1=(1,2,3,4,5,6)
t1=t1[:2]+t1[4:]
print(t1)
x=list(t1)
x.remove(1)
t1=tuple(x)
print(t1)
