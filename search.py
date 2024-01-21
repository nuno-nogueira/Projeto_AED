from tkinter import *
from tkinter import ttk
from homepage import *
from datetime import datetime

def func_search_results_window(tl, search_entry, lbox_categ, selected_date):
    '''
    Abre uma Frame para mostrar resultados de pesquisa
    '''
    f_results= Frame(tl, width=600, height=600)
    f_results.place(x=200,y=60)
    btn_destroy_frame= Button(f_results, text=' X ', command=f_results.destroy)
    btn_destroy_frame.place(x=550,y=30)

    #Treeview
    tree = ttk.Treeview(f_results, columns = ("User", "Category", "Date"), show = "headings", height = 12, selectmode = "browse")
    tree.column("User", width = 220, anchor = "w")
    tree.column("Category", width = 100, anchor = "c")
    tree.column("Date", width = 220, anchor = "c")

    tree.heading("User", text = "User")
    tree.heading("Category", text = "Category")
    tree.heading("Date", text = "Date")
    tree.place(x=20, y=90)

    # Buscar o ficheiro 'all-posts'
    file_all_posts=open('./files/all-posts.txt')
    read_file_all_posts=file_all_posts.readlines()
    file_all_posts.close()
    search_value = search_entry.get() #para buscar o valor de search_entry que já está definida como uma String no ficheiro Homepage.py
    
    # ---- Pesquisa -----------
    # Search Entry bar (username OU Category de fotos)
    for line in read_file_all_posts: #Por cada post
        if search_value== '': #Se a barra de pesquisa estiver vazia
            continue
        if (line.split(";")[0] == search_value) or (line.split(";")[1] == search_value): #Se o que estiver na barra for igual à posição 0 da linha
            tree.insert("", "end", values=(line.split(";")[0], line.split(";")[1], line.split(";")[2])) 
    tree.delete()
    #Search Listbox
    selected_listbox_values = lbox_categ.curselection()
    selected_items = []
    for index in selected_listbox_values:
        item = lbox_categ.get(index)
        selected_items.append(item.strip())
        tree.delete()
    for line in read_file_all_posts:  
        category = str(line.split(";")[1])
        if category in str(selected_items):
            tree.insert("", "end", values=(line.split(";")[0], line.split(";")[1], line.split(";")[2]))
    tree.delete()
    #Search Date
    for line in read_file_all_posts:
        date = str(line.split(";")[2])  #coverter para string para poder comparar
        print(date)
        print('seeeee', selected_date)
        if date == str(selected_date):  #coverter para string para poder comparar
            tree.insert("", "end", values=(line.split(";")[0], line.split(";")[1], line.split(";")[2]))
        tree.delete()
    


    #Abrir um Post na Treeview através do Button ''See Post''
    btn_select_searched_post= Button(f_results, text='See Post', font=('Roboto, 14'))
    btn_select_searched_post.place(x=100,y=500)

def open_tree_post():
        '''
        '''
        print('hi')
        













