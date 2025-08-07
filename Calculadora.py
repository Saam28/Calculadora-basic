import tkinter as tk

ventana = tk.Tk()
ventana.title("Mini calculadora")
ventana.geometry("300x450")
ventana.configure(bg="#eef")


expresiones = tk.StringVar()
resultados = tk.StringVar()

expresion = tk.Label(ventana, textvariable=expresiones, font=("Arial", 14), anchor="e", bg="#eef", fg="#333", relief="groove").pack(fill="both", padx=10, pady=(10, 0))
resultado = tk.Label(ventana, textvariable=resultados, font=("Arial", 24), anchor="e", bg="#eef", fg="#000").pack(fill="both", padx=10, pady=(0, 10))


def agregar(valor):
    operadores = "+-*/"
    actual = expresiones.get()

    # Validación de operadores
    if valor in operadores:
        if not actual and valor in "*/":
            return  # no puede empezar con * o /
        if actual[-1] in operadores:
            return  # no puede haber dos operadores seguidos

    # Validación del punto decimal
    if valor == ".":
        if not actual or actual[-1] == ".":
            return  # no puede comenzar con punto o repetir
        # evitar múltiples puntos en un número
        i = len(actual) - 1
        while i >= 0 and (actual[i].isdigit() or actual[i] == "."):
            if actual[i] == ".":
                return  # ya hay un punto
            i -= 1

    # Si todo pasa, agregar el valor
    expresiones.set(actual + str(valor))
    resultados.set("")


def borrar_ultimo():
    expresiones.set(expresiones.get()[:-1])

def calcula():
    try:
        resultado = eval(expresiones.get())
        
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)
        resultados.set(str(resultado))
    except:
        expresiones.set("ERROR")

def borrar():
    expresiones.set("")
    resultados.set("")


botones = tk.Frame(ventana, bg="#eef")
botones.pack()

numeros = [
    ["7", "8", "9", "/"],
    ["6", "5", "4", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "←"]
]

colores = {
    "=": "#a8e6cf",
    "C": "#ff8a80",
    "←": "#ff8a80",
    "+": "#d0e6ff",
    "-": "#d0e6ff",
    "*": "#d0e6ff",
    "/": "#d0e6ff",
}

for fila in range(len(numeros)):
    botones.grid_rowconfigure(fila, weight=1)
    for col in range(len(numeros[fila])):
        botones.grid_columnconfigure(col, weight=1)
        texto = numeros[fila][col]
        if texto == "=":
            accion = calcula
            
        elif texto == "C":
            accion = borrar
        elif texto == "←":
            accion = borrar_ultimo
        else:
            accion = lambda click=texto: agregar(click)

        color = colores.get(texto, "#ffffff") # Por defecto, blanco

        tk.Button(botones, 
                  text=texto, 
                  command=accion, 
                  font=("Segoe UI", 14), 
                  width=5, 
                  height=2,
                  bg=color
                  ).grid(row=fila, column=col, padx=5, pady=5)

ventana.mainloop()