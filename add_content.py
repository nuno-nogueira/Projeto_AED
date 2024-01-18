from tkinter import *
from search import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.ttk import Combobox
from pathlib import Path #pathlib is a module in the Python standard library that provides an object-oriented interface for working with filesystem paths. The Path class in pathlib represents a filesystem path and comes with various methods for file and directory manipulation.
import os
import datetime

class Add_Post():
  """
  Esta classe é responsável por tudo relacionado com adicionar um post/fotografia \n
  Todos os widgets da janela "Add Post".
  Todas as funções relacionadas.
  """
  def __init__(self, tl_add_photo, homepage, username):
    """
    Permite criar uma window que é um objeto da classe App \n
    Usado para configurar uma janela nova TopLevel
    """
    self.tl_add_photo = tl_add_photo
    self.username = username

#   Icon para voltar á página principal
    icon = Image.open(Path('../Projeto_AED/images/icons/go_back_icon.png')).resize((50, 50))
    icon = ImageTk.PhotoImage(icon)
    self.go_back_btn = Button(self.tl_add_photo, image = icon, bd = 0, bg = 'lightgrey', command = self.go_back)
    self.go_back_btn.image = icon
    self.go_back_btn.place(x = 0, y = 0)

#   Label
    self.add_post_lbl = Label(self.tl_add_photo, text = 'Add Post', font = ('Roboto', 28), bg = 'lightgrey').place(x = 100, y = 10)

#   Botão que chama a função "select_image" que é responsável por adicionar a imagem selecionada ao ecrã
    self.add_photo_btn = Button(self.tl_add_photo, text = 'Add Image', width = 10, height = 2, bd = 2, command = lambda: self.select_image(image_id, cnv_image)).place(x = 70, y = 310)

#   Criar um Canvas para de seguida adicionar a fotografia selecionada pelo utilizador
    cnv_image = Canvas(self.tl_add_photo, width = 400, height = 200)
    cnv_image.place(x = 70, y = 100)

#   Para definir uma imagem inicial
    image_chosen = Image.open(Path("./images/backgrounds/bg.jpg"))
    image_chosen = image_chosen.resize((1000,400))

    self.image = ImageTk.PhotoImage(image_chosen)
    image_id = cnv_image.create_image(0, 0, anchor = CENTER, image = self.image)

#   Label & Entry do nome da fotografia/post
    self.photo_name_lbl = Label(self.tl_add_photo, text = 'Name', font = ('Roboto',18), bg = 'lightgrey').place(x = 70, y = 370)
    self.photo_name = Entry(self.tl_add_photo, width = 25, font = ('Roboto', 14))
    self.photo_name.place(x = 70, y = 400)

    user_dir = "../Projeto_AED/users_photoalbums/" + self.username
    self.albums_list = os.listdir(Path(user_dir))
#   Label, Combobox com todos albuns do utilizador e um botão para criar um álbum que leva a outra janela
    self.add_to_album_lbl = Label(self.tl_add_photo, text = 'Add to Album:', font = ('Roboto', 18), bg = 'lightgrey').place(x = 70, y = 450)
    self.add_to_album = Combobox(self.tl_add_photo, height = 1, width = 15, values = self.albums_list, font = ('Roboto', 14))
    self.add_to_album.place(x = 70, y = 480)
    self.create_album = Button(self.tl_add_photo, text = 'Create Album', font = ('Roboto', 14), bg = '#28942a', fg = 'white', bd = 0, width = 15, height = 2, command = lambda:self.go_to_albums(homepage, username)).place(x = 270, y = 480)

#   Label & Text da descrição da fotografia/post
    self.description_lbl = Label(self.tl_add_photo, text = 'Description', font = ('Roboto', 18), bg = "lightgrey").place(x = 600, y = 50)
    self.description = Text(self.tl_add_photo, width = 40, height = 7, font = ('Roboto', 10), bd = 2)
    self.description.place(x = 600, y = 100)
  
#   Para ir buscar as categorias existentes ao ficheiro da categorias
    f = open(Path('../Projeto_AED/files/categorias.txt'),'r')
    categories = f.readlines()
    f.close()
#   Lista que vai conter as categorias sem o '\n'
#   Não dá para fazer isso para a lista "categories", porque crasha.
    self.category_list = []
    for category in categories:
        category = category.strip('\n') # Remove o '\n' de cada categoria
        self.category_list.append(category)
        
#   Label e Listbox com todas as categorias existentes na app
    self.category_lbl = Label(self.tl_add_photo, text = 'Categories', font = ('Roboto', 18), bg = 'lightgrey').place(x = 600, y = 250)
    self.categories = Combobox(self.tl_add_photo, values = self.category_list, width = 15, font = ('Roboto', 14))
    self.categories.place(x = 600, y = 280)

#   Botão que adiciona uma categoria á imagem escolhida
    self.add_category_btn = Button(self.tl_add_photo, text = 'Add category', width = 15, height = 2, bd = 2, command = self.add_category).place(x = 600, y = 320)

#   Botão que remove uma categoria
    self.remove_category_btn = Button(self.tl_add_photo, text = 'Remove category', width = 15, height = 2, bd = 2, command = self.remove_category).place(x = 600, y = 400)

#   Lista que mostra as categorias escolhidas pelo utilizador
    self.categories_chosen = Listbox(self.tl_add_photo, width = 15, height = 8, font = ('Roboto', 14))
    self.categories_chosen.place(x = 750, y = 320)

    self.create_post_btn = Button(self.tl_add_photo, text = 'Create Post', font = ('Roboto', 14), bg = '#28942a', fg = 'white', bd = 0, width = 15, height = 2, command = self.create_post).place(x = 800, y = 540)

  def select_image(self, image_id, cnv_image):
    """
    Esta função permite ao utilizador escolher uma imagem guardada no seu disco, escolhê-la, \n
    para depois postar na app.
    """
    # Vai buscar o nome do ficheiro que o utilizador inseriu
    self.tl_add_photo.attributes('-topmost', 'false') # Para a janela deixar de ser toplevel (para acessar o explorador de ficheiros)
    filename = filedialog.askopenfilename(title = 'Select Image', initialdir = "./images/backgrounds",
                                          filetypes = (("PNG files","*.png"),("GIF files","*.gif"),("JPG files","*.jpg"),("All Files","*.*")))

    self.image = Image.open(filename) # Abrir o ficheiro
    resized_image = self.image.resize((1000, 400)) # Mudar tamanho
    self.image = ImageTk.PhotoImage(resized_image) # Abrir imagem com a biblioteca PIL (ImageTk)

    cnv_image.itemconfig(image_id, image=self.image) # Mudar imagem presente no Canvas
    
    self.tl_add_photo.attributes('-topmost', 'true') # Para a janela voltar a ser toplevel


  def add_category(self):
    """
    Esta função faz com que o utilizador escolha categorias para o seu post 
    """
    chosen_category = self.categories.get() # Vai buscar o que foi selecionado nas categorias disponíveis
    categories_chosen = self.categories_chosen.get(0,'end') # Vai buscar a lista de categorias selecionadas pelo utilizador
    if self.categories_chosen.size() == 0:
        # Se a lista de categorias escolhidas pelo utilizador estiver vazia:
        # Este if está aqui pois sem ele o conteudo no "else" não funciona
        self.categories_chosen.insert(END, chosen_category) # Insere a categoria escolhida
    else:
        for category in categories_chosen:
            # Loop for pelas categorias que foram escolhidas pelo utilizador
            if category == chosen_category: # Se a categoria selecionada já estiver na lista de categorias escolhidas pelo utilizador
                messagebox.showinfo('Already chosen','You already chose the category you selected!') # Mostra mensagem
        else: # Senão
            self.categories_chosen.insert(END, chosen_category)
           

  def remove_category(self):
    """
    Esta função faz com que ao clique do botão "Remove Category" \n
    Com que apague a categoria selecionada na Listbox
    """
    selected = self.categories_chosen.curselection()
    if not selected:
       messagebox.showerror('Error','Select a category first to delete it!')
    else:
       self.categories_chosen.delete(selected)


  def go_back(self):
     """
     Esta função destroi a janela atual, voltando para a página principal
     """
     self.tl_add_photo.destroy()
 

  def go_to_albums(self, homepage, username):
    """
    Esta função destroi a janela atual, e cria a uma janela para o utilizador criar um
    """
    self.username = username

    self.tl_add_photo.destroy()
    self.tl_create_album = Toplevel(homepage)
    self.tl_create_album.geometry('1000x600+100-100') #Altera largura e altura da janela e posiciona a janela +/- no centro do ecrã
    self.tl_create_album.title('myPhotos')
    self.tl_create_album.resizable(0,0) #Para não se poder redimensionar a janela (para os widgets não saírem do sítio)
    self.tl_create_album.attributes('-topmost', 'true') #Isto faz com que o top level apareça por cima, pois ele por default aparece por baixo do top level da homepage
    self.tl_create_album.configure(bg = 'lightgrey')
    Create_Album(self.tl_create_album, username)
     

  def create_post(self):
    data = datetime.datetime.now()
    name = self.photo_name.get()
    date = data.strftime("%d/%m/%Y") + ';' + data.strftime("%H:%M:%S")
    description = self.description.get('0.0', END)
    categories = self.categories_chosen.get('0', END)
    album = self.add_to_album.get()
    os.chdir('users_photoalbums')
    os.chdir(self.username)
    os.chdir(album)
    os.mkdir(name)
    os.chdir(name)
    name = name + '.txt'
    with open(name, 'x') as file:
        name = name.replace('.txt','')
        file.write('{0}\n{1}\n{2}'.format(name, date, description))
        for category in categories:
           file.write(category+'\n')
        file.close()
    #Adicionar informação de post ao ficheiro 'all-posts.txt
    os.chdir('')
    f_all_posts= open('', 'w', encoding='utf-8')
    f_all_posts.write('\n'+self.username+';'+ self.chosen_category+';')
    f_all_posts.close()
    

class Create_Album():
  def __init__(self, tl_create_album, username):
    self.tl_create_album = tl_create_album
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
    self.add_photo_btn = Button(self.tl_create_album, text = 'Add Images', width = 10, height = 2, bd = 2, command = self.select_image).place(x = 70, y = 310)

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

    
  def select_image(self):
    """
    Esta função permite ao utilizador escolher uma imagem guardada no seu disco, escolhê-la, \n
    para depois postar na app.
    """
#   Vai buscar o nome do ficheiro que o utilizador inseriu
    filename = filedialog.askopenfilename(title = 'Select Image', initialdir = './images/icons',
              filetypes = (('PNG files','*.png'),('GIF files','*.gif'),('All Files','*.*')))

#   Para depois defini-la e adicioná-la ao Canvas
    image = PhotoImage(file = filename)

#   Adicionar a imagem ao Canvas
    self.cnv_image.itemconfig(self.image_id, image=image)


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
    return



  def go_back(self):
     """
     Esta função destroi a janela atual, voltando para a página principal
     """
     self.tl_create_album.destroy()
 

# def func_create_album(self):
#             '''
#             Criar novo album de fotografias para o user
#             '''
#             os.chdir('users_photoalbums')
#             os.chdir(self.username)
#             self.album_name_str = self.album_name.get()
#             if os.path.isdir(self.album_name_str):
#                 messagebox.showerror('Error', 'You already have an album with that name.')
#                 os.chdir('..\\..')
#             else:
#                 os.mkdir(str(self.album_name_str))
#                 messagebox.showinfo('Success', f'Album "{self.album_name_str}" created.')  
#                 os.chdir('..\\..')  
#             return