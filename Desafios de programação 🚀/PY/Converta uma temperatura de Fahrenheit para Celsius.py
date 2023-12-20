from fractions import Fraction
import tkinter as tk
from tkinter import messagebox

def conversão(): 
    try:
        n= int(entry.get())
        f = Fraction(5,9)
        c =float(n - 32) * f
        messagebox.showinfo("Resultado", "A temperatura em Celsius é: {:.2f}".format(c))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")

# Criar janela
janela = tk.Tk()
janela.title("Conversão de temperatura")

# Criar rótulo para o texto "Digite um número:"
rotulo = tk.Label(janela, text="Digite uma temperatura em fahrenheit:")
rotulo.pack(pady=2)

# Criar entrada (entry) para o número
entry = tk.Entry(janela)
entry.pack(pady=25)

# Criar botão para verificar o número
botao_verificar = tk.Button( janela, text="conversão", command=conversão)
botao_verificar.pack()

# Rodar a janela
janela.mainloop()