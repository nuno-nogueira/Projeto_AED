import tkinter as tk
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("500x300")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title
l1 = tk.Label(my_w, text='Your Data', width=10,font=20 )  # added one Label 
l1.grid(row=0,column=0,padx=3,pady=10,columnspan=2) 
t1=tk.Text(my_w,height=6,width=40,bg='lightgreen',font=28)
t1.grid(row=1,column=0,padx=10,columnspan=2)
l2=tk.Label(my_w,text=0,font=22)
l2.grid(row=2,column=0,padx=5,pady=5)
def my_upd(value):
    my_str=t1.get('0.0','end-1c') #The input string except the last line break
    breaks=my_str.count('\n') # Number of line breaks ( except the last one )
    char_numbers=len(my_str)-breaks # Number of chars user has entered 
    l2.config(text=str(char_numbers)) # display number of chars 
    if(char_numbers > 20):
        t1.delete('end-2c') # remove last char of text widget
t1.bind('<KeyRelease>',my_upd) # Key release event to call function.  

my_w.mainloop()  # Keep the window open

import sys
print(sys.path)
