from funcoes import criar_vetor, maior_menor_vetor

def main():
    vetor = criar_vetor(10)

    maior, menor = maior_menor_vetor(vetor)

    print(f"O maior elemento do vetor é {maior}")
    print(f"O menor elemento do vetor é {menor}")

if __name__ == "__main__":
    main()