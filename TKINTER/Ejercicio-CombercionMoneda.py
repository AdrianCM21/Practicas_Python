import tkinter
import customtkinter

def button_funtion():
    tex= entry.get()
    labelP.configure(text=int(tex)*0.03)
    labelE.configure(text=int(tex)*0.00013)
    labelD.configure(text=int(tex)*0.00014)
    
root_tk = tkinter.Tk()

root_tk.geometry('700x440')
root_tk.title('CustomTkinter Test')

button_Convercion = customtkinter.CTkButton(master=root_tk,text='Convertir',width=50,corner_radius=10,command=button_funtion,font=('Inter',14))



entry = customtkinter.CTkEntry(master=root_tk,width=170,height=30,corner_radius=8)
labelD = customtkinter.CTkLabel(master=root_tk,text='0',width=120,height=25,corner_radius=8)
labelE = customtkinter.CTkLabel(master=root_tk,text='0',width=120,height=25,corner_radius=8)
labelP = customtkinter.CTkLabel(master=root_tk,text='0',width=120,height=25,corner_radius=8)
labelD1 = customtkinter.CTkLabel(master=root_tk,text='Dolar:',width=120,height=25,corner_radius=8)
labelE1 = customtkinter.CTkLabel(master=root_tk,text='Euro:',width=120,height=25,corner_radius=8)
labelP1 = customtkinter.CTkLabel(master=root_tk,text='Peso:',width=120,height=25,corner_radius=8)





button_Convercion.place(relx=0.6, rely=0.3, anchor=tkinter.CENTER)
entry.place(relx=0.4, rely=0.3, anchor=tkinter.CENTER)
labelD.place(relx=0.4, rely=0.4, anchor=tkinter.CENTER)
labelE.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)
labelP.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
labelD1.place(relx=0.2, rely=0.4, anchor=tkinter.CENTER)
labelE1.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)
labelP1.place(relx=0.2, rely=0.6, anchor=tkinter.CENTER)
root_tk.mainloop()