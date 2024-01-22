from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk, ImageFilter

from admins import admins
from posts import Posts
from dashboard import dashboard
from add_content import Add_Post, Create_Album

from pathlib import Path #pathlib is a module in the Python standard library that provides an object-oriented interface for working with filesystem paths. The Path class in pathlib represents a filesystem path and comes with various methods for file and directory manipulation.
from tkcalendar import DateEntry # Inserir no terminal: pip install tkcalendar 

import os
import datetime

class Main_App:
    def __init__(self, window, username, admin):
        self.tl = Toplevel(window)
        self.username = username

#       Configurações da janela
        self.tl.geometry('1000x600+100-100') #  Altera largura e altura da janela e posiciona a janela +/- no centro do ecrã
        self.tl.title('myPhotos')
        self.tl.resizable(0,0) #    Para não se poder redimensionar a janela (para os widgets não saírem do sítio)
        
#       Configuração da NavBar
        self.nav_bar = Frame(self.tl, width = 1000, height = 60, bg = '#333')
        self.nav_bar.place(x = 0, y = 0)

#       Configuração da Homepage
        self.homepage = Frame(self.tl, width = 1000, height = 1000, bg = '#fff')
        self.homepage.place(x = 0, y = 60)

#       Chama as classes Nav_Bar e Homepage, respetivamente
        self.Nav_Bar(self.nav_bar, self.homepage, self.tl, admin, self.username)
        self.Homepage(self.username, self.homepage, admin, self.tl, window)

    class Nav_Bar:
        """
        Nesta classe cria-se tudo relacionado com a Nav_Bar \n
        Widgets, layout e funções relacionadas
        """
        def __init__(self, nav_bar, homepage, tl, admin, username):
            self.nav_bar = nav_bar
            self.homepage = homepage
            self.tl = tl
            self.username=username

#           Frame onde aparece os botões de 'See Profile' e 'Log Out'
#           Aparecem quando o utilizador clica no botão com o icone do perfil
            self.profile_click_frame = Frame(self.homepage, width = 200, height = 135, bg = 'white')

#           Frame onde aparece a notificação mais recente e um botão que vai dar á página com todas as notificações
#           Aparecem quando o utilizador clica no botão com o icone da notificação
            self.notifications_click_frame = Frame(self.homepage, width = 250, height = 90, bg = 'lightgrey', bd = '3', relief = 'raised')

#           Label com o logo da app
            self.myPhotos_logo = Label(self.nav_bar, text = 'myPhotos', fg = 'white', bg = '#333333', font =('Roboto', 28)).place(x = 430, y = 5)

            if admin == True:
#               Uma welcome message para os admins
                self.admin_label = Label(self.nav_bar, text = 'Welcome admin '+ self.username + '!', font = ('Roboto', 16), bg = '#333', fg='white').place(x = 10, y = 18)
            else:
#               Uma welcome message só para os users
                self.username_label = Label(self.nav_bar, text = 'Welcome ' + self.username + '!', font = ('Roboto', 16), bg = '#333', fg='white').place(x = 10, y = 18)


#             Icone da homepage (FONTE - SITE FLATICON)
#             icon = Image.open('./images/icons/homepage_icon.png').resize((50,50))
#             icon = ImageTk.PhotoImage(icon)
#             self.homepage_icon = Button(self.nav_bar, image = icon, bg = '#333333', bd = 0)
#             self.homepage_icon.image = icon
#             self.homepage_icon.place(x = 10, y = 5)

#           Icone do perfil (FONTE - SITE FLATICON)
            icon2 = Image.open(Path('../Projeto_AED/images/icons/profile_icon.png')).resize((50,50))
            icon2 = ImageTk.PhotoImage(icon2)
            self.profile_icon = Button(self.nav_bar, image = icon2, bd = 0, bg = '#333333', command = lambda:self.profile_click(admin))
            self.profile_icon.image = icon2
            self.profile_icon.place( x = 940, y = 5)
 

#           ------- Janela com várias estatísticas do utilizador ----------
#           Icon de notificações(FONTE - SITE FLATICON)
            icon3 = Image.open(Path('../Projeto_AED/images/icons/dashboard_icon.png')).resize((40,40))
            icon3 = ImageTk.PhotoImage(icon3)
            self.dashboard_icon = Button(self.nav_bar, image = icon3, bd = 0, bg = '#333333', 
                                         command = lambda: self.dashboard_tl(self.homepage))
            self.dashboard_icon.image = icon3
            self.dashboard_icon.place(x = 800, y = 8)
#           Icon da dashboard (FONTE - SITE FLATICON)
            icon4 = Image.open(Path('../Projeto_AED/images/icons/bell_icon.png')).resize((40,40))
            icon4 = ImageTk.PhotoImage(icon4)
            self.bell_icon = Button(self.nav_bar, image = icon4, bg = '#333333', bd = 0,
                                    command= self.notifications_click)
            self.bell_icon.image = icon4
            self.bell_icon.place(x = 870, y = 8)

#           Botão em que faz com que o utilizador saia da conta com que está conectado e volte à página principal
            self.log_out = Button(self.profile_click_frame, text = 'Log Out', font = ('Roboto', 16), bg = 'lightgrey', bd = '3', relief = 'raised', width = 10, command = self.logging_out)

#           Botão de administrador para gerir a app(abre um top level para a gerência da app)
            if admin == True:
                self.btn_tl_admin = Button(self.profile_click_frame, text = 'Manage App', font = ('Roboto', 16), bg = 'lightgrey', bd = '3', relief = 'raised', width = 10, command = lambda:self.admin_tl(self.homepage))

#           Label onde aparece a notificação mais recente
            self.latest_notification = Label(self.notifications_click_frame, text = 'Onde será inserido a notificação mais recente', bg = 'lightgrey', font = ('Roboto', 8))

#           Botão que vai dar á página com todas as notificações recebidas
            self.all_notifications_btn = Button(self.notifications_click_frame, text = 'See All Notifications', font = ('Roboto', 12), bg = 'white', bd = '0', width = 18)

#           Icone da lupa (FONTE - SITE FLATICON)
#           icon = Image.open('..\\Projeto_AED\\images\\icons\\search_icon.png').resize((27,27))
#           icon = ImageTk.PhotoImage(icon)
#           search_icon = Button(image = icon, bg = '#333333', bd = 0)
#           search_icon.image = icon
#           search_icon.place( x = 185, y = 15)

#           Barra de pesquisa
#           search = Entry(nav_bar, bg = '#E0E0E0', bd = 0, font =('Roboto', 14), width = 15).place(x = 220, y = 15)

        def admin_tl(self, homepage):
                    '''
                    Função para criar um Top Level para aparecer a gerência da app aos admins
                    '''        
                    self.tl_admin = Toplevel(homepage)
                    self.tl_admin.geometry('1000x600+100-100') #Altera largura e altura da janela e posiciona a janela +/- no centro do ecrã
                    self.tl_admin.title('Hello Master, what do you want to do to me?')
                    self.tl_admin.resizable(0,0) #Para não se poder redimensionar a janela (para os widgets não saírem do sítio)
                    self.tl_admin.attributes('-topmost', 'true') #Isto faz com que o top level apareça por cima, pois ele por default aparece por baixo do top level da homepage
                    admins(self.tl_admin)

        def profile_click(self, admin):
            """
            Esta função cria um Frame que aparece quando o utilizador clica no icon do perfil \n
            Aparece as opções de Ver o seu perfil e Sair da Conta
            """
            if self.profile_click_frame.winfo_ismapped(): # Se o frame estiver na janela
                self.profile_click_frame.place_forget()
                self.log_out.place_forget()
                self.btn_tl_admin.place_forget()
            else: # Senão
                self.profile_click_frame.place(x = 870, y = 0)
                self.log_out.place(x = 0, y = 0)
                if admin == True:
                    self.btn_tl_admin.place(x = 0, y = 45)
        
        def notifications_click(self):
            """
            Esta função cria um Frame que aparece quando o utilizador clica no icon das notificações \n
            Aparece a notificação mais recente e um botão que leva á página com acesso a todas as notificações
            """
            if self.notifications_click_frame.winfo_ismapped(): # Se a frame estiver na janela
                self.notifications_click_frame.place_forget()
                self.latest_notification.place_forget()
                self.all_notifications_btn.place_forget()
            else:
                self.notifications_click_frame.place(x = 620, y = 0)
                self.latest_notification.place(x = 0, y = 20)
                self.all_notifications_btn.place(x = 75, y = 55)


        def logging_out(self):
            """
            Esta função pergunta ao utilizador se deseja sair da conta 
            """
            self.tl.destroy() #A janela Top Level é destruída


    class Homepage:
        def __init__(self, username, homepage, admin, tl, window):
            """
            Esta função cria a janela da homepage \n
            É constituida pela barra de navegação e pela página principal \n
            A barra de navegação têm o logo da app, uma barra de pesquisa, icones da dashboard, de notifições e do perfil do utilizador
            """
            self.homepage = homepage
            self.username = username 
            self.tl=tl
            from search import func_search_results_window

#           --- Imagem background ---------
            # Canvas
            canvas = Canvas(self.homepage, width=800, height=540)
            canvas.place(x=200,y=0)
            # Buscar Imagem
            bg_image = Image.open(Path("./images/backgrounds/main_background.jpg"))
            # Redimensionar Imagem
            resized_bg_image = bg_image.resize((800, 540))  #Ajustar tamanho da Imagem (width, height)
            # PhotoImage
            self.bg_img = ImageTk.PhotoImage(resized_bg_image)
            # Adicionar a Imagem ao Canvas
            canvas.create_image(400, 270, anchor=CENTER, image=self.bg_img)


#           --- Frame de Pesquisa ---
            self.f_search= Frame(self.tl, width=200, height=300)
            self.f_search.place(x=0,y=60)
            # Label Título
            self.lbl_search= Label(self.f_search, text='Search', font=('Roboto, 14'))
            self.lbl_search.place(x=20,y=20)
            # Entry:
            self.search_entry= StringVar()
            self.entry_search_bar= Entry(self.f_search, textvariable=self.search_entry, width=20)
            self.entry_search_bar.place(x=20, y=60)
            #Listbox das categorias
            self.lbox_categ = Listbox(self.f_search, height=6, bg='#eee', width=17, selectmode='multiple', font=('Roboto', 10))
            self.lbox_categ.place(x=20,y=90)
            f_categ = open('files\\categorias.txt', 'r', encoding='utf-8')
            lines_categ = f_categ.readlines()
            f_categ.close()        
            for line in lines_categ:
                self.lbox_categ.insert(END, line) #END significa que cada line é inserida no fim do conteúdo da listbox
            # Widget Pick a Date
            self.cal = DateEntry(self.f_search, width=12, background='purple', foreground='white', borderwidth=2)
            self.cal.place(x=20, y=200)
            # Button para selecionar uma data
            select_button = Button(self.f_search, text="Select Date", command=self.func_selected_date)
            select_button.place(x=20, y=220)
            #Button para Pesquisar
            self.btn_search= Button(self.f_search, height=2, text='Search for results', bg='lightblue', 
                                    command=lambda:func_search_results_window(tl, self.search_entry, self.lbox_categ, self.selected_date))
            self.btn_search.place(x=20,y=240) 

#           Frame para Button 'My Albums'
            self.f_btn_my_posts= Frame(self.tl, width=200, height=100, bg='lightblue')
            self.f_btn_my_posts.place(x=0,y=360)
            self.lbl_btn= Button(self.f_btn_my_posts, text='My Albums', width=12, font=('Roboto, 16'),
                                 command=lambda:self.my_albums(self.tl, self.username))
            self.lbl_btn.place(x=20,y=20)

#           Botão para adicionar um post
            self.add_content_btn = Button(self.homepage, text = '+  Add', width = 12, height = 1, bg = '#28942a', fg = 'white', font = ('Roboto', 20), bd = 0, command = self.show_add_content_frame).place(x = 0, y = 450)
#           Frame que aparece quando o utilizador clica no botão '+ Add'
#           Aparece os botões de Fazer um Post e Criar um Album
            self.add_content_frame = Frame(self.homepage, width = 186, height = 125, bg = '#28942a')
            self.add_post = Button(self.add_content_frame, text = 'Add a Post', bg = '#28942a', font = ('Roboto', 16),fg = 'white', bd = 0, width = 15, height = 2, command = lambda: self.add_post_frame(self.homepage, self.username, window))
            self.add_album = Button(self.add_content_frame, text = 'Create an Album', bg = '#28942a', font = ('Roboto', 16),fg = 'white', bd = 0, width = 15, height = 2, command = lambda: self.create_album_frame(self.homepage, self.username, window))

#       -------- FUNÇÕES ------------------------------------------------------------

        def func_selected_date(self):
                    '''
                    Ao carregar 
                    '''
                    
                    self.selected_date = self.cal.get_date() #pegar na data selecionada
                    print('selected date:', self.selected_date)
#       ----------- + POST Button ---------------------------------------------------
        def show_add_content_frame(self):
            """
            Esta função faz com que o Frame para adicionar um post apareça \n
            Dentro da Frame, aparece as opções de criar um post com uma imagem, ou criar um álbum novo
            """
            if self.add_content_frame.winfo_ismapped(): #Se o frame estiver na janela
                self.add_content_frame.place_forget()
                self.add_post.place_forget()
                self.add_album.place_forget()
            else:
                self.add_content_frame.place(x = 800, y = 200)
                self.add_post.place(x = 0, y = 0)
                self.add_album.place(x = 0, y = 60)

        def add_post_frame(self, homepage, username, window):
            self.username = username
            self.tl_add_photo = Toplevel(window)
            self.tl_add_photo.geometry('1000x600+100-100') #Altera largura e altura da janela e posiciona a janela +/- no centro do ecrã
            self.tl_add_photo.title('myPhotos')
            self.tl_add_photo.resizable(0,0) #Para não se poder redimensionar a janela (para os widgets não saírem do sítio)
            self.tl_add_photo.attributes('-topmost', 'true') #Isto faz com que o top level apareça por cima, pois ele por default aparece por baixo do top level da homepage
            self.tl_add_photo.configure(bg = 'lightgrey')
            Add_Post(self.tl_add_photo, homepage, username, window)
            
        def create_album_frame(self, homepage, username, window):
            self.username = username

            self.tl_create_album = Toplevel(window)
            self.tl_create_album.geometry('1000x600+100-100') #Altera largura e altura da janela e posiciona a janela +/- no centro do ecrã
            self.tl_create_album.title('myPhotos')
            self.tl_create_album.resizable(0,0) #Para não se poder redimensionar a janela (para os widgets não saírem do sítio)
            self.tl_create_album.attributes('-topmost', 'true') #Isto faz com que o top level apareça por cima, pois ele por default aparece por baixo do top level da homepage
            self.tl_create_album.configure(bg = 'lightgrey')
            Create_Album(self.tl_create_album, self.username, window)

#       ----------- My Albums Button -------------------------------------------------

        def my_albums(self, tl, username):
            '''
            Abre uma Frame para mostrar os albums do user
            '''
            #Frame 
            self.f_my_albums= Frame(tl, width=800, height=540, bg='#fff')
            self.f_my_albums.place(x=200,y=60)
            btn_destroy_frame= Button(self.f_my_albums, text=' X ', command=self.f_my_albums.destroy)
            btn_destroy_frame.place(x=600,y=10)
            
#           --- Fazer os Álbums aparecer:
            
            #Meter numa variável a diretoria/pasta dos álbums do user
            self.albums_directory=('./users_photoalbums/'+ username) 
            
            # Listar os álbums
            album_folders = []
            for i in os.listdir(self.albums_directory): #Por cada folder
                full_path = os.path.join(self.albums_directory, i) #Está a juntar a diretoria user com a diretoria álbum em vez de usar concatenação
                if os.path.isdir(full_path): #se for uma folder
                    album_folders.append(i) #Adiciona o nome desse album á lista
            
            for idx, album_folder in enumerate(album_folders):
                # Calculate row and column based on the index
                row = idx // 4
                col = idx % 4

                btn_my_album = Button(self.f_my_albums, text=album_folder, bg='#f8d775', width=18, height=5,
                                    command=lambda tl=tl, username=username, folder=album_folder: self.open_my_album_frame(tl, folder, username))
                btn_my_album.grid(row=row, column=col, padx=30, pady=30)

        def open_my_album_frame(self, tl, album_folder, username):
            '''
            Cada Álbum abre uma nova Frame com Publicações
            '''
            # Frame
            self.f_my_album= Frame(tl, width=800, height=600, bg='pink')
            self.f_my_album.place(x=200,y=60)
            # Button Sair Frame
            btn_destroy_frame2= Button(self.f_my_album, text=' X ', command=self.f_my_album.destroy)
            btn_destroy_frame2.place(x=600,y=10)

#           ----- Fazer os Posts aparecerem na Frame do Álbum ---------- 
            
            # Criar um path até ao Álbum clicado
            album_path = os.path.join('.\\users_photoalbums\\', username, album_folder) #não é necessário concatenação, nem \\
            
            # Listar os Posts do meu Álbum
            my_album_post = []
            for i in os.listdir(album_path): #por cada folder(post) dentro da folder(Álbum)
                full_path = os.path.join(album_path , i) #está a juntar a folder(álbum) com a folder(post) em vez de usar concatenação e '\\'
                if os.path.isdir(full_path): #se full_path for uma folder
                    my_album_post.append(i) #Adiciona o nome desse Post à lista



            # Create a Canvas widget to contain the frame and the scrollbar
            canvas = Canvas(self.f_my_album, width=600, height=600, bg='pink')
            canvas.grid(row=0, column=0, sticky="nsew")  # Use grid to make the canvas expandable

            # Create a Frame inside the Canvas to hold your buttons
            frame_inside_canvas = Frame(canvas, bg='pink')
            canvas.create_window((0, 0), window=frame_inside_canvas, anchor="nw")

            # Create a vertical scrollbar
            scrollbar = Scrollbar(self.f_my_album, orient="vertical", command=canvas.yview)
            scrollbar.grid(row=0, column=1, sticky="ns")  # Place scrollbar on the right side

            # Configure the canvas to scroll vertically
            canvas.configure(yscrollcommand=scrollbar.set)

            # Add buttons to the frame_inside_canvas instead of directly to f_my_album
            # for row, i in enumerate(my_album_post):




            # Cada Post vai ser um Button
            for row, i in enumerate(my_album_post): #enumerate cria uma tuple que contém um index 'row' e o correspondente valor 'i' que pertence ao my_album_post.
                post_path = os.path.join(album_path, i) #post_path é o conjunto de paths dos posts do álbum p.e: post_path = ''..\\my_album\\rose_post'' + ''...\\my_album\\cake_post'' + ...

                # Obter a imagem que está dentro da folder, que por sua vez está dentro do Álbum 
                image_files = []
                extensions = ('.png', '.jpg', '.jpeg', '.gif','.webp')
                for extension in extensions:
                    matching_files = []
                    for i in os.listdir(post_path): #por cada Post path
                        if i.lower().endswith(extension):
                            matching_files.append(i) #reunimos as imagens numa lista

                    image_files.extend(matching_files) #adicionar os matching_files à lista image_files

                if image_files: #se a lista tiver pelo menos um elemento, a condição fica True e a próximas linhas são executadas
                    image_path = os.path.join(post_path, image_files[0]) #juntar o path do post com a imagem
                    image = Image.open(image_path)
                    image = image.resize((150, 150)) # width, height
                    photo = ImageTk.PhotoImage(image) #para lembrar o Python que não pedi para apagar nada

                    resized_image = Image.open(image_path)
                    resized_image = resized_image.resize((450, 350))

                    # Criar um novo PhotoImage da imagem redimensionada
                    resized_photo = ImageTk.PhotoImage(resized_image)
                    btn_my_post = Button(frame_inside_canvas, image=photo, width=150, height=150,
                                        command=lambda img=resized_photo, image_path=image_path: Posts(frame_inside_canvas, image_path, img, self.username))
                    btn_my_post.image = photo  #''garbage collection'' para a imagem não ser apagada automaticamente para criar memória livre
                else:
                    btn_my_post = Button(frame_inside_canvas, text=i, width=40, height=5,
                                        command=lambda  img=resized_photo, image_path=image_path: Posts(frame_inside_canvas, image_path, img, self.username))

                btn_my_post.grid(column=row % 3,  row=row // 3, padx=20, pady=40)

            # Update the scroll region when the size of the frame_inside_canvas changes
            frame_inside_canvas.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

#             Icone da lupa (FONTE - SITE FLATICON)
            # icon = Image.open('..\\Projeto_AED\\images\\icons\\search_icon.png').resize((27,27))
            # icon = ImageTk.PhotoImage(icon)
            # search_icon = Button(image = icon, bg = '#333333', bd = 0)
            # search_icon.image = icon
            # search_icon.place( x = 185, y = 15)