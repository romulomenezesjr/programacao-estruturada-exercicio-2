def q1():
    """
    Faça um programa que calcula a
    quantidade de divisores de um
    número (incluindo 1 e o próprio 
    número) que são divisíveis por 3.
    """
    numero = int(input(""))
    quantidade_divisores = 0
    for i in range(2, numero+1):
        if numero % i == 0 and i % 3 == 0:
            quantidade_divisores += 1
    if quantidade_divisores == 0:
        print("O número não possui divisores multiplos de 3")
    else:
        print(
            f"Quantidade de divisores divisiveis por 3: {quantidade_divisores}")
