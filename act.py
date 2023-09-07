def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact(n-1)

y=int(input("enter the number:"))
res=fact(y)

print("factorial of the {} is {}".format(y,res))