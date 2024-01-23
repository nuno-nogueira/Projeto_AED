from tkinter import *
from tkinter import ttk
from homepage import *
from datetime import datetime
import os
from posts import Posts
from albums_comments import Albums_Comments

def func_search_results_window(tl, search_entry, lbox_categ, get_selected_date):
    '''
    Abre uma Frame para mostrar resultados de pesquisa
    '''
    #Frame para mostrar resultados
    f_results= Frame(tl, width=600, height=700)
    f_results.place(x=200,y=60)
    btn_destroy_frame= Button(f_results, text=' X ', command=f_results.destroy)
    btn_destroy_frame.place(x=550,y=30)

    #Treeview
    tree = ttk.Treeview(f_results, columns = ("User", "Category", "Date"), show = "headings", height = 8, selectmode = "browse")
    tree.column("User", width = 150, anchor = "w")
    tree.column("Category", width = 150, anchor = "c")
    tree.column("Date", width = 150, anchor = "c")
    tree.heading("User", text = "User")
    tree.heading("Category", text = "Category")
    tree.heading("Date", text = "Date")
    tree.place(x=20, y=90) 

    #Buscar o ficheiro 'all-posts'
    file_all_posts=open('./files/all-posts.txt', 'r')
    read_file_all_posts=file_all_posts.readlines()
    file_all_posts.close()
    search_value = search_entry.get() #para buscar o valor de search_entry que já está definida como uma String no ficheiro Homepage.py
     
    # ---- Pesquisa de Posts -----------
    
    tree.delete()

    #Search Entry bar:
    for line in read_file_all_posts: #Por cada post
        if search_value== '': #Se a barra de pesquisa estiver vazia
            continue
        if (line.split(";")[0] == search_value) or (line.split(";")[1] == search_value): #Se o que estiver na barra for igual à posição 0 da linha
            tree.insert("", "end", values=(line.split(";")[0], line.split(";")[1], line.split(";")[2])) 

    #Search Listbox:
    selected_listbox_values = lbox_categ.curselection()
    selected_items = []
    for index in selected_listbox_values:
        item = lbox_categ.get(index)
        selected_items.append(item.strip())
        
    for line in read_file_all_posts:  
        category = str(line.split(";")[1])
        if category in str(selected_items):
            tree.insert("", "end", values=(line.split(";")[0], line.split(";")[1], line.split(";")[2])) 
    
    #Search Date 
    if not get_selected_date == '':  
        get_selected_date = str(get_selected_date)
        for line in read_file_all_posts:
            date = str(line.split(";")[2])  #coverter para string para poder comparar
            if date == get_selected_date: 
                tree.insert("", "end", values=(line.split(";")[0], line.split(";")[1], line.split(";")[2])) 
    
    #Button 'Clear history'
    btn_clear_tree= Button(f_results, text='Clear history',
                           command=lambda: clear_tree(tree))
    btn_clear_tree.place(x=30,y=500)
    
    #Abrir um Post na Treeview através do Button ''See Post''
    btn_select_searched_post= Button(f_results, text='See Post', font=('Roboto, 14'),
                                command=lambda:open_tree_post(tree, TclVersion))
    btn_select_searched_post.place(x=100,y=500)
   

def clear_tree(tree):
        '''
        Button 'Clear Search history' retira o conteúdo da tree
        '''
        tree.delete(*tree.get_children())

def open_tree_post(tree, tl):
        '''
        
        '''
        selected_item = tree.selection()

        if selected_item:
            user, album, post_name, category, date = tree.item(selected_item, "values")
            
            users_path = os.path.join('users_photoalbums', user)
            
            if os.path.exists(users_path): # Check if the user folder exists
                album_path = os.path.join(users_path, album)
                
                if os.path.exists(album_path): # Check if the album folder exists
                    post_path = os.path.join(album_path, post_name)
                
                    if os.path.exists(post_path): # Check if the post folder exists
                        print(f"{post_name} is in album.")
                
                        tl_post= Toplevel(tl)
                        tl_post.geometry('900x600+100-100') 
                        tl_post.title('MyPhotos')
                        tl_post.resizable(0,0) 
                        tl_post.configure(bg = 'lightgrey')














