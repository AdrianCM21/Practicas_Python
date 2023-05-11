import tkinter
import customtkinter



def button_funtion():
    print('Buton press')
    e_text = entry2.get()+entry.get()
    Label.configure(text=e_text)

customtkinter.set_appearance_mode('dark')
root_tk = tkinter.Tk()

root_tk.geometry('700x440')
root_tk.title('CustomTkinter Test')

button = customtkinter.CTkButton(master=root_tk,corner_radius=10,command=button_funtion,font=('Inter',14))

entry = customtkinter.CTkEntry(master=root_tk,width=170,height=30,corner_radius=8)
entry2 = customtkinter.CTkEntry(master=root_tk,width=170,height=30,corner_radius=8)


Label = customtkinter.CTkLabel(master=root_tk,text='CTkLabel',width=120,height=25,corner_radius=8)

button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

entry.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)
entry2.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)
Label.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
root_tk.mainloop()