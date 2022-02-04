from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry('820x400')
window.title('Inicio')
window.option_add('*tearOff', FALSE)  # Eliminar underline


# --------------------------------------------------------------
# ------------------- Eventos ventana inicio -------------------
#Descripcion del sistema
def info():
    frame_P3.pack_forget()
    label_P3.place_forget()
    label_inf = Label(master=frame_P3,
          text="Nuestro CRM busca administrar clientes y \n"
               "vender productos de forma sistematizada, \n"
               "bien sea por contratos o ventas individuales.\n "
               "¡Ingresa a nuestro sistema y vive la experiencia!", font="Helvetica 10")
    label_inf.place(x=0, y=25)
    frame_P3.pack(side=TOP, fill="both", expand=True, padx=5, pady=5)

def evento():
    window.deiconify()
    window.destroy()

def inicioCrm():
    crm_ppal = Toplevel()
    crm_ppal.geometry('900x600')
    crm_ppal.title('CRM')
    window.iconify()
    crm_ppal.option_add('*tearOff', FALSE)  # Eliminar underline

    # --------------------------------------------------------------
    # ----------------- Eventos ventana de usuario ------------------
    def ventanaInicio():
        window.deiconify()
        crm_ppal.destroy()

    def act():
        messagebox.showinfo(title="Nuestras funcionalidades",
                            message="Recuerda, con nosotros puedes realizar ventas, devoluciones, ejecutar/finalizar contratos y enviar información masiva a quien pueda interesar.",
                            detail="¡Gracias por elegirnos como tu CRM!")

    def evento():
        window.deiconify()
        window.destroy()

    def venta():
        pass

    def dev():
        pass

    def ejec_contra():
        pass

    def fin_contra():
        pass

    def masivo():
        pass

    def inf():
        messagebox.showinfo(title="Fundadores de Nuestro CRM",
                            message="Leidy Daniela Alzate Florez - Estudiante de matemáticas - Juan Daniel Bula Isaza - Estudiante de estadística - Oscar Andrés Usuga Nanclares - Estudiante de ciencias de la computación",
                            detail="Universidad Nacional De Colombia")

    pane_crm = PanedWindow(master=crm_ppal, orient=VERTICAL)
    pane_crm.pack(fill=BOTH, expand=True)

    # ZONA 1
    zona1 = PanedWindow(master=pane_crm, orient=HORIZONTAL)
    zona1.pack(fill=BOTH, expand=True)
    pane_crm.add(zona1)
    #zona1.pack(fill=BOTH, expand=1)
    #top = Label(pane_crm, text="top pane")
    #pane_crm.add(top)
    # Botones de zona1
    archivo = Button(zona1, text="Archivo", command=quit)
    archivo.pack()
    zona1.add(archivo)

    procesos = Button(zona1, text="Procesos y Consultas", command=quit)
    procesos.pack()
    zona1.add(procesos)

    ayuda = Button(zona1, text="Ayuda", command=quit)
    ayuda.pack()
    zona1.add(ayuda)

    # ZONA 2
    zona2 = PanedWindow(master=pane_crm, orient=VERTICAL)
    zona2.pack(fill=BOTH, expand=True)
    pane_crm.add(zona2)

    nombre_proceso = Label(zona2, text="Nombre del proceso o consulta")
    zona2.add(nombre_proceso)

    descripcion_proceso = Label(zona2, text="Descripcion del detalle del proceso o la consulta")
    zona2.add(descripcion_proceso)



    # --------------------------------------------------------------
    # ------------------- Menú ventana de usuario -------------------
    '''menubar2 = Menu(crm_ppal)
    menu1 = Menu(menubar2)
    menu2 = Menu(menubar2)
    menu3 = Menu(menubar2)

    menubar2.add_cascade(menu=menu1, label='Archivo', command=evento)
    menubar2.add_cascade(menu=menu2, label='Procesos y Consultas', command=evento)
    menubar2.add_cascade(menu=menu3, label='Ayuda', command=evento)

    menu1.add_command(label="Aplicación", command=act)
    menu1.add_command(label="Volver a ventana de inicio", command=ventanaInicio)

    menu2.add_command(label="Realizar una venta", command=venta)
    menu2.add_command(label="Realizar devolución", command=dev)
    menu2.add_command(label="Ejecutar contrato de cliente", command=ejec_contra)
    menu2.add_command(label="Finalizar contrato de cliente", command=fin_contra)
    menu2.add_command(label="Enviar información masiva", command=masivo)

    menu3.add_command(label="Acerca de:", command=inf)

    crm_ppal['menu'] = menubar2
'''
# Eventos del ratón para cambiar hojas de vida
def show_names(e):
    descripcion.pack_forget()
    leidy.pack()
    oscar.pack()
    juan.pack()
    frame_P5.bind("<Button-1>", show_leidy)

def show_leidy(e):
    global descripcion
    oscar.pack_forget()
    juan.pack_forget()

    descripcion = Label(master=frame_P5, text='Estudiante de matemáticas', font="Helvetica 12")
    descripcion.pack()
    frame_P5.bind("<Button-1>", show_oscar)

def show_oscar(e):
    global descripcion
    descripcion.pack_forget()
    leidy.pack_forget()
    juan.pack_forget()
    oscar.pack()
    descripcion = Label(master=frame_P5, text="Estudiante de Ciencias de la Computacion", font="Helvetica 12")
    descripcion.pack()
    frame_P5.bind("<Button-1>", show_juan)

def show_juan(e):
    global descripcion
    descripcion.pack_forget()
    leidy.pack_forget()
    oscar.pack_forget()
    juan.pack()
    descripcion = Label(master=frame_P5, text="Estudiante de estadística. \n Apasionado por la ciencia de datos y el fútbol", font="Helvetica 12")
    descripcion.pack()
    frame_P5.bind("<Button-1>", show_names)

# Eventos del ratón para cambiar imágenes en ventana inicio
def change_img1(e):
    global label_img
    label_img.pack_forget()
    label_img = Label(master=frame_P4)
    photo_img = PhotoImage(file='images/crm3.png')
    photo_img = photo_img.subsample(2)
    label_img['image'] = photo_img
    label_img.pack()
    #label_img.bind("<Enter>", change_img2)

'''def change_img2(e):
    global label_img
    label_img.pack_forget()
    label_img = Label(master=frame_P4)
    photo_img = PhotoImage(file='images/crm4.png')
    photo_img = photo_img.subsample(2)
    label_img['image'] = photo_img
    label_img.pack()
    label_img.bind("<Enter>", change_img1)
'''

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
frame_P1 = Frame(master=outer_frame, borderwidth=2, relief="groove")
frame_P1.pack(side='left', fill="both", expand=True, padx=5, pady=5)

# Frame anidado P3
frame_P3 = Frame(master=frame_P1, width=295, borderwidth=2, relief="groove")
label_P3 = Label(master=frame_P3, text='¡Hola! \n \n ¡Bienvenidos a nuestro CRM!', font="Helvetica 14")
frame_P3.pack(side=TOP, fill="both", expand=True, padx=5, pady=5)
label_P3.place(x=0, y=25)

# Frame anidado P4
frame_P4 = Frame(master=frame_P1, borderwidth=2, relief="groove")
frame_P4.pack(side=BOTTOM)#padx=5, pady=5)

label_img = Label(master=frame_P4)
photo_img = PhotoImage(file='images/crm2.png')
photo_img = photo_img.subsample(2)
label_img['image'] = photo_img
label_img.pack()

boton_ingreso = Button(master=frame_P4, text='Ingresar al sistema', font="Helvetica 14 bold", command=inicioCrm)
boton_ingreso.pack()

# Control del cursor para cambio en imagenes
label_img.bind("<Enter>", change_img1)


# ------- Frame principal P2 -------
frame_P2 = Frame(master=outer_frame, borderwidth=2, relief="groove")
frame_P2.pack(side='right', fill="both", expand=True, padx=5, pady=5)

# Frame anidado P5
frame_P5 = Frame(master=frame_P2, borderwidth=2, relief="groove")
frame_P5.pack(fill="both", expand=True, padx=5, pady=5)

# Nombre de cada integrante
label_P5 = Label(master=frame_P5, text='\n Desarrolladores:', font="Helvetica 14")
label_P5.pack()
leidy = Label(master=frame_P5, text="Leidy Daniela", font="Helvetica 12")
leidy.pack()
oscar = Label(master=frame_P5, text='Oscar Andres', font="Helvetica 12")
oscar.pack()
juan = Label(master=frame_P5, text="Juan Daniel", font="Helvetica 12")
juan.pack()

# Control del cursor para cambio en hojas de vida
frame_P5.bind("<Button-1>", show_leidy)

# Frame anidado P6
frame_P6 = Frame(master=frame_P2, borderwidth=2, relief="groove")
frame_P6.pack(fill="both", expand=True, padx=5, pady=5)
#label_photo = Label(frame_P6)


# -----------------------------------------------------
# ----------- Posicionamiento Grid de fotos -----------
# Foto Leidy
label_leidy = Label(master=frame_P6)
photo_leidy = PhotoImage(file='photos/leidy.png')
photo_leidy = photo_leidy.subsample(3)
label_leidy['image'] = photo_leidy
label_leidy.grid(row=0, column=0)
# Foto Oscar
label_oscar = Label(master=frame_P6)
photo_oscar = PhotoImage(file='photos/oscar.png')
photo_oscar = photo_oscar.subsample(2)
label_oscar['image'] = photo_oscar
label_oscar.grid(row=0, column=1)
# Foto Juan Daniel
label_juan = Label(master=frame_P6)
photo_juan = PhotoImage(file='photos/juandaniel.png')
photo_juan = photo_juan.subsample(4)
label_juan['image'] = photo_juan
label_juan.grid(row=0, column=3)



window.mainloop()