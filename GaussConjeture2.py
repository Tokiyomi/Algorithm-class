# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:21:48 2019

@author: monic
"""

import math

#Function to compute Gauss Conjecture about prime numbers
def conjeture(n):
    return n/math.log(n)

#Function to compute actual number of primes
def pi_n(n):
    


def main():
    
    print ("n\t\t n/log(n) \n")
    
    for i in [10,100,1000,10000,100000,1000000,10000000]:
        print ("{0:.0f}\t\t {1:.2f}".format(i,conjeture(i)))
        
main()
