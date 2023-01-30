#python program to find the factorial of a number
num=int(input("enter the value "))
fac=1
if num<1:
  print("The factorial value is invalid")
elif num>1:
    for i in range (1,num+1):
      fac=fac*i
      if( i == num ):
        print("The factorial value is ",fac)
      # print(fac)
else:
  print("the factorial value is 1")