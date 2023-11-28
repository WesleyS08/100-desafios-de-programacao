import tkinter as tk
from tkinter import messagebox


class Calculadora:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Calculadora")

        # Variável para armazenar a expressão
        self.expressao = tk.StringVar()

        # Entrada para exibir a expressão
        self.entrada = tk.Entry(janela, textvariable=self.expressao, font=(
            'Helvetica', 16), justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4)


        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for botao in botoes:
            tk.Button(janela, text=botao, font=('Helvetica', 14), command=lambda b=botao: self.pressionar_botao(
                b)).grid(row=row_val, column=col_val, padx=10, pady=10)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def pressionar_botao(self, valor):
        if valor == '=':
            try:
                resultado = eval(self.expressao.get())
                self.expressao.set(str(resultado))
            except Exception as e:
                messagebox.showerror("Erro", "Expressão inválida!")
        else:
            self.expressao.set(self.expressao.get() + valor)


# Criar janela
janela = tk.Tk()
calculadora = Calculadora(janela)

# Rodar a janela
janela.mainloop()
