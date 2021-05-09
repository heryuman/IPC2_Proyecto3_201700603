from django.shortcuts import render
import requests
import json

def index(request):

    if request.method == 'POST':
        #print("es post")
        #entrada= request.POST.get('contenido')
        archivo=request.FILES['archivo']
        file=str(archivo.read())
        print(file)
        fichero = {'archivo':file}
        response = requests.post('http://127.0.0.1:5000/subir',json=fichero)

        return render(request,'app/index.html')

    else:
        return render(request,'app/index.html')


def cargar(request):


    if request.method == 'POST':
        print("es post")
        #archivo=request.FILES['archivo']
        #ruta=request.FILES.get('archivo')
        #print("la ruta: ",archivo)
        #fichero={'file': open(str(archivo),'rb')}
        #response = requests.post('http://127.0.0.1:5000/subir',files=fichero)
        #entrada= request.POST.get('entrada')
        #print("la entrada",entrada)


    else:
        return render(request, 'app/cargar.html')







