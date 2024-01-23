from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
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
        
        number_of_albums = 0
        number_of_posts = 0
        # ------------ Número Total de Posts --------------------------
        #Criar um path para a folder do user (que contém os Álbums)
        self.albums_path = os.path.join('.\\users_photoalbums\\', username) #não é necessário concatenação, nem \\        
        #Lista para guardar nomes das folders(Álbums) que estão dentro da folder do user
        for item in  os.listdir(self.albums_path):#iterar cada item da folder do user
                item_path = os.path.join(self.albums_path, item) #criar path para cada Álbum
                for posts in os.listdir(item_path):
                    posts = os.path.join(item_path, posts)
                    if os.path.isdir(posts): #e se for uma folder:
                        number_of_posts += 1
                number_of_albums += 1

        number_of_albums = str(number_of_albums)
        number_of_posts = str(number_of_posts)

        self.lbl_total_albums = Label(self.tl_dashboard, text="Total Number of Albums:" + number_of_albums, font = ('Roboto', 12))
        self.lbl_total_albums.place(x=10,y=10)

        self.lbl_total_posts = Label(self.tl_dashboard, text="Number of Posts:" + number_of_posts, font = ('Roboto', 12))
        self.lbl_total_posts.place(x=10,y=40)
        
        # ------------ Número de Posts por Categoria ------------------
    
        lbl_pick_categ = Label(self.tl_dashboard, text='Number of Posts by Category', font = ('Roboto', 10))
        lbl_pick_categ.place(x=10,y=100)

        #Listbox das categorias
        self.lbox_categ = Listbox(self.tl_dashboard, height=5, selectmode='single', font=('Roboto', 8))
        self.lbox_categ.place(x=10,y=130)

        # Inserir as categorias na Listbox
        f_categ = open('files/categorias.txt', 'r', encoding='utf-8')
        lines = f_categ.readlines()
        f_categ.close()        
        for i in lines:
            self.lbox_categ.insert(END, i) #END significa que cada 'i' é inserido no fim do conteúdo da listbox

        #Button selecionar categoria
        self.btn_pick_categ = Button(self.tl_dashboard, text='Choose category', font = ('Roboto', 8),
                                      command=lambda: self.func_posts_by_categ(self.username))
        self.btn_pick_categ.place(x = 10, y = 200)
        #Label mostrar número de Posts por Categoria
        self.lbl_number_posts_by_categ= Label(self.tl_dashboard, text='')
        self.lbl_number_posts_by_categ.place(x=10, y=230)
        
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
                                    command=lambda: self.func_comments_posts(self.username))
        self.btn_pick_album.place(x = 500, y = 150)
        #Label mostrar número de Comentários por Álbum
        self.lbl_number_comments_posts= Label(self.tl_dashboard, text='', font = ('Roboto', 8))
        self.lbl_number_comments_posts.place(x=10, y=260)
        self.func_comments_posts(self.username)

    def func_comments_posts(self, username):
            '''
            Escolher um Álbum para ver o número de comments
            '''
            number_of_comments = 0
            user_path = os.path.join('users_photoalbums',username) 
            for dirs in os.listdir(user_path):
                dirs = os.path.join(user_path, dirs)
                for files in os.listdir(dirs):
                    files = os.path.join(dirs, files)
                    if os.path.isdir(files):
                        for file in os.listdir(files):
                            if file == 'comments.txt':
                                file = os.path.join(files, file)
                                f = open(file, 'r', encoding= 'utf-8')
                                lines = f.readlines()
                                f.close()
                                if len(lines) > number_of_comments:
                                    number_of_comments = len(lines)
                                    post_name = os.path.dirname(file)
                                    post_name = os.path.basename(post_name)

            number_of_comments = str(number_of_comments)
            self.lbl_number_comments_posts.config(text='Most commented post: ' + post_name + ' (' + number_of_comments + ' comments' + ')')

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

    # - Função Número de Posts por Categoria -------------------------------
        
    def func_posts_by_categ(self, username):
        '''
        Escolher uma categoria para ver o número de posts criados
        '''
        if self.lbox_categ.curselection():
            selected_categ = self.lbox_categ.get(self.lbox_categ.curselection()).strip() #selecionar a linha, dá-me a posição index
        else:
            messagebox.showinfo('Not Found','You have to select a category first!', parent = self.tl_dashboard)
            return
        file_all_posts = open('files/all-posts.txt', 'r', encoding='utf-8')
        read_file = file_all_posts.readlines()
        file_all_posts.close()
        my_categ_posts = []
        print(selected_categ)
        for line in read_file:
            line_parts = line.split(';')
            print(line_parts[1])
            if line_parts[0] == username  and line_parts[1] == selected_categ:
                print('DAOSJJDIAJSAJDKAHJKLJSKJAD')
                my_categ_posts.append(line)
        str_len = len(my_categ_posts)
        str_len = str(str_len)
        self.lbl_number_posts_by_categ.config(text= 'Number of posts from the category ' + selected_categ + ': ' + str_len)
    
    # - Função Número de Comentários por Álbum -------------------------------
        
    # def func_comments_albums(self, username):
    #     '''
    #     Escolher um Álbum para ver o número de comments
    #     '''
    #     selected_alb = self.lbox_albums.curselection()  #selecionar a linha, dá-me a posição index
    #     selected_album = self.lbox_albums.get(selected_alb[0])  #obter o valor da linha selecionada. [0] é a primeira linha que selecionei no caso de ter selecionado mais
            
    #     file_comments_path = os.path.join('users_photoalbums', username, selected_album.strip(), 'comments.txt') #não é necessário concatenação, nem \\
        
    #     file_comments = open(file_comments_path, 'r')
    #     read_file = file_comments.readlines()
    #     file_comments.close()

    #     str_len = len(read_file)
    #     self.lbl_number_comments_albums.config(text=str(str_len))

   
    
    
   