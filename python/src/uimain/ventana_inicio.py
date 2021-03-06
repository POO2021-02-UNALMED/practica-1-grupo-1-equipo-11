import os.path
from tkinter import *
from tkinter import messagebox


window = Tk()
window.geometry('820x440')
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
    label_inf.place(x=50, y=50)
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

    # --------------------------------------------------------------
    # ------------------- Menú ventana de usuario -------------------
    pane_crm = PanedWindow(master=crm_ppal, orient=VERTICAL)
    pane_crm.pack(fill=BOTH, expand=True)

    # ZONA 1
    zona1 = PanedWindow(master=pane_crm, orient=HORIZONTAL)
    zona1.pack(fill=BOTH, expand=True)
    pane_crm.add(zona1)

    # Botones de zona1
    archivo = Menubutton(zona1, text="Archivo", activebackground='lightblue')
    archivo.pack(side=LEFT)
    zona1.add(archivo)

    procesos = Menubutton(zona1, text="Procesos y Consultas", activebackground='lightblue')
    procesos.pack(side=LEFT)
    zona1.add(procesos)

    ayuda = Menubutton(zona1, text="Ayuda", activebackground='lightblue')
    ayuda.pack(side=LEFT)
    zona1.add(ayuda)

    # Configurando menús
    archivo.menu = Menu(archivo, tearoff=0)
    archivo["menu"] = archivo.menu
    archivo.menu.add_command(label="Aplicación", command=act)
    archivo.menu.add_command(label="Volver a ventana de inicio", command=ventanaInicio)

    procesos.menu = Menu(procesos, tearoff=0)
    procesos["menu"] = procesos.menu
    procesos.menu.add_command(label="Realizar una venta", command=venta)
    procesos.menu.add_command(label="Realizar devolución", command=dev)
    procesos.menu.add_command(label="Ejecutar contrato de cliente", command=ejec_contra)
    procesos.menu.add_command(label="Finalizar contrato de cliente", command=fin_contra)
    procesos.menu.add_command(label="Enviar información masiva", command=masivo)

    ayuda.menu = Menu(ayuda, tearoff=0)
    ayuda["menu"] = ayuda.menu
    ayuda.menu.add_command(label="Acerca de", command=inf)

    # ZONA 2
    zona2 = PanedWindow(master=pane_crm, orient=VERTICAL)
    zona2.pack(fill=BOTH, expand=True)
    pane_crm.add(zona2)

    nombre_proceso = Label(zona2, text="Nombre del proceso o consulta")
    zona2.add(nombre_proceso)

    descripcion_proceso = Label(zona2, text="Descripcion del detalle del proceso o la consulta")
    zona2.add(descripcion_proceso)


# Eventos del ratón para cambiar hojas de vida
def show_names(e):
    descripcion.pack_forget()
    frame_P6.pack_forget()
    leidy.pack()
    oscar.pack()
    juan.pack()
    label_photo1['image'] = photo_leidy
    label_photo2['image'] = photo_oscar
    label_photo3['image'] = photo_juan
    label_photo4['image'] = photo_blanco
    frame_P6.pack()

    frame_P5.bind("<Button-1>", show_leidy)

def show_leidy(e):
    global descripcion
    oscar.pack_forget()
    juan.pack_forget()
    descripcion = Label(master=frame_P5, text='Estudiante de matemáticas', font="Helvetica 12")
    descripcion.pack()

    frame_P6.pack_forget()
    label_photo1['image'] = photo_leidy1
    label_photo2['image'] = photo_leidy2
    label_photo3['image'] = photo_leidy3
    label_photo4['image'] = photo_leidy4
    frame_P6.pack()

    frame_P5.bind("<Button-1>", show_oscar)

def show_oscar(e):
    global descripcion
    descripcion.pack_forget()
    leidy.pack_forget()
    juan.pack_forget()
    oscar.pack()
    descripcion = Label(master=frame_P5, text="Estudiante de Ciencias de la Computacion", font="Helvetica 12")
    descripcion.pack()

    frame_P6.pack_forget()
    label_photo1['image'] = photo_oscar1
    label_photo2['image'] = photo_oscar2
    label_photo3['image'] = photo_oscar3
    label_photo4['image'] = photo_oscar4
    frame_P6.pack()

    frame_P5.bind("<Button-1>", show_juan)

def show_juan(e):
    global descripcion
    descripcion.pack_forget()
    leidy.pack_forget()
    oscar.pack_forget()
    juan.pack()
    descripcion = Label(master=frame_P5, text="Estudiante de estadística", font="Helvetica 12")
    descripcion.pack()

    frame_P6.pack_forget()
    label_photo1['image'] = photo_juan1
    label_photo2['image'] = photo_juan2
    label_photo3['image'] = photo_juan3
    label_photo4['image'] = photo_juan4
    frame_P6.pack()

    frame_P5.bind("<Button-1>", show_names)

# Eventos del ratón para cambiar imágenes en ventana inicio
def change_img2(e):
    frame_P4.pack_forget()
    label_img['image'] = img2
    frame_P4.pack(side=BOTTOM)
    label_img.bind('<Enter>', change_img3)

def change_img3(e):
    frame_P4.pack_forget()
    label_img['image'] = img3
    frame_P4.pack(side=BOTTOM)
    label_img.bind('<Enter>', change_img4)

def change_img4(e):
    frame_P4.pack_forget()
    label_img['image'] = img4
    frame_P4.pack(side=BOTTOM)
    label_img.bind('<Enter>', change_img5)

def change_img5(e):
    frame_P4.pack_forget()
    label_img['image'] = img5
    frame_P4.pack(side=BOTTOM)
    label_img.bind('<Enter>', change_img1)

def change_img1(e):
    frame_P4.pack_forget()
    label_img['image'] = img1
    frame_P4.pack(side=BOTTOM)
    label_img.bind('<Enter>', change_img2)
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
label_P3.place(x=65, y=45)

# Frame anidado P4
frame_P4 = Frame(master=frame_P1, borderwidth=2, relief="groove")
frame_P4.pack(side=BOTTOM)#padx=5, pady=5)

# Cargar imágenes
img2 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/images/crm2.png')
img2 = img2.subsample(2)
img3 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/images/crm3.png')
img3 = img3.subsample(2)
img4 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/images/crm4.png')
img4 = img4.subsample(2)
img5 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/images/crm5.png')
img5 = img5.subsample(2)
img1 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/images/LOGOU.png')
img1 = img1.subsample(2)

label_img = Label(master=frame_P4)
label_img['image'] = img2
label_img.pack()

boton_ingreso = Button(master=frame_P4, text='Ingresar al sistema', font="Helvetica 14 bold", command=inicioCrm)
boton_ingreso.pack(side=BOTTOM)

# Control del cursor para cambio en imagenes
label_img.bind("<Enter>", change_img2)


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
Label(master=frame_P5, text="\n", font="Helvetica 12").pack(side=BOTTOM)

# Control del cursor para cambio en hojas de vida
frame_P5.bind("<Button-1>", show_leidy)

# Frame anidado P6
frame_img = Frame(master=frame_P2, borderwidth=2, relief="groove")
frame_img.pack(fill="both", expand=True, padx=5, pady=5)
frame_P6 = Frame(master=frame_img)
frame_P6.pack()

# ----------- Posicionamiento Grid de fotos -----------
# Cargar fotos Leidy
photo_leidy = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/leidy.png')
photo_leidy = photo_leidy.subsample(4)
photo_leidy1 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/leidy1.png')
photo_leidy1 = photo_leidy1.subsample(3)
photo_leidy2 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/leidy2.png')
photo_leidy2 = photo_leidy2.subsample(3)
photo_leidy3 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/leidy3.png')
photo_leidy3 = photo_leidy3.subsample(3)
photo_leidy4 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/leidy4.png')
photo_leidy4 = photo_leidy4.subsample(3)

# Cargar fotos Oscar
photo_oscar = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/oscar.png')
photo_oscar = photo_oscar.subsample(4)
photo_oscar1 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/oscar1.png')
photo_oscar1 = photo_oscar1.subsample(3)
photo_oscar2 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/oscar2.png')
photo_oscar2 = photo_oscar2.subsample(3)
photo_oscar3 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/oscar3.png')
photo_oscar3 = photo_oscar3.subsample(3)
photo_oscar4 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/oscar4.png')
photo_oscar4 = photo_oscar4.subsample(3)

# Cargar fotos Juan Daniel
photo_juan = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/juandaniel.png')
photo_juan = photo_juan.subsample(4)
photo_juan1 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/juandaniel1.png')
photo_juan1 = photo_juan1.subsample(3)
photo_juan2 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/juandaniel2.png')
photo_juan2 = photo_juan2.subsample(3)
photo_juan3 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/juandaniel3.png')
photo_juan3 = photo_juan3.subsample(3)
photo_juan4 = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/juandaniel4.png')
photo_juan4 = photo_juan4.subsample(3)

photo_blanco = PhotoImage(file=f'{os.path.dirname(os.path.abspath(__file__))}/photos/blanco.png')
photo_blanco = photo_blanco.subsample(4)

# Fotos por persona en grid
label_photo1 = Label(master=frame_P6)
label_photo1['image'] = photo_leidy
label_photo1.grid(row=0, column=0)

label_photo2 = Label(master=frame_P6)
label_photo2['image'] = photo_oscar
label_photo2.grid(row=0, column=1)

label_photo3 = Label(master=frame_P6)
label_photo3['image'] = photo_juan
label_photo3.grid(row=1, column=0)

label_photo4 = Label(master=frame_P6)
label_photo4['image'] = photo_blanco
label_photo4.grid(row=1, column=1)

window.mainloop()