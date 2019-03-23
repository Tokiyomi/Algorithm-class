# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 08:28:25 2019

@author: monic
"""

# Loop using snetinels

def main ():
     
    # Variables initialized
    sentinel= -1
    sum= 0 
    counter= 0
    
    #Start with the first number
    n= eval(input("Give me a number, -1 to finish: "))
    
    #Start the Loop
    
    while n != sentinel:
        sum = sum + n
        counter= counter + 1
        n= eval(input("Give a number, -1 to finish: "))
        
    #Finish the Loop

    avg= sum/counter 
   
    print("The average is: {0:.2f}".format(avg))
    
main()