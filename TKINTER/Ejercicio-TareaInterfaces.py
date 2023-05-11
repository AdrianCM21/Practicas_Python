import tkinter
import customtkinter

def button_funtion(e):
    
    if (e==1):
        aux=int(label_div._text)+1
    elif(e==2):
        aux=int(label_div._text)-1
    label_div.configure(text=aux)
    if(label_div._text==10):  
        Labelmas.configure(text=(int(Labelmas._text)+1))
        label_div.configure(text=0)
    elif(label_div._text==-10):
        Labelmen.configure(text=(int(Labelmen._text)+1))
        label_div.configure(text=0)
root_tk = tkinter.Tk()

root_tk.geometry('700x440')
root_tk.title('CustomTkinter Test')

button_arriba = customtkinter.CTkButton(master=root_tk,text='+',width=50,corner_radius=10,command=lambda:button_funtion(1),font=('Inter',14))

button_abajo = customtkinter.CTkButton(master=root_tk,text='-',width=50,corner_radius=10,command=lambda:button_funtion(2),font=('Inter',14))

label_div = customtkinter.CTkLabel(master=root_tk,text='0',width=120,height=25,corner_radius=8)


Labelmas = customtkinter.CTkLabel(master=root_tk,text='0',width=120,height=25,corner_radius=8)
Labelmen = customtkinter.CTkLabel(master=root_tk,text='0',width=120,height=25,corner_radius=8)



button_arriba.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
button_abajo.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
label_div.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

Labelmas.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)
Labelmen.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)
root_tk.mainloop()