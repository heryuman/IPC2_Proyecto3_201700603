import re
from ElementTree_pretty import prettify
class createEvents:
    def __init__(self,caracteres):
        self.caracteres=caracteres
        self.Analizar(self.caracteres)
    
    def Analizar(self,simbolos):
        fechas=re.findall('[A-Z][A-Za-z]+, ?[0-9]{2}/[0-1][0-9]/[0-9]{4}',simbolos)
        print(fechas)
        #Parte que analiza la Linea de reportadores
        reportadores=re.findall('Reportado por: ?<?[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+>?',simbolos)
        print(reportadores)
        for i in range(len(reportadores)):
             print(re.findall('[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+',reportadores[i]))
        afectados=re.findall('Usuarios afectados:.+',simbolos)
        print(afectados,len(afectados))