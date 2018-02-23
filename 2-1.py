def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter a base: "))
exp=int(input("Enter the exponential value: "))
print("Result:",power(base,exp))