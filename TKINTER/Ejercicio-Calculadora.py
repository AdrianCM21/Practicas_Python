import tkinter
import customtkinter


def button_funtion(e):
    if (e==1):
        e_text = int(entry2.get())+int(entry.get())
    elif  (e==2):
        e_text = int(entry2.get())-int(entry.get())
    elif  (e==3):
        e_text = int(entry2.get())*int(entry.get())
    else :
        e_text = int(entry2.get())/int(entry.get())
    Label.configure(text=e_text)

root_tk = tkinter.Tk()

root_tk.geometry('700x440')
root_tk.title('CustomTkinter Test')

button_sum = customtkinter.CTkButton(master=root_tk,text='Sumar',corner_radius=10,command=lambda:button_funtion(1),font=('Inter',14))

button_res = customtkinter.CTkButton(master=root_tk,text='Restar',corner_radius=10,command=lambda:button_funtion(2),font=('Inter',14))
button_mul = customtkinter.CTkButton(master=root_tk,text='Multiplicar',corner_radius=10,command=lambda:button_funtion(3),font=('Inter',14))
button_div = customtkinter.CTkButton(master=root_tk,text='dividir',corner_radius=10,command=lambda:button_funtion(4),font=('Inter',14))

entry = customtkinter.CTkEntry(master=root_tk,width=70,height=30,corner_radius=8)
entry2 = customtkinter.CTkEntry(master=root_tk,width=70,height=30,corner_radius=8)


Label = customtkinter.CTkLabel(master=root_tk,text='CTkLabel',width=120,height=25,corner_radius=8)

button_sum.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)
button_res.place(relx=0.4, rely=0.3, anchor=tkinter.CENTER)
button_mul.place(relx=0.6, rely=0.3, anchor=tkinter.CENTER)
button_div.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)

entry.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)
entry2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
Label.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
root_tk.mainloop()