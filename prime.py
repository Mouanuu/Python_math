#python program to check prime number
num=int(input("enter the value "))
if num==1:
  print("The number is not a prime number")
elif num>1:
    for i in range(2,num):
      # print( i , 'item')
      if num%i ==0 :
        print(num," The number is not a prime number")
        break
      elif i == num -1:
        print(num," The number is a prime number")