class Nodo():
    def __init__(self, dato = None):
        self.dato = dato
        self.next = None
        self.before = None

class ListaCircular():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertar(self, dato):
        new_nodo = dato
        aux = self.head
        if self.head is None:
            self.head = dato
            self.tail = dato
        elif aux.next is None:
            aux.next = new_nodo
            new_nodo.before = aux
            self.tail = new_nodo
            self.head.before = self.tail
        else:
            self.tail.next = new_nodo
            new_nodo.before = self.tail
            self.tail = new_nodo
            self.tail.next = self.head
        self.size += 1

    def imprimir(self):
        if self.head is None:
            print('La lista está vacía')
        else:
            new_node = self.head
            while new_node is not None:
                print(new_node.dato)
                new_node = new_node.next
                if new_node is self.head: #Si vuelve al nodo head ahi se detiene
                    break
    
    def buscar(self, numero):
        aux = self.head
        while aux != None:
            if aux.dato == numero:
                print('Anterior: ', aux.before.dato, ', actual: ', aux.dato, ', siguiente: ', aux.next.dato)
                return aux
            aux = aux.next
        return None

list_circular = ListaCircular()
try: 
    for i in range(0, 5):
        numero = int(input('Ingrese un número: '))
        list_circular.insertar(Nodo(numero))

    print('\n     Lista de números: \n')
    tamaño = list_circular.size
    list_circular.imprimir()
    opcion = int(input('Seleccione un número: '))
    list_circular.buscar(opcion)

except ValueError:
    print('Ingrese solo valores númericos')