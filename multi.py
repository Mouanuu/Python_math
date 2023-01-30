#python program to find the multiplication table
num=int(input("enter the value "))
for i in range(1,11):
  if i==5:
    print("This is step five")
  print(num,"x",i,"=",num*i)