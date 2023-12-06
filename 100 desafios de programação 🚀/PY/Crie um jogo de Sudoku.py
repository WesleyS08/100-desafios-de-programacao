import tkinter as tk
from tkinter import messagebox

# Tabuleiro inicial
tabuleiro_inicial = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Função para verificar se a solução está correta


def verificar_solucao():
    solucao_usuario = []
    for i in range(9):
        linha = []
        for j in range(9):
            entrada = entradas[i][j].get()
            if entrada == "":
                linha.append(0)
            else:
                try:
                    valor = int(entrada)
                    if 1 <= valor <= 9:
                        linha.append(valor)
                    else:
                        messagebox.showerror(
                            "Erro", "Insira apenas números de 1 a 9.")
                        return
                except ValueError:
                    messagebox.showerror(
                        "Erro", "Insira apenas números de 1 a 9 ou deixe em branco.")
                    return
        solucao_usuario.append(linha)

    # Verificar a solução
    if solucao_usuario == tabuleiro_inicial:
        messagebox.showinfo(
            "Parabéns!", "Você resolveu o Sudoku corretamente!")
    else:
        messagebox.showerror("Erro", "Solução incorreta. Tente novamente.")


# Criar janela
janela = tk.Tk()
janela.title("Sudoku")

# Criar entradas para o Sudoku
entradas = [[0]*9 for _ in range(9)]

for i in range(9):
    for j in range(9):
        entradas[i][j] = tk.Entry(janela, width=2, font=('Arial', 16))
        entradas[i][j].grid(row=i, column=j)

# Botão para verificar a solução
botao_verificar = tk.Button(
    janela, text="Verificar Solução", command=verificar_solucao)
botao_verificar.grid(row=9, columnspan=9)

# Preencher as entradas iniciais com os valores do tabuleiro inicial
for i in range(9):
    for j in range(9):
        valor = tabuleiro_inicial[i][j]
        if valor != 0:
            entradas[i][j].insert(0, valor)
            entradas[i][j].config(state="readonly")

# Rodar a janela
janela.mainloop()
