print(" SISTEMA DE VENDAS E COMISSÕES")

total_vendas = 0
total_comissoes = 0
quantidade_vendas = 0

while True:
    print("\n========= MENU =========")
    print("1 - Registrar venda")
    print("2 - Consultar faturamento")
    print("3 - Consultar comissões")
    print("4 - Consultar quantidade de vendas")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        print("\n--- REGISTRAR VENDA ---")

        vendedor = input("Nome do vendedor: ")
        valor = float(input("Valor da venda: R$ "))
        percentual = float(input("Comissão (%): "))

        if valor > 0 and percentual >= 0 and percentual <= 100:
            comissao = valor * percentual / 100

            total_vendas = total_vendas + valor
            total_comissoes = total_comissoes + comissao
            quantidade_vendas = quantidade_vendas + 1

            print("\nVenda registrada com sucesso!")
            print("Vendedor:", vendedor)
            print(f"Valor da venda: R$ {valor:.2f}")
            print(f"Comissão: R$ {comissao:.2f}")

        else:
            print("Erro: valor ou comissão inválidos!")

    elif opcao == "2":
        print("\n--- FATURAMENTO ---")
        print(f"Total vendido: R$ {total_vendas:.2f}")

    elif opcao == "3":
        print("\n--- COMISSÕES ---")
        print(f"Total de comissões: R$ {total_comissoes:.2f}")

    elif opcao == "4":
        print("\n--- QUANTIDADE DE VENDAS ---")
        print("Vendas realizadas:", quantidade_vendas)

    elif opcao == "5":
        print("\nSistema encerrado. Até logo!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
