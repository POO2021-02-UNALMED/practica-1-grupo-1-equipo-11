from tkinter import *

window = Tk()
window.geometry('900x600')
window.title('Inicio')
window.option_add('*tearOff', FALSE)  # Eliminar underline


# -----------------------------------------------
# ------------------- Eventos -------------------

#Descripcion del sistema
def info():
    inf = Label(master=frame_P3,
          text="Nuestro CRM busca administrar \n clientes, mejorar la relación \n entre ellos y vender productos \n de forma sistematizada, bien sea por contratos \n o ventas individuales.\n ¡Ingresa a nuestro sistema y vive la experiencia!").pack()

def evento():
    window.deiconify()
    window.destroy()

def inicioCrm():
    crm_ppal = Toplevel()
    crm_ppal.geometry('900x600')
    crm_ppal.title('CRM')
    window.iconify()
    def ventanaInicio():
        window.deiconify()
        crm_ppal.destroy()
    boton_salida = Button(crm_ppal, text = 'Volver a ventana principal', width = "50", height = "10", font="Helvetica 18 bold", command = ventanaInicio)
    boton_salida.pack()

# Eventos del ratón
def show_names(e):
    descripcion.pack_forget()
    leidy.pack()
    oscar.pack()
    juan.pack()
    leidy.bind("<Button-1>", show_leidy)
    oscar.bind("<Button-1>", show_oscar)
    juan.bind("<Button-1>", show_juan)

def show_leidy(e):
    global descripcion
    oscar.pack_forget()
    juan.pack_forget()

    descripcion = Label(master=frame_P5, text='Estudiante de matemáticas', font="Helvetica 12")
    descripcion.pack()
    leidy.bind("<Button-1>", show_names)

def show_oscar(e):
    global descripcion
    leidy.pack_forget()
    juan.pack_forget()

    descripcion = Label(master=frame_P5, text="Estudiante de Ciencias de la Computacion", font="Helvetica 12")
    descripcion.pack()
    oscar.bind("<Button-1>", show_names)

def show_juan(e):
    global descripcion
    leidy.pack_forget()
    oscar.pack_forget()

    descripcion = Label(master=frame_P5, text="Estudiante de estadística. \n Apasionado por la ciencia de datos y el fútbol", font="Helvetica 12")
    descripcion.pack()
    juan.bind("<Button-1>", show_names)


# ------------------------------------------------
# ----------------  Barra de Menú ----------------
menubar = Menu(window)
menu1 = Menu(menubar)
menubar.add_cascade(menu=menu1, label='Inicio', command=evento)
menu1.add_command(label="Nosotros", command=info)
menu1.add_command(label="Salir de la aplicación", command=evento)
window['menu'] = menubar


# -------------------------------------------------
# --------------- Ventana de inicio ---------------

# ----------  Outer Frame ----------
outer_frame = Frame(window)
outer_frame.pack(side="top", fill="both", expand=True, padx=20, pady=20)

# ------- Frame principal P1 -------
frame_P1 = Frame(master=outer_frame, width=450, height=600, borderwidth=2, relief="groove")
frame_P1.pack(side='left', fill="both", expand=True, padx=5, pady=5)

# Frame anidado P3
frame_P3 = Frame(master=frame_P1, width=450, height=100, borderwidth=2, relief="groove")
label_P3 = Label(master=frame_P3, text='¡Hola! \n \n ¡Bienvenidos a nuestro CRM!', font="Helvetica 18")

frame_P3.pack(fill="both", expand=True, padx=5, pady=5)
label_P3.pack()

# Frame anidado P4
frame_P4 = Frame(master=frame_P1, width=450, height=600, borderwidth=2, relief="groove")
boton_ingreso = Button(master=frame_P4, text='Ingresar al sistema', font="Helvetica 18 bold", command=inicioCrm)
frame_P4.pack(fill="both", expand=True, padx=5, pady=5)
boton_ingreso.pack()

# ------- Frame principal P2 -------
frame_P2 = Frame(master=outer_frame, width=450, height=600, borderwidth=2, relief="groove")
frame_P2.pack(side='right', fill="both", expand=True, padx=5, pady=5)

# Frame anidado P5
frame_P5 = Frame(master=frame_P2, width=450, height=100, borderwidth=2, relief="groove")
frame_P5.pack(fill="both", expand=True, padx=5, pady=5)

# Nombre de cada integrante
label_P5 = Label(master=frame_P5, text='Hoja de vida \n', font="Helvetica 18")
label_P5.pack()
leidy = Label(master=frame_P5, text="Leidy Daniela", font="Helvetica 16")
leidy.pack()
oscar = Label(master=frame_P5, text='Oscar Andres', font="Helvetica 16")
oscar.pack()
juan = Label(master=frame_P5, text="Juan Daniel", font="Helvetica 16")
juan.pack()

# Control del cursor
leidy.bind("<Button-1>", show_leidy)
oscar.bind("<Button-1>", show_oscar)
juan.bind("<Button-1>", show_juan)

# Frame anidado P6
frame_P6 = Frame(master=frame_P2, width=450, height=500, borderwidth=2, relief="groove")
frame_P6.pack(fill="both", expand=True, padx=5, pady=5)
#label_photo = Label(frame_P6)


# -----------------------------------------------------
# ----------- Posicionamiento Grid de fotos -----------
# Foto Leidy
label_leidy = Label(master=frame_P6)
photo_leidy = PhotoImage(file=r'./photos/leidy.png')
photo_leidy = photo_leidy.subsample(3)
label_leidy['image'] = photo_leidy
label_leidy.grid(row=0, column=0)
# Foto Oscar
label_oscar = Label(master=frame_P6)
photo_oscar = PhotoImage(file=r'./photos/oscar.png')
photo_oscar = photo_oscar.subsample(2)
label_oscar['image'] = photo_oscar
label_oscar.grid(row=0, column=1)
# Foto Juan Daniel
label_juan = Label(master=frame_P6)
photo_juan = PhotoImage(file=r'./photos/juandaniel.png')
photo_juan = photo_juan.subsample(4)
label_juan['image'] = photo_juan
label_juan.grid(row=0, column=3)

window.mainloop()