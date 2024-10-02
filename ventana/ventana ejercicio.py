import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ventana de ejercicio")
ventana.geometry("1000x600+250+100")

# Crear frames
frame1 = tk.Frame(ventana)
frame1.configure(bg="peach puff", bd=20)
frame1.place(x=10, y=10, width=480, height=280)

frame2 = tk.Frame(ventana)
frame2.configure(bg="peach puff", bd=20)
frame2.place(x=510, y=10, width=480, height=280)

frame3 = tk.Frame(ventana)
frame3.configure(bg="peach puff", bd=20)
frame3.place(x=10, y=310, width=480, height=280)

frame4 = tk.Frame(ventana)
frame4.configure(bg="peach puff", bd=20)
frame4.place(x=510, y=310, width=480, height=280)

# Crear etiquetas
etiqueta1 = tk.Label(frame3, text="Presiona el botón")
etiqueta1.configure(fg="gray8", bg="rosy brown", font=("Arial", 16))
etiqueta1.place(x=10, y=30, width=400, height=20)

etiqueta2 = tk.Label(frame4, text="Etiqueta")
etiqueta2.configure(fg="gray8", bg="rosy brown", font=("Arial", 16))
etiqueta2.place(x=10, y=110, width=150, height=20)

# Crear botones
boton1 = tk.Button(frame3, text="Botón", font=("Arial", 16), bg="LightSkyBlue3")
boton1.place(x=150, y=110, width=150, height=20)

boton2 = tk.Button(frame4, text="Botón", font=("Arial", 16), bg="LightSkyBlue3")
boton2.place(x=170, y=110, width=150, height=20)

# Configurar ventana principal
ventana.configure(bg="gray")

# Iniciar bucle principal
ventana.mainloop()