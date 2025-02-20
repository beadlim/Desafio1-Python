def main():
    # Missão 1: Restaurando as Regras Escolares 📝
    # Verificar se o aluno foi aprovado ou reprovado
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 6:
        print("Aprovado")
    else:
        print("Reprovado")

    # Missão 2: O Sistema Eleitoral Secreto 📝
    # Verificar se o usuário pode votar
    idade = int(input("Digite sua idade: "))
    if idade >= 16:
        print("Você pode votar.")
    else:
        print("Você não pode votar.")

    # Missão 3: Recuperando o Sistema de Notas 📊
    # Classificar a nota do aluno
    nota = float(input("Digite a nota para ver a classificação: "))
    if 90 <= nota <= 100:
        print("Parabéns, você tirou A!")
    elif 80 <= nota < 90:
        print("Muito bem, você tirou B.")
    elif 70 <= nota < 80:
        print("Bom trabalho, você tirou C.")
    elif 60 <= nota < 70:
        print("Fique atento, você tirou D.")
    else:
        print("Estude um pouco mais, você tirou F.")

    # Missão 4: Restaurando a Identificação de Números ⚖️
    # Somar dois números fornecidos pelo usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"A soma é {num1 + num2}")

    # Missão 5: Recuperando o Cofre de Segurança 🔒
    # Verificar se a senha está correta
    senha = input("Digite a senha: ")
    if senha == "Python123":
        print("Acesso permitido.")
    else:
        print("Senha incorreta.")

    # Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾
    # Exibir os números de 1 a 10 usando um loop while
    print("Contando de 1 a 10:")
    i = 1
    while i <= 10:
        print(i)
        i += 1

    # Missão 7: Organizando a Lista 📋
    # Ordenar e exibir uma lista de números
    lista = [8, 3, 10, 1, 5]
    lista.sort()
    print("Lista ordenada:", lista)

    # Missão 8: Acessando os Registros de Alunos 🏷️
    # Criar uma tupla e exibir o primeiro e último nome
    nomes = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
    print(f"O primeiro nome é {nomes[0]} e o último é {nomes[-1]}")

    # Missão 9: Calculando o Dobro de um Número 🛠️
    # Criar uma função que retorna o dobro de um número
    numero = int(input("Digite um número para ver o dobro: "))
    print(f"O dobro de {numero} é {numero * 2}")

    # Missão 10: Contando Letras 🔄
    # Criar uma função que conta quantas letras há em um nome
    nome = input("Digite um nome: ")
    print(f"O nome {nome} tem {len(nome)} letras.")

if __name__ == "__main__":
    main()
