import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def generate_table(datos, window):

    columns = ('dia', 'peso', 'estado')
    tree = ttk.Treeview(window, columns=columns, show='headings')
    tree.heading('dia', text='Dia')
    tree.heading('peso', text='Peso')
    tree.heading('estado', text='Estado')

    for dato in datos:
        print(dato)
        tree.insert('', tk.END, values=dato)

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            showinfo(title='Informacion', message=(record[0]))

    tree.bind('<<TreeviewSelect>>', item_selected)
    tree.grid(row=0, column=0, sticky='nsew')