import tkinter
import customtkinter

def button_funtion():
    peso= entryPeso.get()
    altura=entryAltura.get()
    labelResultado.configure(text=float(peso)/float(altura)**2)

    
root_tk = tkinter.Tk()

root_tk.geometry('700x440')
root_tk.title('CustomTkinter Test')

button_Convercion = customtkinter.CTkButton(master=root_tk,text='Convertir',width=50,corner_radius=10,command=button_funtion,font=('Inter',14))



entryPeso = customtkinter.CTkEntry(master=root_tk,width=170,height=30,corner_radius=8,validatecommand=( '%i'))
entryAltura = customtkinter.CTkEntry(master=root_tk,width=170,height=30,corner_radius=8)

labelPeso = customtkinter.CTkLabel(master=root_tk,text='Ingrese su peso:',width=120,height=25,corner_radius=8)
labelAltura = customtkinter.CTkLabel(master=root_tk,text='Ingrese su altura:',width=120,height=25,corner_radius=8)
labelResultado = customtkinter.CTkLabel(master=root_tk,text='Peso:',width=120,height=25,corner_radius=8)





button_Convercion.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
entryPeso.place(relx=0.6, rely=0.3, anchor=tkinter.CENTER)
entryAltura.place(relx=0.6, rely=0.4, anchor=tkinter.CENTER)

labelPeso.place(relx=0.4, rely=0.3, anchor=tkinter.CENTER)
labelAltura.place(relx=0.4, rely=0.4, anchor=tkinter.CENTER)
labelResultado.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
root_tk.mainloop()