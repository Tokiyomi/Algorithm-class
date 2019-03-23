# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:15:07 2019

@author: monic
"""

#Program to compute the sum of 3+5+7+9...159

def main():
    y=3
    sum=0
    
    #Compute the first sum 
    
    sum= sum + y
    
    #Start the loop
    
    while (y<159):
        y = y+2
        sum=sum + y
    
    print("The sum of the series is equal to:",sum)
        
main()
        
        
        
        