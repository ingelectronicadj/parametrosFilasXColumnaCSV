import sys

#argv contiene todos los parametros que se le envian al script
parametros = sys.argv

if(len(parametros) < 2):
    print ("Necesita ingresar como parametro el nombre del archivo") # python lectura_csv.py fichero.csv 
    sys.exit(1)
# este es el primer parametro
archivo = parametros[1]
FREQ = int(input("Ingrese la frecuencia:"))
# Esta funcion necesita un nombre de archivo un numero de columna y un valor para buscar
# y le entregara al usuario el dato de las otras columnas como un diccionario
def abrir_archivo_por_columna(nombre_archivo,columna,valor):
    f = open(nombre_archivo,"r") #carga el archivo en modo lectura
    lineas = f.readlines()
    cantidad_lineas = 0
    
    
    for linea in lineas:
        if(cantidad_lineas > 0):
	    # Strip quita caracteres no imprimibles del string
            # Split parte la cadena de texto por el caracter que desee
            lca = linea.strip().split(";")
            print (lca) #imprime toda la tabla en lineas como array hasta encontrar el valor deseado
            columna_1 = lca[0]
            #print (columna_1)
            if(columna_1 == valor):
                return {'Gi': lca[1], 'bi': lca[2], 'Gf': lca[3], 'bf':lca[4], 'Gr':lca[5], 'br':lca[6], 'Go':lca[7], 'bo':lca[8]}
	 
        cantidad_lineas += 1

#print (str(FREQ)) cargo en la variable a el array
a = abrir_archivo_por_columna(archivo,0,str(FREQ))

Gi=a['Gi']
bi=a['bi']
Gf=a['Gf']
bf=a['bf']
Gr=a['Gr']
br=a['br']
Go=a['Go']
bo=a['bo']

print (Gi)
print (bi)
print (Gf)
print (bf)
print (Gr)
print (br)
print (Go)
print (bo)

