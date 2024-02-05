weight=input("Weight: ")
value=input("(L)bs or (K)g: ")
w=int(weight)
if value=='L' or value=='l':
    print("Weight in KG is: "+str(w*0.45))
else:
    print("Weight in lbs is: "+str(w//0.45))