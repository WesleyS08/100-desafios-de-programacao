import random

def jogo_de_adivinhacao():
    # Escolhe um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        # Solicita uma tentativa ao jogador
        tentativa = int(input("Digite a sua tentativa: "))
        tentativas += 1

        # Verifica se a tentativa está correta
        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif tentativa < numero_secreto:
            print("Tente um número mais alto.")
        else:
            print("Tente um número mais baixo.")

# Inicia o jogo
jogo_de_adivinhacao()
