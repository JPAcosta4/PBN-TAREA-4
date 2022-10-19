from re import L


known_instructions =  ["MOV ","PUSH","RST ", "CMP ", "JEQ ", "JLT ", "INC ", "JMP ", "JLE ", 
"POP ","JGE ","SHL ", "SHR ", "ADD ", "AND ", "OR  ", "XOR ", "NOT ", "SUB ", "RST ", "JOV ", "JCR ", "JLT ", "JGT ", "JNE ","CALL",
"RET", "POP ", "OR  "]
instrucciones_ingresadas = [] #Recibe todas las instrucciones del archivo. 
instrucciones_verificadas = [] #Instrucciones que fueron filtradas, si una de instrucciones ingresadas no se encuentra, dice que era errónea. 
data = [] 
hayData = True
hayCode = False
indice_data = 0
lista_instrucciones = ["MOV A,(B)","MOV B,(B)","MOV (B),A","MOV A,B","MOV B,A", 
"ADD A,(B)","ADD A,B","ADD B,A", "SUB A,(B)","SUB A,B"," SUB B,A", "AND A,(B)","AND A,B","AND B,A",
"NOT (B)","NOT A,A","NOT A,B","NOT B,A","NOT B,B","SHL (B)","SHL A,A","SHL A,B","SHL B,A","SHL B,B",
"SHR (B)","SHR A,A","SHR A,B","SHR B,A","SHR B,B","INC (B)","INC B", "RST (B)" "CMP A,(B)","CMP A,B"]
instrucciones_jump_puntos = []
lista_JUMPS =["JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", "JLE", "JCR", "JOV"]
memoria_direcciones = 1
diccionario_instrucciones = {"MOV A,B":"0000000", "MOV B,A":"0000001","MOV A,Lit":"0000010","MOV B,Lit": "0000001",
"MOV A,(Dir)":"0100101", "MOV B,(Dir)":"0100110", "MOV (Dir),A":"0100111","MOV (Dir),B":"0101000", 
"MOV A,(B)":"0101001", "MOV B,(B)":"0101010", "MOV (B),A":"0101011", "ADD A,B":"0000100", 
"ADD B,A":"0000101", "ADD A,Lit":"0000110", "ADD B,Lit":"0000111", "ADD A,(Dir)":"0101100", 
"ADD B,(Dir)":"0101101", "ADD A,(B)":"0101110", "ADD (Dir)":"0101111", "SUB A,B":"0001000", 
"SUB B,A":"0001001","SUB A,Lit":"0001010","SUB B,Lit":"0001011","SUB A,(Dir)":"0110000", 
"SUB B,(Dir)":"0110001","SUB A,(B)":"0110010", "SUB (Dir)":"0110011", "AND A,B":"0001100", 
"AND B,A":"0001101","AND A,Lit":"0001110", "AND B,Lit":"0001111", "AND A,(Dir)":"0110100", 
"AND B,(Dir)":"0110101", "AND A,(B)":"0110110", "AND (Dir)":"0110111","OR A,B":"0010000", 
"OR B,A":"0010001", "OR A,Lit":"0010010", "OR B,Lit":"0010011", "OR A,(Dir)":"0111000", 
"OR B,(Dir)":"0111001", "OR A,(B)":"0111010", "OR (Dir)":"0111011", "NOT A,A":"0010100", 
"NOT A,B":"0010101","NOT B,A":"0010110","NOT B,B":"0010111","NOT (Dir),A":"0111100", 
"NOT (Dir),B":"0111101", "NOT (B)":"0111110", "XOR A,B":"0011000", "XOR B,A":"0011001",
"XOR A,Lit":"0011010", "XOR B,Lit":"0011011", "XOR A,(Dir)":"0111111", "XOR B,(Dir)":"1000000", 
"XOR A,(B)":"1000001", "XOR (Dir)":"1000010", "SHL A,A":"0011100", "SHL A,B":"0011101", 
"SHL B,A":"0011110","SHL B,B":"0011111", "SHL (Dir),A":"1000011", "SHL (Dir),B":"1000100", 
"SHL (B)":"1000101","SHR A,A":"0100000","SHR A,B":"0100001", "SHR B,A":"0100010",
"SHR B,B":"0100011", "SHR (Dir),A":"1000110", "SHR (Dir),A":"1000110", "SHR (Dir),B":"1000111", 
"SHR (B)":"1001000", "INC B":"0100100", "INC (Dir)":"1001001", "INC (B)":"1001010", 
"RST (Dir)":"1001011","RST (B)":"1001100","CMP A,B":"1001101", "CMP A,Lit":"1001110", 
"CMP B,Lit":"1001111", "CMP A,(Dir)":"1010000", "CMP B,(Dir)":"1010000", "CMP A,(B)":"1010010", 
"JMP Dir":"1010011", "JEQ Dir":"1010100", "JNE Dir":"1010101", "JNE Dir":"1010101", "JGT Dir":"1010110",
"JLT Dir":"1010111", "JGE Dir":"1011000", "JLE Dir":"1011001", "JCR Dir":"1011010", "JOV Dir":"1011011",
"CALL":"1011100", "POP":"1011101", "PUSH":"1011110", "RET":"1011111"}
lista_numeros = []
lista_eliminados = []
lista_definicion = [] #Permite cambiar valores de la lista como por EJ: A,(1) -> A,(Dir), de esta manera se puede obtener el opcode después.
instrucciones_data = []
instrucciones_jump = []
jumps_usados = []
lista_agregadas = []
incorrectoArchivo = True
numeros_data = []
diccionario_etiquetas = {}
apariciones_etiquetas = 1

user = 'recabarren.txt'

while incorrectoArchivo:
    #user = input("Ingrese el nombre del archivo, por favor, escriba tambien la extensión de este: ")
    try:
        file = open(user, 'r', encoding='utf-8')
    except: 
        print("No se pudo abrir el archivo.")
    else: 
        incorrectoArchivo = False

for i in file: 
    i = i.replace("\n","")
    i = i.strip()
    if len(i) > 0: 
        instrucciones_ingresadas.append(i)
        instrucciones_verificadas.append(i)
file.close()

if instrucciones_ingresadas[0] != 'DATA:': 
    hayData = False

if hayData: 
    while(instrucciones_ingresadas[indice_data]!='CODE:'): 
        if indice_data>0: 
            data.append(instrucciones_ingresadas[indice_data])
        if indice_data == len(instrucciones_ingresadas)-1: 
            hayCode = False
            print("Si escribe la etiqueta DATA, debe escribir también la etiqueta CODE.")
            break
        indice_data+=1
else: 
    for i in instrucciones_ingresadas: 
        if i == 'CODE:': 
            hayCode = True 
    if hayCode: 
     while(instrucciones_ingresadas[indice_data]!='CODE:'): 
            data.append(instrucciones_ingresadas[indice_data])       
            indice_data+=1

    else:
        usuario_variables = 0
        usuario_variables = int(input("Su código assembly no tiene etiqueta DATA ni CODE, por favor indique el número de variables que este contiene: "))
        while (indice_data<usuario_variables): 
            data.append(instrucciones_ingresadas[indice_data])
            indice_data+=1

for i in data: 
    numeros_data.append(i.split()[1])
    instruccion = i.split()[0]
    instrucciones_data.append(instruccion)


numeros_data_imprimir = []

for i in numeros_data: 
    texto = ' '
    if i.count("#") == 0 and i.count("b") ==0:
        numero_binario =  "{0:08b}".format(int(i))
        if len(numero_binario) <= 8:
            numeros_data_imprimir.append(numero_binario)
    
    elif i.count("#") == 1 and i.count("b") == 0: 
        i = i.replace("#","")
        numero_hexadecimal = "{0:08b}".format(int(i,16))
        if len(numero_hexadecimal)<=8:
            numeros_data_imprimir.append(numero_hexadecimal)

    elif i.count("b") == 1 and i.count("#") == 0: 
        i = i.replace("b","")
        while(len(i)<8): 
            i = '0'+i
        hayNumeros = False
        for numero in i: 
            if int(numero)<2:
                continue
            else: 
                hayNumeros = True
                break
        if len(i) <= (8) and hayNumeros == False:
            numeros_data_imprimir.append(i)    

for instruction in instrucciones_ingresadas: 
    if instruction[:3] in lista_JUMPS and len(instruction)>3:
        dato = instruction.split()[1]
        if instruction.count('0') == 0 and instruction.count('1')==0 and instruction.count('2') == 0 and instruction.count('3') == 0 and instruction.count('4') == 0 and instruction.count('5') == 0 and instruction.count('6') == 0 and instruction.count('7') == 0 and instruction.count('8')==0 and instruction.count('9')==0: 
            if i not in instrucciones_jump:
                instrucciones_jump.append(dato)
            if i.count(':') == 0:
                instrucciones_jump_puntos.append(dato+':')
            elif i.count(":") ==1:
                instrucciones_jump_puntos.append(dato)
variable_reemplazo = ' '
for i in instrucciones_ingresadas: 
    contador_instrucciones = 0
    while (contador_instrucciones<len(instrucciones_jump)):
        if instrucciones_jump[contador_instrucciones] in i and len(i)>len(instrucciones_jump[contador_instrucciones]) and i.count(':')==1 and i.count(' ')>1: 
            variable_reemplazo = i.split()[1] + ' '+ i.split()[2]
            indice = instrucciones_ingresadas.index(i)
            instrucciones_ingresadas[indice] = variable_reemplazo
            instrucciones_verificadas[indice] = variable_reemplazo

            
            break
        contador_instrucciones+=1

for i in instrucciones_ingresadas:
    if i[:4] not in known_instructions and (('RET' != i[:3])) and len(i)>0 and (i[:5] != ('DATA:') and i[:5]!=('CODE:') and instrucciones_ingresadas.index(i)>indice_data and (i not in instrucciones_jump_puntos)): #Ej: MOVI, la elimina. 
        if 'OR' not in i:
            instrucciones_verificadas.remove(i)
            print(i)
            
    else: 
        if i[:3] == 'RET': #Se hace esto porque RET una instrucción que debe ir sola, entonces si escribiera tipo 'RETI' el programa deberia detectarlo. 
            if i.strip() != 'RET': 
                instrucciones_verificadas.remove(i)

if len(data) > 0: #Con esto, se evitan confusiones con los A o B usados en las instrucciones. 
    for elemento in range(len(data)): 
        data[elemento] = data[elemento].lower()

for i in instrucciones_verificadas:
    if i not in lista_instrucciones and instrucciones_verificadas.index(i) > indice_data: 
        if i.count('(') == 1 and i.count(')') == 1 and i.count(',') == 1 and (i.count('A')<4 or i.count('B')<4): #Sección de A,(dir); B,(dir); (Dir), A; (Dir),B ;
           for j in i:  
                texto = ''
                indice = i.index(j)
                if i[indice].isnumeric(): 
                    if i[indice-1] == '(' and (i[indice-2] == ',' and (i[indice-3] == 'A' or i[indice-3] == 'B')): #A,(Dir) 
                        if  ('MOV' in i[:4] or 'ADD' in i[:4]  or 'SUB' in i[:4]  or 'AND' in i[:4] or 'OR' in i[:2] or 'XOR' in i[:4]  or 'CMP' in i[:4] ): #A,(Dir) -> decimales 
                            while(i[indice].isnumeric()): 
                                if indice < len(i):
                                    texto+=i[indice]
                                    indice+=1
                                if indice == len(i):
                                    break
                            numero_binario =  "{0:08b}".format(int(texto))
                            if len(numero_binario) > 8: 
                                lista_eliminados.append(i)
                                print(i)
                                break
                            else: 
                                lista_numeros.append(numero_binario)
                                if i[1:].count("A") == 1: 
                                    if 'OR' not in i[:3]:
                                        lista_definicion.append(i[:3]+' '"A,(Dir)")
                                    else: 
                                        lista_definicion.append(i[:2]+' '"A,(Dir)")
                                elif i[1:].count("B") == 1: 
                                    if 'OR' not in i[:3]:
                                        lista_definicion.append(i[:3]+' '"B,(Dir)")
                                    else: 
                                        lista_definicion.append(i[:2]+' '"B,(Dir)")
                                break
                        else: 
                            lista_eliminados.append(i)
                            print(i)
                            break
                    elif i[indice-1] == '(' and i[indice-2] != ',': #(Dir),B -> Decimales
                        ubicacion = indice
                        if ('MOV' in i[:4] or 'NOT' in i[:4] or 'SHL' in i[:4] or 'SHR' in i[:4]):
                            while(i[indice]!=')'):
                                texto+=i[indice]
                                indice+=1
                            numero_binario = "{0:08b}".format(int(texto))
                            if len(numero_binario) > 8: 
                                lista_eliminados.append(i)
                                print(i)
                                break
                            else: 
                                lista_numeros.append(numero_binario)
                                if (i.count('A')==1):
                                    lista_definicion.append(i[:3]+' '"(Dir),A")
                                elif (i.count('B')==1): 
                                    lista_definicion.append(i[:3]+' '"(Dir),B")    
                                break
                
                        else: 
                            lista_eliminados.append(i)
                            print(i)
                    elif i[indice-1] == '#' or i[indice-2] == '#': #Hexadecimales con números, ej: #37
                            if (i[indice-2] == '(' and ('MOV' in i[:4] or 'ADD' in i[:4]  or 'SUB' in i[:4]  or 'AND' in i[:4] or 'OR' in i[:4] or 'XOR' in i[:4]  or 'CMP' in i[:4])):  #casos (Dir),B  o B,(Dir) -> Hexadecimales numeros
                                while(i[indice].isnumeric()): 
                                    if indice < len(i):
                                        texto+=i[indice]
                                    indice+=1
                                    if indice == len(i): 
                                        break
                                numero_hexadecimal = "{0:08b}".format(int(texto,16))
                                if (len(numero_hexadecimal) > 8): 
                                    lista_eliminados.append(i)
                                    print(i)
                                    break
                                else:
                                    lista_numeros.append(numero_hexadecimal)
                                    if i[1:].count("A") == 1 and (indice+1 == (len(i))):  
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"A,(Dir)")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"A,(Dir)") 
                                    elif i[1:].count("B") == 1 and (indice+1 == (len(i))): 
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"B,(Dir)")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"B,(Dir)")
                                    elif i[1:].count("A") == 1 and (indice+1 < (len(i))):  
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"(Dir),A")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"(Dir),A") 
                                    elif i[1:].count("B") == 1 and (indice+1 < (len(i))): 
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"(Dir),B")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"(Dir),B") 
                            else: 
                                lista_eliminados.append(i)
                                print(i)
                                break
                    elif i[indice-1] == 'b': 
                            if i[indice-2] == '(' and i[indice-3] == ',' and (i[indice-4] == 'A' or i[indice-4] == 'B') and ('MOV' in i[:4] or 'ADD' in i[:4]  or 'SUB' in i[:4]  or 'AND' in i[:4] or 'OR' in i[:4] or 'XOR' in i[:4]  or 'CMP' in i[:4]):  #casos A,(Dir), -> Numeros binarios 
                                while(i[indice].isnumeric()): 
                                    if indice < len(i):
                                        texto+=i[indice]
                                    indice+=1
                                    if indice == len(i): 
                                        break
                                numero_binario = texto
                                for numero in numero_binario: 
                                    if int(numero)>1: 
                                        lista_eliminados.append(i)         
                                        break                      
                                if (len(numero_binario) > 8): 
                                    lista_eliminados.append(i)
                                    break
                                else:
                                    while (len(numero_binario)<8): 
                                        numero_binario = '0'+numero_binario                                    
                                    lista_numeros.append(numero_binario)
                                    if i[1:].count("A") == 1: 
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"A,(Dir)")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"A,(Dir)")
                                    elif i[1:].count("B") == 1: 
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"B,(Dir)")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"B,(Dir)")
                                    break                     
                            elif (i[indice-2] == '('): #(Dir),A
                                if ('MOV' in i[:4] or 'NOT' in i[:4] or 'SHL' in i[:4] or 'SHR' in i[:4]):
                                    while(i[indice].isnumeric()): 
                                        if indice < len(i):
                                            texto+=i[indice]
                                        indice+=1
                                        if indice == len(i): 
                                            break
                                    numero_binario = texto
                                    for numero in numero_binario: 
                                        if int(numero)>1: 
                                            lista_eliminados.append(i)       
                                            break                      
                                    if (len(numero_binario) > 8): 
                                        lista_eliminados.append(i)
                                        break
                                    else:
                                        while (len(numero_binario)<8): 
                                            numero_binario = '0'+numero_binario                                  
                                        lista_numeros.append(numero_binario)
                                        if i.count("A") == 1 and (indice+1 == (len(i))):  
                                                lista_definicion.append(i[:3]+' '"A,(Dir)")
                                        elif i.count("B") == 1 and (indice+1 == (len(i))): 
                                                lista_definicion.append(i[:3]+' '"B,(Dir)")
                                        elif i.count("A") == 1 and (indice+1 < (len(i))):  
                                                lista_definicion.append(i[:3]+' '"(Dir),A")
                                        elif i.count("B") == 1 and (indice+1 < (len(i))): 
                                                lista_definicion.append(i[:3]+' '"(Dir),B")            
                                        break                                               
                                else: 
                                    lista_eliminados.append(i)

                    elif i[indice-1] == '-': 
                            if i[indice-2] == '(' and i[indice-3] == ',' and (i[indice-4] == 'A' or i[indice-4] == 'B') and ('MOV' in i[:4] or 'ADD' in i[:4]  or 'SUB' in i[:4]  or 'AND' in i[:4] or 'OR' in i[:4] or 'XOR' in i[:4]  or 'CMP' in i[:4]):  #casos A,(Dir), -> Numeros binarios 
                                while(i[indice].isnumeric()): 
                                    if indice < len(i):
                                        texto+=i[indice]
                                    indice+=1
                                    if indice == len(i): 
                                        break
                                numero_binario = texto
                                for numero in numero_binario: 
                                    if int(numero)>1: 
                                        lista_eliminados.append(i)         
                                        break                      
                                if (len(numero_binario) > 8): 
                                    lista_eliminados.append(i)
                                    break
                                else:
                                    while (len(numero_binario)<8): 
                                        numero_binario = '0'+numero_binario                                    
                                    lista_numeros.append(numero_binario)
                                    if i[1:].count("A") == 1: 
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"A,(Dir)")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"A,(Dir)")
                                    elif i[1:].count("B") == 1: 
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"B,(Dir)")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"B,(Dir)")
                                    break                     



                elif i[indice] == '#' and i[indice-1] == '(' and i[indice-2] == ',' and ((i[indice+1] == 'A' or i[indice+1] == 'B' or i[indice+1] == 'C' or i[indice+1] == 'D' or i[indice+1] == 'E' or i[indice+1] == 'F')): 
                     if 'MOV' in i[:4] or 'ADD' in i[:4]  or 'SUB' in i[:4]  or 'AND' in i[:4] or 'OR' in i[:4] or 'XOR' in i[:4]  or 'CMP' in i[:4]: #Caso A,(Dir) -> Hexadecimal (Ej: A,(#A1) o (#AA)) (Letras y numeros)
                        texto_letras = ''  
                        while (indice < len(i)-2): 
                            indice+=1
                            texto_letras += i[indice]
                        numero_hexadecimal = "{0:08b}".format(int(texto_letras,16))         
                        if (len(numero_hexadecimal) > 8): 
                            lista_eliminados.append(i)

                            break
                        else:
                            lista_numeros.append(numero_hexadecimal)
                            if i[1:5].count("A") == 1: 
                                if 'OR' not in i[:3]:
                                    lista_definicion.append(i[:3]+' '"A,(Dir)")
                                else: 
                                    lista_definicion.append(i[:2]+' '"A,(Dir)")
                            elif i[1:5].count("B") == 1: 
                                if 'OR' not in i[:3]:
                                    lista_definicion.append(i[:3]+' '"B,(Dir)")
                                else: 
                                    lista_definicion.append(i[:2]+' '"B,(Dir)")
                            break       
                     else: 
                        lista_eliminados.append(i)
                        break                      

                elif i[indice-1] == '#' and i[indice-2] == '(' and ((i[indice] == 'A' or i[indice] == 'B' or i[indice] == 'C' or i[indice] == 'D' or i[indice] == 'E' or i[indice] == 'F')):
                    if ('MOV' in i[:4] or 'NOT' in i[:4] or 'SHL' in i[:4] or 'SHR' in i[:4]):
                        ubicacion_original = indice
                        texto_letras = '' #Caso (Dir),A -> Hexadecimal (Ej: (#AA),A) (solo letras y/o numeros)
                        while (i[indice]!=')'): 
                            texto_letras += i[indice]
                            indice+=1
                        numero_hexadecimal = "{0:08b}".format(int(texto_letras,16))         
                        if (len(numero_hexadecimal) > 8): 
                            lista_eliminados.append(i)
                            break
                        else:
                            lista_numeros.append(numero_hexadecimal)
                            if (i[ubicacion_original+2]) == ',': #Solo una letra, ej: #A
                                if i[ubicacion_original+3] == 'A': 
                                    lista_definicion.append(i[:3]+' '"(Dir),A")
                                else: 
                                     lista_definicion.append(i[:3]+' '"(Dir),B")
                            elif (i[ubicacion_original+3]) == ',':
                                if i[ubicacion_original+4] == 'A': 
                                    lista_definicion.append(i[:3]+' '"(Dir),A")
                                else: 
                                     lista_definicion.append(i[:3]+' '"(Dir),B")                                
    
                            break                                            
                    else:
                        lista_eliminados.append(i)
            
                elif(i.count(",")==1 and i.count("(")==1 and i.count(")")==1 and (i[1:].count("A")==1 or i[1:].count("B")==1) and (i.count('0') == 0 and i.count('1')==0 and i.count('2') == 0 and i.count('3') == 0 and i.count('4') == 0 and i.count('5') == 0 and i.count('6') == 0 and i.count('7') == 0 and i.count('8')==0 and i.count('9')==0)): 
                    hayInstruccion = False
                    for uinstruccion in instrucciones_data: 
                        if uinstruccion in i: 
                            hayInstruccion = True
                            break
                    if  (('MOV' in i[:4] or 'ADD' in i[:4]  or 'SUB' in i[:4]  or 'AND' in i[:4] or 'OR' in i[:2] or 'XOR' in i[:4]  or 'CMP' in i[:4]) and (i[4] != '(') and hayInstruccion):
                            if i[1:].count("A") == 1:     
                                if 'OR' not in i: 
                                    lista_definicion.append(i[:3]+' '"A,(Dir)")
                                else: 
                                    lista_definicion.append(i[:2]+' '"A,(Dir)")       
                            elif i[1:].count("B") == 1: 
                                if 'OR' not in i: 
                                    lista_definicion.append(i[:3]+' '"B,(Dir)")
                                else: 
                                    lista_definicion.append(i[:2]+' '"B,(Dir)")
                            break                    
                    elif (('MOV' in i[:4] or 'NOT' in i[:4] or 'SHL' in i[:4] or 'SHR' in i[:4]) and (i[4] == '(') and hayInstruccion): #(Dir),A               
                            if i[1:].count("A") == 1:     
                                    lista_definicion.append(i[:3]+' '"(Dir),A")    
                            elif i[1:].count("B") == 1: 
                                    lista_definicion.append(i[:3]+' '"(Dir),B")
                            break
                    else: 
                        lista_eliminados.append(i)
                        print(instrucciones_ingresadas.index(i))


                    break           
            

        elif i.count(',')==1 and (i.count('A')<4 or i.count('B')<4) and (i.count(')') == 0 and i.count('(')==0): #Sección de A,Lit ; B,Lit 
            for j in i:
                texto = ''
                indice = i.index(j)
                if i[indice].isnumeric():
                    if 'NOT' in i[:4] or 'SHL' in i[:4] or 'SHR' in i[:4] or 'INC' in i[:4] or 'RST' in i[:4]:
                        lista_eliminados.append(i)
                        break
                    elif i[indice-1] == ',' and (i[indice-2] == 'A' or i[indice-2] == 'B'): #Ej: A,1  , decimales
                        while(i[indice].isnumeric()): 
                            if indice < len(i):
                                texto+=i[indice]
                                indice+=1
                            if indice == len(i):
                                break
                        numero_binario =  "{0:08b}".format(int(texto))
                        if len(numero_binario) > 8: 
                            lista_eliminados.append(i)
                        else: 
                            lista_numeros.append(numero_binario)
                            if i[3:].count("A") == 1: 
                                if 'OR' not in i[:3]:
                                    lista_definicion.append(i[:3]+' '"A,Lit")
                                else: 
                                    lista_definicion.append(i[:2]+' '"A,Lit")
                            elif i[3:].count("B") == 1: 
                                if 'OR' not in i[:3]:
                                    lista_definicion.append(i[:3]+' '"B,Lit")
                                else: 
                                    lista_definicion.append(i[:2]+' '"B,Lit")
                        break
                    
                    elif (i[indice-1] == '#') or (i[indice-2] == '#'): #Ej: A,#37, hexadecimales:
                        if i[indice-1] == '#': 
                            if (i[indice-2] == ',' and (i[indice-3]=='A' or i[indice-3]=='B')):
                                while(i[indice].isnumeric()): 
                                    if indice < len(i):
                                        texto+=i[indice]
                                    indice+=1
                                    if indice == len(i): 
                                        break
                                numero_hexadecimal = "{0:08b}".format(int(texto,16))
                                if (len(numero_hexadecimal) > 8): 
                                    lista_eliminados.append(i)
                                    break
                                else:
                                    lista_numeros.append(numero_hexadecimal)
                                    if i[1:].count("A") == 1: 
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"A,Lit")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"A,Lit") 
                                    elif i[1:].count("B") == 1:
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"B,Lit")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"B,Lit")
                                    break 

                        elif i[indice-2] == '#':  
                            if (i[indice-3] == ',' and (i[indice-4]=='A' or i[indice-4]=='B')):
                                texto+= i[indice-1]
                                while(i[indice].isnumeric()): 
                                    if indice < len(i):
                                        texto+=i[indice]
                                    indice+=1
                                    if indice == len(i): 
                                        break
                                numero_hexadecimal = "{0:08b}".format(int(texto,16))
                                if (len(numero_hexadecimal) > 8): 
                                    lista_eliminados.append(i)
                                    break
                                else:
                                    lista_numeros.append(numero_hexadecimal)
                                    if i[1:].count("A") == 1: 
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"A,Lit")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"A,Lit") 
                                    elif i[1:].count("B") == 1:
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"B,Lit")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"B,Lit")
                                    break 

                    elif i[indice-1] == 'b': 
                            if (i[indice-2] == ',' and (i[indice-3]=='A' or i[indice-3]=='B')):
                                while(i[indice].isnumeric()): 
                                    if indice < len(i):
                                        texto+=i[indice]
                                    indice+=1
                                    if indice == len(i): 
                                        break
                                numero_binario = texto
                                for numero in numero_binario:
                                    if int(numero) >1: 
                                        lista_eliminados.append(i)
                                        break
                                if (len(numero_binario) > 8): 
                                    lista_eliminados.append(i)
                                    break
                                else:
                                    while (len(numero_binario)<8): 
                                        numero_binario = '0'+numero_binario                
                                    lista_numeros.append(numero_binario)
                                    if i[1:].count("A") == 1: 
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"A,Lit")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"A,Lit")
                                    elif i[1:].count("B") == 1: 
                                        if 'OR' not in i[:3]:
                                            lista_definicion.append(i[:3]+' '"B,Lit")
                                        else: 
                                            lista_definicion.append(i[:2]+' '"B,Lit")
                                    break 
                elif (i[indice] == '#' and (i[indice+1] == 'A' or i[indice+1] == 'B' or i[indice+1] == 'C' or i[indice+1] == 'D' or i[indice+1] == 'E' or i[indice+1] == 'F')): 
                    if 'NOT' in i[:4] or 'SHL' in i[:4] or 'SHR' in i[:4] or 'INC' in i[:4] or 'RST' in i[:4]:
                        lista_eliminados.append(i)
                        break
                    else: 
                        texto_letras = ''
                        while (indice < len(i)-1): 
                            indice+=1
                            texto_letras += i[indice]
                        numero_hexadecimal = "{0:08b}".format(int(texto_letras,16))         
                        if (len(numero_hexadecimal) > 8): 
                            lista_eliminados.append(i)
                            break
                        else:
                            lista_numeros.append(numero_hexadecimal)
                            if i[1:5].count("A") == 1: 
                                if 'OR' not in i[:3]:
                                    lista_definicion.append(i[:3]+' '"A,Lit")
                                else: 
                                    lista_definicion.append(i[:2]+' '"A,Lit")
                            elif i[1:5].count("B") == 1: 
                                if 'OR' not in i[:3]:
                                    lista_definicion.append(i[:3]+' '"B,Lit")
                                else: 
                                    lista_definicion.append(i[:2]+' '"B,Lit")
                            break                       

        #Caso (Dir)
        elif i.count('(') == 1 and i.count(')') == 1 and i.count(',') == 0 and (i.count('A')<3 or i.count('B')<3): 
            if ('ADD' in i[:4] or 'SUB' in i[:4]  or 'AND' in i[:4]  or 'OR' in i[:4] or 'XOR' in i[:4] or 'INC' in i[:4]  or 'RST' in i[:4]):
                for j in i:  
                    texto = ''
                    indice = i.index(j)
                    if i[indice].isnumeric(): 
                        if i[indice-1] == '(': 
                            while(i[indice].isnumeric()): 
                                if indice < len(i):
                                    texto+=i[indice]
                                    indice+=1
                                if indice == len(i):
                                    break
                            numero_binario =  "{0:08b}".format(int(texto))
                            if len(numero_binario) > 8: 
                                lista_eliminados.append(i)
                            else: 
                                lista_numeros.append(numero_binario)
                                if 'OR' not in i[:3]:
                                    lista_definicion.append(i[:3]+' '"(Dir)")
                                else: 
                                    lista_definicion.append(i[:2]+' '"(Dir)")                            
                                break            
            #caso hexadecimales con numeros y letras
                        elif (i[indice-1] == '#' and i[indice-2] == '('): 
                                while(i[indice].isnumeric()): 
                                    if indice < len(i):
                                        texto+=i[indice]
                                    indice+=1
                                    if indice == len(i): 
                                        break
                                numero_hexadecimal = "{0:08b}".format(int(texto,16))
                                if (len(numero_hexadecimal) > 8): 
                                    lista_eliminados.append(i)
                                    break
                                else:
                                    lista_numeros.append(numero_hexadecimal)
                                if 'OR' not in i[:3]:
                                    lista_definicion.append(i[:3]+' '"(Dir)")
                                else: 
                                    lista_definicion.append(i[:2]+' '"(Dir)")       
                                break 
                        elif (i[indice-2] == '#' and i[indice-3] == '('): 
                                texto+= i[indice-1]
                                while(i[indice].isnumeric()): 
                                    if indice < len(i):
                                        texto+=i[indice]
                                    indice+=1
                                    if indice == len(i): 
                                        break
                                numero_hexadecimal = "{0:08b}".format(int(texto,16))
                                if (len(numero_hexadecimal) > 8): 
                                    lista_eliminados.append(i)
                                    break
                                else:
                                    lista_numeros.append(numero_hexadecimal)
                                    if 'OR' not in i[:3]:
                                        lista_definicion.append(i[:3]+' '"(Dir)")
                                    else: 
                                        lista_definicion.append(i[:2]+' '"(Dir)")  
                                    break                         

            #caso binario 
                        elif i[indice-1] == 'b' and i[indice-2] == '(' and i.count(",") == 0: 
                                while(i[indice].isnumeric()): 
                                    if indice < len(i):
                                        texto+=i[indice]
                                    indice+=1
                                    if indice == len(i): 
                                        break
                                numero_binario = texto
                                for numero in numero_binario: 
                                    if int(numero)>1: 
                                        lista_eliminados.append(i)        
                                        break                      
                                if (len(numero_binario) > 8): 
                                    lista_eliminados.append(i)
                                    break
                                else:
                                    while (len(numero_binario)<8): 
                                        numero_binario = '0'+numero_binario
                                    lista_numeros.append(numero_binario)
                                    if 'OR' not in i[:3]:
                                        lista_definicion.append(i[:3]+' '"(Dir)")
                                    else: 
                                        lista_definicion.append(i[:2]+' '"(Dir)")  
                                    break     
                    elif (i[indice] == '#' and i[indice-1] == '('):
                            texto_letras = ''
                            indice+=1
                            verificado = True
                            while (i[indice]!=')'): 
                                texto_letras += i[indice]
                                indice+=1
                            try: 
                                numero_hexadecimal = "{0:08b}".format(int(texto_letras,16))
                            except: 
                                    lista_eliminados.append(i)
                                    verificado = False
                                    break         
                            if (len(numero_hexadecimal) > 8) and verificado: 
                                lista_eliminados.append(i)
                                break
                            else:
                                lista_numeros.append(numero_hexadecimal)
                                if 'OR' not in i[:3]:
                                    lista_definicion.append(i[:3]+' '"(Dir)")
                                else: 
                                    lista_definicion.append(i[:2]+' '"(Dir)")  
                                break          

                    elif (i.count('0') == 0 and i.count('1')==0 and i.count('2') == 0 and i.count('3') == 0 and i.count('4') == 0 and i.count('5') == 0 and i.count('6') == 0 and i.count('7') == 0 and i.count('8')==0 and i.count('9')==0):
                        lista_definicion.append(i[:3]+' '"(Dir)")
                        break

            else:
                lista_eliminados.append(i)
                
        elif (i[:3] in lista_JUMPS): 
             if (i.count(",") == 0 and i.count("(") == 0 and i.count(")") == 0): 
                #caso decimales
                for j in i:  
                    texto = ''
                    indice = i.index(j)
                    if i[indice].isnumeric():
                        if i[indice-1] == ' ':
                            while(i[indice].isnumeric()): 
                                if indice < len(i):
                                    texto+=i[indice]
                                    indice+=1
                                if indice == len(i):
                                    break
                            numero_binario =  "{0:08b}".format(int(texto))
                            if len(numero_binario) > 8: 
                                lista_eliminados.append(i)
                                break
                            else: 
                                lista_numeros.append(numero_binario)
                                lista_definicion.append(i[:3]+' '"Dir")
                                break         
                        #hexadecimales con numeros solamente. Ej #37
                        elif i[indice-1] == "#":
                            while(i[indice].isnumeric()):
                                if indice < len(i):
                                    texto+=i[indice]
                                    indice+=1
                                if indice == len(i): 
                                    break
                            numero_hexadecimal = "{0:08b}".format(int(texto,16))
                            if (len(numero_hexadecimal) > 8): 
                                lista_eliminados.append(i)
                                break
                            else:
                                lista_numeros.append(numero_hexadecimal)
                                lista_definicion.append(i[:3]+' '"Dir")
                                break
                        #Caso binario. 
                        elif i[indice-1] == 'b':
                                while(i[indice].isnumeric()): 
                                    if indice < len(i):
                                        texto+=i[indice]
                                    indice+=1
                                    if indice == len(i): 
                                        break
                                numero_binario = texto
                                for numero in numero_binario: 
                                    if int(numero)>1: 
                                        lista_eliminados.append(i)        
                                        break                      
                                if (len(numero_binario) > 8): 
                                    lista_eliminados.append(i)
                                    break
                                else:
                                    while (len(numero_binario)<8): 
                                        numero_binario = '0'+numero_binario
                                    lista_numeros.append(numero_binario)
                                    lista_definicion.append(i[:3]+' '"Dir")
                                    break
                    elif(i[indice] == '#' and (i[indice+1] == 'A' or i[indice+1] == 'B' or i[indice+1] == 'C' or i[indice+1] == 'D' or i[indice+1] == 'E' or i[indice+1] == 'F')): 
                        texto_letras = ''
                        while (indice < len(i)-1): 
                            indice+=1
                            texto_letras += i[indice]
                        numero_hexadecimal = "{0:08b}".format(int(texto_letras,16))         
                        if (len(numero_hexadecimal) > 8): 
                            lista_eliminados.append(i)
                            break
                        else:
                            lista_numeros.append(numero_hexadecimal)
                            lista_definicion.append(i[:3]+' '"Dir")
                            break                  

                    elif(i.count('A') == 0 and i.count('B')==0 and i.count('(')==0 and i.count(')')==0) and (i.count('0') == 0 and i.count('1')==0 and i.count('2') == 0 and i.count('3') == 0 and i.count('4') == 0 and i.count('5') == 0 and i.count('6') == 0 and i.count('7') == 0 and i.count('8')==0 and i.count('9')==0): 
                        hayInstruccion = False
                        for uinstruccion in instrucciones_jump: 
                            if uinstruccion in i: 
                                hayInstruccion=True
                                break
                        if (hayInstruccion):
                            lista_definicion.append(i[:3]+' '"Dir")
                            break
                        
                        else: 
                            lista_eliminados.append(i)
                            break       
             else: 
                lista_eliminados.append(i)

        elif 'POP' in i: 
            lista_definicion.append(i)
        
        elif 'PUSH' in i: 
            lista_definicion.append(i)
        
        elif 'CALL' in i: 
            lista_definicion.append(i)

        elif 'RET'in i: 
            lista_definicion.append(i)

        elif i in instrucciones_jump_puntos: 
            lista_definicion.append(i)
            if i not in diccionario_instrucciones and not i in lista_agregadas:
                diccionario_instrucciones[i] = "123132213127"
                indices = instrucciones_ingresadas.index(i)
                numero_binario =  "{0:08b}".format(int(indices-indice_data-apariciones_etiquetas))
                i=i.replace(":","")
                diccionario_etiquetas[i] = (numero_binario)
                apariciones_etiquetas+=1       
    else: 
        if (i in lista_instrucciones and instrucciones_verificadas.index(i) > indice_data):
            lista_definicion.append(i)         
contador = 0
cuenta_eliminados = 0
while(contador < len (lista_eliminados)): #No se puede usar un loop de for para eliminar así que esto es lo mejor. 
    if lista_eliminados[contador] in instrucciones_verificadas: 
        instrucciones_verificadas.remove(lista_eliminados[contador])
        contador+=1
for i in instrucciones_ingresadas: 
    if i not in instrucciones_verificadas: 
        indice = instrucciones_ingresadas.index(i)
        print(f'La instrucción "{i}" ubicada en la línea {indice+1} no existe.')
        cuenta_eliminados+=1

caracteres = ''
for i in user: 
    if i == '.': 
        break
    else: 
        caracteres+=i

indice_instrucciones = 0
counter = 0 
indice_jump = 0

if len(lista_eliminados)==0 and cuenta_eliminados==0: 
    archivo = open(caracteres+'.out','w',encoding='utf-8')
    numbers = open(caracteres+'.mem','w',encoding='utf-8')
    for ins in instrucciones_verificadas:
        encuentra = False
        if instrucciones_verificadas.index(ins) > indice_data:
            if ins.count("#") or ins.count("b") or ins.count("0") == 1 or ins.count("1") == 1 or ins.count("2") == 1 or ins.count("3") == 1 or ins.count("4") == 1 or ins.count("5") == 1 or ins.count("6") == 1 or ins.count("7") == 1 or ins.count("8") == 1 or ins.count("9") == 1:
                archivo.write(f'{diccionario_instrucciones[lista_definicion[indice_instrucciones]] + lista_numeros[counter]}\n')
                numbers.write(lista_numeros[counter]+'\n')
                indice_instrucciones+=1
                counter+=1
            else:  
                for letra in instrucciones_data: 
                    if letra in ins: 
                        indice = instrucciones_data.index(letra)
                        encuentra = True
                        break
                numero_binario = "{0:08b}".format(int(indice))
                if encuentra and len(instrucciones_data)==len(numeros_data_imprimir) and len(diccionario_instrucciones[lista_definicion[indice_instrucciones]])<8 and ins[:3] not in lista_JUMPS:
                    archivo.write(f'{diccionario_instrucciones[lista_definicion[indice_instrucciones]]+numero_binario}\n')
                else:
                    if len(diccionario_instrucciones[lista_definicion[indice_instrucciones]])<8 and ins[:3] not in lista_JUMPS:
                        archivo.write(f'{diccionario_instrucciones[lista_definicion[indice_instrucciones]]}00000000\n')
                    elif ins[:3] in lista_JUMPS and len(diccionario_etiquetas) >0:
                        archivo.write(f'{diccionario_instrucciones[lista_definicion[indice_instrucciones]]+diccionario_etiquetas[ins[4:]]}\n')

                indice_instrucciones+=1
    archivo.close()       
    numbers.close()

else: 
    print(f'Su programa presenta más de {cuenta_eliminados} error/es, es imposible generar un documento de salida.\n')

