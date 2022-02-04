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

# Frame anidado P6
frame_P6 = Frame(master=frame_P2, width=450, height=500, borderwidth=2, relief="groove")
frame_P6.pack(fill="both", expand=True, padx=5, pady=5)
#label_photo = Label(frame_P6)


window.mainloop()