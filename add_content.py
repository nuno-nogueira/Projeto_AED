from tkinter import *
from search import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.ttk import Combobox
from pathlib import Path #pathlib is a module in the Python standard library that provides an object-oriented interface for working with filesystem paths. The Path class in pathlib represents a filesystem path and comes with various methods for file and directory manipulation.
import os
import datetime
import shutil # Módulo para copiar imagens para poder transferir ficheiros para outras pastas (de)

class Add_Post():
  """
  Esta classe é responsável por tudo relacionado com adicionar um post/fotografia \n
  Todos os widgets da janela "Add Post".
  Todas as funções relacionadas.
  """
  def __init__(self, tl_add_photo, username):
    """
    Permite criar uma window que é um objeto da classe App \n
    Usado para configurar uma janela nova TopLevel
    """
    self.tl_my_post= Toplevel(tl_add_photo)
    self.tl_my_post.geometry('1000x600+100-100') 
    self.tl_my_post.title('MyPhotos')
    self.tl_my_post.resizable(0,0) 
    self.tl_my_post.configure(bg = 'lightgrey')
    self.username = username

#   Icon para voltar á página principal
    icon = Image.open(Path('../Projeto_AED/images/icons/go_back_icon.png')).resize((50, 50))
    icon = ImageTk.PhotoImage(icon)
    self.go_back_btn = Button(self.tl_my_post, image = icon, bd = 0, bg = 'lightgrey', command =  self.go_back)
    self.go_back_btn.image = icon
    self.go_back_btn.place(x = 0, y = 0)

#   Label
    self.add_post_lbl = Label(self.tl_my_post, text = 'Add Post', font = ('Roboto', 28), bg = 'lightgrey').place(x = 100, y = 10)

#   Botão que chama a função "select_image" que é responsável por adicionar a imagem selecionada ao ecrã
    self.add_photo_btn = Button(self.tl_my_post, text = 'Add Image', width = 10, height = 2, bd = 2, command = lambda: self.select_image(image_id, cnv_image)).place(x = 70, y = 310)

#   Criar um Canvas para de seguida adicionar a fotografia selecionada pelo utilizador
    cnv_image = Canvas(self.tl_my_post, width = 400, height = 200)
    cnv_image.place(x = 70, y = 100)

    self.filename = ''
    self.image = ''
    image_id = cnv_image.create_image(200, 100, anchor = CENTER, image = self.image)

#   Label & Entry do nome da fotografia/post
    self.photo_name_lbl = Label(self.tl_my_post, text = 'Name', font = ('Roboto',18), bg = 'lightgrey')
    self.photo_name_lbl.place(x = 70, y = 370)
    self.photo_name = Entry(self.tl_my_post, width = 25, font = ('Roboto', 14))
    self.photo_name.place(x = 70, y = 400)

    user_dir = "../Projeto_AED/users_photoalbums/" + self.username
    self.albums_list = os.listdir(Path(user_dir))
#   Label, Combobox com todos albuns do utilizador e um botão para criar um álbum que leva a outra janela
    self.add_to_album_lbl = Label(self.tl_my_post, text = 'Add to Album:', font = ('Roboto', 18), bg = 'lightgrey').place(x = 70, y = 450)
    self.add_to_album = Combobox(self.tl_my_post, height = 1, width = 15, values = self.albums_list, font = ('Roboto', 14))
    self.add_to_album.place(x = 70, y = 480)

#   Label & Text da descrição da fotografia/post
    self.description_lbl = Label(self.tl_my_post, text = 'Description', font = ('Roboto', 18), bg = "lightgrey").place(x = 600, y = 50)
    self.description = Text(self.tl_my_post, width = 40, height = 6, font = ('Roboto', 10), bd = 2)
    self.description.place(x = 600, y = 100)
    self.chars_warning = Label(self.tl_my_post, text = '', font = ('Roboto', 12), bg = 'lightgrey')
    self.chars_warning.place(x = 600, y = 200)

    def count_chars_in_description(chars):
       """
       Função que conta o nº de caracteres inseridos no widgets Text \n
       O limite é de 150 caracteres \n 
       Se chegar a 130, aparece um aviso, e se chegar a 150, não deixa escrever mais!
       """
       description_str = self.description.get('1.0', 'end-1c') # 'end-1c' é o caracter anterior ao último
       line_breaks = description_str.count('\n') # Para as line breaks não contarem como caracteres
       chars_number = len(description_str) - line_breaks # Subtrair o nº de caracteres pelo nº de line breaks
       if (chars_number >= 150):
          self.description.delete('end-2c')
          self.description.configure(bg = '#e35959')
          self.chars_warning.config(text = 'You have exceeded the 150 characters limit!', bg = '#e35959')
       if (chars_number >= 130 and chars_number < 150):
          self.description.configure(bg = '#d3e359')
          self.chars_warning.config(text = 'You are reaching the 150 characters limit!', bg = '#d3e359')
       if (chars_number < 130):
          self.description.configure(bg = 'white')
          self.chars_warning.config(text = '', bg = 'lightgrey')

    self.description.bind('<KeyRelease>', count_chars_in_description) # Para chamar a função cada vez que o utilizador clica numa tecla
    

#   Para ir buscar as categorias existentes ao ficheiro da categorias
    f = open(Path('../Projeto_AED/files/categorias.txt'),'r')
    categories = f.readlines()
    f.close()
    self.category_list = []
    for category in categories:
        category = category.strip('\n') # Remove o '\n' de cada categoria
        self.category_list.append(category)
        
#   Label e Listbox com todas as categorias existentes na app
    self.category_lbl = Label(self.tl_my_post, text = 'Categories', font = ('Roboto', 18), bg = 'lightgrey').place(x = 600, y = 370)
    self.categories = Combobox(self.tl_my_post, values = self.category_list, width = 15, font = ('Roboto', 14))
    self.categories.place(x = 600, y = 400)
    font_italic = font.Font(family = "Roboto", size = 8, slant = "italic")
    self.category_reminder = Label(self.tl_my_post, text = 'You may only choose 1 category per post', font = font_italic, bg = 'lightgrey').place(x = 600, y = 430)

    self.create_post_btn = Button(self.tl_my_post, text = 'Create Post', font = ('Roboto', 14), bg = '#28942a', fg = 'white', bd = 0, width = 15, height = 2, command = self.create_post).place(x = 800, y = 540)

  def select_image(self, image_id, cnv_image):
    """
    Esta função permite ao utilizador escolher uma imagem guardada no seu disco, escolhê-la, \n
    para depois postar na app.
    """
    # Vai buscar o nome do ficheiro que o utilizador inseriu
    self.tl_my_post.attributes('-topmost', 'false') # Para a janela deixar de ser toplevel (para acessar o explorador de ficheiros)
    self.filename = filedialog.askopenfilename(title = 'Select Image',
                                          filetypes = (("PNG files","*.png"),("GIF files","*.gif"),("JPG files","*.jpg"),("WEBP files","*.webp"),("All Files","*.*")))

    self.image = Image.open(self.filename) # Abrir o ficheiro
    resized_image = self.image.resize((400, 200)) # Mudar tamanho
    self.image = ImageTk.PhotoImage(resized_image) # Abrir imagem com a biblioteca PIL (ImageTk)

    cnv_image.itemconfig(image_id, image=self.image) # Mudar imagem presente no Canvas
    
    self.tl_my_post.attributes('-topmost', 'true') # Para a janela voltar a ser toplevel


  def create_post(self):
    # Se alguma coisa faltar // o utilizador não tiver preenchido
    if self.filename == '':
       messagebox.showerror('Error','You have to choose a picture to make a post!')
       return
    if self.add_to_album.get() == '':
       messagebox.showerror('Error','You have to select an album to save this post!')
       return
    if self.photo_name.get() == '':
       messagebox.showerror('Error', 'You have to select a name for your post!')
       return
    if self.description.get('1.0','end-1c') == '':
       messagebox.showerror('Error','You have to insert a description for your post!')
       return
    if self.categories.get() == '':
       messagebox.showerror('Error','You have to select a category for your post!')
       return
    username = self.username
    data = datetime.datetime.now()
    name = self.photo_name.get()
    date = data.strftime("%Y-%m-%d") + ';' + data.strftime("%H:%M")
    description = self.description.get('1.0', 'end-1c')
    description = description.replace('\n',' ')
    category = self.categories.get()
    album = self.add_to_album.get()
    filename = self.filename       
    os.chdir('users_photoalbums')
    os.chdir(self.username)
    os.chdir(album)
    os.mkdir(name)
    os.chdir(name)
    shutil.copy2(filename, os.getcwd())
    name = name + '.txt'
    with open(name, 'x') as file:
        name = name.replace('.txt','')
        file.write('{0}\n{1}\n{2}\n{3};\n{4}\n0\n-;'.format(username, name, date, description, category))
        file.close()
        messagebox.showinfo('Sucess!','The post has been created! Go check it out in its corresponding album!')
    filename = 'comments.txt'
    with open(filename, 'x') as file:
       file.close()
    
    # Adicionar informação de post ao ficheiro 'all-posts.txt'
    for i in range(4):
        os.chdir('..')  # Voltar quatro pastas atras
    os.chdir('files')
    f_all_posts= open('all-posts.txt', 'a', encoding='utf-8')
    f_all_posts.write('\n{0};{1};{2}'.format(username, category, date))
    f_all_posts.close()
    os.chdir('..\\') # Voltar uma pasta atrás
    self.tl_my_post.destroy()

  def go_back(self):
     """
     Esta função destroi a janela atual, voltando para a página principal
     """
     self.tl_my_post.destroy()
 

class Create_Album():
  def __init__(self, tl_create_album, username):
    self.username = username

    self.tl_create_album = Toplevel(tl_create_album)
    self.tl_create_album.geometry('1000x600+100-100') #Altera largura e altura da janela e posiciona a janela +/- no centro do ecrã
    self.tl_create_album.title('myPhotos')
    self.tl_create_album.resizable(0,0) #Para não se poder redimensionar a janela (para os widgets não saírem do sítio)
    self.tl_create_album.attributes('-topmost', 'true') #Isto faz com que o top level apareça por cima, pois ele por default aparece por baixo do top level da homepage
    self.tl_create_album.configure(bg = 'lightgrey')
    self.username = username

    #   Icon para voltar á página principal
    icon = Image.open(Path('../Projeto_AED/images/icons/go_back_icon.png')).resize((50, 50))
    icon = ImageTk.PhotoImage(icon)
    self.go_back_btn = Button(self.tl_create_album, image = icon, bd = 0, bg = 'lightgrey', command = self.go_back)
    self.go_back_btn.image = icon
    self.go_back_btn.place(x = 0, y = 0)

#   Label
    self.add_post_lbl = Label(self.tl_create_album, text = 'Create Album', font = ('Roboto', 28), bg = 'lightgrey').place(x = 100, y = 10)
    
#   Botão que chama a função "select_image" que é responsável por adicionar a imagem selecionada ao ecrã
    self.add_photo_btn = Button(self.tl_create_album, text = 'Add Images', width = 10, height = 2, bd = 2).place(x = 70, y = 310)

#   Criar um Canvas para de seguida adicionar a fotografia selecionada pelo utilizador
    self.cnv_image = Canvas(self.tl_create_album, width = 400, height = 200)
    self.cnv_image.place(x = 70, y = 100)

#   Para definir uma imagem inicial
    image = PhotoImage(file = '')
    self.image_id = self.cnv_image.create_image(0, 0, anchor = 'c', image=image)

#   Label & Entry do nome da fotografia/post
    self.album_name_lbl = Label(self.tl_create_album, text = 'Name', font = ('Roboto', 18), bg = 'lightgrey').place(x = 70, y = 370)
    self.album_name= StringVar()
    self.album_name_entry = Entry(self.tl_create_album, width = 25, textvariable = self.album_name, font = ('Roboto', 14)).place(x = 70, y = 400)
    self.btn_create_album= Button(self.tl_create_album, width=10, height=1, text='Create', font=('Roboto', 12), fg='#fff', bg='green', command=self.func_create_album).place(x= 70, y= 450)


  def func_create_album(self):
    '''
    Criar novo album de fotografias para o user
    '''
    self.created_album=0
    self.album_name_str = self.album_name.get()
    album_dir = "../Projeto_AED/users_photoalbums/" + self.username + '/' + self.album_name_str
    if os.path.isdir(Path(album_dir)):
        messagebox.showerror('Error', 'You already have an album with that name.')
    else:
        os.mkdir(Path(album_dir))
        messagebox.showinfo('Success', f'Album "{self.album_name_str}" created.') 
        self.created_album=1
        file_comments= open()
    return

  def go_back(self):
     """
     Esta função destroi a janela atual, voltando para a página principal
     """
     self.tl_create_album.destroy()
 