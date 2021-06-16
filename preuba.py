import networkx as nx
import graphviz
from networkx.algorithms.operators.product import _init_product_graph
from networkx.classes.function import edges, info
from networkx.drawing import nx_agraph

G = nx.DiGraph()

Presentacion=[]

"""G.add_node("Daniel")
G.add_node("Willy")
G.add_node("Kimberly")
G.add_node("Fernando")
G.add_node("Jaquelyn")
G.add_node("Javier")

G.add_edge("Daniel", "Javier")
G.add_edge("Javier","Fernando")
G.add_edge("Fernando","Willy")
G.add_edge("Willy","Jaquelyn")
G.add_edge("Jaquelyn","Kimberly")
"""


"""G.nodes["Daniel"]["Informacion"] = "Daniel trabaja en la muni"
print(len(G.nodes))
print(len(G.edges))
print(G.nodes)
print(G.edges)

print(G.nodes(data=True))
print("xd")
print(G["Daniel"])


nx.write_graphml(G, "actores.graphml")
A = nx.nx_agraph.to_agraph(G)
#A.layout('dot')
#A.layout('twopi')
A.layout('fdp')
A.draw('salida.png') # guardar como png
 
graphviz.Source(A.to_string()) # mostrar en jupyter

G2 = nx.read_graphml("actores.graphml")
print(G2.nodes)"""

def IngresarNodo():
    print("Ingrese el nombre del nodo: ")
    nombre=str(input())
    print("Ingrese la informacion que llevara "+ nombre)
    info=str(input())
    G.add_node(nombre)
    G.nodes[nombre]["Informacion"] = info

def leerNodos():
    print("Estos son los nodos que han sido ingresados:")
    for nodo in G.nodes:
        print(nodo)

def Unir2Nodos():
    print("Ingrese el nombre del primer nodo a unir: ")
    nodo1=str(input())
    print("Ingrese el nombre del segundo nodo a unir: ")
    nodo2=str(input())
    G.add_edge(nodo1, nodo2)

def verGrafo():
    """print(G.nodes(data=True))
    nx.write_graphml(G, "preuba.graphml")
    A = nx.nx_agraph.to_agraph(G)
    #A.layout('dot')
    #A.layout('twopi')
    A.layout('fdp')
    A.draw('salida.png') # guardar como png
    
    graphviz.Source(A.to_string()) # mostrar en jupyter

    
    #print(list(G.edges))"""
    print(G.nodes["a"]["Informacion"])
    
def prueba():
    print("Ingrese un nodo")
    nod =input()
    print(list(G.successors(nod))[0])
    print(list(G.predecessors(nod))[0])

def prueba2():
    lista=[]
    lista2=[]
    lista3=[]
    G.add_node("Daniel")
    G.add_node("Javier")
    G.add_node("Kimberly")
    #G.add_node("Fernando")
    #G.add_node("Willy")
    #G.add_node("Jaquelyn")

    G.add_edge("Daniel", "Javier")
    G.add_edge("Javier", "Kimberly")
   #G.add_edge("Jaquelyn", "Javier")
    
    for nodo in G.nodes:
        lista.append(nodo)
        lista2.append(nodo)

    x=0
    for edge in G.edges:
        lista3.append(edge)
    """
    for para impirmir la cabezera de la tabla

    termina el for


    for para imprimir las filas segun el largo del vector de ffilas
        for edge in edges:
            fila= vectorfilas.1
            for culumna en columnas
                if edge.0==culumna and edge.1= fila
                    print1

    for edge in G.edges:
        
        info1=edge[0]
        info2=edge[1]
        print("info 1:" + info1)
        print("info 2:" + info2)
        print("lista2:" + lista2[x])
        print("lista:" + lista[x])
        

        if info1==lista[x] and info2==lista2[x]:
           print("1")
        x+=1
    """
    filaextra=[]
    columnaextra=[]
    print(len(lista))
    print(len(lista2))
    for i in range (int(len(lista))):
        columnaextra.append("0")
    print(columnaextra)
    x=0
    for i in lista2:
        for j in lista:
            k=0
            for edge in G.edges:
                    if k>int(len(lista)):
                        k=0
                    if ((i==edge[0] and j == edge[1]) or (i==edge[1] and j == edge[0])): #:
                        print("SI")
                        print("Valor 1 de edge: "+ edge[0]+" || valor de fila: "+i)
                        print("Valor 2 de edge: "+ edge[1]+" ||  valor de culumna: "+j)
                        columnaextra.index("0")=="1"
                        #f+=1
                    k+=1
                    
                    
            
        print(columnaextra)
        filaextra.append(columnaextra)
        columnaextra.clear()
        #x+=1

    print (filaextra)
    




    """print(list(lista3))
    columnasAux= []
    filasAux=[]
    
    for i in lista:
        for j in lista2:
            x=0
            if x!=1:
                for edge in G.edges:
                    if i==edge[0] and j == edge[1] or (i==edge[1] and j == edge[0]):
                        filasAux.append("1")
                        x=1
            else:
                filasAux.append("0")
                        



    for fila in lista:
        for columna in lista2:
            for edge in G.edges:
                #if edge[0]==fila and edge[1]==columna:
                if "('"+fila+"', '"+columna+"')" in list(lista3):
                    print("1")
                else:
                    print("0")
#>>> 'ol' in 'hola'

                x+=1"""
                
    """for edge in G.edges:
        for fila in lista:
            for columna in lista2:
                if (edge[0]== columna and edge[1]==fila):
                    print(edge)
                    print("1")"""

    #print(list(lista3))
    #print(len(lista2))
    #print(len(lista))
       # print(edge)

if __name__=="__main__":

    while True:
        print("1) Ingresar nodo")
        print("2) Conectar 2 nodos")
        print("3) Ver grafo")
        print("4) Prueba")
        print("Escoja una opcion: ")
        valor=int(input())
        if valor==1:
            IngresarNodo()
        elif valor==2:
            leerNodos()
            Unir2Nodos()
        elif valor==3:
            verGrafo()
            list(G.nodes)
        elif valor==4:
            #prueba()
            prueba2()
        else:
            print("Opcion incorrecta.")