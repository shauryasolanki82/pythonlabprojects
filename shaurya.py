import random as r
name=input("enter your name")
rd=r.randrange(1,10)
for i in range(3):
    num=int(input("enter a no"))
    if(num==rd):
        print("you won")
        break;
    elif(num>rd):
        print("your no is greater")
    elif(num<rd):
        print("your no is smaller")
  
    
