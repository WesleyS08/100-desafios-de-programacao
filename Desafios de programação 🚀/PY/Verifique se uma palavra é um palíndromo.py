import tkinter as tk
from tkinter import messagebox


def palíndromo():
    try:
        word = entry.get()
        if str(word) == str(word)[::-1]:
            messagebox.showinfo("Palíndromo", 'É Palíndromo')
        else:
            messagebox.showinfo("Palíndromo", 'Não é Palíndromo')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite uma palavra válida.")


# Criar janela
janela = tk.Tk()
janela.title("Palavra palíndromo")

# Criar rótulo para o texto "Digite um número:"
rotulo = tk.Label(janela, text="Digite uma palavra para verificar")
rotulo.pack(pady=2)

entry = tk.Entry(janela)
entry.pack(pady=25)

botao_verificar = tk.Button(janela, text="Verificar", command=palíndromo)
botao_verificar.pack()

# Rodar a janela
janela.mainloop()
