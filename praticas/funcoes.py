#gera invoice
def generateInvoice(invoice):
    print(f"O comprador é {invoice['name']}")
    print(f"A idade é {invoice['age']}")

    for i in invoice ['products']:
        productName, productPrice = invoice['products'][i]
        print(f"- {productName}: R$ {productPrice}")


def typeOfCat():
    types = ["Laranja", "Frajola", "Tricolor", "Preto", "Escaminha", "Siamês"]
    print("Escolha seu tipo de gato")
    for i, type in enumerate(types, 1):
        print(f"{i}. {type}")

    choice = int(input("Escolha o número correspondente ao seu tipo de gato:\n"))
    while choice < 1 or choice > len(types):
        print("Escolha inválida. Escolha dentre as opções oferecidas.")
        choice = int(input("Escolha o número correspondente ao seu tipo de gato:\n"))

    return types[choice - 1]