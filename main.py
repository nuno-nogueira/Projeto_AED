from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path #pathlib is a module in the Python standard library that provides an object-oriented interface for working with filesystem paths. The Path class in pathlib represents a filesystem path and comes with various methods for file and directory manipulation.
from users import * #Para importar as classes do ficheiro users.py para poder importar todas as suas funções

# ------------PÁGINA INICIAL--------------------------
class App():
    def __init__(self, window):
        """
        Permite criar uma window que é um objeto da classe App
        """
        self.window = window
#       Criar o Frame da página incial com uma imagem de fundo
        self.main_frame = Frame(self.window, width = 1000, height = 600, bg = '#333333')
        self.main_frame.place(x = 0, y = 0)

#       Mensagem de bem-vindo
        self.welcome_message_label = Label(self.window, text = 'Welcome to \nmyPhotos!', bg = '#333333', font = ('Roboto', 55), fg = 'white').place(x = 300, y = 150)

#       Botão para passar para o frame para criar uma conta!
        self.sign_up_button = Button(self.window, text = 'Sign Up',bg = 'lightblue', fg = 'white', font = ('Roboto', 25), command = self.go_to_sign_up).place(x = 325, y = 350)

#       Botão para passar para o frame para fazer login!
        self.login_button = Button(self.window, text = 'Login',bg = 'lightblue', fg = 'white', font = ('Roboto', 25), command = self.go_to_login).place(x = 575, y = 350)

       
#       Botão com um icon para o utilizador sair da app
        icon = Image.open(Path('../Projeto_AED/images/icons/logout_icon.png')).resize((80,80)) # platfmor independet
        icon = ImageTk.PhotoImage(icon)
        self.leave_app_btn = Button(self.window, image = icon, bd = 0, bg='#333333', command = self.leave_app)
        self.leave_app_btn.image = icon
        self.leave_app_btn.place( x = 920, y = 520)
        self.btn_leave= Button(self.window, text='Leave', command = self.leave_app)


    def go_to_sign_up(self):
        """
        Esta função leva o utilizador á página para criar uma conta
        """
        Sign_Up(self.window)


    def go_to_login(self):
        """
        Esta função leva o utilizador á página para fazer login e acessar a app
        """
        Login(self.window)


    def leave_app(self):
        """
        Esta função pergunta ao utilizador se deseja sair da app 
        """
        answer = messagebox.askquestion('Leave the App', 'Do you wish to leave the app?')    
        if answer == 'yes':
           exit()

        
#--------CONFIGURAÇÕES DE JANELA------------------------------------
window = Tk() #Chama a função Tkinter e cria uma janela
window.geometry('1000x600+100-100') #Altera largura e altura da janela e posiciona a janela +/- no centro do ecrã
window.title('myPotos')
window.resizable(0,0) #Para não se poder redimensionar a janela (para os widgets não saírem do sítio)
window.configure(bg = 'lightgrey')

App(window)

window.mainloop()
