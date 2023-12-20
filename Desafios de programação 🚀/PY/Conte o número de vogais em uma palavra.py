import tkinter as tk
from tkinter import messagebox 

def contagem(): 
    try:
        palavra = str(entry.get())
        vogais = "aeiou"
        totalVogal = 0

        for letra in palavra:
            if letra in vogais:
                totalVogal += 1
        mensagem = f'A palavra {palavra} tem um total de {totalVogal} vogais'
        messagebox.showinfo("Contagem de Vogais", mensagem)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite uma palavra válido.")


# Criar janela
janela = tk.Tk()
janela.title("Contagem de vogais")

# Criar rótulo para o texto "Digite um número:"
rotulo = tk.Label(janela, text="Digite uma palavra:")
rotulo.pack(pady=2)

# Criar entrada (entry) para o número
entry = tk.Entry(janela)
entry.pack(pady=25)

# Criar botão para verificar o número
botao_verificar = tk.Button(janela, text="contar", command=contagem)
botao_verificar.pack()

# Rodar a janela
janela.mainloop()
