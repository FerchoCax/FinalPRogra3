import networkx as nx
import graphviz
from networkx.algorithms.operators.product import _init_product_graph
from networkx.classes.function import edges, info
from networkx.drawing import nx_agraph
from networkx.generators.trees import prefix_tree
import os
from os import remove
G = nx.DiGraph()

lista=[0,0,0,0,0]

Columnas=[]
Filas=[]

def correr():
  listaFinal=[]
  G.add_node("Daniel")
  G.add_node("Javier")
  G.add_node("Kimberly")
  G.add_node("Fernando")

  G.add_edge("Daniel", "Javier")
  G.add_edge("Javier", "Kimberly")
  G.add_edge("Kimberly", "Fernando")


  for i in G.nodes:
    Columnas.append(i)
    Filas.append(i)

  
  for i in range(len(Columnas)):
    lista.append(0)
  #print(lista)
  x=0
  for i in Filas:
    for edge in G.edges:
      for j in Columnas:
      
        
        if ((i==edge[0] and j == edge[1]) or (i==edge[1] and j == edge[0])):
          lista[x]=1
        x+=1
      
      x=0

  
    
    
    print("Lista a guardar: " + str(lista))
    listaFinal.append(lista)
    print("Se vuelven 0 otra vez")
    
  x=0
  for i in range(5):
    for j in range(5):
      if True:
        lista[x]=1
      x+=1
    x=0
    print("Lista a guardar: " + str(lista))
    listaFinal.append(lista)
    print("Se vuelven 0 otra vez")
      
    for i in range(len(lista)):
      lista[i]=0
  
  for i in listaFinal:
    print(i)

 
  
if __name__=="__main__":
  correr()
