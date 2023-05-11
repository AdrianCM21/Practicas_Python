import customtkinter as ctk
import tkinter as tk
from table import generate_table

# Modos : Light, Dark, System
# "System" el que use el SO
ctk.set_appearance_mode("System")

# Colores soportados: green, dark-blue, blue
ctk.set_default_color_theme("green")

# Tamano de la ventana
appWidth, appHeight = 600, 700

datos = []

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Titulo de la ventana
        self.title("GUI Application")
        # Fija el tamano de la ventana
        self.geometry(f"{appWidth}x{appHeight}")

        # Label Nombre
        self.diaLabel = ctk.CTkLabel(self, text="Dia: ")
        self.diaLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Caja de texto
        self.diaEntry = ctk.CTkEntry(self, placeholder_text="1")
        self.diaEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        # Label de Edad
        self.pesoLabel = ctk.CTkLabel(self, text="Peso: ")
        self.pesoLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        # Caja de Edad
        self.pesoEntry = ctk.CTkEntry(self,  placeholder_text="18")
        self.pesoEntry.grid(row=1, column=1, columnspan=3, padx=20,  pady=20, sticky="ew")


        # Gender Radio Buttons
        self.genderVar = tk.StringVar(value="No responde")

        self.bajoRadioButton = ctk.CTkRadioButton(self, text="Bajo",variable=self.genderVar, value="Bajo")
        self.bajoRadioButton.grid(row=2, column=1,  padx=20, pady=20,  sticky="ew")

        self.subioRadioButton = ctk.CTkRadioButton(self, text="Subio", variable=self.genderVar,  value="Subio")
        self.subioRadioButton.grid(row=2, column=2, padx=20, pady=20, sticky="ew")

        self.mantuvoRadioButton = ctk.CTkRadioButton(self, text="mantuvo", variable=self.genderVar,  value="Mantuvo")
        self.mantuvoRadioButton.grid(row=2, column=3, padx=20, pady=20, sticky="ew")

        # Boton
        self.generateResultsButton = ctk.CTkButton(self, text="Generar", command=self.generateResults)
        self.generateResultsButton.grid(row=5, column=1, columnspan=2, padx=20,    pady=20, sticky="ew")

        # Boton tabla
        self.generateResultsButton = ctk.CTkButton(self, text="Abrir", command= lambda: self.abrirtabla(self.diaEntry.get(), self.pesoEntry.get(),   self.genderVar.get(), datos))
        self.generateResultsButton.grid(row=6, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

        # Caja de texto
        self.displayBox = ctk.CTkTextbox(self,  width=200, height=100)
        self.displayBox.grid(row=7, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")

    def abrirtabla(self, nombre, edad, genero, datos):
        datos.append([nombre, edad, genero])
        table_window = tk.Toplevel()
        generate_table(datos, table_window)

    def generateResults(self):
        self.displayBox.delete("0.0", "200.0")
        text = self.createText()
        self.displayBox.insert("0.0", text)


    def createText(self):
        checkboxValue = ""
        text = f"Dia: {self.diaEntry.get()} : \nPeso: {self.pesoEntry.get()} {checkboxValue}\n"
        text += f"{self.genderVar.get()}"

        return text


if __name__ == "__main__":
    app = App()
    app.mainloop()