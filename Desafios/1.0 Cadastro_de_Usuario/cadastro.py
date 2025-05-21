class Celsius():

    def converter_para(self,valor):
        return valor
    
class Fahrenheit():

    def converter_para(self,valor):
        return (valor-32)*5/9
    
class Kelvin():

    def converter_para(self,valor):
        return valor - 273
    
class ConversorFactory():
    @staticmethod

    def obter_conversor(tipo):
        if tipo == 'Celsius':
            return Celsius()
        elif tipo == 'Fahrenheit':
            return Fahrenheit()
        elif tipo == 'Kelvin':
            return Kelvin()
        else :
            return 'Temperatura escolhida errada'
        
conversor = ConversorFactory.obter_conversor("Fahrenheit")
print(conversor.converter_para(212))
        