from pickle import GLOBAL
from tkinter import Y


x = 0
y = 0

def init(a,b):
    global x 
    global y
    
    x = a
    y = b



def sum():
    return x + y

def mult():
    return x*y

def get_operator():
    return input("Enter operator: ")
   