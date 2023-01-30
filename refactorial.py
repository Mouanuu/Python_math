#recursive factorial
def fact(n):
  if n==1 or n==0:
    return 1
  else:
    return (n * fact(n-1))

n=int(input("enter the value"))
if n==0:
  print("The factorial value is 1")
else:
  print("The factorial value is :",fact(n))
  
  #program to find factorial value by recursion
def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)
a=int(input("enter the value :"))
b=fact(a)
print("The factorial value is :",b)