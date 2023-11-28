import time
import tkinter as tk
from tkinter import messagebox


def cronometro(tempo_segundos):
    try:
        while tempo_segundos >= 0:
            minutos, segundos = divmod(tempo_segundos, 60)
            formato_tempo = '{:02d}:{:02d}'.format(minutos, segundos)
            label_tempo.config(text=formato_tempo)
            janela.update()
            time.sleep(1)
            tempo_segundos -= 1

        messagebox.showinfo("Tempo encerrado!")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")


def main():
    try:
        tempo_input = int(entry.get())
        cronometro(tempo_input)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")


# Criar janela
janela = tk.Tk()
janela.title("Cronometro")

# Criar rótulo para o texto "Digite um número:"
rotulo = tk.Label(janela, text="Digite um tempo em segundos:")
rotulo.pack(pady=2)

# Criar entrada (entry) para o número
entry = tk.Entry(janela)
entry.pack(pady=25)

# Criar botão para verificar o número
botao_verificar = tk.Button(janela, text="Contar", command=main)
botao_verificar.pack()

# Criar label para exibir o tempo
label_tempo = tk.Label(janela, text="", font=("Helvetica", 16))
label_tempo.pack(pady=20)

# Rodar a janela
janela.mainloop()
