from tkinter import *
from tkinter import filedialog
import os

class dashboard():
    def __init__(self, tl_dashboard, username):
        '''
        User pode consultar na Dashboard:
        - Número total de Posts
        - Número de Posts por categoria
        '''
        self.tl_dashboard = tl_dashboard
        self.username=username

        # self.lbox_posts= Listbox(self.tl_dashboard, height=10, selectmode='single', font=('Roboto', 16))
        # self.lbox_posts.place(x=80,y=50)

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
        self.btn_pick_album = Button(self.tl_dashboard, text='Choose this Álbum',
                                    command=lambda: self.func_comments_albums(self.username))
        self.btn_pick_album.place(x = 500, y = 150)
        #Label mostrar número de Comentários por Álbum
        self.lbl_number_comments_albums= Label(self.tl_dashboard, text=('0'))
        self.lbl_number_comments_albums.place(x=500, y=200)

        # --- Por Post:

        #Button selecionar Álbum
        self.btn_pick_album = Button(self.tl_dashboard, text='Choose this Álbum',
                                    command=lambda: self.func_comments_albums(self.username))
        self.btn_pick_album.place(x = 500, y = 150)
        #Label mostrar número de Comentários por Álbum
        self.lbl_number_comments_albums= Label(self.tl_dashboard, text=('0'))
        self.lbl_number_comments_albums.place(x=500, y=200)


        # ------------ Número de Comentários por Post ------------------

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
        self.btn_pick_album = Button(self.tl_dashboard, text='Choose this Álbum',
                                    command=lambda: self.func_comments_albums(self.username))
        self.btn_pick_album.place(x = 500, y = 150)
        #Label mostrar número de Comentários por Álbum
        self.lbl_number_comments_albums= Label(self.tl_dashboard, text=('0'))
        self.lbl_number_comments_albums.place(x=500, y=200)

        # post_count = 0
        # lbl_post_count = Label(self.tl_dashboard, text=f"Number of Posts: {post_count}") #''f'' serve para concatenar a string com a variável
        # lbl_post_count.place(x=30,y=50)
        
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
            if line_parts[0] == username and line_parts[1] == str(selected_category.strip()):
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
    
    
# # Example usage:
# file_path = 'path/to/your/file.txt'
# lines_count = count_lines(file_path)
# print(f"The number of lines in '{file_path}' is: {lines_count}")

# # Example usage:
# file_path = 'path/to/your/file.txt'
# lines_count = count_lines(file_path)
# print(f"The number of lines in '{file_path}' is: {lines_count}")
        
        

    # def func_count_post():
    #     '''
    #     Contar o número de Posts
    #     '''
    #     post_count += 1
    #     lbl_count_post.config(text=f"Views: {post_count}") #atualiza a label


#---------------------------------------nr visualizacoes--------------------
        
    # # def func_count_view_post(self, post_views_count, lbl_post_views):
    # #     '''
    # #     Sempre que um user abre um post conta mais uma visualização
    # #     '''

    # #     post_views_count += 1
    # #     lbl_post_views.config(text=f"Views: {post_views_count}") #atualiza a label
        
    # def increment_views(self, post_path):
    #         views_file_path = os.path.join(post_path, "/views.txt")
    #         # Read the current number of views
    #         try:
    #             with open(views_file_path, "r") as views_file:
    #                 current_views = int(views_file.read())
    #         except FileNotFoundError:
    #             # If the file doesn't exist, initialize views to 0
    #             current_views = 0

    #         # Increment the number of views
    #         current_views += 1

    #         # Write the updated number of views back to the file
    #         with open(views_file_path, "w") as views_file:
    #             views_file.write(str(current_views))

    #         return current_views

    # def on_post_button_click(self, img, image_path, username, post_path):
    #         # Increment views and get the updated count
    #         views_count = self.increment_views(post_path)

    #         # Perform other actions as needed (e.g., open the post, display views count, etc.)
    #         print(f"Post opened by {username}. Views: {views_count}")
    #         # Add your code to handle post opening here

    #         # Now you can use the views_count as needed in your application.

    # def increment_views(self, post_path):
    #         views_file_path = os.path.join(post_path, "views.txt")
    #         print(views_file_path)
            
    #         # Read the current number of views
    #         try:
    #             file_read_views = open(views_file_path, 'r')  # Use 'r' mode for reading
    #             content = file_read_views.read().strip()  # Read and remove leading/trailing whitespaces
    #             file_read_views.close()

    #             # Check if the content is not empty before converting to int
    #             if content:
    #                 current_views = int(content)
    #             else:
    #                 current_views = 0
    #         except FileNotFoundError:
    #             # If the file doesn't exist, initialize views to 0
    #             current_views = 0

    #             # Open the file in 'w+' mode to allow both reading and writing
    #             file_write_views = open(views_file_path, 'w+')
    #             file_write_views.write(str(current_views))
    #             file_write_views.close()

    #         # Increment the number of views
    #         current_views += 1
    #         print(current_views)

    #         # Write the updated number of views back to the file
    #         file_write_views = open(views_file_path, 'w')
    #         file_write_views.write(str(current_views))
    #         file_write_views.close()

    #         return current_views
    # def on_post_button_click(self, img, image_path, username, post_path):
    #             # Increment views and get the updated count
    #             views_count = self.increment_views(post_path)

    #             # Perform other actions as needed (e.g., open the post, display views count, etc.)
    #             print(f"Post opened by {username}. Views: {views_count}")
    #             # Add your code to handle post opening here

    #             # Now you can use the views_count as needed in your application.
        
#---------------------------------------nr visualizacoes-------------------- 
    

