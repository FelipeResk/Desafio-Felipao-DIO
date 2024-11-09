from funcoes import generateInvoice

#declaração de dicionário
invoice = {
    #chave: valor
    "name": "Resk",
    "age": 28,
    "products": {
        0: ["p1", 29.90],
        1: ["p2", 129.99],
        2: ["p3", 899.99]
    },
    "taxes": 98.90
}

generateInvoice(invoice)