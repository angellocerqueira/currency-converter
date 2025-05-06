print("=== Conversor de Moedas ===")
print("1 - Real (BRL) → Dólar (USD)")
print("2 - Real (BRL) → Euro (EUR)")
print("3 - Dólar (USD) → Real (BRL)")
print("4 - Euro (EUR) → Real (BRL)")

opcao = input("Escolha uma opção (1-4): ")

if opcao in ['1', '2', '3', '4']:
    valor = float(input("Digite o valor: "))

    if opcao == '1':
        convertido = valor / 5.15
        print(f"R$ {valor:.2f} = US$ {convertido:.2f}")
    elif opcao == '2':
        convertido = valor / 5.55
        print(f"R$ {valor:.2f} = € {convertido:.2f}")
    elif opcao == '3':
        convertido = valor * 5.15
        print(f"US$ {valor:.2f} = R$ {convertido:.2f}")
    elif opcao == '4':
        convertido = valor * 5.55
        print(f"€ {valor:.2f} = R$ {convertido:.2f}")
else:
    print("Opção inválida.")
