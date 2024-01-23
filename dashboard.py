from tkinter import *
from tkinter import filedialog
import os

class dashboard():
    def __init__(self, tl_dashboard, username):
        '''
        User pode consultar na Dashboard:
        - Número total de Posts
        - Número de Posts por categoria
        - Número de Comentários por Álbum OU por Post
        '''
        self.tl_dashboard = tl_dashboard
        self.username=username
        
        # ------------ Número Total de Posts --------------------------
        
        btn_total_posts = Button(self.tl_dashboard, text="See Total Number of Posts", 
                                 command= lambda: self.func_count_total_posts(self.username))
        btn_total_posts.place(x=200,y=20)
        self.lbl_total_posts = Label(self.tl_dashboard, text="Number of Posts: 0")
        self.lbl_total_posts.place(x=200,y=60)
        
        # ------------ Número de Posts por Categoria ------------------
    
        lbl_pick_categ = Label(self.tl_dashboard, text='Number of Posts by Category:')
        lbl_pick_categ.place(x=20,y=20)
        #Listbox das categorias
        self.lbox_categ = Listbox(self.tl_dashboard, height=5, selectmode='single', font=('Roboto', 8))
        self.lbox_categ.place(x=20,y=50)
        f_categ = open('files/categorias.txt', 'r', encoding='utf-8')
        lines = f_categ.readlines()
        f_categ.close()        
        for i in lines:
            self.lbox_categ.insert(END, i) #END significa que cada 'i' é inserido no fim do conteúdo da listbox
        #Button selecionar categoria
        self.btn_pick_categ = Button(self.tl_dashboard, text='Choose this category',
                                      command=lambda: self.func_posts_by_categ(self.username))
        self.btn_pick_categ.place(x = 20, y = 150)
        #Label mostrar número de Posts por Categoria
        self.lbl_number_posts_by_categ= Label(self.tl_dashboard, text=('0'))
        self.lbl_number_posts_by_categ.place(x=20, y=200)
        
        # ------------ Número de Comentários por Álbum OU por Post ------------------
        # --- Por Álbum:
        lbl_pick_album= Label(self.tl_dashboard, text='Pick an Album')
        lbl_pick_album.place
        #Criar um path para a folder do user (que contém os Álbums)
        self.albums_path = os.path.join('.\\users_photoalbums\\', username) #não é necessário concatenação, nem \\
        #Listar os itens dentro da folder do user 
        items_in_user_folder = os.listdir(self.albums_path) 
        #Lista para guardar nomes das folders(Álbums) que estão dentro da folder do user
        folders = []
        for item in items_in_user_folder:#iterar cada item da folder do user
            item_path = os.path.join(self.albums_path, item) #criar path para cada Álbum
            if os.path.isdir(item_path): #e se for uma folder:
                folders.append(item) #vai para a lista
        #Listbox dos Álbums 
        self.lbox_albums= Listbox(self.tl_dashboard, height=5, selectmode='single', font=('Roboto', 8))
        self.lbox_albums.place(x=500,y=50)
        #Inserir Álbums na Listbox
        for folder in folders:
            self.lbox_albums.insert(END, folder)
        #Button selecionar Álbum
        self.btn_pick_album = Button(self.tl_dashboard, text='Number of comments on this Album',
                                    command=lambda: self.func_comments_albums(self.username))
        self.btn_pick_album.place(x = 500, y = 150)
        #Label mostrar número de Comentários por Álbum
        self.lbl_number_comments_albums= Label(self.tl_dashboard, text=('0'))
        self.lbl_number_comments_albums.place(x=500, y=200)


        # # --- Por Post:

        # #Button selecionar Álbum
        # self.btn_pick_album = Button(self.tl_dashboard, text='Number of comments on this Post',
        #                             command=lambda: self.func_comments_albums(self.username))
        # self.btn_pick_album.place(x = 500, y = 150)
        # #Label mostrar número de Comentários por Álbum
        # self.lbl_number_comments_albums= Label(self.tl_dashboard, text=('0'))
        # self.lbl_number_comments_albums.place(x=500, y=200)


        # # ------------ Número de Comentários por Post ------------------

        # lbl_pick_album= Label(self.tl_dashboard, text='Pick an Album')
        # lbl_pick_album.place
        # #Criar um path para a folder do user (que contém os Álbums)
        # self.albums_path = os.path.join('.\\users_photoalbums\\', username) #não é necessário concatenação, nem \\
        # #Listar os itens dentro da folder do user 
        # items_in_user_folder = os.listdir(self.albums_path) 
        # #Lista para guardar nomes das folders(Álbums) que estão dentro da folder do user
        # folders = []
        # for item in items_in_user_folder:#iterar cada item da folder do user
        #     item_path = os.path.join(self.albums_path, item) #criar path para cada Álbum
        #     if os.path.isdir(item_path): #e se for uma folder:
        #         folders.append(item) #vai para a lista
        # #Listbox dos Álbums 
        # self.lbox_albums= Listbox(self.tl_dashboard, height=5, selectmode='single', font=('Roboto', 8))
        # self.lbox_albums.place(x=500,y=50)
        # #Inserir Álbums na Listbox
        # for folder in folders:
        #     self.lbox_albums.insert(END, folder)
        # #Button selecionar Álbum
        # self.btn_pick_album = Button(self.tl_dashboard, text='Number of comments on this Post',
        #                             command=lambda: self.func_comments_albums(self.username))
        # self.btn_pick_album.place(x = 500, y = 150)
        # #Label mostrar número de Comentários por Álbum
        # self.lbl_number_comments_albums= Label(self.tl_dashboard, text=('0'))
        # self.lbl_number_comments_albums.place(x=500, y=200)

    # - Função Número Total de Posts -------------------------------

    def func_count_total_posts(self, username):
            '''
            Número Total de Posts do user
            '''
            file_all_posts = open('files/all-posts.txt', 'r', encoding='utf-8')
            read_file = file_all_posts.readlines()
            file_all_posts.close()

            my_posts = []
            for line in read_file:
                line_parts = line.split(';')
                if line_parts[0] == username:
                    my_posts.append(line)
            str_len = len(my_posts)
            print('str_len')
            self.lbl_total_posts.config(text=f"Number of folders: {str(str_len)}")


    # - Função Número de Posts por Categoria -------------------------------
        
    def func_posts_by_categ(self, username):
        '''
        Escolher uma categoria para ver o número de posts criados
        '''
        selected_categ = self.lbox_categ.curselection()  #selecionar a linha, dá-me a posição index
        selected_category = self.lbox_categ.get(selected_categ[0])  #obter o valor da linha selecionada. [0] é a primeira linha que selecionei no caso de ter selecionado mais

        file_all_posts = open('files/all-posts.txt', 'r', encoding='utf-8')
        read_file = file_all_posts.readlines()
        file_all_posts.close()

        my_categ_posts = []
        for line in read_file:
            line_parts = line.split(';')
            if line_parts[0] == username and line_parts[3] == str(selected_category.strip()):
                my_categ_posts.append(line)
        str_len = len(my_categ_posts)
        self.lbl_number_posts_by_categ.config(text=str(str_len))
    
    # - Função Número de Comentários por Álbum -------------------------------
        
    def func_comments_albums(self, username):
        '''
        Escolher um Álbum para ver o número de comments
        '''
        selected_alb = self.lbox_albums.curselection()  #selecionar a linha, dá-me a posição index
        selected_album = self.lbox_albums.get(selected_alb[0])  #obter o valor da linha selecionada. [0] é a primeira linha que selecionei no caso de ter selecionado mais
            
        file_comments_path = os.path.join('users_photoalbums', username, selected_album.strip(), 'comments.txt') #não é necessário concatenação, nem \\
        
        file_comments = open(file_comments_path, 'r')
        read_file = file_comments.readlines()
        file_comments.close()

        str_len = len(read_file)
        self.lbl_number_comments_albums.config(text=str(str_len))
    
   