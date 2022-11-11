#importar libreria
from tkinter import *
from tkinter import messagebox


#definir funciones
def ordenar():
    if int(n1.get())>int(n2.get()) and int(n2.get())>int(n3.get()):
        t_resultados.insert(INSERT, "el orden es "+n1.get()+", "+n2.get()+", "+n3.get())
    elif int(n2.get())>int(n1.get()) and int(n1.get())>int(n3.get()):
        t_resultados.insert(INSERT, "el orden es "+n2.get()+", "+n1.get()+", "+n3.get())
    elif int(n3.get())>int(n1.get()) and int(n1.get())>int(n2.get()):
        t_resultados.insert(INSERT, "el orden es "+n3.get()+", "+n1.get()+", "+n2.get()) 
    elif int(n3.get())>int(n2.get()) and int(n2.get())>int(n1.get()):
        t_resultados.insert(INSERT, "el orden es "+n3.get()+", "+n2.get()+", "+n1.get())
    elif int(n1.get())>int(n3.get()) and int(n3.get())>int(n2.get()):
        t_resultados.insert(INSERT, "el orden es "+n1.get()+", "+n3.get()+", "+n2.get())
    elif int(n2.get())>int(n3.get()) and int(n3.get())>int(n1.get()):
        t_resultados.insert(INSERT, "el orden es "+n2.get()+", "+n3.get()+", "+n1.get())  
    else :
        t_resultados.insert(INSERT, " Todos los numeros son iguales")  
def borrar():
    n1.set("")
    n2.set("")
    n3.set("")
    t_resultados.delete("0.1", "end")

def cerrar():
    messagebox.showinfo( "Orden","La app se cerrara...")
    ventana_principal.destroy()

ventana_principal=Tk()
ventana_principal.title("Ordenar tres numeros en orden ascendente")
ventana_principal.geometry("700x600")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="light coral")
#definir_variables_globales
n1=StringVar()
n2=StringVar()
n3=StringVar()



#crear_frame_entrada
fr_entrada=Frame(ventana_principal)
fr_entrada.config(bg="powder blue", width=680, height=230)
fr_entrada.place(x=10, y=5)

#crear_frame_operaciones
fr_oper=Frame(ventana_principal)
fr_oper.config(bg="powder blue", width=680, height=160)
fr_oper.place(x=10, y=250)

#crear_frame_resultados
fr_salida=Frame(ventana_principal)
fr_salida.config(bg="powder blue", width=680, height=160)
fr_salida.place(x=10, y=430)

#crear_texto
titulo_pr=Label(fr_entrada, text="Ordenar numeros")
titulo_pr.config(bg="powder blue", fg="black" ,font=("Times", 20))
titulo_pr.place(x=20 ,y=15)
#numeros
n1_lb=Label(fr_entrada, text="Digite un numero:")
n1_lb.config(bg="powder blue", fg="black", font=("arial", 13))
n1_lb.place(x=20, y=130)

n2_lb=Label(fr_entrada, text="Digite un numero:")
n2_lb.config(bg="powder blue", fg="black", font=("arial", 13))
n2_lb.place(x=260, y=130)

n3_lb=Label(fr_entrada, text="Digite un numero:")
n3_lb.config(bg="powder blue", fg="black", font=("arial", 13))
n3_lb.place(x=500, y=130)
#recibir numeros
rec_1=Entry(fr_entrada, textvariable=n1)
rec_1.config(font=("Arial",15), justify=LEFT,)
rec_1.focus_set()
rec_1.place(x=20 ,y=165, width=160)

rec_2=Entry(fr_entrada, textvariable=n2)
rec_2.config(font=("Arial",15), justify=LEFT,)
rec_2.place(x=260 ,y=165, width=160)

rec_3=Entry(fr_entrada, textvariable=n3)
rec_3.config(font=("Arial",15), justify=LEFT,)
rec_3.place(x=500 ,y=165, width=160)

#button resolver
bt_or=Button(fr_oper, text="ordenar", command=ordenar )
bt_or.place(x=30 , y=60, width=140)
#button cerrar
bt_ce=Button(fr_oper, text="Cerrar", command=cerrar )
bt_ce.place(x=500 , y=60, width=140)
#BUTTON LIMPIAR
bt_sumar = Button(fr_oper, text="Borrar", command=borrar)
bt_sumar.place(x=260, y=60, width=140, )
#respuesta
t_resultados = Text(fr_salida)
t_resultados.config(bg="white", fg="black", font=("Arial",25))
t_resultados.place(x=10,y=10, width=660, height= 130)
ventana_principal.mainloop()