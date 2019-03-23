# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:29:14 2019

@author: monic
"""

#Program to compute the sum of the n power of a number between -1 and 1

def main():
    
    #Ask for a number
    x= eval(input("Give me a number between -1 and 1 to compute its sum: "))
    n= eval(input("Give me a power n>0: "))
    
     #Stablish the sum
    sum=0
    i=0

    #Compute the fraction
    fracc= 1/(1-x)
   
    #Compute the sum
    while (i<=n):
        sum= sum + x**i 
        i= i + 1
    
    #Print the sum
    print("The result of the fraction is {0} and the approximate value is {1:.4f}".format(fracc,sum))
    
main()
    

            
            
        
        