capital= {1:'Kabul', 2:'Mexico City', 3:'Beijing', 4:'Cairo', 5:'Paris', 6:'Budapest', 7:'Rome', 8:'Tokyo', 9:'Kuwait City', 10:'Tripoli', 11:'Amsterdam', 12:'Warsaw', 13:'Moscow', 14:'Madrid', 15:'Seoul', 16:'Taipei', 17:'London', 18:'Beirut', 19:'Ottawa', 20:'Lima'}


country= {1:'Afghanistan', 2:'Mexico', 3:'China', 4:'Egypt', 5:'France', 6:'Hungary', 7:'Italy', 8:'Japan', 9:'Kuwait', 10:'Libya', 11:'Netherlands', 12:'Poland', 13:'Russia', 14:'Spain', 15:'South Korea', 16:'Taiwan', 17:'United Kingdom', 18:'Lebanon', 19:'Canada', 20:'Peru'}

# cap_val = list(capital.values())
# country_val = list(country.values())

# # Create a dict
# country_cap = {}

# for i in range(len(cap_val)):
    
     # Add country as key, capital as the value
     # Get country
     # key = country_val [i]
     # country_cap[key] = cap_val[i]

# print(country_cap)


# numbers = [ num for num in range(500, 2001)]
country_cap = { country[num]:capital[num] for num in range(1, 21)}