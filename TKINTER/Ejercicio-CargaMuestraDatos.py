import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import mysql.connector



# Modos : Light, Dark, System
# "System" el que use el SO
ctk.set_appearance_mode("System")

# Colores soportados: green, dark-blue, blue
ctk.set_default_color_theme("green")

# Tamano de la ventana
appWidth, appHeight = 1000, 700

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='practica'
)

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Titulo de la ventana
        self.title("GUI Application")
        # Fija el tamano de la ventana
        self.geometry(f"{appWidth}x{appHeight}")

        self.sel={}
        # Label Raza
        self.diaLabel = ctk.CTkLabel(self, text="Raza: ")
        self.diaLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Caja de texto
        self.diaEntry = ctk.CTkEntry(self, placeholder_text="Pirucbul")
        self.diaEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        # Label Nombre Mascota
        self.mascotaLabel = ctk.CTkLabel(self, text="Mascota: ")
        self.mascotaLabel.grid(row=25, column=0, padx=20, pady=10, sticky="ew")

        # Caja de texto Mascota
        self.mascotaEntry = ctk.CTkEntry(self, placeholder_text="Adivina")
        self.mascotaEntry.grid(row=25, column=1, columnspan=3, padx=20, pady=10, sticky="ew")


        # Boton
        self.BottonGuardadRaza = ctk.CTkButton(self, text="Guardar Raza", command=self.cargarRaza)
        self.BottonGuardadRaza.grid(row=5, column=1, columnspan=2, padx=20,    pady=20, sticky="ew")

        self.ButtonGuardarMascota = ctk.CTkButton(self, text="Guardar Mascota", command=self.cargarMascota)
        self.ButtonGuardarMascota.grid(row=27, column=1, columnspan=2, padx=20,    pady=20, sticky="ew")
       
        # Caja de texto
        self.displayBox = ctk.CTkTextbox(self,  width=200, height=100)
        self.displayBox.grid(row=7, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")

        # Tabla de razas
        columns = ('id', 'raza')
        self.tree = ttk.Treeview( self.master,columns=columns, show='headings')
        self.tree.heading('id', text='ID')
        self.tree.heading('raza', text='RAZA')
        self.cargaRaza()
        
        # Tabla de Mascotas
        columnsMascota = ('id', 'nombre','raza')
        self.treeMascota = ttk.Treeview( self.master,columns=columnsMascota, show='headings')
        self.treeMascota.heading('id', text='ID')
        self.treeMascota.heading('nombre', text='NOMBRE')
        self.treeMascota.heading('raza', text='RAZA')
        self.cargaMascota()
        self.treeMascota.grid(row=25, column=5,padx=10, rowspan=8,pady=10, sticky='nsew')

        # Combo box
        self.combobox = ttk.Combobox(self.master, state="readonly")
        self.combobox.grid(column=1, row=26)
        self.combobox.bind("<<ComboboxSelected>>", self.seleccioncombo)
        self.cargar_combo()

    def seleccioncombo(self,event):
        llaveselecionada = self.combobox.get()
        self.seleccionado = self.sel.get(llaveselecionada)


    def cargar_combo(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM raza")
        filas = mycursor.fetchall()

        for fila in filas:
            llave = fila[1]
            valor = fila[0]
            self.sel[llave] = valor
        self.combobox['values'] = list( self.sel.keys())

    def cargarRaza(self):
        self.displayBox.delete("0.0", "200.0")
        text = self.insertarBd()
        self.cargaRaza()
        self.displayBox.insert("0.0", text)
        self.cargar_combo()

    def cargarMascota(self):
        self.insertarBdMascota()
        self.cargaMascota()

    def insertarBd(self):
        mycursor = mydb.cursor()
        sql = 'INSERT INTO raza(Description) VALUES(%s)'
        val = [self.diaEntry.get(),]
        mycursor.execute(sql,val)
        mydb.commit()
        text = self.diaEntry.get()
        return text
    
    def insertarBdMascota(self):
        mycursor = mydb.cursor()
        sql = 'INSERT INTO mascotas(Mascota,Raza) VALUES(%s,%s)'
        val = [self.mascotaEntry.get(),self.seleccionado]
        mycursor.execute(sql,val)
        mydb.commit()
        return
    def cargaRaza(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT IDRaza,Description	 FROM raza")
        datos = mycursor.fetchall()
        for row in self.tree.get_children():
            self.tree.delete(row)
        for dato in datos:
            self.tree.insert('', tk.END, values=dato)
        self.tree.grid(row=0, column=5,padx=10, rowspan=8,pady=10, sticky='nsew')

        

    def cargaMascota(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT mascotas.IDMascota, mascotas.Mascota, raza.Description	 FROM mascotas inner join raza on mascotas.Raza = raza.IDRaza")
        datos = mycursor.fetchall()
        for row in self.treeMascota.get_children():
            self.treeMascota.delete(row)
        for dato in datos:
            self.treeMascota.insert('', tk.END, values=dato)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()