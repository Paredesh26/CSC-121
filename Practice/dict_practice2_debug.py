# -*- coding: utf-8 -*-

import random as ran
    
def main():

    # get dicts

   capital, country = create_dict()


   user = '1'
   
   incorrect = 0
   
   correct = 0
   
   while user != '0':

        number = ran.randint(1, 21)
        
        right = 'n'
        
        while right == 'n':
            
            print("What is the capital of", country[number], "(press 0 to quit)? ")
            
            user = input()
            
            if user == capital[number]:
                
                right = 'y'
                
                print('You are correct, congratulations!')
                
                correct +=1
                
            elif user =='0':
                
                right ='y'
                
            else:
                
                right = 'n'
                
                print('You are wrong')
                
                incorrect +=1
                
   print('You got ', correct, " correct and got " , incorrect, "incorrect. Thanks for playing" )

   print()
    # now print countries and their capitals
   display(capital, country)




def create_dict():
    
    capital= {1:'kabul', 2:'mexico city', 3:'beijing', 4:'cairo', 5:'paris', 6:'budapest', 7:'rome',
              8:'tokyo', 9:'kuwait city', 10:'tripoli', 11:'amsterdam', 12:'warsaw', 13:'moscow',
              14:'madrid', 15:'seoul', 16:'Taipei', 17:'london', 18:'beirut',
              19:'Ottawa', 20:'Lima'}
    
    
    country= {1:'Afghanistan', 2:'Mexico', 3:'China', 4:'Egypt', 5:'France', 6:'Hungary', 7:'Italy',
              8:'Japan', 9:'Kuwait', 10:'Libya', 11:'Netherlands', 12:'Poland', 13:'Russia',
              14:'Spain', 15:'South Korea', 16:'Taiwan', 17:'United Kingdom', 18:'Lebanon',
              19:'Canada', 20:'Peru'}

    return capital, country



def display(capital, country):

    print(f'{"Country":<20}{"Capital"}')
    
    print("-"*45)

    # Range is for numbers not strings
    for i in range(len(capital)):
        
        print(f'{country[i+1]:<20}{capital[i+1]}')

if __name__ == "__main__":

    main()
    
    


