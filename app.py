from flask import Flask, jsonify, request
from pathlib import Path
import json

app = Flask(__name__)
DATA_FILE = Path("data/api_customers.json")
DATA_FILE.parent.mkdir(exist_ok=True)

def load_customers():
    return json.loads(DATA_FILE.read_text()) if DATA_FILE.exists() else []

def save_customers(customers):
    DATA_FILE.write_text(json.dumps(customers, indent=2))

@app.get("/health")
def health():
    return jsonify({"status": "UP"})

@app.get("/customers")
def get_customers():
    customers = load_customers()
    city = request.args.get("city")
    if city:
        customers = [c for c in customers if c.get("city", "").lower() == city.lower()]
    return jsonify(customers)

@app.get("/customers/<int:customer_id>")
def get_customer(customer_id):
    customer = next((c for c in load_customers() if c["customer_id"] == customer_id), None)
    if customer is None:
        return jsonify({"error": "Customer not found"}), 404
    return jsonify(customer)

@app.post("/customers")
def create_customer():
    data = request.get_json(silent=True)
    required = ["customer_id", "customer_name", "email", "city", "state"]
    if not data or any(k not in data for k in required):
        return jsonify({"error": "Missing required fields"}), 400
    customers = load_customers()
    if any(c["customer_id"] == data["customer_id"] for c in customers):
        return jsonify({"error": "Customer already exists"}), 409
    customers.append(data)
    save_customers(customers)
    return jsonify(data), 201

@app.put("/customers/<int:customer_id>")
def update_customer(customer_id):
    data = request.get_json(silent=True) or {}
    customers = load_customers()
    for i, customer in enumerate(customers):
        if customer["customer_id"] == customer_id:
            updated = {**customer, **data, "customer_id": customer_id}
            customers[i] = updated
            save_customers(customers)
            return jsonify(updated)
    return jsonify({"error": "Customer not found"}), 404

@app.delete("/customers/<int:customer_id>")
def delete_customer(customer_id):
    customers = load_customers()
    filtered = [c for c in customers if c["customer_id"] != customer_id]
    if len(filtered) == len(customers):
        return jsonify({"error": "Customer not found"}), 404
    save_customers(filtered)
    return "", 204

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
