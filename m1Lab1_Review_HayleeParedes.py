# Review of loops and decision structures
# Jan. 26, 2025
# CSC121 m1Lab1– Review
# Haylee

'''
Step 1: Set up a control variable to start the program for a loop. 
Step 2: Set up a way for the program to keep running until user enters in no. 
Step 3: Get value/input from user about how many items they have.
Step 4: Use an if-else statement to get information on the cost per item based off of the number of items the user has.
Step 5: Calculate the total of all the items based off the cost per item and number of items.
Step 6: Display the cost per item.
Step 7: Display the total cost.
Step 8: Ask the user if they wish to run the program again.
Step 9: When user enters no, the program ends and displays to the user that the program is ending.
'''

# Use run_again to start this program.
run_again = "yes"

# Setting up a condition where if the user enters no, the program ends. 
while run_again != "no":
    
    # Get the input from user .
    itemNum = int(input("Enter in the number of items you have: "))

    # Create a if-else statement to get the cost per item based of number of items.

    # Number of items under/equal to 19 cost 4.75 per item.
    if itemNum <= 19:
        # cpi = cost per item
        cpi = 4.75

    # Number of items under/equal to 49 cost 4.50 per item.
    elif itemNum <= 49:
        cpi = 4.50

    # Number of items under/equal to 99 cost 4.25 per item.
    elif itemNum <= 99:
        cpi = 4.25

    # Anything else costs 4.00 per item.
    else:
        cpi = 4.00

    # Calculate the total cost of items based off their cost per item and number of items.
    total = itemNum * cpi

    # Display the cost per item to user.
    print(f"The cost per item is ${cpi:.2f}")

    # Display the total cost to user.
    print(f"The total cost of your items is ${total:.2f}")

    # Ask user if they are running the program again.
    run_again = input("Do you want to run this program again? (Yes/No: ")

# When user enters no, display that they are ending/exiting the program.
print("Exiting program...")

    
