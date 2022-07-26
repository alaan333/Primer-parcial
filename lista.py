
def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]

class nodoLista():
    info, sig,sublista = None, None,None


class Lista():

    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0


    def insertar(self, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        nodo.sublista = Lista()

        if(self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def lista_vacia(self):
        return self.__inicio is None

    def tamanio(self):
        return self.__tamanio

    def barrido(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig
    
    def barrido_lista_lista(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            print('sublista:')
            aux.sublista.barrido()
            # aux1 = aux.sublista.__inicio
            # while(aux1 is not None):
            #     print('  ', aux1.info)
            #     aux1 = aux1.sig

            aux = aux.sig

    def busqueda(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def eliminar(self, clave, campo=None):
        dato = None
        if(criterio(self.__inicio.info, campo) == clave):
            dato = self.__inicio.info
            self.__inicio = self.__inicio.sig
            
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(actual.info, campo) != clave):
                anterior = anterior.sig
                actual = actual.sig

            if(actual is not None):
                dato = actual.info
                anterior.sig = actual.sig
                self.__tamanio=self.__tamanio-1      #para hacer andar un punto habia que restar el tamaño   
        return dato

    def obtener_elemento(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None
    
    def ultimo_descubierto(self):
        aux1=self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(int(aux1.info.named_by.split(', ')[1])<int(aux.info.named_by.split(', ')[1])):
                aux1=aux
            aux = aux.sig
        dato1=aux1.info.named_by.split(',')
        print(f'El ultimo dinosaurio en ser descubierto fue el {aux1.info.name}')
        print(f'Lo descubrio {dato1[0]}')

    def listado_filtrado_especial(self,selec_dino,selec_nivel):
        aux=self.__inicio
        while(aux is not None):
            if (aux.info.nombre in selec_dino and aux.info.nivel_alerta in selec_nivel):
                print(f'Dinosaurio: {aux.info.nombre}')
                print(f'Hora de alerta: {aux.info.hora}')
                print(f'Zona: {aux.info.zona}')
                print(f'Nivel de alerta: {aux.info.nivel_alerta}')
                print()
            aux=aux.sig

    def crear_dos_colas(self,cola_carnivoros,cola_herbivoros):
        aux=self.__inicio
        while(aux is not None):
            if (aux.info.tipo=='carnívoro')  and (aux.info.nivel_alerta=='high' or aux.info.nivel_alerta=='critical'):
                cola_carnivoros.arribo(aux)        
            elif(aux.info.tipo=='herbívoro') and (aux.info.nivel_alerta=='high' or aux.info.nivel_alerta=='critical'):
                cola_herbivoros.arribo(aux)
            aux=aux.sig
        
    def barrido_datos(self):
        aux=self.__inicio
        while(aux is not None):
            print(f'{aux.info.nombre}, {aux.info.nivel_alerta}, {aux.info.hora}, {aux.info.zona}')
            aux=aux.sig
    
    def barrido_compsognathus(self):
        aux=self.__inicio
        while(aux is not None):
            if (aux.info.nombre=='Compsognathus'):
                print(aux.info.zona)
            aux=aux.sig
