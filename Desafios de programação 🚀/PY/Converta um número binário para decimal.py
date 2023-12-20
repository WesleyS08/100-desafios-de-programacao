import tkinter as tk
from tkinter import messagebox


def binario_para_decimal():
    try:
        binario = entry.get()  # Obtém o valor da entrada
        decimal = int(binario, 2)

        messagebox.showinfo(
            "Resultado", f'O número binário {binario} em decimal é: {decimal}')
    except ValueError:
        messagebox.showerror(
            "Erro", "Por favor, digite um número binário válido.")


# Criar janela
janela = tk.Tk()
janela.title("Binário para decimal")

# Criar rótulo para o texto "Digite um número:"
rotulo = tk.Label(janela, text="Digite um número binário:")
rotulo.pack(pady=2)

# Criar entrada (entry) para o número
entry = tk.Entry(janela)
entry.pack(pady=25)

# Criar botão para verificar o número
botao_verificar = tk.Button(
    janela, text="Transformar", command=binario_para_decimal)
botao_verificar.pack()

# Rodar a janela
janela.mainloop()
