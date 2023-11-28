import tkinter as tk
from tkinter import filedialog, messagebox
import timeit


def selecionar_arquivo():
    # Abre a janela de seleção de arquivo
    arquivo_selecionado = filedialog.askopenfilename()

    # Exibe o caminho do arquivo selecionado
    if arquivo_selecionado:
        label_arquivo.config(
            text=f"Arquivo selecionado: {arquivo_selecionado}")

        # Código para medir o tempo de execução
        codigo = "resultado = sum(range(1000))"
        tempo_execucao = timeit.timeit(codigo, number=1000)

        # Exibe o tempo de execução médio em uma caixa de mensagem
        messagebox.showinfo(
            "Tempo de Execução", f"Tempo de execução médio: {tempo_execucao:.6f} segundos")
    else:
        label_arquivo.config(text="Nenhum arquivo selecionado.")


# Criar janela
janela = tk.Tk()
janela.title("Seletor de Arquivo")

# Botão para abrir a janela de seleção de arquivo
botao_selecionar = tk.Button(
    janela, text="Selecionar Arquivo", command=selecionar_arquivo)
botao_selecionar.pack(pady=20)

# Rótulo para exibir o caminho do arquivo selecionado
label_arquivo = tk.Label(janela, text="")
label_arquivo.pack()

# Rodar a janela
janela.mainloop()
