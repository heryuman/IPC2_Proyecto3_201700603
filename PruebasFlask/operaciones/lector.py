import os
class reader:
    def __init__(self,input):
        self.input=input
        
        
    def lector(self):
        
        lchar=(self.input)
        archivo=open('ArchivosSalida/entrada.xml','w')
        archivo.write(lchar+os.linesep)
        archivo.close()

        print("mostando desde lector: ",lchar)
        
        
    