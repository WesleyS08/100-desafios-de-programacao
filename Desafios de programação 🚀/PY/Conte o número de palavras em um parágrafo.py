import tkinter as tk
from tkinter import messagebox


def palavras():
    try:
    
        string = str(entry.get())
        palavras = string.split()
        messagebox.showinfo("O numero de paravras é",
                            f'O paragrado tem {len(palavras)} palavras')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")


# Criar janela
janela = tk.Tk()
janela.title("contagem de palavras em um paragrafo")

# Rótulo e entrada
rotulo_numero = tk.Label(janela, text="Digite um paragrafo:")
rotulo_numero.pack(pady=2)

entry = tk.Entry(janela)
entry.pack(pady=2)


botao_calcular = tk.Button(janela, text="Contar", command=palavras)
botao_calcular.pack(pady=2)

# Rodar a janela
janela.mainloop()
