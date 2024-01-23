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
        self.comments_frame = Frame(self.f_my_album_comments, width=200, height=540)
        self.comments_frame.place(x=10, y=10)

        # Label Title
        self.comments_lbl = Label(self.f_my_album_comments, text='Comments', font=('Roboto', 22), bg='#fff')
        self.comments_lbl.place(x=0, y=0)
        
        # Text
        self.add_comment = Text(self.f_my_album_comments, width=40, height=4, font=('Roboto', 8))
        self.add_comment.place(x=0, y=30)

        # Button
        self.add_comment_btn = Button(self.f_my_album_comments, text='Add Comment', relief='raised', bg='lightgrey',
                                      command=lambda: self.create_comment(path_album_comments_file, self.username))
        self.add_comment_btn.place(x=0, y=140)

        self.chars_warning = Label(self.f_my_album_comments, text='', font=('Roboto', 10), bg='#fff', relief='sunken')
        self.chars_warning.place(x=0, y=180)

        self.update_comments(path_album_comments_file)
        print('hi')
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
            for widget in self.comments_frame.winfo_children():
                widget.destroy()

            f = open(path_album_comments_file, 'r', encoding='utf-8')
            comments_list = [line.strip('\n') for line in f.readlines()]
            f.close()

            y_position = 300
            for line in comments_list:
                author, date, comment = line.split(';')
                
                author_lbl = Label(self.comments_frame, text=author, bg='#f0f0f0', font=('Roboto', 12))
                author_lbl.place(x=5, y=y_position)

                date_lbl = Label(self.comments_frame, text='Posted on: ' + date, bg='#f0f0f0', font=('Roboto', 10))
                date_lbl.place(x=60, y=y_position)

                comment_lbl = Label(self.comments_frame, text=comment, bg='#f0f0f0', font=('Roboto', 8))
                comment_lbl.place(x=30, y=y_position)

                y_position += 70

