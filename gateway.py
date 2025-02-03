from flask import Flask, jsonify
import requests

app = Flask(__name__)

USER_SERVICE_URL = "http://<VM2_IP>:5001"
PRODUCT_SERVICE_URL = "http://<VM3_IP>:5002"
ORDER_SERVICE_URL = "http://<VM4_IP>:5003"

@app.route('/users/<path:subpath>', methods=['GET', 'POST'])
def user_service(subpath):
    response = requests.request(
        method=request.method,
        url=f"{USER_SERVICE_URL}/{subpath}",
        headers=request.headers,
        data=request.get_data()
    )
    return response.content, response.status_code

@app.route('/products/<path:subpath>', methods=['GET', 'POST'])
def product_service(subpath):
    response = requests.request(
        method=request.method,
        url=f"{PRODUCT_SERVICE_URL}/{subpath}",
        headers=request.headers,
        data=request.get_data()
    )
    return response.content, response.status_code

@app.route('/orders/<path:subpath>', methods=['GET', 'POST'])
def order_service(subpath):
    response = requests.request(
        method=request.method,
        url=f"{ORDER_SERVICE_URL}/{subpath}",
        headers=request.headers,
        data=request.get_data()
    )
    return response.content, response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
