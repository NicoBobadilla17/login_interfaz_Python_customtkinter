import customtkinter #libreria

customtkinter.set_appearance_mode('dark') #apariencia de modo oscuro
customtkinter.set_default_color_theme('green') #color verde

root = customtkinter.CTk()
root.geometry('450x400') #tamaño de la interfaz

def login(): #funcion de cuando estemos logueados
    print('Bienvenido')
    
frame = customtkinter.CTkFrame(master=root)#nuestra raiz

frame.pack(pady=30, padx=60, fill='both', expand=True) #tamaño

label = customtkinter.CTkLabel(master=frame, text='Login')

label.pack(pady=12, padx=10)

entrada1 = customtkinter.CTkEntry(master=frame, placeholder_text='Usuario')#entrada de usuario
entrada1.pack(padx=10, pady=12)#tamaño

entrada2 = customtkinter.CTkEntry(master=frame, placeholder_text='Contraseña', show='*')
entrada2.pack(padx=10, pady=12)#tamaño

button = customtkinter.CTkButton(master=frame, text='Login', command=login,)
button.pack(padx=10, pady=12)

root.mainloop()










