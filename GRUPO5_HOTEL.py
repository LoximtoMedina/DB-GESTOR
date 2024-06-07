#Importación de los modulos a utilizar
from tkinter import simpledialog as ing
from tkinter import messagebox as imp
from tkinter import ttk
from tkinter import *
import sqlite3
import time

#Creación de las clases
#Clase que contendrá las funciones de manejo de bases de datos
class bd():

    #Creando el almacenamiento de la conexión
    store = None

    #Creación de las cosas que se usaran al entrar al programa
    def __init__(self):
        #Creación de la base de datos
        self.connection=sqlite3.connect("GRUPO5_HOTEL.db")

        #Creación del método cursor
        self.cursor=self.connection.cursor()

        #Creación de la tabla
        try:
            self.connection.execute("""CREATE TABLE TDHotel(
                ID INTEGER PRIMARY KEY,
                Nombre TEXT,
                TarjetaCrédito INTEGER,
                Habitación text);""")
            imp.showinfo("BASE DE DATOS - HOTEL 'ILUSIONATE CON EL MUNDO'", "Base de datos creada con... ¡ÉXITO!")
        except sqlite3.OperationalError:
            pass

        #Si el almacenamiento está vacío lo rellena
        if bd.store is None:
            bd.store = self

    def singleton(self):
        if self.store is None:
            self.store = db()
        return self.store

    #Creación del def que permitirá ingresar datos a la base de datos
    def input(self, ID, NOMBRE, TARJETA, HABITACION):
        #Ingresando los datos que haya dado el usuario a la base de datos        
        self.cursor.execute(f"INSERT INTO TDHotel (ID, Nombre, TarjetaCrédito, Habitación) VALUES({ID}, '{NOMBRE}', {TARJETA}, '{HABITACION}');")
        #Guardando cambios
        self.connection.commit()

    #Creación del def que permitirá modificar datos de la base de datos
    def modify(self, ID, NOMBRE, TARJETA, HABITACION):
        #Modificando el registro
        self.cursor.execute(f"UPDATE TDHotel SET Nombre='{NOMBRE}', TarjetaCrédito={TARJETA}, Habitación='{HABITACION}' WHERE ID={ID};")
        #Guardando cambios
        self.connection.commit()

    #Creación del def que permitirá eliminar datos de la base de datos
    def delete(self, ID):
        #Eliminando el registro
        self.cursor.execute(f"DELETE FROM TDHotel WHERE ID={ID};")
        #Guardando cambios
        self.connection.commit()

    #Creación del def que permitirá consultar datos de la base de datos
    def consulta(self, criterio):
        if criterio==1:
            #Consulta hecha por ID ordenado por 0-9
            self.cursor.execute("SELECT * FROM TDHotel ORDER BY ID ASC;")

        elif criterio==2:
            #Consulta hecha por ID ordenado por 9-0
            self.cursor.execute("SELECT * FROM TDHotel ORDER BY ID DESC;")

        elif criterio==3:
            #Consulta hecha por Nombre ordenado por A-z
            self.cursor.execute("SELECT * FROM TDHotel ORDER BY Nombre ASC;")

        elif criterio==4:
            #Consulta hecha por Nombre ordenado por z-A
            self.cursor.execute("SELECT * FROM TDHotel ORDER BY Nombre DESC;")

        elif criterio==5:
            #Consulta hecha por Tarjeta de Crédito de 0-9
            self.cursor.execute("SELECT * FROM TDHotel ORDER BY TarjetaCrédito ASC;")

        elif criterio==6:
            #Consulta hecha por Tarjeta de Crédito de 9-0
            self.cursor.execute("SELECT * FROM TDHotel ORDER BY TarjetaCrédito DESC;")

        elif criterio==7:
            #Consulta hecha por Habitación solo la habitación individual
            self.cursor.execute("SELECT * FROM TDHotel WHERE Habitación='Habitación Individual';")

        elif criterio==8:
            #Consulta hecha por Habitación solo la habitación doble
            self.cursor.execute("SELECT * FROM TDHotel WHERE Habitación='Habitación Doble';")

        elif criterio==9:
            #Consulta hecha por Habitación solo la habitación familiar
            self.cursor.execute("SELECT * FROM TDHotel WHERE Habitación='Habitación Familiar';")

        elif criterio==10:
            #Consulta hecha por Habitación solo la habitación ejecutiva
            self.cursor.execute("SELECT * FROM TDHotel WHERE Habitación='Habitación Ejecutiva';")

        elif criterio==11:
            #Muestra la tabla
            self.cursor.execute("SELECT * FROM TDHotel;")

#Clase que contendrá la interfaz gráfica
class bd_gestor():
    #Creación del método constructor
    def __init__(self):
        #Creación de la ventana
        self.main=Tk()
        self.main.title("GESTOR DE BASE DE DATOS - HOTEL - 'HOGAVIRT'")
        self.main.geometry("500x500+430+80")
        self.main.resizable(0,0)
        self.main.config(bg="#E8F3E4")
        self.maincontent()

    #Creación del def que contendrá el conteido de la ventana
    def maincontent(self):
        #Título del menú principal
        self.maintitle=Label(self.main, text="HOTEL - 'HOGAVIRT'", font=("Arial", 18, "bold"), justify="center", bg="#193B0E", fg="White", height=4, width=33).place(relx=0.0, rely=0.0)

        #Botones del menú principal
        self.btninputmenu=Button(self.main, text="Ingresar Datos", font=("Arial", 10, "bold"), bg="#439C25", height=4, width=20, command=self.inputcontent).place(relx=0.14, rely=0.4)
        self.btnmodifymenu=Button(self.main, text="Modificar Datos", font=("Arial", 10, "bold"), bg="#439C25", height=4, width=20, command=self.modifycontent).place(relx=0.54, rely=0.4)
        self.btndeletemenu=Button(self.main, text="Eliminar Datos", font=("Arial", 10, "bold"), bg="#439C25", height=4, width=20, command=self.deletecontent).place(relx=0.14, rely=0.6)
        self.btnconsultmenu=Button(self.main, text="Realizar Consultas", font=("Arial", 10, "bold"), bg="#439C25", height=4, width=20, command=self.consultcontent).place(relx=0.54, rely=0.6)

        self.btnexit=Button(self.main, text="Salir", font=("Arial", 8, "bold"), bg="Darkred", fg="white", height=2, width=8, command=self.exitmain).place(relx=0.0, rely=0.921)

        self.btnfp=Button(self.main, text="Portada", font=("Arial", 8, "bold"), bg="#257E9C", fg="white", height=2, width=8, command=self.fp).place(relx=0.87, rely=0.921)
        self.fp()

    #Creación del def que abrirá la ventana para el ingreso de datos
    def inputcontent(self):
        #Creación de la ventana
        self.secundary=Toplevel(self.main)
        self.secundary.title("GESTOR DE BASE DE DATOS - HOTEL 'ILUSIONATE CON EL MUNDO'")
        self.secundary.geometry("700x680+350+10")
        self.secundary.resizable(0,0)
        self.secundary.config(bg="#E8F3E4")

        #Creación del contenido de la ventana
        #Labels
        self.title=Label(self.secundary, text="INGRESO DE DATOS", font=("Arial", 18, "bold"), justify="center", bg="#193B0E", fg="White", height=2, width=47).place(relx=0.0, rely=0.0)

        self.idtitle=Label(self.secundary, text="ID del Cliente", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.1, rely=0.16)
        self.nametitle=Label(self.secundary, text="Nombre del Cliente", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.1, rely=0.26)
        self.credittitle=Label(self.secundary, text="Tarjeta de Crédito del Cliente", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.1, rely=0.36)
        self.roomtitle=Label(self.secundary, text="Habitación del Cliente", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.1, rely=0.46)

        self.line=Label(self.secundary, bg="#193B0E", height=18, width=1).place(relx=0.5, rely=0.15)

        #Entries
        self.clientid=IntVar()

        bd().singleton().cursor.execute("SELECT MAX(ID) FROM TDHotel;")
        try:
            self.clientid.set(bd().singleton().cursor.fetchone()[0]+1)
        except TypeError:
            self.clientid.set(0)

        self.identry=Entry(self.secundary, font=("Arial", 10, "bold"), justify="center", width=35, state="disabled", textvariable=self.clientid)
        self.identry.place(relx=0.1, rely=0.2)

        self.clientname=StringVar()
        self.nameentry=Entry(self.secundary, font=("Arial", 10), justify="center", width=35, textvariable=self.clientname)
        self.nameentry.place(relx=0.1, rely=0.3)

        self.clientcreditcard=StringVar()
        self.creditcardentry=Entry(self.secundary, font=("Arial", 10), justify="center", width=35, textvariable=self.clientcreditcard)
        self.creditcardentry.place(relx=0.1, rely=0.4)

        #Combobox
        self.roomcombobox=ttk.Combobox(self.secundary, font=("Arial", 10), width=33, state="readonly", values=["Habitación Individual", "Habitación Doble", "Habitación Familiar", "Habitación Ejecutiva"])
        self.roomcombobox.place(relx=0.1, rely=0.5)

        #Buttons
        self.btnaction=Button(self.secundary, text="Ingresar", font=("Arial", 10, "bold"), bg="#439C25", height=4, width=30, command=self.inputindatatable).place(relx=0.55, rely=0.2)
        self.btnback=Button(self.secundary, text="Regresar", font=("Arial", 10, "bold"), bg="DarkRed", fg="white", height=4, width=30, command=self.exitsecundary).place(relx=0.55, rely=0.37)

        #Treeview
        self.datatable=ttk.Treeview(self.secundary, columns=("#1","#2", "#3"))
        self.datatablescrollbar=ttk.Scrollbar(self.secundary, orient="vertical", command=self.datatable.yview).place(relx=0.875, rely=0.6, height=201+25)

        self.datatable.column("#0", width=30)
        self.datatable.column("#1", width=230)
        self.datatable.column("#2", width=140)
        self.datatable.column("#3", width=140)

        self.datatable.heading("#0", text="ID", anchor="center")
        self.datatable.heading("#1", text="Nombre", anchor="center")
        self.datatable.heading("#2", text="Tarjeta de Crédito", anchor="center")
        self.datatable.heading("#3", text="Habitación Alquilada", anchor="center")
        self.datatable.place(relx=0.1, rely=0.6)

        #Extrayendo la tabla desde la base de datos
        bd().singleton().consulta(11)

        #Borrando datos, por si acaso
        self.datatable.delete(*self.datatable.get_children())
        
        #Ingresando la tabla al treeview
        tabla=bd().singleton().cursor.fetchall()
        if tabla!=None:
            for fila in tabla:
                self.datatable.insert("", 'end', text=int(fila[0]), values=(f"{fila[1]}", int(fila[2]), f"{fila[3]}"))

        #Abriendo la ventana
        self.secundary.mainloop()

    #Creación del def que ingresará los datos puestos por el usuario en la base de datos
    def inputindatatable(self):
        #Ingresando los datos en el treeview
        self.datatable.insert("", 'end', text=self.clientid.get(), values=(f"{self.clientname.get()}", self.clientcreditcard.get(), f"{self.roomcombobox.get()}"))

        #Utilizamos la conexión ya creada junto con el def creado en la clase bd para ingresar los datos
        bd().singleton().input(self.clientid.get(), self.clientname.get(), self.clientcreditcard.get(), self.roomcombobox.get())

        #Cambiando el ID para que se puedan seguir ingresando registros
        bd().singleton().cursor.execute("SELECT MAX(ID) FROM TDHotel;")
        self.clientid.set(bd().singleton().cursor.fetchone()[0]+1)

        #Vaciando los entrys que el usuario sí puede cambiar
        self.clientname.set("")
        self.clientcreditcard.set("")
        self.roomcombobox.set("")

    #Creación del def que abrirá la ventana para la modificación de datos
    def modifycontent(self):
        #Creación de la ventana
        self.secundary=Toplevel(self.main)
        self.secundary.title("GESTOR DE BASE DE DATOS - HOTEL 'ILUSIONATE CON EL MUNDO'")
        self.secundary.geometry("700x680+350+10")
        self.secundary.resizable(0,0)
        self.secundary.config(bg="#E8F3E4")

        #Creación del contenido de la ventana
        #Labels
        self.title=Label(self.secundary, text="MODIFICACIÓN DE DATOS", font=("Arial", 18, "bold"), justify="center", bg="#193B0E", fg="White", height=2, width=47).place(relx=0.0, rely=0.0)

        self.idtitle=Label(self.secundary, text="ID del Cliente", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.1, rely=0.16)
        self.nametitle=Label(self.secundary, text="Nombre del Cliente", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.1, rely=0.26)
        self.credittitle=Label(self.secundary, text="Tarjeta de Crédito del Cliente", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.1, rely=0.36)
        self.roomtitle=Label(self.secundary, text="Habitación del Cliente", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.1, rely=0.46)

        self.line=Label(self.secundary, bg="#193B0E", height=18, width=1).place(relx=0.5, rely=0.15)

        #Entries
        self.clientid=IntVar()
        self.identry=Entry(self.secundary, font=("Arial", 10, "bold"), justify="center", width=35, state="disabled", textvariable=self.clientid)
        self.identry.place(relx=0.1, rely=0.2)

        self.clientname=StringVar()
        self.nameentry=Entry(self.secundary, font=("Arial", 10), justify="center", width=35, textvariable=self.clientname)
        self.nameentry.place(relx=0.1, rely=0.3)

        self.clientcreditcard=IntVar()
        self.creditcardentry=Entry(self.secundary, font=("Arial", 10), justify="center", width=35, textvariable=self.clientcreditcard)
        self.creditcardentry.place(relx=0.1, rely=0.4)

        #Combobox
        self.roomcombobox=ttk.Combobox(self.secundary, font=("Arial", 10), width=33, state="readonly", values=["Habitación Individual", "Habitación Doble", "Habitación Familiar", "Habitación Ejecutiva"])
        self.roomcombobox.place(relx=0.1, rely=0.5)

        #Buttons
        self.btnaction=Button(self.secundary, text="Modificar", font=("Arial", 10, "bold"), bg="#439C25", height=4, width=30, command=self.modifyindatatable).place(relx=0.55, rely=0.2)
        self.btnback=Button(self.secundary, text="Regresar", font=("Arial", 10, "bold"), bg="DarkRed", fg="white", height=4, width=30, command=self.exitsecundary).place(relx=0.55, rely=0.37)

        #Treeview
        self.datatable=ttk.Treeview(self.secundary, columns=("#1","#2", "#3"))
        self.datatablescrollbar=ttk.Scrollbar(self.secundary, orient="vertical", command=self.datatable.yview).place(relx=0.875, rely=0.6, height=201+25)

        self.datatable.column("#0", width=30)
        self.datatable.column("#1", width=230)
        self.datatable.column("#2", width=140)
        self.datatable.column("#3", width=140)

        self.datatable.heading("#0", text="ID")
        self.datatable.heading("#1", text="Nombre")
        self.datatable.heading("#2", text="Tarjeta de Crédito")
        self.datatable.heading("#3", text="Habitación Alquilada")
        self.datatable.place(relx=0.1, rely=0.6)

        #Utilizando el evento "TreeviewSelect", que al seleccionar un elemento en el treeview lo ingrese automáticamente a los Entrys
        self.datatable.bind("<<TreeviewSelect>>", self.inputinentry)

        #Extrayendo la tabla desde la base de datos
        bd().singleton().consulta(11)

        #Borrando datos, por si acaso
        self.datatable.delete(*self.datatable.get_children())
        
        #Ingresando la tabla al treeview
        tabla=bd().singleton().cursor.fetchall()
        if tabla!=None:
            for fila in tabla:
                self.datatable.insert("", 'end', text=int(fila[0]), values=(f"{fila[1]}", int(fila[2]), f"{fila[3]}"))

        #Abriendo la ventana
        self.secundary.mainloop()

    #Creación del def que modificara los datos del registro seleccionado del treeview en la base de datos
    def modifyindatatable(self):
        #Utilizamos la conexión ya creada junto con el def creado en la clase bd para modificar los datos del registro
        bd().singleton().modify(self.clientid.get(), self.clientname.get(), self.clientcreditcard.get(), self.roomcombobox.get())

        #Extrayendo la tabla desde la base de datos
        bd().singleton().cursor.execute("SELECT * FROM TDHotel;")
        self.datatable.delete(*self.datatable.get_children())
        
        #Ingresando la tabla al treeview
        tabla=bd().singleton().cursor.fetchall()
        if tabla!=None:
            for fila in tabla:
                self.datatable.insert("", 'end', text=int(fila[0]), values=(f"{fila[1]}", int(fila[2]), f"{fila[3]}"))

    #Creación del def que abrirá la ventana para la eliminación de datos
    def deletecontent(self):
        #Creación de la ventana
        self.secundary=Toplevel(self.main)
        self.secundary.title("GESTOR DE BASE DE DATOS - HOTEL 'ILUSIONATE CON EL MUNDO'")
        self.secundary.geometry("700x680+350+10")
        self.secundary.resizable(0,0)
        self.secundary.config(bg="#E8F3E4")

        #Creación del contenido de la ventana
        #Labels
        self.title=Label(self.secundary, text="ELIMINACIÓN DE DATOS", font=("Arial", 18, "bold"), justify="center", bg="#193B0E", fg="White", height=2, width=47).place(relx=0.0, rely=0.0)

        self.idtitle=Label(self.secundary, text="ID del Cliente", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.1, rely=0.16)
        self.nametitle=Label(self.secundary, text="Nombre del Cliente", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.1, rely=0.26)
        self.credittitle=Label(self.secundary, text="Tarjeta de Crédito del Cliente", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.1, rely=0.36)
        self.roomtitle=Label(self.secundary, text="Habitación del Cliente", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.1, rely=0.46)

        self.line=Label(self.secundary, bg="#193B0E", height=18, width=1).place(relx=0.5, rely=0.15)

        #Entries
        self.clientid=IntVar()
        self.identry=Entry(self.secundary, font=("Arial", 10, "bold"), justify="center", width=35, state="disabled", textvariable=self.clientid)
        self.identry.place(relx=0.1, rely=0.2)

        self.clientname=StringVar()
        self.nameentry=Entry(self.secundary, font=("Arial", 10), justify="center", width=35, state="disabled", textvariable=self.clientname)
        self.nameentry.place(relx=0.1, rely=0.3)

        self.clientcreditcard=IntVar()
        self.creditcardentry=Entry(self.secundary, font=("Arial", 10), justify="center", width=35, state="disabled", textvariable=self.clientcreditcard)
        self.creditcardentry.place(relx=0.1, rely=0.4)

        #Combobox
        self.roomcombobox=ttk.Combobox(self.secundary, font=("Arial", 10), width=33, state="disabled", values=["Habitación Individual", "Habitación Doble", "Habitación Familiar", "Habitación Ejecutiva"])
        self.roomcombobox.place(relx=0.1, rely=0.5)

        #Buttons
        self.btnaction=Button(self.secundary, text="Eliminar", font=("Arial", 10, "bold"), bg="#439C25", height=4, width=30, command=self.deleteindatatable).place(relx=0.55, rely=0.2)
        self.btnback=Button(self.secundary, text="Regresar", font=("Arial", 10, "bold"), bg="DarkRed", fg="white", height=4, width=30, command=self.exitsecundary).place(relx=0.55, rely=0.37)

        #Treeview
        self.datatable=ttk.Treeview(self.secundary, columns=("#1","#2", "#3"))
        self.datatablescrollbar=ttk.Scrollbar(self.secundary, orient="vertical", command=self.datatable.yview).place(relx=0.875, rely=0.6, height=201+25)

        self.datatable.column("#0", width=30)
        self.datatable.column("#1", width=230)
        self.datatable.column("#2", width=140)
        self.datatable.column("#3", width=140)

        self.datatable.heading("#0", text="ID")
        self.datatable.heading("#1", text="Nombre")
        self.datatable.heading("#2", text="Tarjeta de Crédito")
        self.datatable.heading("#3", text="Habitación Alquilada")
        self.datatable.place(relx=0.1, rely=0.6)

        #Utilizando el evento "TreeviewSelect", que al seleccionar un elemento en el treeview lo ingrese automáticamente a los Entrys
        self.datatable.bind("<<TreeviewSelect>>", self.inputinentry)

        #Extrayendo la tabla desde la base de datos
        bd().singleton().consulta(11)

        #Borrando datos, por si acaso
        self.datatable.delete(*self.datatable.get_children())
        
        #Ingresando la tabla al treeview
        tabla=bd().singleton().cursor.fetchall()
        if tabla!=None:
            for fila in tabla:
                self.datatable.insert("", 'end', text=int(fila[0]), values=(f"{fila[1]}", int(fila[2]), f"{fila[3]}"))

        #Abriendo la ventana
        self.secundary.mainloop()

    #Creación del def que eliminara el registro seleccionado del treeview en la base de datos
    def deleteindatatable(self):
        #Utilizamos la conexión ya creada junto con el def creado en la clase bd para borrar el registro
        bd().singleton().delete(self.clientid.get())

        #Extrayendo la tabla desde la base de datos
        bd().singleton().cursor.execute("SELECT * FROM TDHotel;")
        self.datatable.delete(*self.datatable.get_children())
        
        #Ingresando la tabla al treeview
        tabla=bd().singleton().cursor.fetchall()
        if tabla!=None:
            for fila in tabla:
                self.datatable.insert("", 'end', text=int(fila[0]), values=(f"{fila[1]}", int(fila[2]), f"{fila[3]}"))

    #Creación del def que abrirá la ventana para la realización de consultas
    def consultcontent(self):
        self.secundary=Toplevel(self.main)
        self.secundary.title("GESTOR DE BASE DE DATOS - HOTEL 'ILUSIONATE CON EL MUNDO'")
        self.secundary.geometry("700x680+350+10")
        self.secundary.resizable(0,0)
        self.secundary.config(bg="#E8F3E4")

        #Creación del contenido de la ventana
        #Labels
        self.title=Label(self.secundary, text="CONSULTA DE DATOS", font=("Arial", 18, "bold"), justify="center", bg="#193B0E", fg="White", height=2, width=47).place(relx=0.0, rely=0.0)

        self.idtitle=Label(self.secundary, text="Campo que desea usar como criterio", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.09, rely=0.16)
        self.idtitle=Label(self.secundary, text="Filtro: ", font=("Arial", 10, "bold"), bg="#E8F3E4", fg="black").place(relx=0.52, rely=0.16)

        #Combobox
        self.consulcombobox=ttk.Combobox(self.secundary, font=("Arial", 10), width=33, state="readonly", values=["ID", "Nombre", "Tarjeta De Crédito", "Habitación", "Mostrar Tabla"])
        self.consulcombobox.place(relx=0.1, rely=0.2)

        self.filtrocombobox=ttk.Combobox(self.secundary, font=("Arial", 10), width=33, state="readonly", postcommand=self.refresh)
        self.filtrocombobox.place(relx=0.53, rely=0.2)

        #Buttons
        self.btnaction=Button(self.secundary, text="Filtrar", font=("Arial", 10, "bold"), bg="#439C25", height=4, width=31, command=self.consultindatatable).place(relx=0.1, rely=0.3)
        self.btnback=Button(self.secundary, text="Regresar", font=("Arial", 10, "bold"), bg="DarkRed", fg="white", height=4, width=31, command=self.exitsecundary).place(relx=0.53, rely=0.3)

        #Treeview
        self.datatable=ttk.Treeview(self.secundary, columns=("#1","#2", "#3"))
        self.datatablescrollbar=ttk.Scrollbar(self.secundary, orient="vertical", command=self.datatable.yview).place(relx=0.875, rely=0.5, height=201+25)

        self.datatable.column("#0", width=30)
        self.datatable.column("#1", width=230)
        self.datatable.column("#2", width=150)
        self.datatable.column("#3", width=150)

        self.datatable.heading("#0", text="ID")
        self.datatable.heading("#1", text="Nombre")
        self.datatable.heading("#2", text="Tarjeta de Crédito")
        self.datatable.heading("#3", text="Habitación Alquilada")
        self.datatable.place(relx=0.1, rely=0.5)

        #Extrayendo la tabla desde la base de datos
        bd().singleton().consulta(11)

        #Borrando datos, por si acaso
        self.datatable.delete(*self.datatable.get_children())
        
        #Ingresando la tabla al treeview
        tabla=bd().singleton().cursor.fetchall()
        if tabla!=None:
            for fila in tabla:
                self.datatable.insert("", 'end', text=int(fila[0]), values=(f"{fila[1]}", int(fila[2]), f"{fila[3]}"))

        #Abriendo la ventana
        self.secundary.mainloop()
        
    #Creación del def que mostrará la consulta en el treeview en base a los datos de la base de datos
    def consultindatatable(self):
        #Filtro por ID ordenado por 0-9
        if self.consulcombobox.current()==0 and self.filtrocombobox.current()==0:
            bd().singleton().consulta(1)

        #Filtro por ID ordenado por 9-0
        elif self.consulcombobox.current()==0 and self.filtrocombobox.current()==1:
            bd().singleton().consulta(2)

        #Filtro por Nombre ordenado por A-z
        elif self.consulcombobox.current()==1 and self.filtrocombobox.current()==0:
            bd().singleton().consulta(3)
        #Filtro por Nombre ordenado por z-A
        elif self.consulcombobox.current()==1 and self.filtrocombobox.current()==1:
            bd().singleton().consulta(4)

        #Filtro por Tarjeta de Crédito de 0-9
        elif self.consulcombobox.current()==2 and self.filtrocombobox.current()==0:
            bd().singleton().consulta(5)
        #Filtro por Tarjeta de Crédito de 9-0
        elif self.consulcombobox.current()==2 and self.filtrocombobox.current()==1:
            bd().singleton().consulta(6)
        
        #Filtro por Habitación solo la habitación individual
        elif self.consulcombobox.current()==3 and self.filtrocombobox.current()==0:
            bd().singleton().consulta(7)
        #Filtro por Habitación solo la habitación doble
        elif self.consulcombobox.current()==3 and self.filtrocombobox.current()==1:
            bd().singleton().consulta(8)
        #Filtro por Habitación solo la habitación familiar
        elif self.consulcombobox.current()==3 and self.filtrocombobox.current()==2:
            bd().singleton().consulta(9)
        #Filtro por Habitación solo la habitación ejecutiva
        elif self.consulcombobox.current()==3 and self.filtrocombobox.current()==3:
            bd().singleton().consulta(10)

        #Filtro que muestra la tabla
        elif self.consulcombobox.current()==4:
            bd().singleton().consulta(11)

        #Borrando los datos anteriores
        self.datatable.delete(*self.datatable.get_children())
        #Extrayendo los datos de la base de datos
        tabla=bd().singleton().cursor.fetchall()
        #Ingresando los registros extraidos al treeview
        for fila in tabla:
            self.datatable.insert("", 'end', text=int(fila[0]), values=(f"{fila[1]}", int(fila[2]), f"{fila[3]}"))
        
    #Creación del def que ingresará la información que está ya en la base de datos en los entrys para que el usuario pueda modificar o borrar dicha información
    def inputinentry(self, event):
        try:
            #Selección del ID del elemento seleccionado
            ID = self.datatable.item(self.datatable.selection()[0],"text")

            #Selección el registro que tenga el ID que se seleccionó
            bd().singleton().cursor.execute(f"SELECT * FROM TDHotel WHERE ID={ID}")
            registro=bd().singleton().cursor.fetchone()

            #Ubicación de cada dato de cada columna en los entrys
            self.clientid.set(registro[0]) 
            self.clientname.set(registro[1])
            self.clientcreditcard.set(registro[2])
            self.roomcombobox.set(registro[3])
        except IndexError:
            pass

    #Creación del def que permitirá cambiar los valores del segundo combobox en la ventana de consultas
    def refresh(self):
        if self.consulcombobox.current()==0:
            self.filtrocombobox.config(state="normal")
            self.filtrocombobox["values"]=["0-9", "9-0"]
            self.datatable.delete(*self.datatable.get_children())

        elif self.consulcombobox.current()==1:
            self.filtrocombobox.config(state="readonly")
            self.filtrocombobox["values"]=["A-z", "z-A"]
            self.datatable.delete(*self.datatable.get_children())

        elif self.consulcombobox.current()==2:
            self.filtrocombobox.config(state="normal")
            self.filtrocombobox["values"]=["0-9", "9-0"]
            self.datatable.delete(*self.datatable.get_children())

        elif self.consulcombobox.current()==3:
            self.filtrocombobox.config(state="readonly")
            self.filtrocombobox["values"]=["Habitación Individual", "Habitación Doble", "Habitación Familiar", "Habitación Ejecutiva"]
            self.datatable.delete(*self.datatable.get_children())

        elif self.consulcombobox.current()==4:
            self.filtrocombobox["values"]=[""]
            self.filtrocombobox.set("")

    #Creación del def que mostrará la información acerca de los integrantes de este proyecto
    def fp(self):
        imp.showinfo("GESTOR DE BASE DE DATOS - HOTEL 'ILUSIONATE CON EL MUNDO'", "INSTITUTO MARISTA LA INMACULADA \n \n Este trabajo, para la clase de programación, fue hecho con mucho amor por: \n \n 1-Gabriela Cruz - 09 - Diseñadora \n 2-Mayra Donaire - 13 - Diseñadora \n 2-Ángel Flores - 21 - Programador \n 4-Cristian Medina - 23 - Programador \n 5-Daniel Reyes - 25 - Estructura de la BD \n 6-Diego Vásquez - 26 - Programador \n 7-E. Jezael Yanes - 29 - Diseñador \n 8-Fabio Dominguez - 33 - Diseñador \n \n Para nuestro querido docente: Marco Tulio Madrid")

    #Creación del def que permitirá salir del programa
    def exitmain(self):
        confirmacion=imp.askyesno("GESTOR DE BASE DE DATOS - HOTEL 'ILUSIONATE CON EL MUNDO'", "¿Realmente deséa salir del menú principal?")

        if confirmacion==1:
            imp.showinfo("GESTOR DE BASE DE DATOS - HOTEL 'ILUSIONATE CON EL MUNDO'", "¡Bye, Bye!")
            self.main.destroy()

    #Creación del def que permitirá regresar al menú principal
    def exitsecundary(self):
        self.secundary.destroy()

#Llamando a la clase bd_gestor, luego un llamado a la ventana principal y por último la iniciación del ciclo para poder mostrar la interfaz gráfica creada
bd_gestor().main.mainloop()

#Cambio 1