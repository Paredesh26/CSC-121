# Use of loops and decision structures
# Feb. 2, 2025
# CSC121 m1Lab2– Review
# Haylee Paredes

'''
Step 1: Get the 1st route distance from the user.
Step 2: Get the speed of the route. miles per hour
Step 3: Ask user if they would like to add more routes. (Yes or No)
Step 4: If user says yes to adding more route repeat steps 1-3 until user answers no in step 3.
Step 5: When user says no in step 3, display the fastest route the user can take. 
'''
# fR = fastest route. Placeholder until fastest route is found.
fR = 0

# fT = fastest time. Base placeholder until less amount of time is found.
fT = 9999

# rNum = route number. This is so the user knows how many routes they have entered starting at 1. 
rNum = 1

# moreR = more routes. This is similar to keep_going so the program keeps asking the user if they want to add more routes.
moreR = 'y'


while moreR.lower() == 'y':
    
    # Get input from user about route distance.
    dist = float(input(f"Enter route {rNum} distance (miles): "))
    
    # Prompt an error message if user enters a negative number. User must enter a number greater than zero. Then re-ask the user to enter in a new number. 
    while dist <=0:
        print("Error, route distance must be greater than 0.")
        dist = float(input(f"Enter route {rNum} distance (miles): "))
    
    # Get input from user about speed.
    speed = float(input(f"Enter route {rNum} speed (miles/hour: "))
    
    # Prompt an error message if user enters a negative number. User must enter a number greater than zero. Then re-ask the user to enter in a new number. 
    while speed <=0:
        print("Error, speed must be greater than 0.")
        speed = float(input(f"Enter route {rNum} speed (miles/hour: "))
    
    # Get the calculated time in minutes(hours to minutes).
    minutes = round((dist / speed) * 60)
    
    # Use an if-else statement to find out the fastest route. Keep route 1 as fastest if there are no other routes.
    if rNum == 1:
        fT = minutes
        fR = rNum
        
    # If the user adds more routes, check which is the fastest. 
    elif minutes < fT:
        fT = minutes
        fR = rNum
    
    # Ask the user if they want to add ore routes.
    moreR = input("More routes (y/n)? ").lower()
    
    # Make the number go up based on how many routes the user enters in. 
    rNum += 1
    
# Display the fastest route to the user.
print(f"Route {fR} is fastest; {fT} minutes")
    
    
    
    