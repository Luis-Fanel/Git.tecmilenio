from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

class Pedido:
    def __init__(self, conexion, cursor):
        self.conexion = conexion
        self.cursor = cursor
    
    def consultar_pedido(self, numero_pedido):
        consulta = "SELECT * FROM pedidos WHERE numero_pedido = ?"
        self.cursor.execute(consulta, (numero_pedido,))
        pedido_info = self.cursor.fetchone()
        return pedido_info

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta', methods=['POST'])
def consulta():
    numero_pedido = request.form.get('numero_pedido')
    
    if not numero_pedido:
        return jsonify({'mensaje': 'Número de pedido requerido'})
    
    conexion = sqlite3.connect('happyburger.db')
    cursor = conexion.cursor()
    pedido = Pedido(conexion, cursor)
    pedido_info = pedido.consultar_pedido(numero_pedido)
    
    if not pedido_info:
        return jsonify({'mensaje': 'Pedido no encontrado'})
    
    pedido_dict = {
        'numero_pedido': pedido_info[0],
        'nombre_cliente': pedido_info[1],
        'direccion_entrega': pedido_info[2]
    }
    
    return jsonify(pedido_dict)

if __name__ == '__main__':
    app.run()
