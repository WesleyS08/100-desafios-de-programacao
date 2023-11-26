import tkinter as tk
from tkinter import messagebox 

def verificar_numero(): 
    try:
        numero = int(entry.get())
        if numero == 0:
            messagebox.showinfo("Resultado", f'O número {numero} é zero!')
        elif numero % 2 == 0:
            messagebox.showinfo("Resultado", f'O número {numero} é par!')
        else:
            messagebox.showinfo("Resultado", f'O número {numero} é ímpar!')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")

# Criar janela
janela = tk.Tk()
janela.title("Verificador de Números")

# Criar rótulo para o texto "Digite um número:"
rotulo = tk.Label(janela, text="Digite um número:")
rotulo.pack(pady=2)

# Criar entrada (entry) para o número
entry = tk.Entry(janela)
entry.pack(pady=25)

# Criar botão para verificar o número
botao_verificar = tk.Button( janela, text="Verificar", command=verificar_numero)
botao_verificar.pack()

# Rodar a janela
janela.mainloop()