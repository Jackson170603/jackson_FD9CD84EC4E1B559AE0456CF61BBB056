def leap(n):
 if n%4 ==0:
   print("{} is a leap year".format(n))
 else:
   print("{} is not aleap year".format(n))

y=int(input("enter the year:"))
res=leap(y)