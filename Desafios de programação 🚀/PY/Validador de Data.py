import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def validar_data():
    try:
        data_str = entry.get()
        data = datetime.strptime(data_str, "%d/%m/%Y")
        messagebox.showinfo("Validação de Data", f'A data {data_str} é válida!')
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido. Por favor, use o formato DD/MM/AAAA.")

# Criar janela
janela = tk.Tk()
janela.title("Validador de Data")

# Criar rótulo para o texto "Digite uma data:"
rotulo = tk.Label(janela, text="Digite uma data para validar (DD/MM/AAAA)")
rotulo.pack(pady=2)

entry = tk.Entry(janela)
entry.pack(pady=25)

botao_validar = tk.Button(janela, text="Validar Data", command=validar_data)
botao_validar.pack()

# Rodar a janela
janela.mainloop()
