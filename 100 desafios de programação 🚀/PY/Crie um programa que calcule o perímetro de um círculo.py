import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        pi = float(3.14)
        r = float(entry.get())
        
        # Calcular o perímetro
        p = 2 * pi * r
        messagebox.showinfo("Perímetro", f'O perímetro da sua circunferência é: {p:.2f} cm')

        # Calcular a área
        a = pi * r * r
        messagebox.showinfo("Área", f'A área da sua circunferência é: {a:.2f} cm²')

    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")

# Criar janela
janela = tk.Tk()
janela.title("Cálculo de Circunferência")

# Criar rótulo para a entrada do raio
rotulo = tk.Label(janela, text="Digite o raio da circunferência:")
rotulo.pack(pady=5)

# Criar entrada para o raio
entry = tk.Entry(janela)
entry.pack(pady=5)


# Criar botão para calcular 
botao_calcular = tk.Button(
    janela, text="Calcular", command=calcular)
botao_calcular.pack(pady=10)

# Criar rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=10)

# Rodar a janela
janela.mainloop()
