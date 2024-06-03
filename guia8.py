#def promedio_estudiante(nombre_archivo_notas:str, lu:str) -> float:
  #  n:list[int] = []
 #   archivo = open(nombre_archivo_notas)
#    lineas = archivo.readlines()
    #for i in range (0,len(lineas)):
   #     linea_separada = separar_en_palabras(lineas[i])
  #  x:int = 0
 #   for i2 in (0,len(n)):
#        x += n[i2]
    
#    promedio = x/len(n)
#    return promedio

#print (promedio_estudiante)


def a_lista (s:str) -> list:
    n:list = []
    palabra:str = ""
    for i in range (0,len(s)):
        if s[i] == ',':
            n.append(palabra)

from queue import Queue as Cola
import random

def generar_nros_al_azar (cantidad:int, desde:int, hasta:int) -> Cola:
    c = Cola()
    for i in range (0,cantidad):
        elemento = random.randint(desde,hasta)
        print (elemento)
        c.put(elemento)

#print (generar_nros_al_azar(4,2,8))

def cantidad_elementos (c:Cola) -> int:
    n:list = []
    x:int = 0
    while not c.empty():
        elemento = c.get()
        n.append (elemento)
        x += 1
    
    for i in range (0,len(n)):
        print (n[i])
        c.put(n[i])
    
    return x

def buscar_el_maximo (c:Cola) -> int:
    n:list = []
    maximo:int = 0

    while not c.empty():
        elemento = c.get()
        n.append (elemento)
    
    for i in range(0,len(n)):
        if n[i] > maximo:
            maximo = n[i]
    for i2 in range (0,len(n)):
        print (n[i2])
        c.put(n[i2])
    
    return maximo

cola2 = Cola()
cola2.put((3,"hola","xd"))
cola2.put((4,"chau","h"))
cola2.put((2,"no","si"))
cola2.put((5,"no se","taylor"))

def pertenece (x,y:list) -> bool:
    for i in range (0,len(y)):
        if y[i] == x:
            return True
    return False



def armar_secuencia_de_bingo() -> Cola:
    x:int = 0
    salieron:list = []
    while x != 100:
        elemento = random.randint(0,99)
        if not pertenece(elemento,salieron):
            salieron.append(elemento)
            x+=1
    c = Cola()
    for i in range (0,len(salieron)):
        c.put(salieron[i])
    return c

def toList (c:Cola):
    l = []
    while not c.empty():
        l.append(c.get())
    return l

def repetido (y:list) -> bool:
    n:list = []
    for i in range(0,len(y)):
        if not pertenece(y[i],n):
            n.append(y[i])
        else:
            return True
    return False

def jugar_carton_bingo(carton:list[int],bolillero:Cola[int]) -> int:

    cantidad_rondas:int = 0
    salieron:list = []
    rearmar_bolliero:list = []

    while len(salieron) < 12:
        bolita = bolillero.get()

        if pertenece (bolita,carton):
            salieron.append(bolita)
            rearmar_bolliero.append(bolita)
            cantidad_rondas += 1
        else:
            rearmar_bolliero.append(bolita)
            cantidad_rondas += 1

    while not bolillero.empty():
        elemento = bolillero.get()
        rearmar_bolliero.append(elemento)
    
    for i in rearmar_bolliero:
        bolillero.put(i)

    return cantidad_rondas

#print (jugar_carton_bingo([1,2,31,43,52,6,73,8,94,15,11,12],armar_secuencia_de_bingo()))

def n_pacientes_urgentes (c:Cola[(int,str,str)]) -> int:
    restaurar_cola = []
    pacientes_urgentes:int = 0
    while not c.empty():
        pacientes = c.get()
        restaurar_cola.append(pacientes)
        if  pacientes[0] < 4:
            pacientes_urgentes += 1
    
    for i in restaurar_cola:
        #print (i)
        c.put(i)
    
    return pacientes_urgentes

#print (n_pacientes_urgentes(cola2))

#def atencion_a_clientes (c:)

def agrupar_por_longitud (nombre_archivo:str) -> dict:
    archivo = open(nombre_archivo)
    linea = archivo.readline()
    d:dict = {}
    while linea != '':
        lineaseparada = separar_en_palabras(linea)
        for i in lineaseparada

#POR EJEMPLO: d:dict = {"messi": 3, "ronaldo":2}
#d["ronaldo"] = 2
#d["ronaldo"] += 1 --> PASA A VALER 3
#d["neymar"] = 4 --> SE CREA DENTRO DEL DICCIONARIO "neymar" : 4
#"iniesta" in d --> chequea si existe la clave en el diccionario. En este caso, devolveria FALSE.
#DICCIONARIO = LISTA DE TUPLAS    







        

