from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk, ImageFilter
from albums_comments import Albums_Comments
from admins import admins
from posts import Posts
from dashboard import dashboard
from add_content import Add_Post, Create_Album

from notifications import show_notifications
from search import *
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
# ------------------------
#         self.nav_bar = None
#         self.Nav_Bar(self.nav_bar, self.homepage, self.tl, admin, self.username)

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
            self.profile_click_frame = Frame(self.homepage, width = 200, height = 85, bg = 'white')

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

# -------------------------------------------
#         def search_user(self):
#             username_to_search = self.user_search_entry.get()
#             if username_to_search:
#                 self.tl.destroy()  # Fechar a janela atual para exibir os resultados em uma nova janela
#                 new_window = Tk()
#                 new_window.geometry('1000x600+100-100')
#                 new_window.title('Search Results')
#                 new_window.resizable(0, 0)
#                 Main_App(new_window, username_to_search, admin=False)

# ---------- Icons NavBar ---------------------------------------------------------
            
#           Icone da homepage (FONTE - SITE FLATICON)
            icon = Image.open('./images/icons/homepage_icon.png').resize((40,40))
            icon = ImageTk.PhotoImage(icon)
            self.homepage_icon = Button(self.nav_bar, image = icon, bg = '#333333', bd = 0,
                                        command= self.home_btn)
            self.homepage_icon.image = icon
            self.homepage_icon.place(x = 380, y = 7)

#           Icone do perfil (FONTE - SITE FLATICON)
            icon2 = Image.open(Path('../Projeto_AED/images/icons/profile_icon.png')).resize((40,40))
            icon2 = ImageTk.PhotoImage(icon2)
            self.profile_icon = Button(self.nav_bar, image = icon2, bd = 0, bg = '#333333', command = lambda:self.profile_click(admin))
            self.profile_icon.image = icon2
            self.profile_icon.place( x = 940, y = 8)
 
#           Icon de dashboard (FONTE - SITE FLATICON)
            icon3 = Image.open(Path('../Projeto_AED/images/icons/dashboard_icon.png')).resize((35,35))
            icon3 = ImageTk.PhotoImage(icon3)
            self.dashboard_icon = Button(self.nav_bar, image = icon3, bd = 0, bg = '#333333', 
                                         command = lambda: self.dashboard_tl(self.homepage))
            self.dashboard_icon.image = icon3
            self.dashboard_icon.place(x = 800, y = 8)

#           Icon das notificações (FONTE - SITE FLATICON)
            icon4 = Image.open(Path('../Projeto_AED/images/icons/bell_icon.png')).resize((40,40))
            icon4 = ImageTk.PhotoImage(icon4)
            self.bell_icon = Button(self.nav_bar, image = icon4, bg = '#333333', bd = 0,
                                    command= lambda: self.notifications_click_tl(self.homepage))
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
        
        def home_btn(self, homepage_canvas):
            '''
            Fecha as frames que estiverem abertas para voltar ao início da App
            '''
            self.homepage_canvas= homepage_canvas
            self.homepage_canvas.canvas.place(x=0,y=0)
            


        def dashboard_tl(self, homepage):
                    '''
                    Função para criar um Top Level para aparecer a gerência da app aos admins
                    '''        
                    self.tl_dashboard = Toplevel(homepage)
                    self.tl_dashboard.geometry('800x500+100-100') #Altera largura e altura da janela e posiciona a janela +/- no centro do ecrã
                    self.tl_dashboard.title('Dashboard')
                    self.tl_dashboard.resizable(0,0) #Para não se poder redimensionar a janela (para os widgets não saírem do sítio)
                    self.tl_dashboard.attributes('-topmost', 'true') #Isto faz com que o top level apareça por cima, pois ele por default aparece por baixo do top level da homepage
                    dashboard(self.tl_dashboard, self.username)

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
                self.profile_click_frame.lift()
                self.log_out.place(x = 0, y = 0)
                if admin == True:
                    self.btn_tl_admin.place(x = 0, y = 45)
        
        def notifications_click_tl(self,homepage):
            """
            Esta função cria um Frame que aparece quando o utilizador clica no icon das notificações \n
            Aparece a notificação mais recente e um botão que leva á página com acesso a todas as notificações
            """
            self.tl_notifications_click = Toplevel(homepage)
            self.tl_notifications_click.geometry('800x500+100-100') #Altera largura e altura da janela e posiciona a janela +/- no centro do ecrã
            self.tl_notifications_click.title('Notifications')
            self.tl_notifications_click.resizable(0,0) #Para não se poder redimensionar a janela (para os widgets não saírem do sítio)
            self.tl_notifications_click.attributes('-topmost', 'true') #Isto faz com que o top level apareça por cima, pois ele por default aparece por baixo do top level da homepage
            show_notifications(self.tl_notifications_click)
            
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
            self.canvas = Canvas(self.homepage, width=800, height=540)
            self.canvas.place(x=200,y=0)
            # Buscar Imagem
            bg_image = Image.open(Path("./images/backgrounds/main_background.jpg"))
            # Redimensionar Imagem
            resized_bg_image = bg_image.resize((800, 540))  #Ajustar tamanho da Imagem (width, height)
            # PhotoImage
            self.bg_img = ImageTk.PhotoImage(resized_bg_image)
            # Adicionar a Imagem ao self.Canvas
            self.canvas.create_image(400, 270, anchor=CENTER, image=self.bg_img)

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
            self.cal = DateEntry(self.f_search, width=8, background='purple', foreground='white', borderwidth=2)
            self.cal.place(x=20, y=205)
            # Button para selecionar uma data
            select_button = Button(self.f_search, text="Select this Date", bg='#fff', command=self.get_selected_date)
            select_button.place(x=95, y=200)
            # Button para pesquisar
            self.btn_search = Button(self.f_search, width=20, height=2, text='Search for Posts', bg='lightblue',
                                    command=lambda: func_search_results_window(tl, self.search_entry, self.lbox_categ, self.selected_date))
            self.btn_search.place(x=20, y=240)
            
 
#           --- Frame para Button 'My Albums' -----------------
            self.frame_myalbums= Frame(self.tl, width=200, height=60, bg='pink')
            self.frame_myalbums.place(x=0,y=350)
            self.btn_myalbums= Button(self.frame_myalbums, text='My Albums', width=12, font=('Roboto', 16),
                                 command=lambda:self.my_albums(self.tl, self.username))
            self.btn_myalbums.place(x=20,y=15)

#           --- Frame para Button 'Following' -----------------
            self.frame_following= Frame(self.tl, width=200, height=60, bg='lightblue')
            self.frame_following.place(x=0,y=410)
            self.lbl_following= Button(self.frame_following, text='Following', width=12, font=('Roboto', 16),
                                 command=lambda:self.my_albums(self.tl, self.username))
            self.lbl_following.place(x=20,y=15)

#           --- Button '+ Add' -----------------------------------
            self.add_content_btn = Button(self.tl, text = '+  Add', width = 14, height = 1, bg = '#28942a', fg = 'white', font = ('Roboto', 18), bd = 0, command = self.show_add_content_frame).place(x = 0, y = 470)
#           Frame que aparece quando o utilizador clica no botão '+ Add'
#           Aparecem os botões de fazer um Post e criar um Album
            self.add_content_frame = Frame(self.tl, width = 202, height = 150, bg = '#28942a')
            self.add_post = Button(self.add_content_frame, text = 'Add a Post', bg = '#28942a', font = ('Roboto', 14),fg = 'white', bd = 0, width = 20, 
                                   command = lambda: Add_Post(window, username))
            self.add_album = Button(self.add_content_frame, text = 'Create an Album', bg = '#28942a', font = ('Roboto', 14),fg = 'white', bd = 0, width = 20, 
                                    command = lambda: Create_Album(window, username))



#       ------------------------------- FUNÇÕES HOMEPAGE ----------------------------

        def get_selected_date(self):
            '''
            '''
            self.selected_date = self.cal.get_date()
            print(self.selected_date)
                

#       ----------- + POST Button ---------------------------------------------------
        
        def show_add_content_frame(self):
            """
            Esta função faz com que o Frame para adicionar um post apareça
            Dentro da Frame, aparece as opções de criar um post com uma imagem, ou criar um álbum novo
            """
            if self.add_content_frame.winfo_ismapped(): #Se o frame estiver na janela
                self.add_content_frame.place_forget()
                self.add_post.place_forget()
                self.add_album.place_forget()
            else:
                self.add_content_frame.place(x = 0, y = 510)
                self.add_post.place(x = 0, y = 5)
                self.add_album.place(x = 0, y = 50)


#       ----------- My Albums Button -------------------------------------------------

        def my_albums(self, tl, username):
            '''
            Abre uma Frame para mostrar os albums do user
            '''
            #Frame 
            self.f_my_albums= Frame(tl, width=800, height=540, bg='#fff')
            self.f_my_albums.place(x=200,y=60)
            btn_destroy_frame= Button(self.f_my_albums, text=' X ', command=self.f_my_albums.destroy)
            btn_destroy_frame.place(x=0,y=0)
            
#           --- Fazer os Álbums aparecer:
            #Meter numa variável a diretoria/pasta dos álbums do user
            self.albums_directory=('./users_photoalbums/'+ username) 
            
            # Listar os álbums
            album_folders = []
            for i in os.listdir(self.albums_directory): #Por cada folder
                full_path = os.path.join(self.albums_directory, i) #Está a juntar a diretoria user com a diretoria álbum em vez de usar concatenação
                if os.path.isdir(full_path): #se for uma folder
                    album_folders.append(i) #Adiciona o nome desse album á lista
            for idx, album_folder in enumerate(album_folders): #enumerate retorna o index idx e o valor(album_folder) de cada elemento da lista
                # Calcular row e col apartir do index
                row = idx // 4
                col = idx % 4
                btn_my_album = Button(self.f_my_albums, text=album_folder, bg='#f8d775', width=18, height=5,
                                    command=lambda tl=tl, username=username, folder=album_folder: self.open_my_album_frame(tl, folder, username))
                btn_my_album.grid(row=row, column=col, padx=30, pady=30)

        def open_my_album_frame(self, tl, album_folder, username):
            '''
            Cada Álbum abre uma nova Frame com Publicações e Comentários do Álbum
            '''
            from edit_albums import edit_album
            self.album_folder = album_folder  # para poder usar no file albums_comments
            # Frame do Album com os seus Posts
            self.f_my_album = Frame(tl, width=800, height=600, bg='pink')
            self.f_my_album.place(x=200, y=60)
            # Button Close Album
            btn_destroy_frame = Button(self.f_my_album, text=' X ', command=self.f_my_album.destroy)
            btn_destroy_frame.place(x=0, y=0)
            # Button Edit Album
            btn_edit_album = Button(self.f_my_album,text='Edit',
                                    command=edit_album)
            btn_edit_album.place(x=30,y=0)

            # Frame com Comentários
            self.f_my_album_comments = Frame(self.f_my_album, width=250, height=540, bg='pink')
            self.f_my_album_comments.place(x=588, y=50)
            Albums_Comments(self.f_my_album_comments, self.album_folder, self.username)



            # ----- Fazer os Posts aparecerem na Frame do Álbum ---------- 
            
            # Criar um path até ao Álbum clicado
            album_path = os.path.join('.\\users_photoalbums\\', username, self.album_folder) #não é necessário concatenação, nem \\
            
            # Listar os Posts do meu Álbum
            my_album_post = []
            for i in os.listdir(album_path): #por cada folder(post) dentro da folder(Álbum)
                full_path = os.path.join(album_path , i) #está a juntar a folder(álbum) com a folder(post) em vez de usar concatenação e '\\'
                if os.path.isdir(full_path): #se full_path for uma folder
                    my_album_post.append(i) #Adiciona o nome desse Post à lista

            # Frame dentro da Frame f_my_album para aparecerem os buttons/posts
            frame_myalbum_posts = Frame(self.f_my_album, bg='#fff', width=600, height=500)  # Corrected the typo here
            frame_myalbum_posts.place(x=0, y=50)
            
            # Cada Post vai ser um Button:
            for row, i in enumerate(my_album_post): #enumerate cria uma tuple que contém um index 'row' e o correspondente valor 'i' que pertence ao my_album_post
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
                    btn_my_post = Button(frame_myalbum_posts, image=photo, width=150, height=150,
                                        command=lambda img=resized_photo, image_path=image_path: Posts(frame_myalbum_posts, image_path, img, self.username))
                    btn_my_post.image = photo  #''garbage collection'' para a imagem não ser apagada automaticamente para criar memória livre
                else:
                    btn_my_post = Button(frame_myalbum_posts, text=i, width=40, height=5,
                                        command=lambda  img=resized_photo, image_path=image_path: Posts(frame_myalbum_posts, image_path, img, self.username))
                btn_my_post.grid(column=row % 3,  row=row // 3, padx=20, pady=10)

           
    def open_user_frame(self, username, tl):
            '''
            Verifica se o user existe 
            '''
            self.search_value = self.search_entry.get()
            # --- Fazer os Álbums aparecer:
            # Meter numa variável a diretoria/pasta dos álbums do user
            print('hi')
            print(self.search_value)
            user_folder = os.path.join("users_photoalbums", self.search_value)
            print(user_folder)
            if os.path.exists(user_folder):
                user_album_frame = Frame(tl, width=600, height=540)
                user_album_frame.place(x=300, y=60)
                user_album_frame.lift()

            # Listar os álbums
            user_album_folders = []
            for i in os.listdir(user_folder): #Por cada folder
                full_path = os.path.join(user_folder, i) #Está a juntar a diretoria user com a diretoria álbum em vez de usar concatenação
                if os.path.isdir(full_path): #se for uma folder
                    user_album_folders.append(i) #Adiciona o nome desse album á lista
            
            for idx, user_album_folder in enumerate(user_album_folders):
                # CalculaR row and column apartir do index
                row = idx // 4
                col = idx % 4
                btn_my_album = Button(user_album_frame, text=user_album_folder, bg='#f8d775', width=18, height=5,
                                    command=lambda tl=tl, username=username, folder=user_album_folder: self.open_user_album_frame(tl, folder, username))
                btn_my_album.grid(row=row, column=col, padx=30, pady=30)

# ---------------------------------------------------------------------------

    def open_user_album_frame(self, tl, user_album_folder, username):
            '''
            Cada Álbum abre uma nova Frame com Publicações e Comentários do Álbum
            '''
            
            self.user_album_folder=user_album_folder#para poder usar no file albums_comments
            # Frame com Publicações
            self.f_my_album= Frame(tl, width=800, height=600, bg='pink')
            self.f_my_album.place(x=200,y=60)
            # Frame com Comentários
            self.f_my_album_comments= Frame(tl, width=200, height=540, bg='blue')
            self.f_my_album_comments.place(x=800,y=60)
            Albums_Comments(self.f_my_album_comments, self.user_album_folder, self.username)

            

#           ----- Fazer os Posts aparecerem na Frame do Álbum ---------- 
            
            # Criar um path até ao Álbum clicado
            album_path = os.path.join('.\\users_photoalbums\\', username, self.user_album_folder) #não é necessário concatenação, nem \\
            
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
            scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
            scrollbar.grid(row=0, column=1, sticky="ns")  # Place scrollbar on the right side

            # Configure the canvas to scroll vertically
            canvas.configure(yscrollcommand=scrollbar.set)
            # Configure the column weights
            self.f_my_album.grid_columnconfigure(0, weight=1)  # Make column 0 (canvas) expandable

            # Ensure that the canvas expands with the frame
            self.f_my_album.update_idletasks()  # Update the layout to get the correct size
            canvas.config(scrollregion=canvas.bbox("all"))  # Update scroll region to include the actual size

            # Adjust the placement of the scrollbar
            scrollbar.place(x=600, y=0, height=600)
  




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
