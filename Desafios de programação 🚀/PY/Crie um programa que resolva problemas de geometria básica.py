import tkinter as tk
from tkinter import ttk
import math


def calcular_retangulo():
    try:
        base = float(entry_base_retangulo.get())
        altura = float(entry_altura_retangulo.get())

        area = base * altura
        perimetro = 2 * (base + altura)

        resultado_retangulo_label.config(
            text=f"Área: {area}\nPerímetro: {perimetro}")

    except ValueError:
        resultado_retangulo_label.config(
            text="Por favor, insira valores numéricos para a base e altura.")


def calcular_circulo():
    try:
        raio = float(entry_raio_circulo.get())

        area = math.pi * raio**2
        perimetro = 2 * math.pi * raio

        resultado_circulo_label.config(
            text=f"Área: {area}\nPerímetro: {perimetro}")

    except ValueError:
        resultado_circulo_label.config(
            text="Por favor, insira um valor numérico para o raio.")


# Criar a janela principal
root = tk.Tk()
root.title("Cálculos de Geometria Básica")

# Criar widgets para o retângulo
frame_retangulo = ttk.Frame(root, padding="10")
frame_retangulo.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_base_retangulo = ttk.Label(frame_retangulo, text="Base:")
label_base_retangulo.grid(column=0, row=0, padx=5, pady=5, sticky=tk.E)

entry_base_retangulo = ttk.Entry(frame_retangulo)
entry_base_retangulo.grid(column=1, row=0, padx=5, pady=5, sticky=(tk.W, tk.E))

label_altura_retangulo = ttk.Label(frame_retangulo, text="Altura:")
label_altura_retangulo.grid(column=0, row=1, padx=5, pady=5, sticky=tk.E)

entry_altura_retangulo = ttk.Entry(frame_retangulo)
entry_altura_retangulo.grid(column=1, row=1, padx=5,
                            pady=5, sticky=(tk.W, tk.E))

botao_calcular_retangulo = ttk.Button(
    frame_retangulo, text="Calcular", command=calcular_retangulo)
botao_calcular_retangulo.grid(column=0, row=2, columnspan=2, pady=10)

resultado_retangulo_label = ttk.Label(frame_retangulo, text="")
resultado_retangulo_label.grid(column=0, row=3, columnspan=2)

# Criar widgets para o círculo
frame_circulo = ttk.Frame(root, padding="10")
frame_circulo.grid(column=1, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_raio_circulo = ttk.Label(frame_circulo, text="Raio:")
label_raio_circulo.grid(column=0, row=0, padx=5, pady=5, sticky=tk.E)

entry_raio_circulo = ttk.Entry(frame_circulo)
entry_raio_circulo.grid(column=1, row=0, padx=5, pady=5, sticky=(tk.W, tk.E))

botao_calcular_circulo = ttk.Button(
    frame_circulo, text="Calcular", command=calcular_circulo)
botao_calcular_circulo.grid(column=0, row=1, columnspan=2, pady=10)

resultado_circulo_label = ttk.Label(frame_circulo, text="")
resultado_circulo_label.grid(column=0, row=2, columnspan=2)

# Iniciar o loop da interface gráfica
root.mainloop()
