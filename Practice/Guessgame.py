import random

run_again == 'yes'

while run_again == 'yes'
    capitals = {'USA': 'Washingtion D.C', 'Turkey': 'Istanbul', 'Japan': 'Tokyo', 'China': 'Bejing'}
    
    # Diplay the country ans ask user to guess the capital 
    
    # Get list of the country
    countries = list(capitals.keys())
    
    # print(countries)
    # Pick a country randomly
    country = random.choice(countries)
    guess = input("What is the capital of " + country + "? ")
    
    # Check if guess is correct
    if guess == capitals[country]:
        print("Well Done!!")
    else:
        print("Incorrect!!!!!")