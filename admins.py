from tkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from pathlib import Path #pathlib is a module in the Python standard library that provides an object-oriented interface for working with filesystem paths. The Path class in pathlib represents a filesystem path and comes with various methods for file and directory manipulation.


class admins():
    '''
    Funções dos admins num TopLevel()
    '''

    def __init__(self, tl_admin):
        '''
        Construtor 
        '''
        self.tl_admin = tl_admin

        # --- 1º Ação: Remover um user: --------------------------------------------------------------------------------------
        
        #Title
        self.lbl_check_users= Label(self.tl_admin, text='Remove a User', fg='blue', font=('Roboto, 14'))
        self.lbl_check_users.place(x=50, y=50)

        # Listbox dos users
        self.lbox_users = Listbox(self.tl_admin, height=10, selectmode='single', font=('Roboto', 14))
        self.lbox_users.grid(row=0, column=0, padx=50, pady=100)
        f_users = open('files\\users.txt', 'r', encoding='utf-8')
        lines = f_users.readlines()
        f_users.close()        
        for i in lines:
            self.lbox_users.insert(END, i) #END significa que cada 'i' é inserido no fim do conteúdo da listbox

        #Button para remover user
        self.btn_remove_user = Button(self.tl_admin, relief='raised', text='Remove', bg= '#fff', fg='#333', border = '0', padx=5, pady=5, font=('Roboto', 14), command=self.func_remove_account)
        self.btn_remove_user.place(x = 50, y = 380)
        #Button para guardar remoção
        self.btn_save = Button(self.tl_admin, relief='raised', text='Save', bg= 'green', fg='#fff', border = '0', padx=5, pady=5, font=('Roboto', 14), command=self.func_save_account_deletion)
        self.btn_save.place(x = 210, y = 380)

        # --- 2ª Ação: Adicionar ou Remover uma categoria de fotos: --------------------------------------------------------------
        
        #Title
        self.lbl_categories= Label(self.tl_admin, text='Add/Remove a Category', fg='blue', font=('Roboto, 14'))
        self.lbl_categories.place(x=375, y=50)

        #Listbox das categorias
        self.lbox_categories = Listbox(self.tl_admin, height=10, selectmode='single', font=('Roboto', 14))
        self.lbox_categories.grid(row=0, column=1, padx=50, pady=100)
        f_categories = open('files\\categorias.txt', 'r', encoding='utf-8')
        lines_categories = f_categories.readlines()
        f_categories.close()        
        for line in lines_categories:
            self.lbox_categories.insert(END, line) #END significa que cada line é inserida no fim do conteúdo da listbox

        #Entry para adicionar nova categoria na Listbox
        self.new_category= StringVar()
        self.entry_new_category= Entry(self.tl_admin, width=16, textvariable=self.new_category)
        self.entry_new_category.place(x = 375, y = 380)
        #Buttons para adicionar e remover da Listbox, e guardar em ficheiro
        self.btn_add_category = Button(self.tl_admin, text="Add", bg= '#ccc', fg='white', border = '0', padx=5, pady=5, font=('Roboto', 14), command=lambda: self.func_add_remove_category(1))
        self.btn_add_category.place(x = 375, y = 410)
        self.btn_remove_category = Button(self.tl_admin, text="Remove", bg= '#ccc', fg='white', border = '0', padx=5, pady=5, font=('Roboto', 14), command=lambda: self.func_add_remove_category(2))
        self.btn_remove_category.place(x = 375, y = 460)
        self.btn_save_category = Button(self.tl_admin, text="Save", bg= 'green', fg='white', border = '0', padx=5, pady=5, font=('Roboto', 14), command=lambda: self.func_add_remove_category(3))
        self.btn_save_category.place(x = 375, y = 510)

        # --- 3ª Ação: Gerir Notificações: -----------------------------------------------------------------------------------------
        
        #Title
        self.lbl_manage_notif= Label(self.tl_admin, text='Manage Notifications', fg='blue', font=('Roboto, 16'))
        self.lbl_manage_notif.place(x=720, y=50)

        #LabelFrame para conter os radiobuttons
        self.lblframe_notif= LabelFrame(self.tl_admin, text='Type of Notifications', width=200, height=300, font=('Roboto, 10'), relief='sunken', bd=2)
        self.lblframe_notif.place(x=720, y=100)
        notification= StringVar()
        cb1= Checkbutton(self.lblframe_notif, text='Content of the day', font=('Roboto, 10'), variable=notification)
        cb1.place(x=10,y=10)
    
    # --- FUNÇÕES ---------------------
    def func_remove_account(self):

        f = open  (Path('')/'Projeto_AED'/'files'/'users.txt', 'r')
        lines = f.readlines()        
        self.lbox_users= Listbox(self.tl_admin, height=10, selectmode='single', font=('Roboto', 14))
        for line in lines:
            self.lbox_users.insert(END, line) #END significa que cada line é inserida no fim do conteúdo da listbox
            self.lbox_users.place(x = 30, y = 240)

   
    def func_save_account_deletion(self):
        """
        Guarda a remoção de uma conta no ficheiro ao carregar no botão
        """
        f = open('..\\Projeto_AED\\files\\users.txt', "w", encoding="utf-8")
        content = self.lbox_users.size() #conta nº de contas na ListBox
        for i in range(content): #iterar contas
            account = self.lbox_users.get(i) #obter cada uma das contas da ListBox 
            if account.find("\n") == -1:
                account = account + "\n"
            f.write(account)    
        f.close()
        messagebox.showinfo('Success!', 'The user was deleted.')

    def func_add_remove_category(self, button_number):
        '''
        Permite ao admin adicionar ou remover uma categoria da Listbox, e guardar alterações em ficheiro
        '''
        self.button_number=button_number #Error:'admins' object has no attribute 'button_number'
        #Ao clicar no Button 'Add':
        if self.button_number == 1: 
            self.lbox_categories.insert('end', self.new_category.get()) 
            self.new_category.set('') 
        #Ao clicar no Button 'Remove':
        elif self.button_number == 2: 
            self.lbox_categories.delete(self.lbox_categories.curselection())
        #Ao clicar no Button 'Save':
        elif self.button_number == 3: 
            self.new_categories = open('files\\categorias.txt', "w", encoding="utf-8")
            content = self.lbox_categories.size() # conta nº de categorias na ListBox
            for i in range(content): #iterar categorias
                self.category = self.lbox_categories.get(i) #obter cada uma das categorias
                if self.category.find("\n") == -1:
                    self.category = self.category + "\n"
                self.new_categories.write(self.category) #guarda em ficheiro
             



