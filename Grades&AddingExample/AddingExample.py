# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:24:34 2025

@author: paredesh3418
"""

import GradesExample as gr

def main():
    
    gr.welcome()
    
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    
    # add numbers
    total = num1 + num2
    print(total)

main()