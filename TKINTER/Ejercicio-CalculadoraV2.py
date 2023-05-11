import customtkinter as ctk
import tkinter as tk


# Modos : Light, Dark, System
# "System" el que use el SO
ctk.set_appearance_mode("System")

# Colores soportados: green, dark-blue, blue
ctk.set_default_color_theme("green")

# Tamano de la ventana
appWidth, appHeight = 600, 500



class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Titulo de la ventana
        self.title("GUI Application")
        # Fija el tamano de la ventana
        self.geometry(f"{appWidth}x{appHeight}")

        # Label Nombre
        self.nameLabel = ctk.CTkLabel(self,
                                      text="Name")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        # Caja de texto
        self.aEntry = ctk.CTkEntry(self)
        self.aEntry.grid(row=1, column=1,
                            columnspan=1, padx=20,
                            pady=20, sticky="ew")


        # Caja de Edad
        self.bEntry = ctk.CTkEntry(self)
        self.bEntry.grid(row=1, column=2,
                           columnspan=1, padx=20,
                           pady=20, sticky="ew")

        # Gender Label
        self.genderLabel = ctk.CTkLabel(self,
                                        text="Operaciones")
        self.genderLabel.grid(row=2, column=0,
                              padx=10, pady=20,
                              sticky="ew")

        # Gender Radio Buttons
        self.genderVar = tk.StringVar(value="s")

        self.sumaRadioButton = ctk.CTkRadioButton(self,
                                                  text="Suma",
                                                  variable=self.genderVar,
                                                  value="s")
        self.sumaRadioButton.grid(row=2, column=1,
                                  padx=5, pady=20,
                                  sticky="ew")

        self.restaRadioButton = ctk.CTkRadioButton(self,
                                                  text="Resta",
                                                  variable=self.genderVar,
                                                  value="r")
        self.restaRadioButton.grid(row=2, column=2,
                                  padx=5, pady=20,
                                  sticky="ew")


        self.multiplicacionRadioButton = ctk.CTkRadioButton(self,
                                                    text="Multiplicacion",
                                                    variable=self.genderVar,
                                                    value="m")
        self.multiplicacionRadioButton.grid(row=2, column=3,
                                    padx=5, pady=20,
                                    sticky="ew")
        
        self.divicionRadioButton = ctk.CTkRadioButton(self,
                                                    text="Divicion",
                                                    variable=self.genderVar,
                                                    value="d")
        self.divicionRadioButton.grid(row=2, column=4,
                                    padx=5, pady=20,
                                    sticky="ew")


        # Boton
        self.generateResultsButton = ctk.CTkButton(self,
                                                   text="=",
                                                   command=self.generateResults)
        self.generateResultsButton.grid(row=5, column=1,
                                        columnspan=1, padx=20,
                                        pady=20, sticky="ew")

        # Caja de texto
        self.displayBox = ctk.CTkTextbox(self,
                                         width=200,
                                         height=100)
        self.displayBox.grid(row=6, column=0,
                             columnspan=4, padx=20,
                             pady=20, sticky="nsew")


    def generateResults(self):
        self.displayBox.delete("0.0", "200.0")
        text = self.createText()
        self.displayBox.insert("0.0", text)


    def createText(self):
        ope =self.genderVar.get()
        if ope=='s':
            text = int(self.aEntry.get())+int(self.bEntry.get())
        elif ope=='r':
            text = int(self.aEntry.get())-int(self.bEntry.get())
        elif ope=='m':
            text = int(self.aEntry.get())*int(self.bEntry.get())
        elif ope=='d':
            text = int(self.aEntry.get())/int(self.bEntry.get())
       
        return text


if __name__ == "__main__":
    app = App()
    app.mainloop()