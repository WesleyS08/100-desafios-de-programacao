import tkinter as tk
from tkinter import ttk


class CalculadoraGorjeta:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Gorjeta")

        self.label_conta = ttk.Label(root, text="Conta total:")
        self.label_conta.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)

        self.entry_conta = ttk.Entry(root, width=20)
        self.entry_conta.grid(column=1, row=0, padx=10, pady=5)

        self.label_percentagem = ttk.Label(
            root, text="Percentagem de Gorjeta:")
        self.label_percentagem.grid(
            column=0, row=1, padx=10, pady=5, sticky=tk.W)

        self.entry_percentagem = ttk.Entry(root, width=20)
        self.entry_percentagem.grid(column=1, row=1, padx=10, pady=5)

        self.botao_calcular = ttk.Button(
            root, text="Calcular Gorjeta", command=self.calcular_gorjeta)
        self.botao_calcular.grid(column=0, row=2, columnspan=2, pady=10)

        self.label_resultado = ttk.Label(root, text="")
        self.label_resultado.grid(
            column=0, row=3, columnspan=2, padx=10, pady=5)

    def calcular_gorjeta(self):
        try:
            conta_total = float(self.entry_conta.get())
            percentagem_gorjeta = float(self.entry_percentagem.get())
            gorjeta = (percentagem_gorjeta / 100) * conta_total
            total_com_gorjeta = conta_total + gorjeta

            resultado = f"Gorjeta: R${gorjeta:.2f}\nTotal com Gorjeta: R${total_com_gorjeta:.2f}"
            self.label_resultado.config(text=resultado)

        except ValueError:
            self.label_resultado.config(
                text="Insira valores numéricos válidos.")


if __name__ == "__main__":
    root = tk.Tk()
    calculadora_gorjeta = CalculadoraGorjeta(root)
    root.mainloop()
