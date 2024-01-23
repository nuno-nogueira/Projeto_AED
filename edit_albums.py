from tkinter import *
import os
from tkinter import messagebox

def edit_album(username, album_folder, f_my_album):
    '''
    Permite ao user editar os seus PhotoAlbums
    '''
    # Toplevel para ferramentas de edição
    edit_album_tl = Toplevel(f_my_album)
    edit_album_tl.geometry('400x200')
    edit_album_tl.title("Edit Album")
    # Label new name
    lbl_change_name = Label(edit_album_tl, text="New Album Name:")
    lbl_change_name.pack()
    # Entry new name
    new_name_entry = Entry(edit_album_tl)
    new_name_entry.pack()
    # Button Save Changes
    btn_change_name = Button(edit_album_tl, text="Save Changes", bg='pink', command=lambda: change_album_name(new_name_entry, album_folder))
    btn_change_name.pack()

    # Label delete
    lbl_change_name = Label(edit_album_tl, text="Do you wish to delete your Album?")
    lbl_change_name.pack()
    # Button delete Album
    btn_delete = Button(edit_album_tl, text="Delete Album", bg='red', command=lambda:delete_album(album_folder))
    btn_delete.pack()

    def change_album_name(new_name_entry, album_folder):
        '''
        Mudar o nome do Album
        '''
        new_name = new_name_entry.get()
        if new_name:
            #path original do album e path nova do album
            original_path = os.path.join('./users_photoalbums', username, album_folder)
            new_path = os.path.join('./users_photoalbums', username, new_name)
            #mudar o nome
            os.rename(original_path, new_path)
            edit_album_tl.destroy()
            messagebox.showinfo('Album name changed. Reopen your Albums to confim.') 

    def delete_album(album_folder):
        '''
        Eliminar o Album
        '''
        # Path do album
        album_path = os.path.join('./users_photoalbums', username, album_folder)
        # Eliminar a folder e os conteúdos
        for file_or_subfolder in os.listdir(album_path): #por cada item no album
            file_or_subfolder_path = os.path.join(album_path, file_or_subfolder) #cria path de todos os itens
            if os.path.isdir(file_or_subfolder_path): #se for folder, delete
                delete_folder(file_or_subfolder_path)
            else: #se for file, delete também
                os.remove(file_or_subfolder_path)

        # Depois de eliminar o conteúdo, eliminar o Album
        os.rmdir(album_path)
        messagebox.showinfo('Album deleted. Reopen your Albums to confim.') 


    def delete_folder(folder_path):
        '''
        Para eliminar uma pasta
        '''
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                delete_folder(item_path)
            else:
                os.remove(item_path)
        os.rmdir(folder_path)

