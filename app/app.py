
from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Yhteys tietokantaan
conn = psycopg2.connect("dbname=lumenpudotus user=postgres password=yourpassword")

@app.route('/orders', methods=['GET'])
def get_orders():
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders")
    orders = cur.fetchall()
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    user_id = request.json['user_id']
    order_date = request.json['order_date']
    start_time = request.json['start_time']
    end_time = request.json['end_time']
    
    cur = conn.cursor()
    cur.execute("INSERT INTO orders (user_id, order_date, start_time, end_time) VALUES (%s, %s, %s, %s)",
                (user_id, order_date, start_time, end_time))
    conn.commit()
    return jsonify({'status': 'Order created successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
