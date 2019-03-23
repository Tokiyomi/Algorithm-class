# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:13:22 2019

@author: monic
"""
#Program to determine the number of prime numbers given n
def main():
    
    n= eval(input("Give me a number: "))
    
    primeCounter=0 #Acumulador de primos
    divCounter=0 #Acumulador de divisores
    
    for number in range (2,n+1):
    
        for divisor in range (2,number+1):
        
            if number%divisor==0:
            
                divCounter= divCounter+1
        
        if divCounter==1:
                primeCounter= primeCounter+1
        
        divCounter=0
            
        
    print("The number {0} has {1} prime numbers".format(n,primeCounter))
        
main()

            
    