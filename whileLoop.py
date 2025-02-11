# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:24:42 2025

@author: paredesh3418
"""
'''
run_again = 'yes'
while run_again.lower() == 'yes':

    quantity = float(input("Enter quantity: "))
    
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
    
    run_again = input("Do you want to run the program again? (yes to re-run) ")
'''

quantity = float(input("Enter quantity or -1 to terminate: "))

while quantity !=-1 and quantity >=0:
    
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
    
    quantity = float(input("Enter quantity or -1 to terminate: "))