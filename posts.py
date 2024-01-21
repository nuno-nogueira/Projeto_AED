from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter
from pathlib import Path #pathlib is a module in the Python standard library that provides an object-oriented interface for working with filesystem paths. The Path class in pathlib represents a filesystem path and comes with various methods for file and directory manipulation.
from tkcalendar import DateEntry # Inserir no terminal: pip install tkcalendar 
import shutil # Módulo para passar as imagens de uma diretoria qualquer para a pasta dos posts
import os
import datetime


#       ----- Abrir um Post ao clicar no meu álbum de fotos ---------- 
class Posts():
    def __init__(self, f_my_album, image_path, image, username):
        ''' 
        Cada Post abre um TopLevel()
        '''
        self.username = username
        self.tl_my_post= Toplevel(f_my_album)
        self.tl_my_post.geometry('900x600+100-100') 
        self.tl_my_post.title('MyPhotos')
        self.tl_my_post.resizable(0,0) 
        self.tl_my_post.configure(bg = 'lightgrey')

#       Canvas com a Imagem do Post
        canvas = Canvas(self.tl_my_post, width=450, height=350)
        canvas.place(x=20,y=20)
            
#       Redimensionar usando o método zoom
        canvas.create_image(225, 175, anchor=CENTER, image=image)

#       Garantir que não seja coletada pelo garbage collector
        canvas.image = image

        # -----------DAR GOSTOS E FAVORITOS --------
#       Para voltar uma pasta atras para depois encontrar o ficheiro .txt
        path = os.path.dirname(image_path)
        files = []
        for  i in os.listdir(path): 
#       Para encontrar o ficheiro .txt!!
            if i.find('.txt') != -1:
                if i == 'comments.txt':
                    comments_file = os.path.join(path, i)
                else:
                    post_name = os.path.join(path, i)

#       Para aparecer as informações do post (nome, descrição, data)
        f = open(post_name, 'r')
        content = [line.strip('\n') for line in f.readlines()] # Para remover line breaks de cada item na lista
        f.close()
        who_posted = content[0]
        post_name = content[1]
        post_date = content[2]
        post_description = content[3]
        categories_chosen = content[4:]

#       Botão para dar gosto // Remover gosto
        self.like_btn = Button(self.tl_my_post, text = 'Like', width = 8, bg = '#E04F5F', bd = '1', fg = 'black', font = ('Roboto', 12), command = self.like_and_dislike)
        self.like_btn.place(x = 360, y = 370)

        self.likes = Label(self.tl_my_post, text = 0, fg = '#E04F5F', font = ('Roboto', 14)).place(x = 445, y = 370)

#       Botão para adicionar // Remover dos favoritos
        self.favorite_btn = Button(self.tl_my_post, text = 'Add To Favorites', width = 20, bg = '#FFCB2F', bd = '1', fg = 'black', font = ('Roboto', 12), command = self.add_favorites)
        self.favorite_btn.place(x = 150, y = 370)

#       ----------- Nome do post / descrição / quando foi postado
        self.post_name_lbl = Label(self.tl_my_post, text= post_name, font = ('Roboto', 18), bg = '#F0F0F0')
        self.post_name_lbl.place(x = 20, y = 410)
            
        self.post_date_lbl = Label(self.tl_my_post, text= "Posted by: "+ who_posted + '; ' + post_date, font = ('Roboto', 8),  bg = '#F0F0F0')
        self.post_date_lbl.place( x = 20, y = 450)
            
        self.post_description_lbl = Label(self.tl_my_post, text = post_description, font = ('Roboto', 10), bg = '#F0F0F0')
        self.post_description_lbl.place( x = 20, y = 465)
        
#       ------------------- Comentários --------------------------
        self.comments_lbl = Label(self.tl_my_post, text = 'Comments', font = ('Roboto', 22), bg = 'lightgrey').place(x = 500, y = 10)
        self.comments_frame = Frame(self.tl_my_post, width = 380, height = 1000, relief = 'sunken', bd = '2', bg = "#F0F0F0")
        self.comments_frame.place(x = 500, y = 70)

        self.add_comment = Text(self.comments_frame, width = 40, height = 4, font = ('Roboto', 8))
        self.add_comment.place(x = 10, y = 5)

        self.add_comment_btn = Button(self.comments_frame, text = 'Add Comment', relief = 'raised', bg = 'lightgrey', command = lambda: self.create_comment(comments_file))
        self.add_comment_btn.place(x = 255, y = 35)
        self.chars_warning = Label(self.comments_frame, text = '', font = ('Roboto', 10), bg = '#F0F0F0')
        self.chars_warning.place(x = 10, y = 65)
        self.update_comments(comments_file)

#       ------ Botão para modificar o post (imagem, nome, descrição; Exclusivamente para quem criou o post)
        self.edit = Button(self.tl_my_post, text = 'Edit', width = 8, bg = 'lightgrey', font = ('Roboto', 12), command =lambda image=image: Edit(self.tl_my_post, who_posted, post_name, post_description, categories_chosen, path, image))
        if self.username == who_posted:
            self.edit.place( x = 30, y = 550)

        def count_chars_in_comment(chars):
            """
            Função que conta o nº de caracteres inseridos no widgets Text \n
            O limite é de 100 caracteres \n 
            """
            description_str = self.add_comment.get('1.0', 'end-1c') # Exceto o último line break
            line_breaks = description_str.count('\n') # Para as line breaks não contarem como caracteres
            chars_number = len(description_str) - line_breaks
            if (chars_number >= 100):
                self.add_comment.delete('end-2c')
                self.add_comment.configure(bg = '#e35959')
                self.chars_warning.config(text = 'You have exceeded the 100 characters limit!', bg = '#e35959')
            else:
                self.add_comment.configure(bg = 'white')
                self.chars_warning.config(text = '', bg = 'lightgrey')
        self.add_comment.bind('<KeyRelease>', count_chars_in_comment) # Para chamar a função cada vez que o utilizador clica numa tecla

    def like_and_dislike(self):
        if self.like_btn.cget("text") == "Like":
            self.like_btn.config(text = "Dislike")
        else: 
            self.like_btn.config(text = "Like")

    def add_favorites(self):
        if self.favorite_btn.cget("text") == "Add To Favorites":
            self.favorite_btn.config(text = "Remove from Favorites")
        else:
            self.favorite_btn.config(text = "Add To Favorites")
            
    def create_comment(self, comments_file):
        """
        Esta função vai buscar o comentário escrito no Text "self.add_comment" \n
        E também quem escreveu o comentário e guarda essas informações no ficheiro \n
        "comments.txt" que está presente na pasta de cada post.
        """
        comment = self.add_comment.get('1.0', 'end-1c')
        author = self.username
        data = datetime.datetime.now()
        date = data.strftime('%b %d') + ', ' + data.strftime('%H:%M')
        f = open(comments_file, 'a', encoding = 'utf-8')
        f.write(author + ';' + date + ';' + comment + '\n')
        f.close()
        self.update_comments(comments_file)

    def update_comments(self, comments_file):
        """
        Esta função vai buscar ao ficheiro "comments.txt" todos os comentários escritos para este post \n
        De seguida, são mostrados todos os comentários na Frame "self.comments_frame" \n
        E os seus respetivos autores.
        """
#       Meter numa variável a diretoria/pasta dos álbums do user
#       Para voltar uma pasta atras para depois encontrar o ficheiro .txt
        f = open(comments_file, 'r', encoding = 'utf-8')
        comments_list = [line.strip('\n') for line in f.readlines()] # Para remover line breaks de cada item na lista
        f.close()
#       Listar os comentários
        comment_author = [] # Armazenar a lista de quem escreveu os comentários
        dates = [] # Armazenar as horas em que cada comentário foi feito
        comments = [] # Armazenar a lista de comentários escritos
        for line in comments_list: #Por cada folder
            comment_author.append(line[:line.find(';')])
            dates.append(line[line.find(';') + 1:line.rfind(';')])
            comments.append(line[line.rfind(';') + 1:])
#       Variaveis para guardar o posicionamento das Labels e depois incrementar
            x_author = 5 
            y_author = 90
            x_comment = 30
            y_comment = 120
            x_date = 60
            y_date = 92
            for authors in comment_author:
                author_lbl = Label(self.comments_frame, text = authors, bg = '#f0f0f0', font = ('Roboto',12))
                author_lbl.place( x = x_author, y = y_author)
                y_author += 70
            for date in dates:
                date_lbl = Label(self.comments_frame, text = 'Posted on: ' + date, bg = '#f0f0f0', font = ('Roboto', 10))
                date_lbl.place(x = x_date, y = y_date)
                y_date += 70
            for comment in comments:
                comment_lbl = Label(self.comments_frame, text = comment, bg = '#f0f0f0', font = ('Roboto', 8))
                comment_lbl.place(x = x_comment, y = y_comment)
                y_comment += 70
            
class Edit():
    def __init__(self, tl_my_post, who_posted, post_name, post_description, categories_chosen, path, image):
        self.edit_post= Toplevel(tl_my_post)
        self.edit_post.geometry('900x600+100-100') 
        self.edit_post.title('MyPhotos')
        self.edit_post.resizable(0,0) 
        self.edit_post.configure(bg = 'lightgrey')

        self.edit_mode_lbl = Label(self.edit_post, text = 'Edit Mode', font = ('Roboto', 24), bg = 'lightgrey').place(x = 20, y = 5)

        self.edit_image = Button(self.edit_post, text = 'Edit Image', relief = 'raised', bg = '#F0F0F0', font = ('Roboto', 16), command = lambda: self.select_image(image_id, canvas))
        self.edit_image.place(x = 20, y = 410)

#       Canvas com a Imagem do Post
        canvas = Canvas(self.edit_post, width=450, height=350)
        canvas.place(x = 20,y = 50)
            
#       Redimensionar usando o método zoom
        image_id = canvas.create_image(225, 175, anchor=CENTER, image=image)

#       Garantir que não seja coletada pelo garbage collector
        canvas.image = image

        self.name_edit_lbl = Label(self.edit_post, text = 'Edit Name:', font = ('Roboto', 18), bg = 'lightgrey').place(x = 20, y = 460)
        self.name_edit = Entry(self.edit_post, text = who_posted, width = 20, font = ('Roboto', 14))
        self.name_edit.place(x = 20, y = 495)
        
        self.name_edit.delete(0, END) # Apagar o conteudo existente, para depois ser substituido pelo novo
        self.name_edit.insert(0, post_name)

        self.description_edit_lbl = Label(self.edit_post, text = 'Edit Description', font = ('Roboto', 18), bg = 'lightgrey').place(x = 520, y = 60)
        self.description_edit = Text(self.edit_post, width = 40, height = 5, font = ('Roboto', 10))
        self.description_edit.place(x = 520, y = 100)
        self.chars_warning = Label(self.edit_post, text = '', font = ('Roboto', 12), bg = 'lightgrey')
        self.chars_warning.place(x = 520, y = 200)
        self.description_edit.insert(END, post_description)
        def count_chars_in_description(chars):
            """
            Função que conta o nº de caracteres inseridos no widgets Text \n
            O limite é de 150 caracteres \n 
            Se chegar a 130, aparece um aviso, e se chegar a 150, não deixa escrever mais!
            """
            description_str = self.description_edit.get('1.0', 'end-1c') # 'end-1c' é o caracter anterior ao último
            line_breaks = description_str.count('\n') # Para as line breaks não contarem como caracteres
            chars_number = len(description_str) - line_breaks # Subtrair o nº de caracteres pelo nº de line breaks
            if (chars_number >= 150):
                self.description_edit.delete('end-2c')
                self.description_edit.configure(bg = '#e35959')
                self.chars_warning.config(text = 'You have exceeded the 150 characters limit!', bg = '#e35959')
            if (chars_number >= 130 and chars_number < 150):
                self.description_edit.configure(bg = '#d3e359')
                self.chars_warning.config(text = 'You are reaching the 150 characters limit!', bg = '#d3e359')
            if (chars_number < 130):
                self.description_edit.configure(bg = 'white')
                self.chars_warning.config(text = '', bg = 'lightgrey')

        self.description_edit.bind('<KeyRelease>', count_chars_in_description) # Para chamar a função cada vez que o utilizador clica numa tecla


        #   Para ir buscar as categorias existentes ao ficheiro da categorias
        f = open(Path('../Projeto_AED/files/categorias.txt'),'r')
        categories = f.readlines()
        f.close()
        self.category_list = []
        for category in categories:
            category = category.strip('\n') # Remove o '\n' de cada categoria
            self.category_list.append(category)
        
        self.category_lbl = Label(self.edit_post, text = 'Edit Categories', font = ('Roboto', 18), bg = 'lightgrey').place(x = 520, y = 250)
        self.categories = Combobox(self.edit_post, values = self.category_list, width = 15, font = ('Roboto', 14)).place(x = 520, y = 280)

#       Botão que adiciona uma categoria á imagem escolhida
        self.add_category_btn = Button(self.edit_post, text = 'Add category', width = 15, height = 2, bd = 2).place(x = 520, y = 320)

#       Botão que remove uma categoria
        self.remove_category_btn = Button(self.edit_post, text = 'Remove category', width = 15, height = 2, bd = 2).place(x = 520, y = 400)

#       Lista que mostra as categorias escolhidas pelo utilizador
        self.categories_chosen = Listbox(self.edit_post, width = 15, height = 6, font = ('Roboto', 14))
        self.categories_chosen.place(x = 640, y = 320)

        pos = 0 
        for category in categories_chosen:
            self.categories_chosen.insert(pos, category)
            pos += 1

        self.save_changes_btn = Button(self.edit_post, text = 'Save Changes', bg = '#28942a', font = ("Roboto", 16), fg = 'white', bd = 0, command = lambda: self.save_changes(path, who_posted))
        self.save_changes_btn.place(x = 640, y = 500)

        
    def select_image(self, image_id, canvas):
        """
        Esta função permite ao utilizador escolher uma imagem guardada no seu disco, escolhê-la, \n
        para depois postar na app.
        """
    #   Vai buscar o nome do ficheiro que o utilizador inseriu
        self.edit_post.attributes('-topmost', 'false') # Para a janela deixar de ser toplevel (para acessar o explorador de ficheiros)
        self.filename = filedialog.askopenfilename(title = 'Select Image',
                                          filetypes = (("PNG files","*.png"),("GIF files","*.gif"),("JPG files","*.jpg"),("WEBP files","*.webp"),("All Files","*.*")))

        self.image = Image.open(self.filename) # Abrir o ficheiro
        resized_image = self.image.resize((450, 350)) # Mudar tamanho
        self.image = ImageTk.PhotoImage(resized_image) # Abrir imagem com a biblioteca PIL (ImageTk)

        canvas.itemconfig(image_id, image=self.image) # Mudar imagem presente no Canvas
    
        self.edit_post.attributes('-topmost', 'true') # Para a janela voltar a ser toplevel

    # def save_changes(self, path, who_posted):
    #     new_name = self.name_edit.get()
    #     new_description = self.description_edit.get('1.0','end-1c')
    #     new_categories_chosen = self.categories_chosen.get('0', END)
    #     new_filename = self.filename
    #     os.chdir(path)
    #     for file in os.listdir(os.getcwd()):
    #         if file.find('.txt') != -1:
    #             if not file == 'comments.txt':
    #                 f = open(file, 'r',encoding = 'utf-8')
    #                 content = [line.strip('\n') for line in f.readlines()]
    #                 user = content[0]
    #                 date = content[2]
    #                 f.close()
    #                 # os.remove(file)
    #                 new_file = new_name + '.txt'
    #                 f = open(new_file, 'x', encoding = 'utf-8')
    #                 f.write('{0}\n{1}\n{2}\n{3}'.format(who_posted, new_name, date, new_description))
    #                 for category in new_categories_chosen:
    #                     f.write('\n'+str(category))
    #                 f.close()
    #                 os.chdir('..\\')
    #                 os.mkdir(new_name)

                    
                    
            # else:
            #     pass
                # os.remove(file)
