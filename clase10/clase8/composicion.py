class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.estado ='en_reposo'
        self.motor = Motor(cilindros = 4)

    def acelerar(self, tipo ='despacio'):
        if tipo =='rapida':
            self.motor.inyectar_gasolina(10)
        else:
            self.motor.inyectar_gasolina(3)

        self.estado = 'en_movimiento'

    def get_info_auto(self):
        #retorna informacion del auto
        pass

class Motor:
    def __init__(self, cilindros, tipo='diesel'):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass
    
    def get_info_motor(self):
        return "Imprime informacion del motor"
    
if __name__ == '__main__':
    mi_motor = Motor(6,'nafta')

    mi_auto = Automovil('Tundra','Toyota','gris')
    mi_auto.motor = mi_motor

    mi_auto.acelerar('rapida')

    print(mi_auto.get_info_auto())
    print(mi_auto.motor.get_info_motor())