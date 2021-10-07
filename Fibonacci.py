# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:51:46 2021

@author: mx
"""

from tkinter import *
root=Tk()
root.title("fibonacci")
root.geometry("400x400")

label_series=Label(root,text="Fibonacci series : ")

def fibonacci():
    num=10
    first_no=0
    second_no=1
    sum=0
    counter=1
    while(counter<=num):
        counter=counter+1
        label_series["text"]+=str(sum)+" "
        first_no=second_no
        second_no=sum
        sum=first_no+second_no
        
btn = Button(root, text="Show Fibonacci Series", command=fibonacci)
btn.pack()
label_series.pack()
root.mainloop()
        