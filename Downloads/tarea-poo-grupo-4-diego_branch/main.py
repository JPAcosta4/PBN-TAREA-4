
from venv import create
from locales import Local
from kioskos import Kiosko
from multitiendas import Multitienda
from registerowner import RegisterOwner
from tiendas import Tienda
from registerowner import RegisterOwner
from parse_options import ParseOptions
from datetime import date, time, datetime #libreria recomendada para las fechas, ver donde y como usarla. 
from read_data import Read_Data


kioskos,tiendas,multi,owners= Read_Data.read()



while True:
    option_selected=ParseOptions.get_option()
    if option_selected==0:      #salir
        break
    if option_selected==1:      #menu de locales
        #deben listar los locales con su informacion m ́as importante y dar la opcion de acceder al local deseado.
        numerotienda=1
        lenkiosko=lentienda=lenmulti=0
        print("lista de kioskos")
        for i in kioskos:
            print("Local "+str(numerotienda))
            numerotienda+=1
            lenkiosko+=1
            i.AccessLocal
        print("\nlista de tiendas")
        for i in tiendas:
            print("Local "+str(numerotienda))
            numerotienda+=1
            lentienda+=1
            i.AccessLocal
        print("\nlista de multitiendas")
        for i in multi:
            print("Local "+str(numerotienda))
            numerotienda+=1
            lenmulti+=1
            i.AccessLocal
        while True:
            local_option=ParseOptions.get_local_option()
            if local_option==0:     #salir
                break
            if local_option==1:     #crear orden de arriendo
                try:
                    createlocal= int(input("ingrese el tipo de local a crear\n1 para kioskos\n2 para tiendas\n3 para multitiendas\n"))
                except ValueError:
                    print("no se ingreso un numero")
                    break
                if createlocal==1:
                    kioskos.append(Kiosko("","","","","",""))
                    kioskos[lenkiosko].EditValues
                    lenkiosko+=1
                elif createlocal==2:
                    tiendas.append(Tienda("","","","","",""))
                    tiendas[lentienda].EditValues
                    lentienda+=1
                elif createlocal==3:
                    multi.append(Multitienda("","","","","",""))
                    multi[lenmulti].EditValues
                    lenmulti+=1
                else:
                    print("ingrese un numero entre 1 y 3")
            if local_option==2:     #editar orden de arriendo
                try:
                    modlocal=int(input("ingrese el numero de local a modificar: "))
                except ValueError:
                    print("no se ingreso un numero")
                    break
                    
                if modlocal<=lenkiosko:
                    modlocal=modlocal-1
                    kioskos[modlocal].EditValues
                elif modlocal<=(lenkiosko+lentienda):
                    modlocal=modlocal-lenkiosko-1
                    tiendas[modlocal].EditValues
                elif modlocal<=(lenkiosko+lentienda+lenmulti):
                    modlocal=modlocal-lenkiosko-lentienda-1
                    multi[modlocal].EditValues
                else:
                    print("ingrese un numero de local valido")
            
            if local_option==3:     #eliminar orden de arriendo
                try:
                    modlocal=int(input("ingrese el numero de local a eliminar: "))
                except ValueError:
                    print("no se ingreso un numero")
                    break
                if modlocal<=lenkiosko:
                    modlocal=modlocal-1
                    kioskos.pop(modlocal)
                    lenkiosko-=1
                    numerotienda-=1
                elif modlocal<=(lenkiosko+lentienda):
                    modlocal=modlocal-lenkiosko-1
                    tiendas.pop(modlocal)
                    lenkiosko-=1
                    numerotienda-=1
                elif modlocal<=(lenkiosko+lentienda+lenmulti):
                    modlocal=modlocal-lenkiosko-lentienda-1
                    multi.pop(modlocal)
                    lenkiosko-=1
                    numerotienda-=1
                else:
                    print("ingrese un numero de local valido")
            
                
            if local_option==4:     #ingresar ganancias
                try:
                    modlocal=int(input("ingrese el numero de local al cual ingresar ganancias: "))
                except ValueError:
                    print("no se ingreso un numero")
                    break
                    
                if modlocal<=lenkiosko:
                    print(modlocal)
                    modlocal=modlocal-1
                    kioskos[modlocal].ChangeProfit
                elif modlocal<=(lenkiosko+lentienda):
                    modlocal=modlocal-lenkiosko-1
                    tiendas[modlocal].ChangeProfit
                elif modlocal<=(lenkiosko+lentienda+lenmulti):
                    modlocal=modlocal-lenkiosko-lentienda-1
                    multi[modlocal].ChangeProfit
                else:
                    print("ingrese un numero de local valido")
    if option_selected==2:      #menu de reportes
        while True:
            report_option=ParseOptions.get_report_option()  
            if report_option==0:        #salir
                break
            if report_option==1:        #total de renta cobrada en fecha especifica
                pass
            if report_option==2:        #Total de renta pagada por arrendatario
                pass
            if report_option==3:        #Lista de locales arrendados por arrendatario especifico
                pass
            if report_option==4:        #Locales pertenecientes a una categoria
                try:
                    categoriaingresada=str(input("ingrese categoria a buscar:"))
                except ValueError:
                    print("ingrese texto")
                    break
                for i in kioskos:
                    diccionario=i.AccessLocal
                    if diccionario["Categoria"]==categoriaingresada:
                        print(diccionario["Nombre"])
                for i in tiendas:
                    diccionario=i.AccessLocal
                    if diccionario["Categoria"]==categoriaingresada:
                        print(diccionario["Nombre"])
                for i in multi:
                    diccionario=i.AccessLocal
                    if diccionario["Categoria"]==categoriaingresada:
                        print(diccionario["Nombre"])                        
                                            
    if option_selected==3:      #listar arriendos
        for i in kioskos:
            diccionario=i.AccessLocal
            if diccionario["RUT"]=="":
                print(diccionario)
        for i in tiendas:
            diccionario=i.AccessLocal
            if diccionario["RUT"]=="":
                print(diccionario)
        for i in multi:
            diccionario=i.AccessLocal
            if diccionario["RUT"]=="":
                print(diccionario)   
    if option_selected==4:      #buscar local
        try:
            nombrelocal=str(input("ingrese categoria a buscar:"))
        except ValueError:
            print("ingrese texto")
            break
        for i in kioskos:
            diccionario=i.AccessLocal
            if diccionario["Categoria"]==categoriaingresada:
                print(diccionario["Nombre"])
        for i in tiendas:
            diccionario=i.AccessLocal
            if diccionario["Categoria"]==categoriaingresada:
                print(diccionario["Nombre"])
        for i in multi:
            diccionario=i.AccessLocal
            if diccionario["Categoria"]==categoriaingresada:
                print(diccionario["Nombre"]) 
        