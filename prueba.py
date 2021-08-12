import datetime
import random

diccionario = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ, '
cadena = 'Ingenieria Informatica, inteligencia artificial'

random.seed(2)
startTime = datetime.datetime.now() 

print("    Aproximación\t                       Generación\tTiempo")


#Generar aleatoriamente los genes definiendo la POBLACION
def generarPadre(tamaño):
    genes = [] #se almacena la secuencia aleatoria de genes
    while len(genes) < tamaño: 
        sampleSize = min(tamaño - len(genes), len(diccionario))
        genes.extend(random.sample(diccionario,sampleSize)) #se obtiene la muestra de la poblacion aleatoria 
    return ''.join(genes) #se devuelve una cadena 
    


#Funcion fitness , que compara si hay caracter igual a la cadena
def obtenerFitness(aproximacion):
    return sum(1 for expected, actual in zip(cadena,aproximacion) if expected == actual)



#Funcion de mutación de la cadena 
def mutacion(padre):
    index = random.randrange(0,len(padre))
    genesHijos = list(padre)
    newGene, alternate = random.sample(diccionario,2)
    genesHijos[index] = alternate if newGene == genesHijos[index] else newGene
    return ''.join(genesHijos)


#Imprimir resultado en pantalla
def display(aproximacion):
    timeDiff = datetime.datetime.now() - startTime
    fitness = obtenerFitness(aproximacion)
    print('{}\t{}\t{}'.format(aproximacion,fitness,timeDiff))


#Inicializar parametros
mejorPadre = generarPadre(len(cadena))
mejorFitness = obtenerFitness(mejorPadre)
display(mejorPadre)



#Se crea un ciclo While para iterar hasta obtener nuestra cadena 
while True:
    
    hijo = mutacion(mejorPadre)
    hijoFitness = obtenerFitness(hijo)
    if mejorFitness >= hijoFitness:
        continue
    display(hijo)
    if hijoFitness >= len(mejorPadre):
        break
    mejorFitness = hijoFitness
    mejorPadre = hijo