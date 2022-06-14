from jurassic_park import dinosaurs
from lista import Lista

class Dinosaurio:

    def __init__(self, name, type, number, period, named_by):
        self.name = name
        self.type = type
        self.number = number
        self.period = period
        self.named_by=named_by
    
    def __str__(self):
        return f'{self.name},{self.number}'

class Alerta:

    def __init__(self, time,zone_code,dino_number,alert_level):
        self.time=time
        self.zone_code=zone_code
        self.dino_number=dino_number
        self.alert_level=alert_level

    def __str__(self):
        return f"{self.nombre} - {self.nivel}"

lista_dinosaurios = Lista()

file=open('C:/Users/Fernando Paz/Primer proyecto JS/Algoritmo2022/Algoritmo y estructura de datos/PythonAlan/Archivoslocales/Primer-parcial/alerts.txt')
lineas = file.readlines()
lineas.pop(0)
print(lineas[0])

for dino in dinosaurs:
    lista_dinosaurios.insertar(Dinosaurio(dino['name'],
                                           dino['type'],
                                           dino['number'],
                                           dino['period'], 
                                           dino['named_by']),'name')
# for dino in dinosaurs:
#     for i in range(len(lineas)):
#         alerta = lineas[i].split(';')
#         pos = lista_dinosaurios.busqueda(dino['number'], 'number')
#         if (pos.info.number==alerta[2]):
#             pos.sublista.insertar(Alerta(alerta[0],
#                                      alerta[1],
#                                     alerta[2],
#                                     alerta[4]),)

# for i in range(4):
#     linea=lineas[i].split(';')
#     for i in range(len(dinosaurs)):    
#         lista_dinosaurios.obtener_elemento(i)
        
lista_dinosaurios.barrido() 
print()   

lista_dinosaurios.ultimo_descubierto()
print()
print(len(lineas))
