class Carro:
    def __init__(self, marca, modelo, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.ligado:
            print("Carro já está ligado, nada acontece")
        else: 
            print("Carro Ligado")
            self.ligado = True

    def desligar(self):
        if self.ligado:
            print("Carro Desligado")
            self.ligado = False
        else:
            print("Carro já está desligado, nada acontece")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"{self.velocidade} km/h")
        else: 
            print("Não é possível acelerar, carro desligado")

    def frear(self):
        if self.ligado:
            self.velocidade -= 1
            print(f"{self.velocidade} km/h")
        else:
            print("Não é possível frear, carro desligado")  

# Criando uma instância do Carro
fusca = Carro("Volks", "Fusca", "Azul", "Gasolina")

# Ligando o carro
fusca.ligar()
