from tkinter import*
from tkinter import messagebox,ttk
import tkinter as tk


#Funciones de la APP
def calcular_IMC():
    peso = float(entry_e.get())
    altura = float(entry_d.get())
    imc = round(peso / (altura ** 2), 2)
    t_resultados.insert(INSERT, f"el IMC del estdiante {imc}\n")
   

def calcular_Prom():
    Nota1 = float(entry_f.get())
    Nota2 = float(entry_g.get())
    Nota3 = float(entry_h.get())
    Nota4 = float(entry_i.get())
    promedio = round((Nota1 + Nota2 + Nota3 +Nota4) / 4, 2)
    t_resultados.insert(INSERT, f"Promedio del estudiante: {promedio}\n")

def borrar():
    messagebox.showinfo("Datos Medicos", "Se borraran todos los datos")
    nombre_estudiante.set("")
    Peso.set("")
    Altura.set("")
    Nota1.set("")
    Nota2.set("")
    Nota3.set("")
    Nota4.set("")
    t_resultados.delete("1.0", "end")


def salir():
    messagebox.showinfo("Datos Medicos", "La APP se cerrara, ¿Desea continuar?")
    ventana_principal.destroy()


#Diseño de la app
ventana_principal = tk.Tk( )

# Cargar el archivo de imagen desde el disco.
icono = tk.PhotoImage(file="img\informemedico.png")

# Establecerlo como ícono de la ventana.
ventana_principal.iconphoto(True, icono)

#Titulo de la ventana
ventana_principal.title("Datos Medicos")

#Tamaño de la ventana
ventana_principal.geometry("500x800")

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fonde de la ventana
ventana_principal.config(bg="magenta")

#Variables de control
nombre_estudiante = StringVar()
Altura = StringVar()
Peso = StringVar()
Nota1 = StringVar()
Nota2 = StringVar()
Nota3 = StringVar()
Nota4 = StringVar()
AC = ["15", "16", "17", "18", "19", "20","21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50"]
AC_selected = StringVar()


#Ventana secundaria superior
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=250)
frame_entrada.place(x=10, y=20)

#Logo de la ONG
logo = PhotoImage(file="img\logo_medico_toplavel.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=11, y=1)

#Informacion del paciente
lb_titulo = Label(frame_entrada, text="Datos del estudiante")
lb_titulo.config(bg="white", fg="purple", font=("Viner hand ITC", 18))
lb_titulo.place(x=230, y=10)

#Etiqueta para Paciente
lb_a = Label(frame_entrada, text="Estudiante: ")
lb_a.config(bg="white", fg="Red", font=("times new roman", 17))
lb_a.place(x=225, y=60)

#Caja de texto 
entry_a = Entry(frame_entrada, textvariable=nombre_estudiante)
entry_a.config(bg="white", fg="Black", font=("Bahnschrift Light", 12))
entry_a.focus_set()
entry_a.place(x=335, y=60, width=129, height=30)

#recoleccion de datos
lb_titulo = Label(frame_entrada, text="recoleccion de datos")
lb_titulo.config(bg="white", fg="lime green", font=("Viner hand ITC", 18))
lb_titulo.place(x=230, y=120)
#recoleccion de datos medicos
lb_titulo = Label(frame_entrada, text="Datos academicos")
lb_titulo.config(bg="white", fg="orange", font=("Footlight MT Light", 18))
lb_titulo.place(x=290, y=200)
#recoleccion de datos academicos
lb_titulo = Label(frame_entrada, text="Datos medicos")
lb_titulo.config(bg="white", fg="orange", font=("Footlight MT Light", 18))
lb_titulo.place(x=10, y=200)
#Ventana secundaria intermedio
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=310)
frame_operaciones.place(x=10, y=265)

#Etiqueta para Altura
lb_d = Label(frame_operaciones, text="Altura(M): ")
lb_d.config(bg="white", fg="violet", font=("Viner hand ITC", 13))
lb_d.place(x=10, y=30)

#Caja de texto
entry_d = Entry(frame_operaciones, textvariable=Altura)
entry_d.config(bg="white", fg="Black", font=("Footlight MT Light", 12))
entry_d.place(x=113, y=30, width=115, height=30)

#Etiqueta para Peso corporal
lb_e = Label(frame_operaciones, text="Peso(Kg): ")
lb_e.config(bg="white", fg="violet", font=("Viner hand ITC", 15))
lb_e.place(x=10, y=120)

#Caja de texto
entry_e = Entry(frame_operaciones, textvariable=Peso)
entry_e.config(bg="white", fg="Black", font=("Footlight MT Light", 12))
entry_e.place(x=113, y=120, width=115, height=30)

#Etiqueta para Nota 1
lb_f = Label(frame_operaciones, text="Nota 1: ")
lb_f.config(bg="white", fg="violet", font=("Viner hand ITC", 15))
lb_f.place(x=240, y=10)

#Caja de texto
entry_f = Entry(frame_operaciones, textvariable=Nota1)
entry_f.config(bg="white", fg="Black", font=("Footlight MT Light", 12))
entry_f.place(x=320, y=10, width=115, height=30)

#Etiqueta para Nota 2
lb_g = Label(frame_operaciones, text="Nota 2: ")
lb_g.config(bg="white", fg="violet", font=("Viner hand ITC", 15))
lb_g.place(x=240, y=60)

#Caja de texto
entry_g = Entry(frame_operaciones, textvariable=Nota2)
entry_g.config(bg="white", fg="Black", font=("Footlight MT Light", 12))
entry_g.place(x=320, y=60, width=115, height=30)

#Etiqueta para Nota 3
lb_h = Label(frame_operaciones, text="Nota 3: ")
lb_h.config(bg="white", fg="violet", font=("Viner hand ITC", 15))
lb_h.place(x=240, y=115)

#Caja de texto
entry_h = Entry(frame_operaciones, textvariable=Nota3)
entry_h.config(bg="white", fg="Black", font=("Footlight MT Light", 12))
entry_h.place(x=320, y=115, width=115, height=30)

#Etiqueta para Nota 4
lb_i = Label(frame_operaciones, text="Nota 4: ")
lb_i.config(bg="white", fg="violet", font=("Viner hand ITC", 15))
lb_i.place(x=240, y=165)

#Caja de texto
entry_i = Entry(frame_operaciones, textvariable=Nota4)
entry_i.config(bg="white", fg="Black", font=("Footlight MT Light", 12))
entry_i.place(x=320, y=165, width=115, height=30)

#Boton de calcular IMC
bt_calcular=Button(frame_operaciones, text="calcular IMC", command=calcular_IMC)
bt_calcular.place(x=10, y=220,width=100, height=30)

#Boton de calcular Promedio
bt_calcular=Button(frame_operaciones, text="calcular promedio", command=calcular_Prom)
bt_calcular.place(x=130, y=220,width=100, height=30)

#Boton de Borrar
bt_calcular=Button(frame_operaciones, text="Borrar", command=borrar)
bt_calcular.place(x=250, y=220,width=100, height=30)

#Boton de salir
bt_salir=Button(frame_operaciones, text="salir", command=salir)
bt_salir.place(x=370, y=220,width=100, height=30)


#Ventana secundaria inferior
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=575)

#Area de texto para resultados
t_resultados=Text(frame_resultados)
t_resultados.config(bg="black", fg="green", font=("Courier", 20))
t_resultados.place(x=10, y=10, width=460, height=160)

#Correr el programa
ventana_principal.mainloop()