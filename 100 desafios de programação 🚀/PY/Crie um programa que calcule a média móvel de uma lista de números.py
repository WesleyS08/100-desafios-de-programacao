import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calcular_media_movel():
    try:
        lista = [float(valor) for valor in entry_lista.get().split(',')]
        janela = int(entry_janela.get())

        medias = calcular_media_movel_funcao(lista, janela)

        resultado_label.config(text=f'Médias Móveis: {medias}')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite valores válidos.")


def calcular_media_movel_funcao(lista, janela):
    if janela <= 0 or janela > len(lista):
        raise ValueError(
            "A janela deve ser um valor positivo menor ou igual ao tamanho da lista.")

    medias = []
    for i in range(len(lista) - janela + 1):
        sublista = lista[i:i+janela]
        media = sum(sublista) / janela
        medias.append(media)

    return medias


# Criar janela
janela = tk.Tk()
janela.title("Cálculo de Média Móvel")

# Criar rótulo para a entrada da lista
label_lista = tk.Label(janela, text="Digite a lista (separada por vírgulas):")
label_lista.pack(pady=5)

# Criar entrada para a lista
entry_lista = tk.Entry(janela)
entry_lista.pack(pady=5)

# Criar rótulo para a entrada da janela
label_janela = tk.Label(janela, text="Tamanho da lista:")
label_janela.pack(pady=5)

# Criar entrada para a janela
entry_janela = tk.Entry(janela)
entry_janela.pack(pady=5)

# Criar botão para calcular a média móvel
botao_calcular = tk.Button(
    janela, text="Calcular Média Móvel", command=calcular_media_movel)
botao_calcular.pack(pady=10)

# Criar rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=10)

# Rodar a janela
janela.mainloop()
