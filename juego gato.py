#-----Las biblotecas de uso------------
from tkinter import *
from PIL import ImageTk, Image #importar imagen 
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk
import random
#----------------------------funciones de la maquina
def iniciar_juego():
    global ventana_juego_1, fondo
    tamano = int(opcion_var.get())
    ventana_config.withdraw()
    ventana_juego_1 = tk.Tk()
    ventana_juego_1.title("Gato 3x3")
    ancho_ventana = 400
    alto_ventana = 500
    ancho_pantalla = ventana_juego_1.winfo_screenwidth()
    alto_pantalla = ventana_juego_1.winfo_screenheight()
    posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
    posicion_y = int((alto_pantalla / 2) - (alto_ventana / 2))
    ventana_juego_1.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
    label = Label(ventana_juego_1, text="Juego de gato 3x3", font=("Ice kingdom", 8), fg="white", bg="#C679B4")
    label.pack()
    boton = Button(ventana_juego_1, text="⇦",font=("Ice kingdom", 11), fg="white", bg="#C679B4",command=lambda:regresar_ventana12())
    boton.pack(side="right", padx=(50,10), pady=(50,10))
    frame = tk.Frame(ventana_juego_1)
    frame.pack()
    tablero = [" " for _ in range(tamano ** 2)]
    botones = []
    def hacer_movimiento(index):
        if tablero[index] == " ":
            tablero[index] = jugador_actual
            boton = botones[index]
            boton.config(text=jugador_actual, state="disabled")
            if hay_ganador(jugador_actual):
                etiqueta.config(text=f"¡{jugador_actual} ha ganado!")
                desactivar_botones()
            elif hay_empate():
                etiqueta.config(text="¡Empate!")
                desactivar_botones()
            else:
                cambiar_turno()
    def cambiar_turno():
        nonlocal jugador_actual
        if jugador_actual == "X":
            jugador_actual = "O"
            etiqueta.config(text="Turno: O (Máquina)")
            turno_maquina()
        else:
            jugador_actual = "X"
            etiqueta.config(text="Turno: X (Jugador)")
    def turno_maquina():
        if hay_movimientos_disponibles():
            mejor_movimiento = encontrar_mejor_movimiento()
            tablero[mejor_movimiento] = jugador_actual
            boton = botones[mejor_movimiento]
            boton.config(text=jugador_actual, state="disabled")
            if hay_ganador(jugador_actual):
                etiqueta.config(text=f"¡{jugador_actual} ha ganado!")
                desactivar_botones()
            elif hay_empate():
                etiqueta.config(text="¡Empate!")
                desactivar_botones()
            else:
                cambiar_turno()
    def hay_ganador(jugador):
        lines = obtener_lineas_ganadoras()
        for line in lines:
            if all(tablero[i] == jugador for i in line):
                return True
        return False
    def hay_empate():
        return all(cell != " " for cell in tablero)
    def desactivar_botones():
        for boton in botones:
            boton.config(state="disabled")
    def hay_movimientos_disponibles():
        return any(cell == " " for cell in tablero)
    def encontrar_mejor_movimiento():
        movimientos_disponibles = [i for i in range(len(tablero)) if tablero[i] == " "]
        return random.choice(movimientos_disponibles)
    def obtener_lineas_ganadoras():
        lineas = []
        # Filas
        lineas.extend([[i+j for j in range(tamano)] for i in range(0, tamano**2, tamano)])
        # Columnas
        lineas.extend([[i+j for j in range(0, tamano**2, tamano)] for i in range(tamano)])
        # Diagonal principal
        lineas.append([i*(tamano+1) for i in range(tamano)])
        # Diagonal secundaria
        lineas.append([i*(tamano-1) for i in range(1, tamano+1)])
        return lineas
    etiqueta = tk.Label(ventana_juego_1, text="Turno: X (Jugador)")
    etiqueta.pack()
    jugador_actual = "X"
    for i in range(tamano ** 2):
        boton = tk.Button(frame, text=" ", width=10, height=4, command=lambda idx=i: hacer_movimiento(idx))
        boton.grid(row=i // tamano, column=i % tamano)
        botones.append(boton)
    ventana_juego_1.mainloop()
#---------------------------------------------4x4 maquina-------------------------------
def iniciar_juego_1():
    global ventana_juego,fondo_1
    tamano = int(opcion_v.get())
    ventana_conf.withdraw()
    ventana_juego = tk.Tk()
    ventana_juego.title("Gato 4x4 ")
    ancho_ventana = 500
    alto_ventana = 600
    ancho_pantalla = ventana_juego.winfo_screenwidth()
    alto_pantalla = ventana_juego.winfo_screenheight()
    posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
    posicion_y = int((alto_pantalla / 2) - (alto_ventana / 2))
    ventana_juego.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
    label = Label(ventana_juego, text="Juego de gato 4x4", font=("Ice kingdom", 14), fg="white", bg="#C679B4")
    label.pack()
    boton = Button(ventana_juego, text="⇦",font=("Ice kingdom", 11), fg="white", bg="#C679B4",command=lambda:regresar_ventana11())
    boton.pack(side="right", padx=(50,10), pady=(50,10))
    frame = tk.Frame(ventana_juego)
    frame.pack()
    tablero = [" " for _ in range(tamano ** 2)]
    botones = []
    def hacer_movimiento(index):
        if tablero[index] == " ":
            tablero[index] = jugador_actual
            boton = botones[index]
            boton.config(text=jugador_actual, state="disabled")
            if hay_ganador(jugador_actual):
                etiqueta.config(text=f"¡{jugador_actual} ha ganado!")
                desactivar_botones()
            elif hay_empate():
                etiqueta.config(text="¡Empate!")
                desactivar_botones()
            else:
                cambiar_turno()
    def cambiar_turno():
        nonlocal jugador_actual
        if jugador_actual == "X":
            jugador_actual = "O"
            etiqueta.config(text="Turno: O (Máquina)")
            turno_maquina()
        else:
            jugador_actual = "X"
            etiqueta.config(text="Turno: X (Jugador)")
    def turno_maquina():
        if hay_movimientos_disponibles():
            mejor_movimiento = encontrar_mejor_movimiento()
            tablero[mejor_movimiento] = jugador_actual
            boton = botones[mejor_movimiento]
            boton.config(text=jugador_actual, state="disabled")
            if hay_ganador(jugador_actual):
                etiqueta.config(text=f"¡{jugador_actual} ha ganado!")
                desactivar_botones()
            elif hay_empate():
                etiqueta.config(text="¡Empate!")
                desactivar_botones()
            else:
                cambiar_turno()
    def hay_ganador(jugador):
        lines = obtener_lineas_ganadoras()
        for line in lines:
            if all(tablero[i] == jugador for i in line):
                return True
        return False
    def hay_empate():
        return all(cell != " " for cell in tablero)
    def desactivar_botones():
        for boton in botones:
            boton.config(state="disabled")
    def hay_movimientos_disponibles():
        return any(cell == " " for cell in tablero)
    def encontrar_mejor_movimiento():
        movimientos_disponibles = [i for i in range(len(tablero)) if tablero[i] == " "]
        return random.choice(movimientos_disponibles)
    def obtener_lineas_ganadoras():
        lineas = []
        # Filas
        lineas.extend([[i+j for j in range(tamano)] for i in range(0, tamano**2, tamano)])
        # Columnas
        lineas.extend([[i+j for j in range(0, tamano**2, tamano)] for i in range(tamano)])
        # Diagonal principal
        lineas.append([i*(tamano+1) for i in range(tamano)])
        # Diagonal secundaria
        lineas.append([i*(tamano-1) for i in range(1, tamano+1)])
        return lineas
    etiqueta = tk.Label(ventana_juego, text="Turno: X (Jugador)")
    etiqueta.pack()
    jugador_actual = "X"
    for i in range(tamano ** 2):
        boton = tk.Button(frame, text=" ", width=10, height=4, command=lambda idx=i: hacer_movimiento(idx))
        boton.grid(row=i // tamano, column=i % tamano)
        botones.append(boton)
    ventana_juego.mainloop()
#---------------------------------------------5x5 maquina-------------------------------
def iniciar_juego_2():
    global ventana_juego
    tamano = int(opcion_va.get())
    ventana_con.withdraw()
    ventana_juego = tk.Tk()
    ventana_juego.title("Gato 5x5")
    ancho_ventana = 600
    alto_ventana = 600
    ancho_pantalla = ventana_juego.winfo_screenwidth()
    alto_pantalla = ventana_juego.winfo_screenheight()
    posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
    posicion_y = int((alto_pantalla / 2) - (alto_ventana / 2))
    ventana_juego.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
    label = Label(ventana_juego, text="Juego de gato 5x5", font=("Ice kingdom", 12), fg="white", bg="#C679B4")
    label.pack()
    boton = Button(ventana_juego, text="⇦",font=("Ice kingdom", 11), fg="white", bg="#C679B4",command=lambda:regresar_ventana10())
    boton.pack(side="right", padx=(50,10), pady=(50,10))
    frame = tk.Frame(ventana_juego)
    frame.pack()
    tablero = [" " for _ in range(tamano ** 2)]
    botones = []
    def hacer_movimiento(index):
        if tablero[index] == " ":
            tablero[index] = jugador_actual
            boton = botones[index]
            boton.config(text=jugador_actual, state="disabled")
            if hay_ganador(jugador_actual):
                etiqueta.config(text=f"¡{jugador_actual} ha ganado!")
                desactivar_botones()
            elif hay_empate():
                etiqueta.config(text="¡Empate!")
                desactivar_botones()
            else:
                cambiar_turno()
    def cambiar_turno():
        nonlocal jugador_actual
        if jugador_actual == "X":
            jugador_actual = "O"
            etiqueta.config(text="Turno: O (Máquina)")
            turno_maquina()
        else:
            jugador_actual = "X"
            etiqueta.config(text="Turno: X (Jugador)")
    def turno_maquina():
        if hay_movimientos_disponibles():
            mejor_movimiento = encontrar_mejor_movimiento()
            tablero[mejor_movimiento] = jugador_actual
            boton = botones[mejor_movimiento]
            boton.config(text=jugador_actual, state="disabled")
            if hay_ganador(jugador_actual):
                etiqueta.config(text=f"¡{jugador_actual} ha ganado!")
                desactivar_botones()
            elif hay_empate():
                etiqueta.config(text="¡Empate!")
                desactivar_botones()
            else:
                cambiar_turno()
    def hay_ganador(jugador):
        lines = obtener_lineas_ganadoras()
        for line in lines:
            if all(tablero[i] == jugador for i in line):
                return True
        return False
    def hay_empate():
        return all(cell != " " for cell in tablero)
    def desactivar_botones():
        for boton in botones:
            boton.config(state="disabled")
    def hay_movimientos_disponibles():
        return any(cell == " " for cell in tablero)
    def encontrar_mejor_movimiento():
        movimientos_disponibles = [i for i in range(len(tablero)) if tablero[i] == " "]
        return random.choice(movimientos_disponibles)
    def obtener_lineas_ganadoras():
        lineas = []
        # Filas
        lineas.extend([[i+j for j in range(tamano)] for i in range(0, tamano**2, tamano)])
        # Columnas
        lineas.extend([[i+j for j in range(0, tamano**2, tamano)] for i in range(tamano)])
        # Diagonal principal
        lineas.append([i*(tamano+1) for i in range(tamano)])
        # Diagonal secundaria
        lineas.append([i*(tamano-1) for i in range(1, tamano+1)])
        return lineas
    etiqueta = tk.Label(ventana_juego, text="Turno: X (Jugador)")
    etiqueta.pack()
    jugador_actual = "X"
    for i in range(tamano ** 2):
        boton = tk.Button(frame, text=" ", width=10, height=4, command=lambda idx=i: hacer_movimiento(idx))
        boton.grid(row=i // tamano, column=i % tamano)
        botones.append(boton)
    ventana_juego.mainloop()
#------------------------------------------------Fuciones de la maquina---------------------------------
def seleccionar_tamano_3():
    ventana_maquin.withdraw()
    global ventana_config, opcion_var,fondo
    ventana_config = Toplevel()
    ventana_config.title("Gato 3x3")
    ancho_ventana = 400
    alto_ventana = 400
    ancho_pantalla = ventana_config.winfo_screenwidth()
    alto_pantalla = ventana_config.winfo_screenheight()
    posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
    posicion_y = int((alto_pantalla / 2) - (alto_ventana / 2))
    ventana_config.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}") 
    fondo = Image.open("fondo principal.png")
    fondo = ImageTk.PhotoImage(fondo)
    label_fondo_5 = Label(ventana_config, image=fondo)
    label_fondo_5.place(x=0, y=0, relwidth=1, relheight=1)
    opcion_var = tk.StringVar()
    etiqueta = tk.Label(ventana_config, text="Recuerde seleccionar la opción de gato 3x3:",font=("Ice kingdom", 11), fg="white", bg="#572975")
    etiqueta.pack()
    opcion_3x3 = tk.Radiobutton(ventana_config, text="gato 3x3", variable=opcion_var, value="3",font=("Ice kingdom", 11), fg="white", bg="#572975")
    opcion_3x3.pack()
    boton_jugar = tk.Button(ventana_config, text="Jugar",font=("Ice kingdom", 11), fg="white", bg="#572975", command=iniciar_juego)
    boton_jugar.pack()
    # Botón para regresar a la ventana principal
    boton_regresar = Button(ventana_config, text="➢",font=("Ice kingdom", 11), fg="white", bg="#572975",command=lambda:regresar_ventana7())
    boton_regresar.pack(side="left", padx=10, pady=(150, 10))

def seleccionar_tamano_4():
    ventana_maquin.withdraw() 
    global ventana_conf,opcion_v,fondo_g
    ventana_conf = Toplevel()
    ventana_conf.title("Gato 4x4")
    ancho_ventana = 400
    alto_ventana = 400
    ancho_pantalla = ventana_conf.winfo_screenwidth()
    alto_pantalla = ventana_conf.winfo_screenheight()
    posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
    posicion_y = int((alto_pantalla / 2) - (alto_ventana / 2))
    ventana_conf.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}") 
    fondo_g = Image.open("fondo principal.png")
    fondo_g = ImageTk.PhotoImage(fondo_g)
    fondo_6 = Label(ventana_conf, image=fondo_g)
    fondo_6.place(x=0, y=0, relwidth=1, relheight=1)
    opcion_v = tk.StringVar()
    etiqueta = tk.Label(ventana_conf, text="Recuerde seleccionar la opción de gato 4x4:",font=("Ice kingdom", 11), fg="white", bg="#572975")
    etiqueta.pack()
    opcion_4x4 = tk.Radiobutton(ventana_conf, text="4x4", variable= opcion_v, value="4",font=("Ice kingdom", 11), fg="white", bg="#572975")
    opcion_4x4.pack()
    boton_jugar = tk.Button(ventana_conf, text="Jugar",font=("Ice kingdom", 11), fg="white", bg="#572975", command=iniciar_juego_1)
    boton_jugar.pack()
    # Botón para regresar a la ventana principal
    boton_regresar = Button(ventana_conf, text="➢",font=("Ice kingdom", 11), fg="white", bg="#572975",command=lambda:regresar_ventana8())
    boton_regresar.pack(side="left", padx=10, pady=(150, 10))

def seleccionar_tamano_5():
    global ventana_con, opcion_va,fondo_c
    ventana_con = Toplevel()
    ventana_con.title("Gato 5x5")
    ancho_ventana = 400
    alto_ventana = 400
    ancho_pantalla = ventana_con.winfo_screenwidth()
    alto_pantalla = ventana_con.winfo_screenheight()
    posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
    posicion_y = int((alto_pantalla / 2) - (alto_ventana / 2))
    ventana_con.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}") 
    fondo_c = Image.open("fondo principal.png")
    fondo_c = ImageTk.PhotoImage(fondo_c)
    label_fondo_5 = Label(ventana_con, image=fondo_c)
    label_fondo_5.place(x=0, y=0, relwidth=1, relheight=1)
    opcion_va = tk.StringVar()
    etiqueta = tk.Label(ventana_con, text="Recuerde seleccionar la opción de gato 4x4:",font=("Ice kingdom", 11), fg="white", bg="#572975")
    etiqueta.pack()
    opcion_5x5 = tk.Radiobutton(ventana_con, text="5x5", variable=opcion_va, value="5",font=("Ice kingdom", 11), fg="white", bg="#572975")
    opcion_5x5.pack()
    boton_jugar = tk.Button(ventana_con, text="Jugar",font=("Ice kingdom", 11), fg="white", bg="#572975", command=iniciar_juego_2)
    boton_jugar.pack()
    # Botón para regresar a la ventana principal
    boton_regresar = Button(ventana_con, text="➢",font=("Ice kingdom", 11), fg="white", bg="#572975",command=lambda:regresar_ventana9())
    boton_regresar.pack(side="left", padx=10, pady=(150, 10))

#-----------------------------Fuciones del juego jugadores----------------
def bloquear():
    for i in range(0,9):
        listaBotones[i].config(state="disable")
def iniciar_j():
    for i in range(0,9):
        listaBotones[i].config(state="normal")
        listaBotones[i].config(bg="#B983FF")
        listaBotones[i].config(text="")
        t[i] = "N"
    global nombre_jugador_1, nombre_jugador_2
    nombre_jugador_1 = simpledialog.askstring("Jugadores","Por favor escriba el nombre del jugador1: ")
    nombre_jugador_2 = simpledialog.askstring("Jugadores","Por favor escriba el nombre del jugador2: ")
    turno_jugador.set("Turno: "+nombre_jugador_1)
def cambiar(num):
    global turno,nombre_jugador_1,nombre_jugador_2
    if t[num] == "N" and turno == 0:
        listaBotones[num].config(text="X")
        listaBotones[num].config(font=("Ice kingdom", 9),fg="#FBF46D")
        t[num]="X"
        turno=1
        turno_jugador.set("Turno: "+nombre_jugador_2)
    elif t[num] == "N" and turno == 1:
        listaBotones[num].config(text="O")
        listaBotones[num].config(font=("Ice kingdom", 9),fg="#B4FE98")
        t[num]="O"
        turno=0
        turno_jugador.set("Turno: "+nombre_jugador_1)
    listaBotones[num].config(state="disable")
    verificar()
def verificar():
    if(t[0]=="X" and t[1]=="X" and t[2]=="X") or (t[3]=="X" and t[4]=="X" and t[5]=="X") or (t[6]=="X" and t[7]=="X" and t[8]=="X"): #Horizoantales
        bloquear()
        messagebox.showinfo("Ganador","Ganastes Jugador 🏆: "+nombre_jugador_1)
    elif(t[0]=="X" and t[3]=="X" and t[6]=="X") or (t[1]=="X" and t[4]=="X" and t[7]=="X") or (t[2]=="X" and t[5]=="X" and t[8]=="X"): #Verticales
        bloquear()
        messagebox.showinfo("Ganador","Ganastes Jugador 🏆: "+nombre_jugador_1)
    elif(t[0]=="X" and t[4]=="X" and t[8]=="X") or (t[2]=="X" and t[4]=="X" and t[6]=="X"): #Diagonales
        bloquear()
        messagebox.showinfo("Ganador","Ganastes Jugador 🏆:"+nombre_jugador_1)
    elif(t[0]=="O" and t[1]=="O" and t[2]=="O") or (t[3]=="O" and t[4]=="O" and t[5]=="O") or (t[6]=="O" and t[7]=="O" and t[8]=="O"): #Horizoantales
        bloquear()
        messagebox.showinfo("Ganador","Ganastes Jugador 🏆:"+nombre_jugador_2)
    elif(t[0]=="O" and t[3]=="O" and t[6]=="O") or (t[1]=="O" and t[4]=="O" and t[7]=="O") or (t[2]=="O" and t[5]=="O" and t[8]=="O"): #Verticales
        bloquear()
        messagebox.showinfo("Ganador","Ganastes Jugador 🏆:"+nombre_jugador_2)
    elif(t[0]=="O" and t[4]=="O" and t[8]=="O") or (t[2]=="O" and t[4]=="O" and t[6]=="O"): #Diagonales
        bloquear()
        messagebox.showinfo("Ganador","Ganastes Jugador 🏆:"+nombre_jugador_2)
    elif all(t[i] != "N" for i in range(9)):  # Empate
        bloquear()
        messagebox.showinfo("Empate", "Ambos jugadores empataron 😂")
#-----------------------------configuracion 4x4 -------------------------------------------------------
def bloquear_4():
    for i in range(0,16):
        listaBotones[i].config(state="disable")
def iniciar_4():
    for i in range(0,16):
        listaBotones[i].config(state="normal")
        listaBotones[i].config(bg="#B983FF")
        listaBotones[i].config(text="")
        t[i] = "N"
    global nombre_jugador_1, nombre_jugador_2
    nombre_jugador_1 = simpledialog.askstring("Jugadores","Por favor escriba el nombre del jugador1: ")
    nombre_jugador_2 = simpledialog.askstring("Jugadores","Por favor escriba el nombre del jugador2: ")
    turno_jugador.set("Turno: "+nombre_jugador_1)
def cambiar_4(num):
    global turno,nombre_jugador_1,nombre_jugador_2
    if t[num] == "N" and turno == 0:
        listaBotones[num].config(text="X")
        listaBotones[num].config(font=("Ice kingdom", 9),fg="#FBF46D")
        t[num]="X"
        turno=1
        turno_jugador.set("Turno: "+nombre_jugador_2)
    elif t[num] == "N" and turno == 1:
        listaBotones[num].config(text="O")
        listaBotones[num].config(font=("Ice kingdom", 9),fg="#B4FE98")
        t[num]="O"
        turno=0
        turno_jugador.set("Turno: "+nombre_jugador_1)
    listaBotones[num].config(state="disable")
    verificar_4()
def verificar_4():
    for i in range(0,13,4):
        if(t[i]=="X" and t[i+1]=="X" and t[i+2]=="X") or (t[i+1]=="X" and t[i+2]=="X" and t[i+3]=="X"):#Horizoantales
            bloquear_4()
            messagebox.showinfo("Ganador","Ganastes Jugador 🏆: "+nombre_jugador_1)
            continue
    for i in range(0,4,1):
        if(t[i]=="X" and t[i+4]=="X" and t[i+8]=="X") or (t[i+4]=="X" and t[i+8]=="X" and t[i+12]=="X"): #Verticales
            bloquear_4()
            messagebox.showinfo("Ganador","Ganastes Jugador 🏆: "+nombre_jugador_1)
            continue
    for i in range(0,5,4):
        if(t[i]=="X" and t[i+5]=="X" and t[i+10]=="X") or (t[i+1]=="X" and t[i+6]=="X" and t[i+11]=="X")or (t[i+2]=="X" and t[i+5]=="X" and t[i+8]=="X")or (t[i+3]=="X" and t[i+6]=="X" and t[i+9]=="X"): #Diagonales
            bloquear_4()
            messagebox.showinfo("Ganador","Ganastes Jugador 🏆:"+nombre_jugador_1)
            continue
    for i in range(0,13,4):
        if(t[i]=="O" and t[i+1]=="O" and t[i+2]=="O") or (t[i+1]=="O" and t[i+2]=="O" and t[i+3]=="O"):#Horizoantales
            bloquear_4()
            messagebox.showinfo("Ganador","Ganastes Jugador 🏆: "+nombre_jugador_2)
            continue
    for i in range(0,4,1):
        if(t[i]=="O" and t[i+4]=="O" and t[i+8]=="O") or (t[i+4]=="O" and t[i+8]=="O" and t[i+12]=="O"): #Verticales
            bloquear_4()
            messagebox.showinfo("Ganador","Ganastes Jugador 🏆: "+nombre_jugador_2)
            continue
    for i in range(0,5,4):
        if(t[i]=="O" and t[i+5]=="O" and t[i+10]=="O") or (t[i+1]=="O" and t[i+6]=="O" and t[i+11]=="O")or (t[i+2]=="O" and t[i+5]=="O" and t[i+8]=="O")or (t[i+3]=="O" and t[i+6]=="O" and t[i+9]=="O"): #Diagonales
            bloquear_4()
            messagebox.showinfo("Ganador","Ganastes Jugador 🏆:"+nombre_jugador_2)
            continue
        elif all(t[i] != "N" for i in range(16)):  # Empate
            bloquear_4()
            messagebox.showinfo("Empate", "Ambos jugadores empataron 😂")
#---------------------------------Configuracion gato 5x5----------------------------------------------
def bloquear_5():
    for i in range(0,25):
        listaBotones[i].config(state="disable")
def iniciar_5():
    for i in range(0,25):
        listaBotones[i].config(state="normal")
        listaBotones[i].config(bg="#B983FF")
        listaBotones[i].config(text="")
        t[i] = "N"
    global nombre_jugador_1, nombre_jugador_2
    nombre_jugador_1 = simpledialog.askstring("Jugadores","Por favor escriba el nombre del jugador1: ")
    nombre_jugador_2 = simpledialog.askstring("Jugadores","Por favor escriba el nombre del jugador2: ")
    turno_jugador.set("Turno: "+nombre_jugador_1)
def cambiar_5(num):
    global turno,nombre_jugador_1,nombre_jugador_2
    if t[num] == "N" and turno == 0:
        listaBotones[num].config(text="X")
        listaBotones[num].config(font=("Ice kingdom", 9),fg="#FBF46D")
        t[num]="X"
        turno=1
        turno_jugador.set("Turno: "+nombre_jugador_2)
    elif t[num] == "N" and turno == 1:
        listaBotones[num].config(text="O")
        listaBotones[num].config(font=("Ice kingdom", 9),fg="#B4FE98")
        t[num]="O"
        turno=0
        turno_jugador.set("Turno: "+nombre_jugador_1)
    listaBotones[num].config(state="disable")
    verificar_5()
def verificar_5():
    for i in range(0,21,5):
        if(t[i]=="X" and t[i+1]=="X" and t[i+2]=="X") or (t[i+1]=="X" and t[i+2]=="X" and t[i+3]=="X")or (t[i+2]=="X" and t[i+3]=="X" and t[i+4]=="X"):#Horizoantales
            bloquear_5()
            messagebox.showinfo("Ganador","Ganastes Jugador 🏆: "+nombre_jugador_1)
            continue
    for i in range(0,5,1):
        if(t[i]=="X" and t[i+5]=="X" and t[i+10]=="X") or (t[i+5]=="X" and t[i+10]=="X" and t[i+15]=="X")or (t[i+10]=="X" and t[i+15]=="X" and t[i+20]=="X"): #Verticales
            bloquear_5()
            messagebox.showinfo("Ganador","Ganastes Jugador 🏆: "+nombre_jugador_1)
            continue
    for i in range(0,11,5):
        if(t[i]=="X" and t[i+6]=="X" and t[i+12]=="X") or (t[i+1]=="X" and t[i+7]=="X" and t[i+13]=="X")or (t[i+2]=="X" and t[i+8]=="X" and t[i+14]=="X")or (t[i+2]=="X" and t[i+6]=="X" and t[i+10]=="X") or (t[i+3]=="X" and t[i+7]=="X" and t[i+11]=="X") or (t[i+4]=="X" and t[i+8]=="X" and t[i+12]=="X"): #Diagonales
            bloquear_5()
            messagebox.showinfo("Ganador","Ganastes Jugador 🏆:"+nombre_jugador_1)
            continue
    for i in range(0,21,5):
        if(t[i]=="O" and t[i+1]=="O" and t[i+2]=="O") or (t[i+1]=="O" and t[i+2]=="O" and t[i+3]=="O")or (t[i+2]=="O" and t[i+3]=="O" and t[i+4]=="O"):#Horizoantales
            bloquear_5()
            messagebox.showinfo("Ganador","Ganastes Jugador 🏆: "+nombre_jugador_2)
            continue
    for i in range(0,5,1):
        if(t[i]=="O" and t[i+5]=="O" and t[i+10]=="O") or (t[i+5]=="O" and t[i+10]=="O" and t[i+15]=="O")or (t[i+10]=="O" and t[i+15]=="O" and t[i+20]=="O"): #Verticales
            bloquear_5()
            messagebox.showinfo("Ganador","Ganastes Jugador 🏆: "+nombre_jugador_2)
            continue
    for i in range(0,13,5):
        if(t[i]=="O" and t[i+6]=="O" and t[i+12]=="O") or (t[i+1]=="O" and t[i+7]=="O" and t[i+13]=="O")or (t[i+2]=="O" and t[i+8]=="O" and t[i+14]=="O")or (t[i+2]=="O" and t[i+6]=="O" and t[i+10]=="O") or (t[i+3]=="O" and t[i+7]=="O" and t[i+11]=="O") or (t[i+4]=="O" and t[i+8]=="O" and t[i+12]=="O"): #Diagonales
            bloquear_5()
            messagebox.showinfo("Ganador","Ganastes Jugador 🏆:"+nombre_jugador_2)
            continue
        elif all(t[i] != "N" for i in range(25)):# Empate
            bloquear_5()
            messagebox.showinfo("Empate", "Ambos jugadores empataron 😂")
#--------------------Crecaion de la ventana principal-------------
raiz = Tk() #Crea la ventana
raiz.title("Principal") #titulo de la ventana
turno = 0
nombre_jugador_1 = ""
nombre_jugador_2 = ""
turno_jugador = StringVar()
listaBotones = []
t = []
ancho_ventana = 400
alto_ventana = 200
ancho_pantalla = raiz.winfo_screenwidth()
alto_pantalla = raiz.winfo_screenheight()
posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
posicion_y = int((alto_pantalla / 2) - (alto_ventana / 2))
raiz.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")  # Establecer el tamaño y posición de la ventana 
#-----------------------------------------Ventana principal-------------------------------
#--------------------Fondo de la ventana------------------------
imagen_fondo = Image.open("fondo principal.png")
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
label_fondo = Label(raiz, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
#---------------------------------------------------------------
#-------------------------Configuracion de la segunda ventana------
def abri_ventana():
    global ventana 
    raiz.withdraw() #cierra la ventana principal raiz
    global imagen
    ventana= Toplevel(raiz)#Crea la ventana
    ventana.title("Juego Gato")#titulo de la ventana
    ancho_ventana2 = 400
    alto_ventana2 = 200
    ancho_pantalla2 = ventana.winfo_screenwidth()
    alto_pantalla2 = ventana.winfo_screenheight()
    posicion_x2 = int((ancho_pantalla2 / 2) - (ancho_ventana2 / 2))
    posicion_y2 = int((alto_pantalla2 / 2) - (alto_ventana2 / 2))
    ventana.geometry(f"{ancho_ventana2}x{alto_ventana2}+{posicion_x2}+{posicion_y2}")
#----------------------------Fondo------------------------------------------------
    imagen= ImageTk.PhotoImage(Image.open("fondo principal.png"))
    label_fondo2 = Label(ventana, image=imagen)
    label_fondo2.place(x=0, y=0, relwidth=1, relheight=1)
    #-----------------------------------El tiulo principal de la ventana----------------
    label = Label(ventana, text="Bienvenidos al juego gato", font=("Ice kingdom", 14), fg="white", bg="#572975")
    label.pack()
    #--------------------------------------Los botones de la ventana----------------------
    boton_1 = Button(ventana, text="Jugador vs Jugador",font=("Ice kingdom", 11), fg="white", bg="#572975", command=lambda:ventana_judadores())
    boton_1.pack(side="right", padx=10, pady=(150, 10))
    boton_2 = Button(ventana, text="Jugador vs Maquina",font=("Ice kingdom", 11), fg="white", bg="#572975",command=lambda:ventana_maquina())
    boton_2.pack(side="left", padx=10, pady=(150, 10))
    # Botón para regresar a la ventana principal
    boton_regresar = Button(ventana, text="➢",font=("Ice kingdom", 11), fg="white", bg="#572975",command=lambda:regresar_ventana())
    boton_regresar.pack(side="left", padx=10, pady=(150, 10))
#-----------------------------------Termina la configuracion de la segunda ventana------------------------------
#-----------------------------------Metodo de regresara la ventana-------------------------------------------
def regresar_ventana():
    ventana.destroy() # Cerrar la ventana "Juego Gato"
    raiz.deiconify()  # Mostrar la ventana principal nuevamente
def regresar_ventana2():
    ventana_juagor.destroy() # Cerrar la ventana "Juegador"
    ventana.deiconify()  # Mostrar la ventana principal nuevamente
def regresar_ventana3():
    ventana_maquin.destroy() # Cerrar la ventana "maquina"
    ventana.deiconify()  # Mostrar la ventana principal nuevamente
def regresar_ventana4():
    gato_3.destroy() # Cerrar la ventana "Gato3x3"
    ventana_juagor.deiconify()  # Mostrar la ventana juagadores nuevamente
def regresar_ventana5():
    gato_4.destroy() # Cerrar la ventana "Gato4x4"
    ventana_juagor.deiconify()  # Mostrar la ventana juagadores nuevamente
def regresar_ventana6():
    gato_5.destroy() # Cerrar la ventana "Gato5x5"
    ventana_juagor.deiconify()  # Mostrar la ventana juagadores nuevamente
def regresar_ventana7():
    ventana_config.destroy() # Cerrar la ventana "Gato5x5"
    ventana_maquin.deiconify()  # Mostrar la ventana juagadores nuevamente
def regresar_ventana8():
    ventana_conf.destroy() # Cerrar la ventana "Gato5x5"
    ventana_maquin.deiconify()  # Mostrar la ventana juagadores nuevamente
def regresar_ventana9():
    ventana_con.destroy() # Cerrar la ventana "Gato5x5"
    ventana_maquin.deiconify()  # Mostrar la ventana juagadores nuevamente
def regresar_ventana10():
    ventana_juego.destroy() # Cerrar la ventana "Gato5x5"
    ventana_con.deiconify()  # Mostrar la ventana juagadores nuevamente
def regresar_ventana11():
    ventana_juego.destroy() # Cerrar la ventana "Gato4x4"
    ventana_conf.deiconify()  # Mostrar la ventana juagadores nuevamente
def regresar_ventana12():
    ventana_juego_1.destroy() # Cerrar la ventana "Gato3x3"
    ventana_config.deiconify()  # Mostrar la ventana juagadores nuevamente
#-----------------------------------Metodo de regresara la ventana-------------------------------------------
#------------------------------------Configuración de la ventana de jusgadores-----------------------------------
def ventana_judadores():
    global ventana_juagor
    ventana.withdraw() 
    global imagen2
    ventana_juagor= Toplevel(raiz)#Crea la ventana
    ventana_juagor.title("Juegador vs Jugador")#titulo de la ventana
    ancho_ventana2 = 400
    alto_ventana2 = 200
    ancho_pantalla2 = ventana_juagor.winfo_screenwidth()
    alto_pantalla2 = ventana_juagor.winfo_screenheight()
    posicion_x2 = int((ancho_pantalla2 / 2) - (ancho_ventana2 / 2))
    posicion_y2 = int((alto_pantalla2 / 2) - (alto_ventana2 / 2))
    ventana_juagor.geometry(f"{ancho_ventana2}x{alto_ventana2}+{posicion_x2}+{posicion_y2}")# Establecer el tamaño y posición de la ventana 
#----------------------------Fondo------------------------------------------------
    imagen2= ImageTk.PhotoImage(Image.open("fondo principal.png"))
    label_fondo2 = Label(ventana_juagor, image=imagen2)
    label_fondo2.place(x=0, y=0, relwidth=1, relheight=1)
    #-----------------------------------El tiulo principal de la ventana----------------
    label = Label(ventana_juagor, text="Jugador vs Jugador", font=("Ice kingdom", 14), fg="white", bg="#572975")
    label.pack()
    #--------------------------------------Los botones de la ventana----------------------
    boton_1 = Button(ventana_juagor, text="Gato 3x3",font=("Ice kingdom", 14), fg="white", bg="#572975",command=lambda:gato_3x3())
    boton_1.pack(side="left", padx=10, pady=10)
    boton_2 = Button(ventana_juagor, text="Gato 4x4",font=("Ice kingdom", 14), fg="white", bg="#572975",command=lambda:gato_4x4())
    boton_2.pack(side="left", padx=10, pady=10)
    boton_3 = Button(ventana_juagor, text="Gato 5x5",font=("Ice kingdom", 14), fg="white", bg="#572975",command=lambda:gato_5x5())
    boton_3.pack(side="left", padx=10, pady=10)
    boton_4 = Button(ventana_juagor, text="➢",font=("Ice kingdom", 11), fg="white", bg="#572975",command=lambda:regresar_ventana2())
    boton_4.pack(side="right", padx=10, pady=(150, 10))
#--------------------------------------------Terminar la configuracion de juagador vs jugador-----------------------------
#-----------------------------------------Configuracion de la ventana jugador vs maquina----------------------------------
def ventana_maquina():
    global ima
    ventana.withdraw() 
    global ventana_maquin
    ventana_maquin= Toplevel(raiz)#Crea la ventana
    ventana_maquin.title("Juegador vs Maquina ")#titulo de la ventana
    ancho_ventana2 = 400
    alto_ventana2 = 200
    ancho_pantalla2 = ventana_maquin.winfo_screenwidth()
    alto_pantalla2 = ventana_maquin.winfo_screenheight()
    posicion_x2 = int((ancho_pantalla2 / 2) - (ancho_ventana2 / 2))
    posicion_y2 = int((alto_pantalla2 / 2) - (alto_ventana2 / 2))
    ventana_maquin.geometry(f"{ancho_ventana2}x{alto_ventana2}+{posicion_x2}+{posicion_y2}")# Establecer el tamaño y posición de la ventana 
#----------------------------Fondo------------------------------------------------
    ima= ImageTk.PhotoImage(Image.open("fondo principal.png"))
    label_fondo2 = Label(ventana_maquin, image=ima)
    label_fondo2.place(x=0, y=0, relwidth=1, relheight=1)
    #-----------------------------------El tiulo principal de la ventana----------------
    label = Label(ventana_maquin, text="Jugador vs Maquina", font=("Ice kingdom", 14), fg="white", bg="#572975")
    label.pack()
    #--------------------------------------Los botones de la ventana----------------------
    boton_1 = Button(ventana_maquin, text="Gato 3x3",font=("Ice kingdom", 14), fg="white", bg="#572975",command=lambda:seleccionar_tamano_3())
    boton_1.pack(side="left", padx=10, pady=10)
    boton_2 = Button(ventana_maquin, text="Gato 4x4",font=("Ice kingdom", 14), fg="white", bg="#572975",command=lambda:seleccionar_tamano_4())
    boton_2.pack(side="left", padx=10, pady=10)
    boton_3 = Button(ventana_maquin, text="Gato 5x5",font=("Ice kingdom", 14), fg="white", bg="#572975",command=lambda:seleccionar_tamano_5())
    boton_3.pack(side="left", padx=10, pady=10)
    boton_4 = Button(ventana_maquin, text="➢",font=("Ice kingdom", 11), fg="white", bg="#572975",command=lambda:regresar_ventana3())
    boton_4.pack(side="right", padx=10, pady=(150, 10))
#------------------------------------------Terminar la configuracion de juagador vs maquina-------------------------------------------
#-----------------------------------------Gato 3x3----------------------------
def gato_3x3 ():
    global gato_3
    global photo
    ventana_juagor.withdraw()
    gato_3 = tk.Toplevel()
    gato_3.title("Gato 3x3")
    ancho_ventana2 = 400
    alto_ventana2 = 500
    ancho_pantalla2 = gato_3.winfo_screenwidth()
    alto_pantalla2 = gato_3.winfo_screenheight()
    posicion_x2 = int((ancho_pantalla2 / 2) - (ancho_ventana2 / 2))
    posicion_y2 = int((alto_pantalla2 / 2) - (alto_ventana2 / 2))
    gato_3.geometry(f"{ancho_ventana2}x{alto_ventana2}+{posicion_x2}+{posicion_y2}")
    #----------------------------Fondo------------------------------------------------
    photo= ImageTk.PhotoImage(Image.open("photo.png"))
    label_fondo2 = Label(gato_3, image=photo)
    label_fondo2.place(x=0, y=0, relwidth=1, relheight=1)
    #-----------------------------------El tiulo principal de la ventana----------------
    label = Label(gato_3, text="Juego de gato 3x3", font=("Ice kingdom", 8), fg="white", bg="#C679B4")
    label.pack()
    for i in range(0,9):
        t.append("N")
    boton_0 = Button(gato_3,width=9,height=3,command=lambda:cambiar(0))
    listaBotones.append(boton_0)
    boton_0.place(x=70,y=70)
    boton_1 = Button(gato_3,width=9,height=3,command=lambda:cambiar(1))
    listaBotones.append(boton_1)
    boton_1.place(x=170,y=70)
    boton_2 = Button(gato_3,width=9,height=3,command=lambda:cambiar(2))
    listaBotones.append(boton_2)
    boton_2.place(x=270,y=70)
    boton_3 = Button(gato_3,width=9,height=3,command=lambda:cambiar(3))
    listaBotones.append(boton_3)
    boton_3.place(x=70,y=170)
    boton_4 = Button(gato_3,width=9,height=3,command=lambda:cambiar(4))
    listaBotones.append(boton_4)
    boton_4.place(x=170,y=170)
    boton_5 = Button(gato_3,width=9,height=3,command=lambda:cambiar(5))
    listaBotones.append(boton_5)
    boton_5.place(x=270,y=170)
    boton_6 = Button(gato_3,width=9,height=3,command=lambda:cambiar(6))
    listaBotones.append(boton_6)
    boton_6.place(x=70,y=270)
    boton_7 = Button(gato_3,width=9,height=3,command=lambda:cambiar(7))
    listaBotones.append(boton_7)
    boton_7.place(x=170,y=270)
    boton_8 = Button(gato_3,width=9,height=3,command=lambda:cambiar(8))
    listaBotones.append(boton_8)
    boton_8.place(x=270,y=270)
    turno_e = Label(gato_3,textvariable=turno_jugador)
    turno_e.place(x=55,y=30)
    iniciar = Button(gato_3,bg="#C679B4",fg="white",font=("Ice kingdom", 14),text="Inicar juego",width=15,height=3,command=lambda:iniciar_j())
    iniciar.place(x=130,y=350)
    boton_4 = Button(gato_3, text="⇦",font=("Ice kingdom", 11), fg="white", bg="#C679B4",command=lambda:regresar_ventana4())
    boton_4.pack(side="right", padx=(350,10), pady=(350,10))
    bloquear()
#-----------------------------------------Gato 4x4----------------------------
def gato_4x4 ():
    global gato_4
    global photos
    ventana_juagor.withdraw()
    gato_4 = tk.Toplevel()
    gato_4.title("Gato 4x4")
    ancho_ventana2 = 500
    alto_ventana2 = 600
    ancho_pantalla2 = gato_4.winfo_screenwidth()
    alto_pantalla2 = gato_4.winfo_screenheight()
    posicion_x2 = int((ancho_pantalla2 / 2) - (ancho_ventana2 / 2))
    posicion_y2 = int((alto_pantalla2 / 2) - (alto_ventana2 / 2))
    gato_4.geometry(f"{ancho_ventana2}x{alto_ventana2}+{posicion_x2}+{posicion_y2}")
    #----------------------------Fondo------------------------------------------------
    photos= ImageTk.PhotoImage(Image.open("photo.png"))
    label_fondo2 = Label(gato_4, image=photos)
    label_fondo2.place(x=0, y=0, relwidth=1, relheight=1)
    #-----------------------------------El tiulo principal de la ventana----------------
    label = Label(gato_4, text="Juego de gato 4x4", font=("Ice kingdom", 14), fg="white", bg="#C679B4")
    label.pack()
    for i in range(0,16):
        t.append("N")
    boton_0 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(0))
    listaBotones.append(boton_0)
    boton_0.place(x=70,y=70)
    boton_1 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(1))
    listaBotones.append(boton_1)
    boton_1.place(x=170,y=70)
    boton_2 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(2))
    listaBotones.append(boton_2)
    boton_2.place(x=270,y=70)
    boton_3 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(3))
    listaBotones.append(boton_3)
    boton_3.place(x=370,y=70)
    boton_4 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(4))
    listaBotones.append(boton_4)
    boton_4.place(x=70,y=170)
    boton_5 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(5))
    listaBotones.append(boton_5)
    boton_5.place(x=170,y=170)
    boton_6 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(6))
    listaBotones.append(boton_6)
    boton_6.place(x=270,y=170)
    boton_7 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(7))
    listaBotones.append(boton_7)
    boton_7.place(x=370,y=170)
    boton_8 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(8))
    listaBotones.append(boton_8)
    boton_8.place(x=70,y=270)
    boton_9 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(9))
    listaBotones.append(boton_9)
    boton_9.place(x=170,y=270)
    boton_10 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(10))
    listaBotones.append(boton_10)
    boton_10.place(x=270,y=270)
    boton_11 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(11))
    listaBotones.append(boton_11)
    boton_11.place(x=370,y=270)
    boton_12 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(12))
    listaBotones.append(boton_12)
    boton_12.place(x=70,y=370)
    boton_13 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(13))
    listaBotones.append(boton_13)
    boton_13.place(x=170,y=370)
    boton_14 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(14))
    listaBotones.append(boton_14)
    boton_14.place(x=270,y=370)
    boton_15 = Button(gato_4,width=9,height=3,command=lambda:cambiar_4(15))
    listaBotones.append(boton_15)
    boton_15.place(x=370,y=370)
    turno_e = Label(gato_4,textvariable=turno_jugador)
    turno_e.place(x=55,y=30)
    iniciar = Button(gato_4,bg="#C679B4",fg="white",font=("Ice kingdom", 14),text="Inicar juego",width=15,height=3,command=lambda:iniciar_4())
    iniciar.place(x=175,y=450)
    boton_4 = Button(gato_4, text="⇦",font=("Ice kingdom", 11), fg="white", bg="#C679B4",command=lambda:regresar_ventana5())
    boton_4.pack(side="right", padx=(350,10), pady=(350,10))
    bloquear_4()
#-----------------------------------------Gato 5x5----------------------------
def gato_5x5 ():
    global gato_5
    global photoss
    ventana_juagor.withdraw()
    gato_5 = tk.Toplevel()
    gato_5.title("Gato 5x5")
    ancho_ventana2 = 600
    alto_ventana2 = 700
    ancho_pantalla2 = gato_5.winfo_screenwidth()
    alto_pantalla2 = gato_5.winfo_screenheight()
    posicion_x2 = int((ancho_pantalla2 / 2) - (ancho_ventana2 / 2))
    posicion_y2 = int((alto_pantalla2 / 2) - (alto_ventana2 / 2))
    gato_5.geometry(f"{ancho_ventana2}x{alto_ventana2}+{posicion_x2}+{posicion_y2}")
    #----------------------------Fondo------------------------------------------------
    photoss= ImageTk.PhotoImage(Image.open("photo.png"))
    label_fondo2 = Label(gato_5, image=photoss)
    label_fondo2.place(x=0, y=0, relwidth=1, relheight=1)
    #-----------------------------------El tiulo principal de la ventana----------------
    label = Label(gato_5, text="Juego de gato 5x5", font=("Ice kingdom", 12), fg="white", bg="#C679B4")
    label.pack()
    for i in range(0,25):
        t.append("N")
    boton_0 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(0))
    listaBotones.append(boton_0)
    boton_0.place(x=70,y=70)
    boton_1 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(1))
    listaBotones.append(boton_1)
    boton_1.place(x=170,y=70)
    boton_2 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(2))
    listaBotones.append(boton_2)
    boton_2.place(x=270,y=70)
    boton_3 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(3))
    listaBotones.append(boton_3)
    boton_3.place(x=370,y=70)
    boton_4 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(4))
    listaBotones.append(boton_4)
    boton_4.place(x=470,y=70)
    boton_5 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(5))
    listaBotones.append(boton_5)
    boton_5.place(x=70,y=170)
    boton_6 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(6))
    listaBotones.append(boton_6)
    boton_6.place(x=170,y=170)
    boton_7 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(7))
    listaBotones.append(boton_7)
    boton_7.place(x=270,y=170)
    boton_8 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(8))
    listaBotones.append(boton_8)
    boton_8.place(x=370,y=170)
    boton_9 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(9))
    listaBotones.append(boton_9)
    boton_9.place(x=470,y=170)
    boton_10 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(10))
    listaBotones.append(boton_10)
    boton_10.place(x=70,y=270)
    boton_11 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(11))
    listaBotones.append(boton_11)
    boton_11.place(x=170,y=270)
    boton_12 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(12))
    listaBotones.append(boton_12)
    boton_12.place(x=270,y=270)
    boton_13 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(13))
    listaBotones.append(boton_13)
    boton_13.place(x=370,y=270)
    boton_14 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(14))
    listaBotones.append(boton_14)
    boton_14.place(x=470,y=270)
    boton_15 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(15))
    listaBotones.append(boton_15)
    boton_15.place(x=70,y=370)
    boton_16 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(16))
    listaBotones.append(boton_16)
    boton_16.place(x=170,y=370)
    boton_17 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(17))
    listaBotones.append(boton_17)
    boton_17.place(x=270,y=370)
    boton_18 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(18))
    listaBotones.append(boton_18)
    boton_18.place(x=370,y=370)
    boton_19 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(19))
    listaBotones.append(boton_19)
    boton_19.place(x=470,y=370)
    boton_20 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(20))
    listaBotones.append(boton_20)
    boton_20.place(x=70,y=470)
    boton_21 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(21))
    listaBotones.append(boton_21)
    boton_21.place(x=170,y=470)
    boton_22 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(22))
    listaBotones.append(boton_22)
    boton_22.place(x=270,y=470)
    boton_23 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(23))
    listaBotones.append(boton_23)
    boton_23.place(x=370,y=470)
    boton_24 = Button(gato_5,width=9,height=3,command=lambda:cambiar_5(24))
    listaBotones.append(boton_24)
    boton_24.place(x=470,y=470)
    turno_e = Label(gato_5,textvariable=turno_jugador)
    turno_e.place(x=55,y=30)
    iniciar = Button(gato_5,bg="#C679B4",fg="white",font=("Ice kingdom", 14),text="Inicar juego",width=15,height=3,command=lambda:iniciar_5())
    iniciar.place(x=200,y=550)
    boton_4 = Button(gato_5, text="⇦",font=("Ice kingdom", 11), fg="white", bg="#C679B4",command=lambda:regresar_ventana6())
    boton_4.pack(side="right", padx=(350,10), pady=(350,10))
    bloquear_5()
#-----------------------------------Aquí termina los gatos de jugadores vs jugadores-------------------------------------------
#------------------------Crear el boton princinpal-----------------
boton = Button(raiz, text="Iniciar juego",font=("Ice kingdom", 14), fg="white", bg="#572975",command=lambda:abri_ventana())
boton.pack(side="right", padx=10, pady=(150, 10), anchor="se")
#----------------------se monostrara en la ventana----------------------------------------
raiz.mainloop() #Lo que muestra en la ventana
