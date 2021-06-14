#Matematica estructural y logica: Raid Battle Semana 13
#Camilo Andres Morillo Cervantes - 202015224
#Basado en: https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm\

from random import randrange

class ArbBin:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def agregar(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = ArbBin(data)
                else:
                    self.left.agregar(data)
            elif data > self.data:
                if self.right is None:
                    self.right = ArbBin(data)
                else:
                    self.right.agregar(data)
        else:
            self.data = data

    def darAlturaDelArbol(self, data):
        if data==None:
            altura=0
        else:
            altura=1+max(self.darAlturaDelArbol(data.left), self.darAlturaDelArbol(data.right))
        return altura
    

    def darTamañoDelArbol(self, data):
        if data==None:
            tamano=0
        else:
            tamano=1+self.darTamañoDelArbol(data.left)+self.darTamañoDelArbol(data.right)
        return tamano

    def eliminar(self, data):
        if self.data != data:
            if data < self.data:
                if self.left == data:
                    self.left = None
                else:
                    self.left.eliminar(data)
            elif data > self.data:
                if self.right == data:
                    self.right = None
                else:
                    self.right.eliminar(data)
        else:
            self.data = None

    def darTotalNodosEnNivel(self, data, k, actual, altura):
        if k < altura and data != None:
            if k==actual:
                nodos=self.darTamañoDelArbol(data)
                if data.left != None:
                    nodos=nodos-self.darTamañoDelArbol(data.left)
                if data.right != None:
                    nodos=nodos-self.darTamañoDelArbol(data.right)
            else:
                actual=actual+1
                nodos=self.darTotalNodosEnNivel(data.left, k, actual, altura)+self.darTotalNodosEnNivel(data.right, k, actual, altura)
        else:
            nodos=0
        return nodos
    
    def Problema2(self, data):
        altura=self.darAlturaDelArbol(data)
        tamano=self.darTamañoDelArbol(data)
        print("[darTamañoDelArbol(𝑎𝑟𝑏𝑜𝑙)]", tamano,"≤", (2**altura)-1, "[2^darAlturaDelArbol(arbol)-1]")

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        if self.data != None:
            print( self.data),
        if self.right:
            self.right.PrintTree()


    
num=int(input("Ingrese la cantidad de elementos a agregar en el arbol binario: "))
k=int(input("Ingrese el nivel del cual quiere conocer el numero de nodos: "))

#Agregar elementos
if num==0:
    root=ArbBin(None)
elif num==1:
    r=randrange(999)
    print("Root:",r)
    root=ArbBin(r)
else:
    for i in range(num):
        r=randrange(999)
        if i==0:
            print("Root:",r)
            root=ArbBin(r)
        else:
            print("Agregado:",r)
            root.agregar(r)
    
#Imprimir datos
print("Altura del arbol:", root.darAlturaDelArbol(root))
print("Tamaño del arbol:",root.darTamañoDelArbol(root))
print("Total de nodos en el nivel",k,":",root.darTotalNodosEnNivel(root, k, 0, root.darAlturaDelArbol(root)))
root.Problema2(root)
