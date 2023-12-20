import tkinter as tk
from tkinter import messagebox

# Lista para armazenar os números
lista = []


def adicionar():
    try:
        # Adicionar o número à lista
        numero = int(entry_altura.get())
        lista.append(numero)
        messagebox.showinfo("Sucesso", f"Número {numero} adicionado à lista!")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")


def calcular_media():
    try:
        # Verificar se a lista não está vazia
        if len(lista) == 0:
            messagebox.showerror(
                "Erro", "A lista está vazia. Adicione números antes de calcular a média.")
        else:
            # Calcular a média
            resultado = sum(lista) / len(lista)
            messagebox.showinfo(
                "Média", f'O resultado da média é: {resultado}')
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")


# Criar janela
janela = tk.Tk()
janela.title("Média de uma lista")

# Rótulo e entrada para número
rotulo_numero = tk.Label(janela, text="Digite um número para a lista:")
rotulo_numero.pack(pady=2)

entry_altura = tk.Entry(janela)
entry_altura.pack(pady=2)

# Botão para adicionar número
botao_adicionar = tk.Button(janela, text="Adicionar", command=adicionar)
botao_adicionar.pack(pady=2)

# Botão para calcular média
botao_media = tk.Button(janela, text="Calcular Média", command=calcular_media)
botao_media.pack(pady=2)

# Rodar a janela
janela.mainloop()
