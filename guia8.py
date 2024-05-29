def contar_lineas(nombre:str) -> int:
    archivo = open(nombre,'r')
    i:int = 0
    n = archivo.readline()
    while n != '':
        i += 1
        n = archivo.readline()
        n
    return i

def existe_palabra (palabra:str, archivo:str) -> bool:
    abrir = open(archivo,'r')
    linea = abrir.readline()
    while linea != '':
        palabras = separar_en_palabras(linea)
        if pertenece (palabra, palabras) == True:
            return True
        else:
            linea = abrir.readline()
    return False

def separar_en_palabras (palabras:str) -> list[str]:
    n:list[str] = []
    for i in range(0,len(palabras)):
        if i != '':
            n += palabras[i]
        else:
            n.append([])
    return n


def pertenece(x:str, y:list) -> bool:
    i:int = 0
    res:bool = False
    for i in range (0,len(y)):
        if y[i] == x:
            res = True
    return res

def es_comentario (linea:str) -> bool:
    for i in range(0,len(linea)):
        if linea[i] == '#' and i != 0:
            for i2 in range(0,i):
                if linea[i2] != ' ':
                    return False
            return True
        elif linea [i] == '#' and i == 0:
            return True
    return False


def clonar_sin_comentarios (nombrearchivo:str) -> str:
    n:list[chr] = "" 
    abrir = open(nombrearchivo)
    linea = abrir.readline()
    while linea != ' ':
        if (es_comentario(linea)) == False:
            print (linea)
            n += linea
            linea = abrir.readline()
            print (n)
        else:
            print ("esta es la linea comentada", linea)
            linea = abrir.readline()
            

   # abrirarchivo = open ("sincomentarios.txt",'w')
    #escribir = abrirarchivo.write(n)
    #return escribir

print (clonar_sin_comentarios ("prueba.txt"))
#def invertir_lineas(nombrearchivo:str) -> str:





