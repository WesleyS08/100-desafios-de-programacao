import tkinter as tk
from tkinter import messagebox


def fatorial():
    try:
        # Obter o número da entrada
        numero = int(entry.get())

        # Verificar se o número é negativo
        if numero < 0:
            messagebox.showerror(
                "Erro", "Por favor, digite um número não-negativo.")
            return

        # Inicializar o resultado com 1, pois o fatorial de 0 e 1 é 1
        resultado = 1

        # Calcular o fatorial usando um loop while
        i = 1
        while i <= numero:
            resultado *= i
            i += 1

        # Exibir o resultado
        messagebox.showinfo("Sucesso", f"O fatorial de {numero} é {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")


# Criar janela
janela = tk.Tk()
janela.title("Fatorial de um número")

# Rótulo e entrada para número
rotulo_numero = tk.Label(janela, text="Digite um número para o cálculo:")
rotulo_numero.pack(pady=2)

entry = tk.Entry(janela)
entry.pack(pady=2)

# Botão para calcular fatorial
botao_calcular = tk.Button(janela, text="Calcular Fatorial", command=fatorial)
botao_calcular.pack(pady=2)

# Rodar a janela
janela.mainloop()
