import tkinter as tk
from tkinter import messagebox


def soma_numeros():
    try:
        numero1 = int(entry.get())
        numero2 = int(entry2.get())

        resultado = numero1 + numero2
        messagebox.showinfo("O resultado da soma",
                            f'{numero1} + {numero2} = {resultado}')
    except ValueError:
        messagebox.showerror("ERRO!!!!")


# criar janela
janela = tk.Tk()
janela.title("Soma de números")

# Criar rótulo para o texto "Digite um número:"
rotulo = tk.Label(janela, text="Digite o primeiro número:")
rotulo.pack(pady=2)

# Criar entrada (entry) para o primeiro número
entry = tk.Entry(janela)
entry.pack(pady=2)

# Criar rótulo para o texto "Digite outro número:"
rotulo2 = tk.Label(janela, text="Digite o segundo número:")
rotulo2.pack(pady=2)

# Criar entrada (entry) para o segundo número
entry2 = tk.Entry(janela)
entry2.pack(pady=2)

# Criar botão para somar os números
botao_somar = tk.Button(janela, text="Somar", command=soma_numeros)
botao_somar.pack()

# Rodar a janela
janela.mainloop()
