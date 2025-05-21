class Celsius():
    def converter(self,valor):
        return valor
    
class Fahrenheit():
    def converter(valor):
        return (valor-32)*5/9
    
class Kelvin():
    def converter(valor):
        return valor - 273
    
class ConversorFactory():
    def obter_conversor(tipo):
        if tipo == 'Celsius':
            return Celsius()
        elif tipo == 'Fahrenheit':
            return Fahrenheit()
        elif tipo == 'Kelvin':
            return Kelvin()
        else :
            return 'valor incorreto'
        
conversor = ConversorFactory.obter_conversor("Fahrenheit")
print(conversor.converter(212))