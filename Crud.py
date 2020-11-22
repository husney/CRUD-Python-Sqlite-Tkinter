from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Crud")
bg_principal = "#b4c1d9"
root.config(bg=bg_principal)

coneto = False

idB = StringVar()
nombre = StringVar()
apellido = StringVar()
password = StringVar()
direccion = StringVar()


#Funciones
def abrirDb():
    entro = False
    try:
        global conecto
        conexion = sqlite3.connect("DBUSUARIOS")
        cursor = conexion.cursor()
        messagebox.showinfo("Base de datos", "Conectado Correctamente a la Base de datos")
        entro = True
        conecto = True
    except:
        messagebox.showerror("Base de datos", "Error al conectarse a la Base de datos")

    if entro:
        try:
            cursor.execute("""
                    CREATE TABLE USUARIOS(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NOMBRE VARCHAR(20),
                        APELLIDO VARCHAR(20),
                        PASSWORD VARCHAR(20),
                        DIRECCION VARCHAR(100),
                        COMENTARIOS VARCHAR(200)
                    );            
            """)
        except:
            pass

def salir():
    op = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if op == "yes":
        exit()

def sqlOperaciones(op):
    conexion = sqlite3.connect("DBUSUARIOS")
    cursor = conexion.cursor()
    if op == 1:
        cursor.execute(
            "INSERT INTO USUARIOS(NOMBRE, APELLIDO, PASSWORD, DIRECCION, COMENTARIOS)"+
            "VALUES"+
            "('"+ nombre.get() +"',"+
            "'"+ apellido.get() + "',"+
            "'"+password.get()+ "',"+
            "'"+direccion.get()+"',"+
            "'"+comentariosText.get("1.0",END)+"')"
        )
        conexion.commit()
        print("Guardado") 
        limpiar()

    if op == 2:
        cursor.execute("SELECT * FROM USUARIOS WHERE ID = "+idB.get())
        datos = cursor.fetchall()
        idB.set(datos[0][0])
        nombre.set(datos[0][1])
        apellido.set(datos[0][2])
        password.set(datos[0][3])
        direccion.set(datos[0][4])
        comentariosText.insert(1.0,datos[0][5])
        limpiar()

    if op == 3:
        cursor.execute(
            "UPDATE USUARIOS SET NOMBRE = '"+nombre.get()+"',"+
            "APELLIDO = '"+apellido.get()+"',"+
            "PASSWORD = '"+password.get()+"',"+
            "DIRECCION = '"+direccion.get()+"',"+
            "COMENTARIOS = '"+comentariosText.get("1.0", END)+"'"+
            "WHERE ID = "+idB.get()
        )
        conexion.commit()
        limpiar()

    if op == 4:
        cursor.execute("DELETE FROM USUARIOS WHERE ID = "+idB.get())
        conexion.commit()
        limpiar()
    
      
def limpiar():
    idB.set("")
    nombre.set("")
    apellido.set("")
    password.set("")
    direccion.set("")
    comentariosText.delete(1.0, END)

def licencia():
    messagebox.showinfo("Licencia", "Este programa ha sido creado con fines educativos")

def acercaDe():
    messagebox.showinfo("Acerca de", "Este programa crea un pequeño fichero sql lite y trabaja sobre el")


#Menu

menuBar = Menu(root)

root.config(menu = menuBar)

archivo = Menu(menuBar, tearoff=0)
archivo.add_command(label="Abrir DB", command=abrirDb)
archivo.add_command(label="Salir", command=salir)

crud = Menu(menuBar, tearoff=0)
crud.add_command(label="Create", command=lambda:sqlOperaciones(1))
crud.add_command(label="Read", command=lambda:sqlOperaciones(2))
crud.add_command(label="Update", command=lambda:sqlOperaciones(3))
crud.add_command(label="Delete", command=lambda:sqlOperaciones(4))

ayuda = Menu(menuBar, tearoff=0)
ayuda.add_command(label="Licencia", command=licencia)
ayuda.add_command(label="Acerca de", command=acercaDe)

menuBar.add_cascade(label="Archivo", menu=archivo)
menuBar.add_cascade(label="CRUD", menu=crud)
menuBar.add_cascade(label="Ayuda", menu=ayuda)



#FrameBody



frameBody = Frame(root, width=400, height=300, bg=bg_principal )
frameBody.pack(fill="both", expand="True")
frameBody.grid_propagate(False)
#Elementos del FrameBody


idlbl = Label(frameBody, text="ID: ", bg=bg_principal)
idlbl.grid(row=0, column=0, pady=10, padx=10)

idEntry = Entry(frameBody, textvariable=idB)
idEntry.grid(row=0, column=1, pady=10, padx=10)


nombrelbl = Label(frameBody, text="Nombre: ", bg=bg_principal)
nombrelbl.grid(row=1, column=0, pady=10, padx=10)

nombreEntry = Entry(frameBody, textvariable=nombre)
nombreEntry.grid(row=1, column=1, pady=10, padx=10)

apellidolbl = Label(frameBody, text="Apellido: ",  bg=bg_principal)
apellidolbl.grid(row=2, column=0, pady=10, padx=10)

apellidotxt = Entry(frameBody, textvariable=apellido)
apellidotxt.grid(row=2, column=1, pady=10, padx=10)

passwordlbl = Label(frameBody, text="Contraseña: ", bg=bg_principal)
passwordlbl.grid(row=3, column=0, pady=10, padx= 10)

passwordEntry = Entry(frameBody, show="*", textvariable=password)
passwordEntry.grid(row=3, column=1, pady=10, padx=10)

direccionlbl = Label(frameBody, text="Dirección: ", bg=bg_principal)
direccionlbl.grid(row=4, column=0, pady=10, padx=10)

direccionEntry = Entry(frameBody, textvariable=direccion)
direccionEntry.grid(row=4, column=1, pady=10, padx=10)

comentarioslbl = Label(frameBody, text="Comentarios: ", bg=bg_principal)
comentarioslbl.grid(row=5, column=0, pady=10, padx=10)

comentariosText = Text(frameBody, width=15, height=7)
comentariosText.grid(row=5, column=1, pady=10, padx=10)

scrollComentarios = Scrollbar(frameBody, command=comentariosText.yview)
scrollComentarios.grid(row=5, column=2, sticky="nsew")

comentariosText.config(yscrollcommand=scrollComentarios.set)


#Frame Footer

frameFooter = Frame(root, bg=bg_principal)
frameFooter.pack()

limpiarBtn = Button(frameFooter, text="Limpiar", command=limpiar)
limpiarBtn.grid(row=0, column=1, pady=10, padx=10)


#Frame operaciones

frameOperaciones = Frame(root, bg=bg_principal)
frameOperaciones.pack()

createBtn = Button(frameOperaciones, text="Create", command=lambda:sqlOperaciones(1))
createBtn.grid(row=0, column=0, pady=10, padx=10)

readBtn = Button(frameOperaciones, text="Read", command=lambda:sqlOperaciones(2))
readBtn.grid(row=0, column=1, pady=10, padx=10)

updateBtn = Button(frameOperaciones, text="Update", command=lambda:sqlOperaciones(3))
updateBtn.grid(row=0, column=2, pady=10, padx=10)

deleteBtn = Button(frameOperaciones, text="Delete", command=lambda:sqlOperaciones(4))
deleteBtn.grid(row=0, column=3, pady=10, padx=10)



root.mainloop()