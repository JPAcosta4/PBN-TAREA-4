from abc import ABC, abstractmethod

class Local(ABC): #abstracta porque es heredera de kiosko, tiendas y multitiendas. 
    
    
    @abstractmethod
    def AccessLocal(self): #permite desplegar la información necesaria para el local
        pass

    @abstractmethod
    def EditValues(self): #pensada para verificar que rut, enabled, etc.. cumplan con su propiedad de int o str, con try y except.
        pass 
       
    @abstractmethod
    def IsEnabled(self): #tiene pase de movilidad o no. 
        pass 

    
    @abstractmethod
    def DeleteRent(self): #permite eliminar el arrendatario actual
        pass 
    
    @abstractmethod
    def ComputeRent(self): #calcula el valor del arriendo según el tipo de local. 
        pass 

    @abstractmethod
    def IsCompatible(self): #la gracia es que compare la categoria con el tipo de local. 
        pass
    
    @abstractmethod
    def ChangeProfit(self): 
        pass 

