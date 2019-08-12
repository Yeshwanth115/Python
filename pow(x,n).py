def power(x,n):
    if(n==0):
        return 1
    temp=(pow(x,int(n/2)))
    if(int(n%2)==0):
        return (temp*temp)
    else:
        return(2*temp*temp)
print(power(3,2))
