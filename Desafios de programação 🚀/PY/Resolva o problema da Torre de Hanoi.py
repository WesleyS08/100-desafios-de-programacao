import tkinter as tk
from tkinter import ttk


class TorreHanoi:
    def __init__(self, root):
        self.root = root
        self.root.title("Torre de Hanoi")

        self.canvas = tk.Canvas(
            root, height=300, width=600, background="white")
        self.canvas.grid(column=0, row=0, padx=10, pady=10)

        self.n_discos_label = ttk.Label(root, text="Número de Discos:")
        self.n_discos_label.grid(column=0, row=1, padx=10, pady=5)

        self.n_discos_entry = ttk.Entry(root)
        self.n_discos_entry.grid(column=1, row=1, padx=10, pady=5)

        self.iniciar_button = ttk.Button(
            root, text="Iniciar", command=self.iniciar_torre_hanoi)
        self.iniciar_button.grid(column=2, row=1, padx=10, pady=5)

        self.n_discos = 0
        self.discos = {}

    def iniciar_torre_hanoi(self):
        try:
            self.n_discos = int(self.n_discos_entry.get())
        except ValueError:
            self.mostrar_erro("Insira um número válido de discos.")
            return

        self.limpar_tela()

        # Inicializa as torres
        self.discos = {0: list(range(self.n_discos, 0, -1)), 1: [], 2: []}

        self.desenhar_torre_hanoi(self.n_discos, 0, 1, 2)

    def desenhar_torre_hanoi(self, n, origem, destino, auxiliar):
        if n > 0:
            # Move n-1 discos de origem para auxiliar usando destino como auxiliar
            self.desenhar_torre_hanoi(n-1, origem, auxiliar, destino)

            # Move o disco restante de origem para destino
            self.desenhar_movimento(origem, destino)

            # Move os n-1 discos de auxiliar para destino usando origem como auxiliar
            self.desenhar_torre_hanoi(n-1, auxiliar, destino, origem)

    def desenhar_movimento(self, origem, destino):
        try:
            disco = self.discos[origem].pop()
            self.discos[destino].append(disco)
        except IndexError:
            # Ignora tentativas de mover discos de uma torre vazia
            pass

        # Atualiza a visualização gráfica do movimento
        self.atualizar_visualizacao()

    def limpar_tela(self):
        self.canvas.delete("all")
        self.discos = {}

    def atualizar_visualizacao(self):
        self.canvas.delete("all")

        largura_torre = 20
        altura_torre = 200
        espacamento_torres = 200

        for torre in range(3):
            x_base = torre * espacamento_torres + 50
            y_base = 300

            # Desenha a base da torre
            self.canvas.create_rectangle(
                x_base - largura_torre / 2, y_base, x_base + largura_torre / 2, y_base - 10, fill="black")

            # Desenha os discos na torre
            for i, disco in enumerate(self.discos.get(torre, [])):
                largura_disco = 20 + disco * 10
                altura_disco = 10
                y_disco = y_base - (i + 1) * altura_disco

                self.canvas.create_rectangle(
                    x_base - largura_disco / 2, y_disco, x_base + largura_disco / 2, y_disco + altura_disco, fill="blue")

    def mostrar_erro(self, mensagem):
        tk.messagebox.showerror("Erro", mensagem)


if __name__ == "__main__":
    root = tk.Tk()
    torre_hanoi = TorreHanoi(root)
    root.mainloop()
