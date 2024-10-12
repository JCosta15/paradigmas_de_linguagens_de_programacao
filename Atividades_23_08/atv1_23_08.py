from funcoes import criar_vetor,valores,somarValoresVetor
def main():
    vetor = criar_vetor(8)

    x,y = valores()

    soma = somarValoresVetor(vetor,x,y)

    print(f"A soma dos valores nas posições x e y é {soma}")

if __name__ == "__main__":
    main()