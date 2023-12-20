import tkinter as tk
from tkinter import messagebox

def calcular_juros_compostos():
    try:
        principal = float(entry.get())
        taxa = float(entry2.get())
        tempo = int(entry3.get())
        vezes_composto = int(entry4.get())

        # Converte a taxa de porcentagem para uma fração
        taxa_decimal = taxa / 100.0

        # Calcula o montante usando a fórmula de juros compostos
        montante = principal * (1 + taxa_decimal /
                                vezes_composto) ** (vezes_composto * tempo)

        resultado = montante
        messagebox.showinfo(f"O montante final após {tempo} anos é:",f' R${resultado:.2f}')
    except ValueError:
        messagebox.showerror("ERRO!!!!")


# criar janela
janela = tk.Tk()
janela.title("Juros Compostos")

# Criar rótulo para o texto "Digite um número:"
rotulo = tk.Label(janela, text="Digite o valor inicial:")
rotulo.pack(pady=2)

# Criar entrada (entry) para o primeiro número
entry = tk.Entry(janela)
entry.pack(pady=2)

# Criar rótulo para o texto "Digite outro número:"
rotulo2 = tk.Label(janela, text="Digite a taxa de juros anual (%):")
rotulo2.pack(pady=2)

# Criar entrada (entry) para o segundo número
entry2 = tk.Entry(janela)
entry2.pack(pady=2)

# Criar rótulo para o texto "Digite outro número:"
rotulo3 = tk.Label(janela, text="Digite o número de anos:")
rotulo3.pack(pady=2)

# Criar entrada (entry) para o segundo número
entry3 = tk.Entry(janela)
entry3.pack(pady=2)

# Criar rótulo para o texto "Digite outro número:"
rotulo4 = tk.Label(
    janela, text="Digite o número de vezes que os juros são compostos por ano: ")
rotulo4.pack(pady=2)

# Criar entrada (entry) para o segundo número
entry4 = tk.Entry(janela)
entry4.pack(pady=2)

# Criar botão para somar os números
botao_somar = tk.Button(janela, text="Calcular",
                        command=calcular_juros_compostos)
botao_somar.pack()

# Rodar a janela
janela.mainloop()


