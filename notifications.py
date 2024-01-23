#Ficheiro com tudo relacionado com as notificações

from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path #pathlib is a module in the Python standard library that provides an object-oriented interface for working with filesystem paths. The Path class in pathlib represents a filesystem path and comes with various methods for file and directory manipulation.
from users import * #Para importar as classes do ficheiro users.py para poder importar todas as suas funções
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import tkinter as tk
import time

class show_notifications():
    def __init__(self, tl_notifications_click):
        self.tl_notifications_click = tl_notifications_click
       

   
        lbl_notifications = Label(self.tl_notifications_click, text=self.message)
        lbl_notifications.place(x=200, y=60)














# def show_notification():
#     messagebox.showinfo("Notification", "This is a simple notification.")

# # Create the main window
# window = tk.Tk()
# window.title("Notification")

# # Create a button to trigger the notification 
# notification_button = tk.Button(window, text="Show Notification", command=show_notification)
# notification_button.pack(pady=20)

# # Start the Tkinter event loop
# window.mainloop()

# ---------------------------------------------------------
# def notify_me ()
#     # se no sitiu de por like n houver nenhuma mudança 
#     if ( notify_entry.get()==''):
#     # there is no new notifications
#     else:
#         notification.notify(title='alert',Message=notify_like.get(),timeout=60)


# window = Tk() #Chama a função Tkinter e cria uma janela
# window.geometry('200x60-100-100') #Altera largura e altura da janela e posiciona a janela +/- no centro do ecrã
# window.title('Notification')
# window.resizable(0,0) #Para não se poder redimensionar a janela (para os widgets não saírem do sítio)
# window.configure(bg = '#fff')

# notify_label='this is notifyaction'
# label=tk.Label(window,text=notify_label, font=("Helvetica", 16))
# label.pack(pady=20)

# window.mainloop()