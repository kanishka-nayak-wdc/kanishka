is_hot=False
if is_hot:
    print("Its a hot day")
else:
    print("its a cold day")
    print("be careful")
    
print("Enjoy Your day")

temp=input("enter temp ")
temp1=int(temp)
if temp1>20:
    print("hot")
elif temp1>10 and temp1<20:
    print("normal")
elif temp1==10:
    print("its a perfect day")
else:
    print("cold")
