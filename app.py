from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect('ims.db')
    conn.row_factory = sqlite3.Row
    return conn

# API to get all products (inventory items)
@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM product').fetchall()
    conn.close()
    
    return jsonify([dict(item) for item in items])

# API to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    conn = get_db_connection()
    conn.execute('INSERT INTO product (Supplier, Category, name, price, qty, status) VALUES (?, ?, ?, ?, ?, ?)', 
                 (data['Supplier'], data['Category'], data['name'], data['price'], data['qty'], data['status']))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Product added successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
