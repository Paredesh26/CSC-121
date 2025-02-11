# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:11:06 2025

@author: paredesh3418
"""

def main():
   
    # call the welcome funtion
    first, last = welcome()
    
    print("Hello", first, last)
    print()
    # call the getGrade function
    getGrade()
    
def welcome():
    '''
    Fuction doesn't require arguments.
    Asks user to enter their name and says hi to them.
    '''
    
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    print()
    
    return first, last

def getGrade():
    '''
    Asks user to enter score and determine code.
    
    Returns
    -------
    None.

    '''
    score = float(input("Enter score or -1 to terminate: "))

    while score != -1:
        
        while score < 0 or score > 100:
    # get score 
            print("INVALID SCORE!!!! Enter a valid score (0-100)")
            score = float(input("Enter score: "))
        
        # determine letter grade
        
        if score >= 90:
            print('A')
            
        elif score >= 80:
            print('B')
        
        elif score >= 70:
            print('C')
        
        else:
            print('F')
            
        score = float(input("Enter score or -1 to terminate: "))
    
if __name__ == "__main__":
    main() 