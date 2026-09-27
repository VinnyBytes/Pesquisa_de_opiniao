# Garantindo que os contadores iniciem em zero
quantidade_excelente = 0
quantidade_bom = 0
quantidade_ruim = 0
# Mensaem de saudação
print("\nSejam bem-vindos à pesquisa de opinião TudoWeb\n")
# Laço de repetição. O range define quantas vezes o loop irá continuar
for numero_entrevistado in range(1, 51):
    # Dados de entrada
    print(f"\nEntrevistado nº: {numero_entrevistado}")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")

    while True:
        try:
            opiniao = int(input(
                "Diga para nós o que achou do nosso atendimento: "
                "\n1: EXCELENTE" \
                "\n2: BOM" \
                "\n3: RUIM:" \
                "\n Digiite a sua escolha:"
            ))
            if opiniao in (1, 2, 3): # para garantir que as respostas estejam dentro do solicitado
                break
            print("Opcao invalida. Digite 1, 2 ou 3.") 
        except ValueError:
            print("Entrada invalida. Digite 1, 2 ou 3.")
    # Processamento de dados 
    if opiniao == 1:
        quantidade_excelente += 1
    elif opiniao == 2:
        quantidade_bom += 1
    elif opiniao == 3:
        quantidade_ruim += 1
    #confirma para o usuário que a resposta dele foi registrda
    print(f"Resposta registrada para {nome}, {idade} anos.")
    # Saída de dados
print("\n--- Resultado da pesquisa ---")
print(f"Respostas EXCELENTE: {quantidade_excelente}")
print(f"Resposts BOM:{quantidade_bom}")    
print(f"Respostas RUIM: {quantidade_ruim}")
