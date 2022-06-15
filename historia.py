from jurassic_park import dinosaurs
from lista import Lista

lista_de_alertas=Lista()
lista_dinosaurios = Lista()

class Dinosaurio:

    def __init__(self, name, type, number, period, named_by):
        self.name = name
        self.type = type
        self.number = number
        self.period = period
        self.named_by=named_by
    
    def __str__(self):
        return f'{self.name}'

class Datos_de_alertas:

    def __init__(self, hora, zona, numero_d, nivel_alerta,nombre):
        self.hora = hora 
        self.zona = zona
        self.numero_d = numero_d
        self.nivel_alerta = nivel_alerta
        self.nombre=nombre
    
    def __str__(self):
        return str(self.numero_d)

#--------Lista armada solo para mostrar los datos del ultimo descubierto-------------------------------
for dino in dinosaurs:
    lista_dinosaurios.insertar(Dinosaurio(dino['name'],
                                           dino['type'],
                                           dino['number'],
                                           dino['period'], 
                                           dino['named_by']),'name')
lista_dinosaurios.ultimo_descubierto()
lista_dinosaurios.barrido()
print()
# ----------------------------------------------------------------------------------------------------

file=open('C:/Users/Fernando Paz/Primer proyecto JS/Algoritmo2022/Algoritmo y estructura de datos/PythonAlan/Archivoslocales/Primer-parcial/alerts.txt')
lineas = file.readlines()
lineas.pop(0)
#print(lineas[0])

def busqueda(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['name']

#----------------------------------Para armar la lista-------------------------------------
for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    dato.append(busqueda(dato[2]))
    #print(dato[0])
    #lista_de_alertas.insertar(dato)
    lista_de_alertas.insertar(Datos_de_alertas(dato[0],
                                            dato[1],
                                            dato[2],
                                            dato[3],
                                            dato[4]), 'numero_d')

# print(lista_de_alertas.tamanio())
print()
lista_de_alertas.barrido()


zonas_a_eliminar=['WYG075','SXH966','LYF010']

# for i in range(len(lineas)):
#     dato=lista_de_alertas.obtener_elemento(i)
#     #print(dato[1])
#     if (dato.zona in zonas):
#         lista_de_alertas.eliminar(dato,i)
#         print(dato[4])
#         print(dato[0])
# for i in range(lista_de_alertas.tamanio()):
#     dato=lista_de_alertas.obtener_elemento(i)
#     print(dato.zona)
#     if (dato.zona in zonas_a_eliminar):
#         lista_de_alertas.eliminar(dato.zona,'numero_d')

for i in range(3):
    dato=lista_de_alertas.busqueda(zonas_a_eliminar[i],'zona')
    print(dato.info.zona)
    lista_de_alertas.eliminar(dato.info.zona,'zona')
#lista_dinosaurios.barrido() 
print()   
#print(len(lineas))
