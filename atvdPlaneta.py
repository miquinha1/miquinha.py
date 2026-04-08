# Micais Tavazes e Felipe Silva

class planeta:
    def __init__(self, nomePlaneta, gravidadePlaneta):
        self.nomePlaneta = nomePlaneta
        self.gravidadePlaneta = gravidadePlaneta

    def setNomePlaneta(self, nome):
        self.nomePlaneta = nome
        
    def getNomePlaneta(self):
        return self.nomePlaneta
    
    def setGravidadePlaneta(self, gravidade):
        self.gravidadePlaneta = gravidade

    def getGravidadePlaneta(self):
        return self.gravidadePlaneta
    
    def calcularPeso(self, massa):
        peso = massa * self.gravidadePlaneta
        return f'{peso} N'

class TestarPlaneta:
    def main():

        nome = input('Digite o nome do planeta: ')
        gravidade = float(input('Digite a gravidade do planeta: '))

        P = planeta(nome, gravidade)

        massa = float(input('Digite a massa do corpo: '))
        peso = P.calcularPeso(massa)

        novaGravidade = float(input('Digite uma nova gravidade para o planeta: '))
        P.setGravidadePlaneta(novaGravidade)

        peso = P.calcularPeso(massa)
        print('O peso do planeta com a nova gravidade é:', peso)

TestarPlaneta.main()