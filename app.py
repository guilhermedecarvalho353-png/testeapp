# projeto Exemplo : Calculando de Média do Aluno



# 
def calcular_media(media1, nota2):
    return (nota1 + nota2)/2
# Sistema de notas de Alunos 
    print("=== Sistema de Notas do aluno ===")
    # Perguntando a nota 
    n1 = float(input("Digite a primeira nota : "))
    n2 = float(input("Digite a segunda nota : "))
    # Calcular a média de notas 
    media = calcular_media(n1,n2)
    printf(f"A média dinal é: {media.2f}")

    #Verificando se a pessoa foi aprovada 

    if media >=7.0:
        print("Status : APROVADO!")

    else :
        print("Status : REPROVADO.")