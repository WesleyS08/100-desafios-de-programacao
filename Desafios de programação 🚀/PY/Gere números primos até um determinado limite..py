import tkinter as tk
from tkinter import messagebox


def gerar_primos():
    try:
        limite = int(entry.get())
        lista_primos = gerar_primos_lista(limite)
        messagebox.showinfo(
            "Números Primos", f"Números primos até {limite}: {lista_primos}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")


def gerar_primos_lista(limite):
    primos = []
    for numero in range(2, limite + 1):
        eh_primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(numero)
    return primos


# Criar janela
janela = tk.Tk()
janela.title("Números Primos")

# Criar rótulo para o texto "Digite um número:"
rotulo = tk.Label(janela, text="Digite um número:")
rotulo.pack(pady=2)

# Criar entrada (entry) para o número
entry = tk.Entry(janela)
entry.pack(pady=25)

# Criar botão para verificar o número
botao_verificar = tk.Button(janela, text="Gerar Primos", command=gerar_primos)
botao_verificar.pack()

# Rodar a janela
janela.mainloop()
