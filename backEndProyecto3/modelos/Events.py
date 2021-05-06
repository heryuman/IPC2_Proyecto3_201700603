class event:
    def __init__(self, lugarFecha, reportadoPor, listaAfectados, error):
        self.lugaryFecha = lugarFecha
        self.reportadoPor = reportadoPor
        self.listaAfectados = listaAfectados
        self.descError = error

    def getDateTime(self):
        return self.lugaryFecha

    def getReportadoPor(self):
        return self.reportadoPor

    def getListaAfectados(self):
        return self.listaAfectados

    def getError(self):
        return self.descError