from products import products
from flask import jsonify, request
from flask_api.models.Product import Product
from app import app

"""
GET a la ruta de productos
"""
@app.route('/products')
def getProducts():
    return jsonify({"products": products}), 200

"""
POST a la ruta de productos
"""
@app.route('/products', methods=['POST'])
def addProduct():
    newProduct = Product(
        request.json['name'],
        request.json['price'],
        request.json['quantity']
    )

    products.append({'name': newProduct.name, 'price': newProduct.price, 'quantity': newProduct.quantity})

    return jsonify({
        'msg': 'Product added successfully',
        'products': products
    }), 201

"""
PUT a la ruta productos pasando como parametro el nombre del producto
"""
@app.route('/products/<string:product_name>', methods=['PUT'])
def updateProduct(product_name):
    productFound = [
        product for product in products if product['name'] == product_name]

    if len(productFound) > 0:
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']

        return jsonify({
            'msg': 'Product Updated',
            'product': productFound[0]
        }), 200

    return jsonify({'msg': 'Product not found'}), 404

"""
DELETE a la ruta productos pasando como parametro el nombre del producto
"""
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [
        product for product in products if product['name'] == product_name]
    if len(productFound) > 0:
        products.remove(productFound[0])
        return jsonify({'msg': 'Product deleted', 'products': products}), 200
    return jsonify({'msg': 'Product not found'}), 404

"""
GET  a la ruta productos pasando como parametro el nombre del producto
"""
@app.route('/products/<string:product_name>')
def method_name(product_name):
    products_found = [
        product for product in products if product['name'] == product_name]

    if not products_found:
        return jsonify({'msg': 'Product not found'}), 404
    return jsonify(products_found), 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'code': e.code,
        'name': e.name,
        'description': e.description,
        'msg': 'Ingresa una URL habilitada'
    }), 404