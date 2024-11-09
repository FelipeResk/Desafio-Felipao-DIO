#gera invoice
def generateInvoice(invoice):
    print(f"O comprador é {invoice['name']}")
    print(f"A idade é {invoice['age']}")

    for i in invoice ['products']:
        productName, productPrice = invoice['products'][i]
        print(f"- {productName}: R$ {productPrice}")