import tkinter as tk
from tkinter import messagebox


def verificar_expressao():
    try:
        expressao = entry.get()
        resultado = eval(expressao)
        messagebox.showinfo("Verificação de Expressão",
                            f'A expressão é válida e o resultado é: {resultado}')
    except Exception as e:
        messagebox.showerror("Erro", f"A expressão não é válida. Erro: {e}")


# Criar janela
janela = tk.Tk()
janela.title("Verificação de Expressão Matemática")

# Criar rótulo para o texto "Digite uma expressão:"
rotulo = tk.Label(
    janela, text="Digite uma expressão matemática para verificar")
rotulo.pack(pady=2)

entry = tk.Entry(janela)
entry.pack(pady=25)

botao_verificar = tk.Button(
    janela, text="Verificar", command=verificar_expressao)
botao_verificar.pack()

# Rodar a janela
janela.mainloop()
