import tkinter as tk
from tkinter import messagebox


def texto():
    try:
        palavra = str(entry.get())
        mensagem = f'A palavra {palavra} ao contario fica {palavra[::-1]} '
        messagebox.showinfo("Palavra ao contrário", mensagem)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite uma palavra válido.")


# Criar janela
janela = tk.Tk()
janela.title("texto ao contrário")

# Criar rótulo para o texto "Digite um número:"
rotulo = tk.Label(janela, text="Digite uma palavra:")
rotulo.pack(pady=2)

# Criar entrada (entry) para o número
entry = tk.Entry(janela)
entry.pack(pady=25)

# Criar botão para verificar o número
botao_verificar = tk.Button(janela, text="inverter", command=texto)
botao_verificar.pack()

# Rodar a janela
janela.mainloop()
