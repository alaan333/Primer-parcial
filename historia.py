
from jurassic_park import dinosaurs
from lista import Lista
from cola import Cola 

lista_de_alertas=Lista()
lista_dinosaurios = Lista()
cola_carnivoros=Cola()
cola_herbivoros=Cola()
lista_para_OwenGrady=Lista()

class Datos_de_alertas:

    def __init__(self, hora, zona, numero_d, nivel_alerta,nombre,tipo):
        self.hora = hora 
        self.zona = zona
        self.numero_d = numero_d
        self.nivel_alerta = nivel_alerta
        self.nombre=nombre
        self.tipo=tipo
    
    def __str__(self):
        return (self.numero_d)

#--------Lista armada solo para mostrar los datos del ultimo descubierto-------------------------------
# class Dinosaurio:      

#     def __init__(self, name, type, number, period, named_by):
#         self.name = name
#         self.type = type
#         self.number = number
#         self.period = period
#         self.named_by=named_by
    
#     def __str__(self):
#         return f'{self.name}'

# for dino in dinosaurs:
#     lista_dinosaurios.insertar(Dinosaurio(dino['name'],
#                                            dino['type'],
#                                            dino['number'],
#                                            dino['period'], 
#                                            dino['named_by']),'name')
# lista_dinosaurios.ultimo_descubierto()
# lista_dinosaurios.barrido()
# print()
# ----------------------------------------------------------------------------------------------------

file=open('C:/Users/Fernando Paz/Primer proyecto JS/Algoritmo2022/Algoritmo y estructura de datos/PythonAlan/Archivoslocales/Primer-parcial/alerts.txt')
lineas = file.readlines()
lineas.pop(0)

def agregar_nombre(buscado):                 
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['name']
def agregar_tipo(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['type']


for linea in lineas:
    dato = linea.split(';') #para formar el vector
    dato[3] = dato[3][:-1] #para borrar /n
    dato.append(agregar_nombre(dato[2])) 
    dato.append(agregar_tipo(dato[2]))
    lista_de_alertas.insertar(Datos_de_alertas(dato[0],
                                            dato[1],
                                            dato[2],
                                            dato[3],
                                            dato[4],
                                            dato[5]), 'numero_d')
print()

                                                #Eliminar zona
                                      
zonas_a_eliminar=['WYG075','SXH966','LYF010']
for i in range(3):
    pos = lista_de_alertas.eliminar(zonas_a_eliminar[i],'zona')
    if pos:
        print(f'La zona {pos.zona} fue eliminada')
    else:
        print('la zona no esta en la lista')
print()
# print(lista_de_alertas.tamanio()) 
# #para comprobar que se eliminaron bien
# for i in range(3):
#     pos=lista_de_alertas.busqueda(zonas_a_eliminar[i],'zona')
#     if pos:
#         lista_de_alertas.eliminar(pos)
#         print(f'La zona {pos.info.zona} fue eliminada')
#     else:
#         print('La zona no esta en la lista')
# print()

                                            #Modificar nombre de dinosaurio
dato=lista_de_alertas.busqueda('HYD195','zona')
if dato:
    dato.info.nombre='Mosasaurus'
    print('Se ha modificado el nombre del dinosaurio')
else:
    print(f'La zona no fue encontrada en la lista')  
print()

# Listado filtrado de los datos que solo incluya datos de los dinosaurios: Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con
# nivel  ́critical’ o ‘high’.
print('------Listado de Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con nivel critical o high-------')
selec_dino=['Tyrannosaurus Rex', 'Spinosaurus', 'Giganotosaurus']
selec_nivel=['critical','high']
lista_de_alertas.listado_filtrado_especial(selec_dino,selec_nivel)

#Insertar en dos colas, una con los datos de dinosaurios carnívoros 
# y otra con los herbívoros, descarten las de nivel ‘low’ y ‘medium’.
lista_de_alertas.crear_dos_colas(cola_carnivoros,cola_herbivoros)
# print('Carnivoros: ')
# for i in range(cola_carnivoros.tamanio()):     
#     print(cola_carnivoros.mover_al_final().info.nombre)
# print()
# print('Herbivoros: ')  
# for i in range(cola_herbivoros.tamanio()):  
#     print(cola_herbivoros.mover_al_final().info.nombre)
# print()

print('                             -----------Alertas de carnivoros---------- ')
print()
for i in range(cola_carnivoros.tamanio()):
    dato=cola_carnivoros.mover_al_final()
    if (dato.info.zona!='EPC944'):
        print(f'Nombre del dinosairio: {dato.info.nombre}')
        print(f'Zona de la alerta: {dato.info.zona}')
        print(f'Hora de la alerta: {dato.info.hora}')
        print()

for i in range(lista_de_alertas.tamanio()):
    dato=lista_de_alertas.obtener_elemento(i)
    if (dato.nombre=='Raptors (Dromaeosauridae)'or dato.nombre=='Carnotaurus'):
        lista_para_OwenGrady.insertar(dato,'nombre')
print('---------------------------Lista de dinosaurios para Owen------------------- ')
lista_para_OwenGrady.barrido_datos()
print()
print('-----------------Zonas donde se puede encontrar dinosaurios Compsognathus--------')
lista_de_alertas.barrido_compsognathus()

    




