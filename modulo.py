class Caja:
 
 def __init__(self, caja={},valoresPermitidos={1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0},total=0,error=0):
       #constructor, self actua como this en kotlin
         self.caja = caja
         self.total = total
         self.error = error
         self.valoresPermitidos = valoresPermitidos
         valueError = False
         
         for k in caja.keys():
           if not k in valoresPermitidos.keys():
             valueError = True
             error = k
         if valueError == True:
            caja = {}
            valueError = False
            print(f"ValueError: Denominacion '{error}' no permitida")
         

 def agregar(self,nuevacaja={},valoresPermitidos={1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0}):
   checkpoint = self.caja
   valueError = False 
   self.valoresPermitidos = valoresPermitidos
   self.nuevacaja= nuevacaja
   for k in nuevacaja.keys():
      if k in valoresPermitidos.keys():
        if not k in self.caja.keys(): 
         self.caja[k] = 0
        self.caja[k] = self.caja[k] + nuevacaja[k]
      else:
       self.error = k
       valueError = True
   if valueError == True:
     self.caja = checkpoint
     valueError = False
     print(f"ValueError: Denominacion '{self.error}' no permitida")

 def quitar(self,elements={},valoresPermitidos={1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0}):
   self.elements = elements
   self.valoresPermitidos = valoresPermitidos 
   checkpoint = self.caja
   typeError = ""
   error = {}
   for k,v in elements.items():
     if k in self.caja.keys() and v <= self.caja[k]:
       self.caja[k] = self.caja[k] - elements[k]
     elif v > self.caja[k]:
       typeError = "faltanBilletes"
       error[k] = 0
       error[k] = v
   if typeError == "faltanBilletes":
     print(f"No hay {v} billetes de {k}")
     typeError = "" 

  

def str(self):
   self.total = 0
   for item in self.caja.items():
     if item[1] != 0:
       self.total +=  (item[0] * item[1])
   print(f"Caja {self.caja} total: {self.total} pesos")
  