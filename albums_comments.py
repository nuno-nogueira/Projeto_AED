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
class Albums_Comments():
    def __init__(self, f_my_album_comments, album_folder, username):
        ''' 
        Comentários para quando um user abre um Álbum
        '''
        self.username=username
        # Path do comments.txt desse Album
        path_album_comments_file = os.path.join('.\\users_photoalbums\\', username, album_folder, 'comments.txt')
        self.f_my_album_comments = f_my_album_comments
        # Frame para inserir conteúdo
        self.comments_frame = Frame(self.f_my_album_comments, width=250, height=540, bg = '#f0f0f0')
        self.comments_frame.place(x=0, y=0)

        # Label Title
        self.comments_lbl = Label(self.f_my_album_comments, text='Comments', font=('Roboto', 22), bg='#f0f0f0')
        self.comments_lbl.place(x=10, y=5)
        
        # Text
        self.add_comment = Text(self.f_my_album_comments, width=34, height=5, font=('Roboto', 8), bd = '2')
        self.add_comment.place(x=0, y=50)

        # Button
        self.add_comment_btn = Button(self.f_my_album_comments, text='Add Comment', relief='raised', bg='lightgrey',
                                      command=lambda: self.create_comment(path_album_comments_file, self.username))
        self.add_comment_btn.place(x=120, y=120)

        self.chars_warning = Label(self.f_my_album_comments, text='', font=('Roboto', 8), bg='#f0f0f0', bd = 0)
        self.chars_warning.place(x=0, y=150)

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
                self.chars_warning.config(text = '', bg = '#F0F0F0')
        self.add_comment.bind('<KeyRelease>', count_chars_in_comment) # Para chamar a função cada vez que o utilizador clica numa tecla

        self.update_comments(path_album_comments_file)
#      
    def create_comment(self, path_album_comments_file, username):
        """
        Esta função vai buscar o comentário escrito no Text "self.add_comment" \n
        E também quem escreveu o comentário e guarda essas informações no ficheiro \n
        "comments.txt" que está presente na pasta de cada post.
        """
        self.username=username
        comment = self.add_comment.get('1.0', 'end-1c')
        author = self.username
        data = datetime.datetime.now()
        date = data.strftime('%b %d') + ', ' + data.strftime('%H:%M')
        f = open(path_album_comments_file, 'a', encoding = 'utf-8')
        f.write(author + ';' + date + ';' + comment + '\n')
        f.close()
        self.update_comments(path_album_comments_file)

    
    def update_comments(self, path_album_comments_file):
        # Clear existing comments
            f = open(path_album_comments_file, 'r', encoding='utf-8')
            comments_list = [line.strip('\n') for line in f.readlines()] # Para remover line breaks de cada item na lista
            f.close()
            comment = [line.strip(';') for line in comments_list]

            
            y_author = 170
            y_date = 172
            y_comment = 200
            for line in comments_list:
                author, date, comment = line.split(';')
                
                author_lbl = Label(self.comments_frame, text=author, bg='#f0f0f0', font=('Roboto', 12))
                author_lbl.place(x=5, y=y_author)
                y_author += 100

                date_lbl = Label(self.comments_frame, text='Posted on: ' + date, bg='#f0f0f0', font=('Roboto', 10))
                date_lbl.place(x=60, y=y_date)
                y_date += 100

                comment_lbl = Text(self.comments_frame, width = 35, height = 4,  bg='#f0f0f0', font=('Roboto', 8), bd = 0)
                comment_lbl.place(x=10, y= y_comment)
                comment_lbl.insert(END, comment)
                comment_lbl.config(state = 'disabled')
                y_comment += 100

