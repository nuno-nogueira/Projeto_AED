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

        # Label mostra o número total de albúns criado pelo utilizador
        self.lbl_total_albums = Label(self.tl_dashboard, text="Total Number of Albums: " + number_of_albums, font = ('Roboto', 12))
        self.lbl_total_albums.place(x=10,y=10)

        # Label que mostra o número total de posts feito pelo utilizador
        self.lbl_total_posts = Label(self.tl_dashboard, text="Number of Posts: " + number_of_posts, font = ('Roboto', 12))
        self.lbl_total_posts.place(x=10,y=40)
        
        # Label que mostra o post com mais comentários
        self.lbl_number_comments_posts= Label(self.tl_dashboard, text='', font = ('Roboto', 12))
        self.lbl_number_comments_posts.place(x=10, y=70)

        # ------------ Número de Posts por Categoria ------------------
    
        lbl_pick_categ = Label(self.tl_dashboard, text='Number of Posts by Category', font = ('Roboto', 10))
        lbl_pick_categ.place(x=10,y=100)

        #Listbox das categorias
        self.lbox_categ = Listbox(self.tl_dashboard, height=5, selectmode='single', font=('Roboto', 10))
        self.lbox_categ.place(x=10,y=130)

        # Inserir as categorias na Listbox
        f_categ = open('files/categorias.txt', 'r', encoding='utf-8')
        lines = f_categ.readlines()
        f_categ.close()        
        for i in lines:
            self.lbox_categ.insert(END, i) #END significa que cada 'i' é inserido no fim do conteúdo da listbox

        #Button selecionar categoria
        self.btn_pick_categ = Button(self.tl_dashboard, text='Choose category', font = ('Roboto', 10),
                                      command=lambda: self.func_posts_by_categ(self.username))
        self.btn_pick_categ.place(x = 10, y = 210)
        #Label mostrar número de Posts por Categoria
        self.lbl_number_posts_by_categ= Label(self.tl_dashboard, text='')
        self.lbl_number_posts_by_categ.place(x=10, y=235)
        
        # ------------ Número de Comentários por Álbum e por Post ------------------
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
        self.lbox_albums= Listbox(self.tl_dashboard, height=5, selectmode='single', font=('Roboto', 10))
        self.lbox_albums.place(x=300,y=130)

        #Inserir Álbums na Listbox
        for folder in folders:
            self.lbox_albums.insert(END, folder)

        #Button selecionar Álbum
        self.btn_pick_album = Button(self.tl_dashboard, text='Number of comments on this Album', font = ('Roboto', 10),
                                    command=lambda: self.func_comments_albums(self.username))
        self.btn_pick_album.place(x = 300, y = 210)


        # Label mostrar número de Comentários por Álbum  
        self.lbl_number_comments_albums= Label(self.tl_dashboard, text='', font = ('Roboto', 10))
        self.lbl_number_comments_albums.place(x=300, y=250)

        self.func_comments_posts(self.username)

    # - Função Post com mais comentários

    def func_comments_posts(self, username):
            '''
            Esta função corre ao abrir se o TopLevel da Dashboard \n
            Verifica TODOS os posts no user, e encontra o que tem mais comentários, e o seu respetivo nome
            '''
            number_of_comments = 0
            user_path = os.path.join('users_photoalbums',username) 
            for dirs in os.listdir(user_path): # Percorre todas as pastas/ficheiros de cada album
                dirs = os.path.join(user_path, dirs)
                for files in os.listdir(dirs): # Percorre todas as pastas/ficheiros de post
                    files = os.path.join(dirs, files)
                    if os.path.isdir(files): #Se a variavel 'files' for uma pasta:
                        for file in os.listdir(files): # Percorre por todos os ficheiros dentro da pasta de cada post
                            if file == 'comments.txt': # Quando encontrar o ficheiro 'comments.txt':
                                file = os.path.join(files, file) 
                                f = open(file, 'r', encoding= 'utf-8')
                                lines = f.readlines() # Conta o nº de linhas, e assim, o nº de comentários
                                f.close()
                                if len(lines) > number_of_comments: # Se o atual ficheiro tiver mais comentários que o atual ficheiro com mais comentários
                                    number_of_comments = len(lines) # Esse ficheiro passa a ser o novo ficheiro com mais comentários
                                    for file in os.listdir(files):  
                                        # Para encontrar o nome do post (que possa ter sido editado)
                                        if file.endswith('.txt') and file != 'comments.txt':
                                            post_name = file
                                            post_name = post_name.replace('.txt','')



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
        
    def func_comments_albums(self, username):
        '''
        Escolher um Álbum para ver o número de comments p/ album \n
        Dependendo do Álbum que o utilizador seleciona
        '''
        if  not self.lbox_albums.curselection(): # Verificar se o utilizador selecionou uma opção
            messagebox.showinfo('Error','You need to select an album first!', parent = self.tl_dashboard)
            return
        
        selected_album = self.lbox_albums.get(self.lbox_albums.curselection())  #selecionar a linha, dá-me a posição index
       
        # Path para o ficheiro 'comments.txt' do album selecionado
        file_comments_path = os.path.join('users_photoalbums', username, selected_album, 'comments.txt') #não é necessário concatenação, nem \\
        
        file_comments = open(file_comments_path, 'r')
        read_file = file_comments.readlines()
        file_comments.close()

        str_len = len(read_file)
        str_len = str(str_len)
        self.lbl_number_comments_albums.config(text= str_len) # Inserir na Label 'lbl_number_comments_albums'

   
    
    
   