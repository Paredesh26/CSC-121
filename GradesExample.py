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
    
    score = float(input("Enter score or -1 to terminate: "))
    
    # call the getGrade function
    grade = getGrade(score)
    
    print('Your grade is ', grade)
    
def welcome():
    '''
    Fuction doesn't require arguments.
    Asks user to enter their name and says hi to them.
    '''
    
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    print()
    
    return first, last

def getGrade(score):
    '''
    Parameter: score(float)
    Determines grade of score.
    
    Returns
    -------
    None.

    '''

    while score != -1:
        
        while score < 0 or score > 100:
    # get score 
            print("INVALID SCORE!!!! Enter a valid score (0-100)")
            score = float(input("Enter score: "))
        
        # determine letter grade
        
        if score >= 90:
            grade = 'A'
            
        elif score >= 80:
            grade = 'B'
        
        elif score >= 70:
            grade = 'C'
        
        else:
            grade = 'F'
            
        score = float(input("Enter score or -1 to terminate: "))
    return grade 
    
if __name__ == "__main__":
    main() 