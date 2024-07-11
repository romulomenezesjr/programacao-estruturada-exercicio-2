def q1():
    """
    Faça um programa que calcula a
    quantidade de divisores de um
    número (incluindo 1 e o próprio 
    número) que são divisíveis por 3.

     Parte 1 
        - Programa que mostra os divisores de um número

    Parte 2 
        - Com os números que são divisores: 
        - Verificar se são divisiveis por 3
            - Incremento um contador
    """
    contador = 0
    numero = int(input("Digite um número: ")) # 4
    # os divisores deste 'numero'
    # 4: 1,2,3,4
    for i in range(1, numero + 1): # parte 1
        if (numero % i == 0) and (i % 3 == 0):
            contador += 1
    print(contador)

def q2():
    """
    Escreva um programa que receba como entrada dois 
    números inteiros e retorne a soma dos números 
    positivos no intervalo definido por eles, 
    considerando inclusive os extremos.
    
    Parte 1:
        - Receber os dois numeros
    """

    menor = int(input("Digite o 1o numero: ")) # 10
    maior = int(input("Digite o 2o numero: ")) # 5

    #   5 < 10
    if maior < menor:
        temp = maior # temp = 5
        maior = menor # maior = 10
        menor = temp # menor = 5

    soma = 0
    for i in range(menor, maior + 1):
        if i > 0:
            soma += i
    print(soma)


def q3():
    """
    Um professor precisa saber qual a média das 
    notas de uma sala e pediu sua ajuda para construir
    um programa que permita inserir as notas finais de
    cada aluno e, ao final, exibir a média da sala.

    Lembre-se que as notas variam de 0 a 10 e o
    professor digitará -1 quando quiser encerrar as entradas. 
    
    """
    qnt, soma, nota = 0, 0, 0
    while True:
        nota = int(input("Digite uma nota: "))
        
        if nota == -1:
            break

        if nota not in range(0,11):
            print("Valor da nota está fora do intervalo.")
            continue

        soma += nota
        qnt += 1
            

    media = soma / qnt

    print(f"A média das notas foi {media}")
    

q3()
    
