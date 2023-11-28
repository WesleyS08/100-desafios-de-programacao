import tkinter as tk
from tkinter import messagebox
import requests


def calcular_imc():
    altura = float(entry_altura.get())
    peso = float(entry_peso.get())

    # Cálculo do IMC
    imc = peso / (altura ** 2)
    # Exibição do IMC e categoria
    if imc < 18.5:
        mensagem = f"Seu IMC é: {imc:.2f}\nMagreza"
    elif 18.5 <= imc <= 24.9:
        mensagem = f"Seu IMC é: {imc:.2f}\nNormal"
    elif 25 <= imc <= 29.9:
        mensagem = f"Seu IMC é: {imc:.2f}\nSobrepeso"
    elif 30 <= imc <= 39.9:
        mensagem = f"Seu IMC é: {imc:.2f}\nObesidade"
    else:
        mensagem = f"Seu IMC é: {imc:.2f}\nObesidade Grave"

    # Exibe a mensagem
    messagebox.showinfo("Resultado", mensagem)

# Criar janela
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Rótulo e entrada para altura
rotulo_altura = tk.Label(janela, text="Altura (metros):")
rotulo_altura.pack()
entry_altura = tk.Entry(janela)
entry_altura.pack()

# Rótulo e entrada para peso
rotulo_peso = tk.Label(janela, text="Peso (quilos):")
rotulo_peso.pack()
entry_peso = tk.Entry(janela)
entry_peso.pack()

# Botão para calcular o IMC
botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack()

# Rodar a janela
janela.mainloop()
