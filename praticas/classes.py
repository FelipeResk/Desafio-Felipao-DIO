class formaDeBolo:
    def __init__(self, saborMassa, saborRecheio):
        self.saborMassa = saborMassa
        self.saborRecheio = saborRecheio

    def exibir_informacoes (self):
        print(f"Massa de {self.saborMassa}")
        print(f"Recheio de {self.saborRecheio}")