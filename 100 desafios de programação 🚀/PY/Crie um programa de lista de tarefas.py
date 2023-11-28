import tkinter as tk
from tkinter import messagebox


class ListaDeTarefas:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Lista de Tarefas")

        # Lista para armazenar as tarefas
        self.tarefas = []

        # Entrada para adicionar tarefas
        self.entrada_tarefa = tk.Entry(janela, width=40)
        self.entrada_tarefa.grid(row=0, column=0, padx=10, pady=10)

        # Botão para adicionar tarefas
        botao_adicionar = tk.Button(
            janela, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        botao_adicionar.grid(row=0, column=1, padx=10, pady=10)

        # Listabox para exibir as tarefas
        self.lista_tarefas = tk.Listbox(janela, width=40, height=10)
        self.lista_tarefas.grid(
            row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botão para remover tarefa selecionada
        botao_remover = tk.Button(
            janela, text="Remover Tarefa", command=self.remover_tarefa)
        botao_remover.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def adicionar_tarefa(self):
        nova_tarefa = self.entrada_tarefa.get()
        if nova_tarefa:
            self.tarefas.append(nova_tarefa)
            self.atualizar_lista_tarefas()
            self.entrada_tarefa.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Por favor, digite uma tarefa.")

    def remover_tarefa(self):
        indice_selecionado = self.lista_tarefas.curselection()
        if indice_selecionado:
            indice_selecionado = int(indice_selecionado[0])
            del self.tarefas[indice_selecionado]
            self.atualizar_lista_tarefas()
        else:
            messagebox.showwarning(
                "Atenção", "Selecione uma tarefa para remover.")

    def atualizar_lista_tarefas(self):
        self.lista_tarefas.delete(0, tk.END)
        for tarefa in self.tarefas:
            self.lista_tarefas.insert(tk.END, tarefa)


# Criar janela
janela = tk.Tk()
lista_tarefas = ListaDeTarefas(janela)

# Rodar a janela
janela.mainloop()
