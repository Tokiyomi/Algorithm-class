# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 07:10:21 2019

@author: monic
"""

def main ():
    
    #Ask for type of convertion
    print("Choose C to Celcius, choose F to fahrenheit, choose K to Kelvin")
    NewTempUnit= input ("Which temperature unit do you want? ")
    OldTempUnit= input("Which temperature unit do you have? ")
    
    #Ask for the value
    
    Temp = eval(input ("Which is the temperature value? "))
    
    #Compute convertion
    if NewTempUnit=='F'and OldTempUnit=='C':
        NewTempValue = (Temp * 1.8 + 32)
        print("{0:.2f} °C is equal to {1:.2f} °F".format(Temp,NewTempValue))
    
    else:
        NewTempValue = (Temp - 32)/1.8
        print("{0:.2f} °F is equal to {1:.2f} °C".format(Temp,NewTempValue))
    
main ()
        