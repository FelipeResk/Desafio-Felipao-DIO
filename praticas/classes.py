class formaDeBolo:
    def __init__(self, saborMassa, saborRecheio):
        self.saborMassa = saborMassa
        self.saborRecheio = saborRecheio

    def exibir_informacoes (self):
        print(f"Massa de {self.saborMassa}")
        print(f"Recheio de {self.saborRecheio}")


class Cat:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def catFur(self):
        if self.type == "Laranja":
            fur = "Laranja"
        elif self.type == "Frajola":
            fur = "Branco e preto"
        elif self.type == "Tricolor":
            fur = "Três cores"
        elif self.type == "Preto":
            fur = "Preta"
        elif self.type == "Escaminha":
            fur = "Misturada"
        else:
            fur = "Albino"
        return fur