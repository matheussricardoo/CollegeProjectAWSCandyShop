"""In-memory academic catalog and order API.

Academic project by Matheus Ricardo; local demonstration, not a production service.
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

products_db = [
    {"id": 1, "name": "Brigadeiro Gourmet", "category": "doce", "flavor": "chocolate", "price": 3.50, "stock": 25},
    {"id": 2, "name": "Beijinho Premium", "category": "doce", "flavor": "coco", "price": 3.50, "stock": 20},
    {"id": 3, "name": "Torta de Chocolate", "category": "torta", "flavor": "chocolate", "price": 45.00, "stock": 5},
    {"id": 4, "name": "Torta de Morango", "category": "torta", "flavor": "morango", "price": 48.00, "stock": 3},
    {"id": 5, "name": "Quindim", "category": "doce", "flavor": "coco", "price": 4.00, "stock": 15},
    {"id": 6, "name": "Pudim de Leite", "category": "doce", "flavor": "caramelo", "price": 35.00, "stock": 8},
    {"id": 7, "name": "Torta de Limão", "category": "torta", "flavor": "limão", "price": 42.00, "stock": 2},
    {"id": 8, "name": "Trufa de Chocolate", "category": "doce", "flavor": "chocolate", "price": 2.50, "stock": 50},
]

next_order_id = 1
orders_db = []

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "Candy Shop API",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/products')
def get_all_products():
    return jsonify({
        "products": products_db,
        "total": len(products_db)
    })

@app.route('/api/products/lowstock')
def get_lowstock_products():
    try:
        threshold = int(request.args.get('threshold', 10))
        if threshold < 0:
            raise ValueError
    except (TypeError, ValueError):
        return jsonify({"error": "threshold must be a non-negative integer"}), 400
    products = [p for p in products_db if p['stock'] <= threshold]
    return jsonify({"products": products, "count": len(products), "threshold": threshold})


from threading import Lock
inventory_lock = Lock()


@app.route('/api/orders', methods=['POST'])
def create_order():
    global next_order_id
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not isinstance(data.get('items'), list) or not data['items']:
        return jsonify({"error": "items must be a non-empty array"}), 400
    customer = data.get('customer', {})
    if not isinstance(customer, dict):
        return jsonify({"error": "customer must be an object"}), 400
    quantities = {}
    for item in data['items']:
        if not isinstance(item, dict):
            return jsonify({"error": "Each item must be an object"}), 400
        product_id = item.get('product_id')
        quantity = item.get('quantity', 1)
        if type(product_id) is not int or type(quantity) is not int or quantity <= 0:
            return jsonify({"error": "product_id must be an integer and quantity a positive integer"}), 400
        quantities[product_id] = quantities.get(product_id, 0) + quantity

    with inventory_lock:
        order_items = []
        for product_id, quantity in quantities.items():
            product = next((p for p in products_db if p['id'] == product_id), None)
            if product is None:
                return jsonify({"error": f"Product {product_id} not found"}), 404
            if product['stock'] < quantity:
                return jsonify({"error": f"Insufficient stock for {product['name']}"}), 400
            order_items.append({
                "product_id": product_id, "product_name": product['name'],
                "quantity": quantity, "unit_price": product['price'],
                "subtotal": round(product['price'] * quantity, 2),
            })
        for product in products_db:
            product['stock'] -= quantities.get(product['id'], 0)
        order = {
            "id": next_order_id, "customer": customer, "items": order_items,
            "total": round(sum(item['subtotal'] for item in order_items), 2),
            "created_at": datetime.now().isoformat(),
        }
        orders_db.append(order)
        next_order_id += 1
    return jsonify({"success": True, "order": order}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25000, debug=False)
