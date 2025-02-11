# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:47:48 2025

@author: paredesh3418
"""

'''
num = int(input("Enter number of customers: "))

# ask for quantity
for x in range(1,num+1):
    
    print("Enter info for customer #", x)
    
    quantity = float(input("Enter quantity: "))

# evaluate 
'''
'''
if quantity is >= 15 --> 15%
if > 10 --> 10%
if >5 --> 5%
'''
'''
if quantity >= 15:
    
    discount = 0.15

elif quantity >= 10:
    
    discount = 0.10

elif quantity >= 5:
    
    discount = 0.05
    
else: 
    discount = 0
    
# determine pay

result = (quantity * 4) - discount

# display
# format can be used to get decimal points like rounded decimal points

print("Discount", discount)
print("Total $", format(result, '.2f'), sep = '')
'''

days = int(input("Enter num of days business operates: "))
print()

# accumulator variable
total = 0
for day in range(1,days+1):
    
    amount = float(input("Enter amount generated for day #"+str(day)+" $"))
    total += amount 

print("Final profit generated $",total)