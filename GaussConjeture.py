# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:14:12 2019

@author: monic
"""

import math

def gauss_conjeture(n):
    
    gauss= n/(math.log(n))
    
    return gauss


def main():
    
    n= eval(input("Give me a bigger number of elements: "))
    m= eval(input("Give me the real amount of prime terms in that quantity of elements: "))
    
    r= gauss_conjeture(n)
    number_of_primes= r//1
    
    print("The number of prime numbers according to Gauss is: {0:.0f}".format(number_of_primes))
    
    lim= (r/m) *100
    
    print("The Gauss conjeture is similar in a rate of {0:.2f} %".format(lim)) 
    
    
main()


    
    
    