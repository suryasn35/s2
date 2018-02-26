n=int(input("Enter a number"))
sum=0
num=n
while n>0:
	r=n%10
	sum=sum+(r**3)
	n=n//10
#	b=sum
if sum==num:
	print("yes")
else:
	print("no")