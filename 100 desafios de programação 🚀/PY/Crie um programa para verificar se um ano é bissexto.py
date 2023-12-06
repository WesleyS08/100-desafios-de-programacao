import tkinter as tk
from tkinter import messagebox

def contar():
    try:
        ano =int(entry.get())
        if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
            messagebox.showinfo("Ano Bissexto", f'O ano {ano} é bissexto')
        else:
            messagebox.showinfo("Ano Não Bissexto",
                                f'O ano {ano} não é bissexto')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")


# Criar janela
janela = tk.Tk()
janela.title("Ano bissexto")

# Criar rótulo para o texto "Digite um número:"
rotulo = tk.Label(janela, text="Digite um ano para verificar")
rotulo.pack(pady=2)

# Criar entrada (entry) para o número
entry = tk.Entry(janela)
entry.pack(pady=25)

# Criar botão para verificar o número
botao_verificar = tk.Button(janela, text="verificar", command=contar)
botao_verificar.pack()

# Rodar a janela
janela.mainloop()
