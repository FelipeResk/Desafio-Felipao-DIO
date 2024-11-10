class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "Mago":
            ataque = "atacou com magia"
        elif self.tipo == "Guerreiro":
            ataque = "atacou com a espada"
        else:
            ataque = "atirou com arco e flecha"
        print(f"Seu {self.tipo} {ataque}")