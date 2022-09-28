from locales import Local

class Tienda(Local):
    
    def __init__(self,name,enabled,rut,category,rent,profit): #datos predeterminados que al editarse se solicita su validación.
        self.name = name
        self.enabled = enabled
        self.rut = rut
        self.category = category 
        self.rent = rent 
        self.profit = profit

    @property
    def AccessLocal(self): 
        dictionary = {}
        dictionary = {"Nombre":self.name,"Habilitado":self.enabled,"RUT":self.rut, "Categoría": self.category, "Valor arriendo": self.rent, "Ganancias":self.profit}
        if (dictionary["RUT"]==None): 
            print("Este local no posee un arrendatario actualmente.")

        elif (dictionary["Nombre"]==None): 
            print("Esta tienda aún no tiene nombre.")
        return dictionary
    @property
    def EditValues(self): #Permite cambiar los datos para un local arrendado.
     
        while (True):
            try: 
                self.name = input("Ingrese el nombre de la tienda, solamente con letras: ")
                self.name = int(self.name)
            except ValueError: 
                break 
            else:  
                print("Ingrese solo letras por favor.")
                continue
       
        while (True):
            try: 
                self.enabled = input("Ingrese una 's' si el local está habilitado para servir comida, en caso contrario, ingrese una 'n': ")
                self.enabled = int(self.enabled)
            except ValueError: 
                    if (self.enabled=="s" or self.enabled=="n"): 
                        break                        
                    else: 
                        print("Ingrese solo la letra s o n por favor")
            else:  
                print("Ingrese solo letras por favor.")
                continue 

        while (True):
                self.rut = str(input("Ingrese el rut del arrendatario (con puntos y guión): "))
                self.rut = str(self.rut)
                verificates_points = 0
                verificates_dash = 0

                if (self.rut.count(".")==2 and self.rut.count("-")==1 and (len(self.rut)<=12 and len(self.rut)>=11)):
                                     
                    if(len(self.rut)==12):
                       if (self.rut[2]=="." and self.rut[6]=="." and self.rut[10]=="-"): 
                            break
                       else: 
                            print("Rut inválido, por favor, intente nuevamente.")
                    else: 
                        if(self.rut[1]=="." and self.rut[5]=="." and self.rut[9]=="-"):
                            break
                        else:
                             print("Rut inválido, por favor, intente nuevamente.")                           
                    break
                else: 
                    print("Rut inválido, por favor, intente nuevamente.")

        while (True):
            try: 
                self.category = input("Ingrese la categoría del local, solamente con letras: ")
                self.category = int(self.category)
            except ValueError: 
                break 
            else:  
                print("Ingrese solo letras por favor.")
                continue

        while (True):
            try: 
                self.rent = float(input("Ingrese el valor de arriendo del local: "))
                self.rent = float(self.rent)
            except ValueError: 
                print("Ingrese solo números por favor")
            else:  
                break
        dictionary = {}
        print("Los valores para la orden de arriendo han sido actualizados:\n")
        dictionary = {"Nombre": self.name,"Habilitado":self.enabled,"RUT":self.rut, "Categoría": self.category, "Valor arriendo": self.rent}
        print(dictionary)
        print("\n")
        return dictionary
 
    @property 
    def DeleteRent(self): 
        if (len(self.rut) >=11 and len(self.rut)<=12):
            self.rut = None
        else: 
            print("No se puede eliminar, la orden de arriendo no ha sido creada aún.")

    @property
    def IsEnabled(self):
        if (self.enabled == 's'): 
            print("El local está habilitado para servir comida en el local.")

        elif (self.enabled == None): 
            print("Aún no hay información disponible.")

        else:
            print("El local no se encuentra habilitado para servir comida en el local.")    

    @property
    def ComputeRent(self): 
        self.rent = (self.rent + (0.15*self.profit))

    @property
    def IsCompatible(self): #la gracia es que compare la categoria con el tipo de local. 
        pass

    @property 
    def ChangeProfit(self): 
        cicle = 0 
       
        while(cicle <1): 
            try: 
                user = int(input("Ingrese las ganancias del local: "))
            except ValueError:
                print("Por favor, ingrese solo números.\n") 
                continue 
        
            else: 
                if (user < 0): 
                    print("Ingrese un número mayor que 0.\n")
                else: 
                    self.profit = user 
                    cicle+=1




""" cliente1 = Tienda(None, None, None, 'restoran',20000,200000)
cliente2 = Tienda("Marcelos", "s", "0", 'juegos',20000,200000)

cliente1.AccessLocal """



