import random

# Sorteia a posição da bala (1 até 6)
bala = random.randint(1, 6)

print("Vamos brincar? Gire o tambor e tente a sorte...")
escolha = int(input("Escolha uma posição do tambor (1 a 6): "))

# Verifica se a escolha é válida
if escolha < 1 or escolha > 6:
    print("Erro! Escolha uma posição entre 1 e 6.")

else:
    # Verifica se acertou a bala
    if escolha == bala:
        print("BUMMM! MORREU OTÁRIO")
    else:
        print("Mlk sortudo! Sobreviveu.")
