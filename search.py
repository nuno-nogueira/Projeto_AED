from tkinter import *
from tkinter import ttk
from homepage import *

def func_search_results_window(tl, search_entry, lbox_categ, selected_date):
    '''
    Abre uma Frame para mostrar resultados de pesquisa
    '''
    f_results= Frame(tl, width=600, height=600)
    f_results.place(x=200,y=60)
    btn_destroy_frame= Button(f_results, text=' X ', command=f_results.destroy)
    btn_destroy_frame.place(x=550,y=30)

    #Treeview
    tree = ttk.Treeview(f_results, columns = ("Utilizador", "Categoria", "Data"), show = "headings", height = 12, selectmode = "browse")
    tree.column("Utilizador", width = 220, anchor = "w")
    tree.column("Categoria", width = 100, anchor = "c")
    tree.column("Data", width = 220, anchor = "c")

    tree.heading("Utilizador", text = "Utilizador")
    tree.heading("Categoria", text = "Categoria")
    tree.heading("Data", text = "Data")
    tree.place(x=20, y=90)

    # Buscar o ficheiro 'all-posts'
    f_all_posts=open('./files/all-posts.txt')
    read_f_all_posts=f_all_posts.readlines()
    f_all_posts.close()
    search_value = search_entry.get() #para buscar o valor de search_entry que já está definida como uma String no ficheiro Homepage.py
    
    # ---- Pesquisa -----------
    #Search Entry bar (username OU categoria de fotos)
    for line in read_f_all_posts: #Por cada post
        if search_value== '': #Se a barra de pesquisa estiver vazia
            continue
        if line.split(";")[0] == search_value or line.split(";")[1] == search_value: #Se o que estiver na barra for igual à posição 0 ou 1 da linha
            tree.insert("", "end", values=(line.split(";")[0], line.split(";")[1], line.split(";")[2]))
    
    #Search Listbox
    selected_indexes = lbox_categ.curselection()
    selected_items = []
    for index in selected_indexes:
        item = lbox_categ.get(index)
        selected_items.append(item.strip())
    for line in read_f_all_posts:  
        category = str(line.split(";")[1])
        if category in str(selected_items):
            tree.insert("", "end", values=(line.split(";")[0], line.split(";")[1], line.split(";")[2]))
    #Search data
    for line in read_f_all_posts:
        date = str(line.split(";")[2])  #coverter para string para poder comparar
        if date == str(selected_date):  #coverter para string para poder comparar
            tree.insert("", "end", values=(line.split(";")[0], line.split(";")[1], line.split(";")[2]))