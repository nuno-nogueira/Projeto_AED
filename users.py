from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from homepage import Main_App #Para importar a função homepage_window (função que cria a janela homepage) que está no ficheiro homepage.py
from pathlib import Path #pathlib is a module in the Python standard library that provides an object-oriented interface for working with filesystem paths. The Path class in pathlib represents a filesystem path and comes with various methods for file and directory manipulation.
import os

#----------------------------------SIGN UP-----------------------------------------------------------
class Sign_Up():
    def __init__(self, window):
        """
        Função para mostrar o frame para o utilizador Criar Conta
        Neste frame, o utilizador cria uma conta com um nome de utilizador, o seu email, e a password
        """
#       Configurações da janela da TopLevel
        self.tl = Toplevel(window)
        self.tl.geometry('1000x600+100-100') #  Altera largura e altura da janela e posiciona a janela +/- no centro do ecrã
        self.tl.title('myPhotos')
        self.tl.resizable(0,0) #    Para não se poder redimensionar a janela (para os widgets não saírem do sítio)

#       Variável que cria a frame para a página do Sign Up
        self.sign_up_frame = Frame(self.tl, width = 1000, height = 600, bg = '#333')
        self.sign_up_frame.place(x = 0, y = 0)

#       Label com 'Sign Up'
        self.sign_up_message = Label(self.tl, text = 'Sign Up', font = ('Roboto', 55), bg = '#333', fg='lightblue').place(x = 380, y = 90)

#       Variáveis para o utilizador inserir o email//cria input e entry
        self.email = StringVar()
        self.email.set('')
        self.email_label = Label(self.tl, text = 'Email:', font = ('Roboto', 12), bg = '#333', fg='#fff').place(x = 340, y = 220)
        self.email_entry = Entry(self.tl, width = 25, font = ('Roboto', 12), textvariable = self.email).place(x = 400, y = 220)

#       Variáveis para o utilizador inserir o username// cria input e entry
        self.username = StringVar() #   Variável do username que o utilizador inserir (mais tarde para criar conta)
        self.username.set('')
        self.username_label = Label(self.tl, text = 'Username: ', font = ('Roboto', 12), bg = '#333', fg='#fff').place(x = 307, y = 270)
        self.username_entry = Entry(self.tl, width = 25, font = ('Roboto', 12), textvariable = self.username).place(x = 400, y = 270)

#       Variáveis para o utilizador inserir a password// cria input e entry
        self.password = StringVar()
        self.password.set('')
        self.password_label = Label(self.tl, text = 'Password:', font = ('Roboto', 12), bg = '#333', fg='#fff').place(x = 307, y = 320)
        self.password_entry = Entry(self.tl, width = 25, font = ('Roboto', 12), textvariable = self.password, show ='*').place( x = 400, y = 320)

#       Variáveis para o utilizador confirmar a password// cria input e entry
        self.confirm_password = StringVar()
        self.confirm_password.set('')
        self.confirm_password_label = Label(self.tl, text = 'Confirmar Password:', font = ('Roboto', 12), bg = '#333', fg='#fff').place(x = 230, y = 370)
        self.confirm_password_entry = Entry(self.tl, width = 25, font = ('Roboto', 12), textvariable = self.confirm_password, show ='*').place( x = 400, y = 370)

#       Botão para criar conta
        self.create_account_button = Button(self.tl, text = 'Create Account', width=18, font = ('Roboto', 16), bg = '#333', fg = 'lightblue', command = self.create_account).place(x = 400, y = 430)

#       Botão para voltar à página principal
        self.go_back_button = Button(self.tl, text = 'Go Back', font = ('Roboto', 16), bg = 'white', fg = '#333', command = self.go_back_sign_up).place(x = 70, y = 510)

    def go_back_sign_up(self):
        """
        Função para quando o utilizador clica no botão 'Go Back', volta á página principal
        """
        self.tl.destroy()
        return

    def create_account(self):
        """
        Esta função junta todas as informações reunidas nos inputs 
        e cria uma conta com essas informações
        """
#       Para ir buscar as variáveis dos inputs
        self.email = self.email.get() 
        self.username = self.username.get()
        self.password = self.password.get()
        self.confirm_password = self.confirm_password.get()


#       Se algum dos inputs não tiver sido preenchido
        if self.email == '' or self.username == '' or self.password == '' or self.confirm_password == '':
#       Cria-se uma messagebox a mostrar um erro!
            messagebox.showerror('Error','You have to fill all the spaces!') #Cria-se uma messagebox a mostrar um erro!
            return #    A função termina


#       Se as passwords que o utilizador inseriu não forem iguais:
        if self.password != self.confirm_password:
#       Cria-se uma messagebox a mostrar um erro!
            messagebox.showerror('Error','The passwords you inserted are not the same! \n Try again!') 
            return #    A função termina
    

#       Se o utilizador inseriu não tiver nenhum '@', não é um email!
        if self.email.find('@') == -1:
#       Se for igual a -1 significa que não encontrou nenhum '@'!
            messagebox.showerror('Error','Insert a valid email!')
            return #    A função termina
    
#       Abre-se o ficheiro onde estão presentes as informações dos utilizadores em modo leitura para verificar se o username que o utilizador inseriu já está presente no ficheiro
      
        f = open(Path('../Projeto_AED/files/users.txt'),'r')
        self.conteudo = f.readlines() # Lê todo o conteudo presente no ficheiro 'users.txt'
        f.close() # Fecha o ficheiro

        for linhas in self.conteudo:
            """
            Ciclo for que percorre TODAS as linhas presentes na variavel 'conteudo' onde foi extraído todas as informações guardadas no ficheiro 'users.txt'
            """
            self.email_repetido = linhas[:linhas.find(';')]#Esta variável serve para buscar o user em cada linha para depois verificar se combina com o user que o utilizador inseriu
            if self.email == self.email_repetido:
#           Se for igual, mostra uma messagebox com um erro
                messagebox.showinfo('Try again!','The username you put is already in use! Try another one!') 
                return #    A função termina
            self.user_repetido = linhas[linhas.find(';') + 1:linhas.rfind(';')] #Esta variável serve para buscar o email em cada linha para depois verificar se combina com o user que o utilizador inseriu
            if self.username == self.user_repetido:
#           Se for igual, mostra uma messagebox com um erro
                messagebox.showinfo('Try again!','The email you put has an account associated to it already!') 
                return #    A função termina
        
        #   Se nem o username e nem o username que o utilizador inseriu não estiverem no ficheiro, pode-se assim criar uma conta nova com as informações que o utilizador inseriu
        self.conteudo = self.email + ';' + self.username + ';' + self.password #A variável conteudo guarda o username, o email, e a password inseridos para depois inserir no ficheiro 

#       Abre o ficheiro 'utilizadores.txt' em modo append
        f = open('./files/users.txt','a')
        f.write(self.conteudo + '\n') #  Escreve o que está guardado na variável conteudo 
        f.close() # Fecha o ficheiro

#       E mostra-se uma messagebox onde informa o utilizador que a conta foi criada com sucesso!! :DD
        messagebox.showinfo('Done!','You have sucessfully created an account in myPhotos! \n Login to start using the app! :)')
        self.go_back_sign_up()

#       Criar folder no momento de criar conta para armazenar os albums de fotografias desse user
        os.chdir('users_photoalbums')
        os.mkdir(self.username)

#----------------------------------LOGIN-----------------------------------------------------------

class Login():
    def __init__(self, window):
#       Configurações da janela nova
        self.tl = Toplevel(window)
        self.tl.geometry('1000x600+100-100') #Altera largura e altura da janela e posiciona a janela +/- no centro do ecrã
        self.tl.title('myPhotos')
        self.tl.resizable(0,0) #Para não se poder redimensionar a janela (para os widgets não saírem do sítio)

        self.window = window

#       Cria frame para o login
        self.login_frame = Frame(self.tl, width = 1000, height = 600, bg = '#333')
        self.login_frame.place(x = 0, y = 0)

#       Titulo da página
        self.login_message = Label(self.tl, text = 'Login', font = ('Roboto', 55), bg = '#333333', fg='lightblue').place(x = 400, y = 150)

#       Variável que guarda a informação inserida no entry do username \\ Entry e Label
        self.username = StringVar() 
        self.username.set('')
        self.username_label = Label(self.tl, text = 'Username:', font = ('Roboto', 12), bg = '#333333', fg='#fff').place(x = 290, y = 300)
        self.username_entry = Entry(self.tl, width = 25, font = ('Roboto', 12), textvariable = self.username).place(x = 380, y = 300)
    
#       Variável que guarda a informação inserida na entry da password \\ Entry e Label
        self.password = StringVar()
        self.password.set('')
        self.password_label = Label(self.tl, text = 'Password:', font = ('Roboto', 12), bg = '#333333', fg='#fff').place(x = 290, y = 350)
        self.password_entry = Entry(self.tl, width = 25, font = ('Roboto', 12), textvariable = self.password, show ='*').place( x = 380, y = 350)

#       Botão para criar conta
        self.login_button = Button(self.tl, text = 'Login', width=7, font = ('Roboto', 16), bg = '#333', fg = 'lightblue', command = self.login).place(x = 445, y = 400)    

#       Botão para voltar à página principal
        self.go_back_button = Button(self.tl, text = 'Go Back', font = ('Roboto', 16), bg = 'white', fg = '#333', command = self.go_back_login).place(x = 70, y = 510)
 

    def go_back_login(self):
        """
        Função para quando o utilizador clica no botão 'Go Back', a janela volta á página principal
    """
        self.tl.destroy() # Destroi a janela TopLevel (janela atual)
        return


    def login(self):
        """
        Esta função junta as informações inseridas na frame de login \n
        Verifica se o username e password que o utilizador inseriu estão guardadas e corretas! \n
        Se não tiver, informa o utilizador o que está errado e/ou em falta
        """
#       Vai buscar o que foi inserido nas entries do Username e Password
        self.username = self.username.get()
        self.password = self.password.get() 
        admin = False

#       Se o utilizador não tiver inserido algum ou nenhum dos campos, mostra uma messagebox com erro
        if self.username == '' or self.password == '':
            messagebox.showerror('Erro','You have to fill all the spaces!')
            return

#       Abre-se o ficheiro 'users.txt' em modo leitura
        f = open(Path('../Projeto_AED/files/users.txt'),'r')
        self.conteudo = f.readlines() # A variável 'conteudo' vai buscar toda a informação escrita no ficheiro
        f.close() # Fechar o ficheiro

        for linhas in self.conteudo:
            """
            Ciclo for que percorre TODAS as linhas de informação presentes na variável conteudo
            """
#           ADMINS
            if self.username == 'sandra' and self.password == '123' or self.username =='nuno' and self.password == '456' or self.username == 'ken' and self.password == '789':
                admin = True
                messagebox.showinfo('Sucess!','Welcome admin! :)')
                self.tl.destroy()
                Main_App(self.window, self.username, admin)
                return

            self.verificar_username = linhas[linhas.find(';') + 1:linhas.rfind(';')] #Esta variável vai buscar o username presente em cada linha na variável 'conteudo'
            self.verificar_pass = linhas[(linhas.rfind(';') + 1):-1] #Esta variável vai buscar a password presente em cada linha na variável 'conteudo'

            #Se o username E password estiverem corretas, mostra-se uma messagebox a informar o utilizador que foi feito login com sucesso!
            if self.username == self.verificar_username and self.password == self.verificar_pass:
                messagebox.showinfo('Done!','You have sucessfully loged into the myPhotos! :)\n ')
                self.tl.destroy()
                Main_App(self.window, self.username, admin)
                return
        
#       Se depois de ter percorrido a variável 'conteudo' toda e não ter-se encontrado as informações da conta:
#       Mostra-se uma messagebox de erro a informar o utilizador o ocorrido!
        messagebox.showerror('Error','The data you inserted in incorrect, try again!')
