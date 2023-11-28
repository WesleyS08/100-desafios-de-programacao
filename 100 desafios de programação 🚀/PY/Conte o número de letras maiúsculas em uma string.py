import tkinter as tk
from tkinter import messagebox


def palavras():
    try:
        contagem = 0
        string = str(entry.get())
        for caractere in string:
            if caractere.isupper():
                contagem += 1
        messagebox.showinfo("O numero de letras maisculas é", f'A  palavra {string} tem {contagem} letras maiusculas')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")


# Criar janela
janela = tk.Tk()
janela.title("Letras maiusculas em uma palavra")

# Rótulo e entrada 
rotulo_numero = tk.Label(janela, text="Digite ua palavra:")
rotulo_numero.pack(pady=2)

entry = tk.Entry(janela)
entry.pack(pady=2)


botao_calcular = tk.Button(janela, text="Contar", command=palavras)
botao_calcular.pack(pady=2)

# Rodar a janela
janela.mainloop()
