# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 07:16:15 2019

@author: monic
"""
import math

def my_cot1(x,n):
    
    #Declare
    sign=-1 
    sum= 0.5*math.pi
    
    #Start the loop
    for i in range (0, n+1):
        index= (2*i +1)
        sum= sum + sign*(1/index * (x**(index)))
        sign=sign*(-1)
        
    return sum

def main():
    
    #Ask for the variables
    x = eval(input("Input the angle in pi radians bewtween -1 and 1 "))
    n = eval(input("Input a power n "))
    
    r = my_cot1(x,n)
        
    #Output
    print("The aproximation is equal to {0:.4f} rad".format(r))
    
main()
