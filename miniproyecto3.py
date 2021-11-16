diccionario_ingredientes={}
diccionario_recetas={}
usuario=[""]

def cargar_diccionario_ingredientes():
    ingredientes=open("ingredientes.txt","r",encoding="UTF-8")
    for linea in ingredientes:
        linea_limpia=linea.strip()
        lista_linea=linea_limpia.split(" ")
        diccionario_ingredientes[lista_linea[0]]=int(lista_linea[1])
    ingredientes.close()
        
        
def cargar_diccionario_recetas():
    recetas=open("recetas.csv","r",encoding="UTF-8")
    for linea in recetas:
        linea_limpia=linea.strip()
        lista_linea=linea_limpia.split(",")
        diccionario_recetas[lista_linea[0]]=lista_linea[1:len(lista_linea)]
    recetas.close()


cargar_diccionario_ingredientes()
cargar_diccionario_recetas()
        
        
def printStocks():
    print("Stock actual de ingredientes disponibles:")
    for ingredientes,cantidad in diccionario_ingredientes.items():
        print(ingredientes+" "+str(cantidad))


def reponerIngredientes(ingredientes):
    for i in range(0,len(ingredientes)):
        if ingredientes[i] in diccionario_ingredientes:
            diccionario_ingredientes[ingredientes[i]]+=1


def prepararReceta(receta):
    if receta in diccionario_recetas:
        ingredientes_faltantes=""
        numero_ingredientes_faltantes=0
        comprobacion=True
        for i in range(0,len(diccionario_recetas[receta])):
            if not diccionario_ingredientes[diccionario_recetas[receta][i]] > 0:
                ingredientes_faltantes+=diccionario_recetas[receta][i]+", "
                numero_ingredientes_faltantes+=1
                comprobacion=False
        if comprobacion:
            for i in range(0,len(diccionario_recetas[receta])):
                diccionario_ingredientes[diccionario_recetas[receta][i]]-=1
        else:
            ingredientes_faltantes=ingredientes_faltantes[:len(ingredientes_faltantes)-2]
            if numero_ingredientes_faltantes==1:
                print("*** No se puede hacer "+receta+" porque falta "+ingredientes_faltantes+" ***")
            else:
                ultima_coma=ingredientes_faltantes.rindex(", ")
                ingredientes_faltantes=ingredientes_faltantes[:ultima_coma]+ingredientes_faltantes[ultima_coma:].replace(", "," y ")
                print("*** No se puede hacer "+receta+" porque faltan "+ingredientes_faltantes+" ***")
        
    else:
        print("*** Lo sentimos pero no preparamos "+receta+" ***")
        




while usuario[0].upper()!="STOP":
    usuario=input("Ingresa PREPARAR 'Receta', REPONER 'ingrediente1 ingrediente2 ... ingredienteN' o STOP: ")
    usuario=usuario.split(" ")
    if usuario[0].upper()=="PREPARAR":
        prepararReceta(usuario[1])
        printStocks()
    elif usuario[0].upper()=="REPONER":
        reponerIngredientes(usuario)
        printStocks()
    elif usuario[0].upper()!="STOP":
        print("Has introducido algo de manera incorrecta.")

print("\n")        
print("El programa ha terminado.")
        

