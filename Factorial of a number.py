num=int(input("enter a number:"))
factorial=1
if num<0:
    print("no factorial for negative numbers")
elif num==0:
       print("zero")
else:
         for i in range(1,num+1):   
               factorial=factorial*i
         print("factorial of ",num,"is",factorial)