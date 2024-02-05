print('''
start - to start the car
stop - to stop the car
quit - to quit
''')
status=""
pre=""
while status.lower()!="quit":
    status=input(">").lower()
    if status.lower()=="start" and status.lower()!=pre:
        print("car started...Ready to go")
    elif status.lower()=="start" and status.lower()==pre:
        print("Car has already started")
    elif status.lower()=="stop" and status.lower()!=pre:
        print("Time to stop the car")
    elif status.lower()=="stop" and status.lower()==pre:
        print("Car has been stopped")    
    pre=status.lower()
   
        
