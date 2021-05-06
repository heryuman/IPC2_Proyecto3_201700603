from flask import Flask,jsonify,request
from operaciones.lector import reader

import os
app=Flask(__name__)



from products import products

@app.route('/ping')
def ping():
    return jsonify({'message':'pong'})

@app.route('/products')
def getProductos():
    return jsonify(products)
@app.route('/subir',methods=['POST'])
def subir():
    if request.method== 'POST':
        requestData=request.get_json()
        content=requestData['archivo']
        #print(content)
        nlector= reader(str(content))
        nlector.lector()

        return jsonify({'message': 'received'})




if __name__=='__main__':
    app.run(port=5000)
