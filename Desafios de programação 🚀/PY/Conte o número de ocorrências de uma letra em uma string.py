import tkinter as tk
from tkinter import messagebox


def palavras():
    try:
        texto = str(entry.get())
        carac = str(entry1.get())

        messagebox.showinfo("O numero de repetição é",
                            f'O {texto} inserido possui {texto.count(carac)} caracteres "{carac}" ')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")


# Criar janela
janela = tk.Tk()
janela.title("Contagem de letras iguais")

# Rótulo e entrada
rotulo_numero = tk.Label(janela, text="Digite ua palavra:")
rotulo_numero.pack(pady=2)

entry = tk.Entry(janela)
entry.pack(pady=2)

rotulo_numero = tk.Label(janela, text="Digite um caracter:")
rotulo_numero.pack(pady=2)

entry1 = tk.Entry(janela)
entry1.pack(pady=2)


botao_calcular = tk.Button(janela, text="Contar", command=palavras)
botao_calcular.pack(pady=2)

# Rodar a janela
janela.mainloop()
