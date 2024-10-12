def criar_vetor(tamanho):
    vetor = [0] * tamanho

    for i in range(tamanho):
        vetor[i] = int(input(f"Digite  o valor da posição {i}: "))

    return vetor

def soma(x,y):
    soma = x + y

    return soma

def valores():
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    return x,y

def somarValoresVetor(vetor,x,y):
    s = soma(vetor[x],vetor[y])
    return s

def maior_menor_vetor(vetor):
    maior = vetor[0]
    menor = vetor[0]

    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
        elif vetor[i] < menor:
            menor = vetor[i]

    return maior, menor