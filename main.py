from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/medingen'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    image = db.Column(db.String(255))
    salt_content = db.Column(db.String(255))price = db.Column(db.Float)
    reviews = db.Column(db.Text)

# API endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            "id": product.id,
            "name": product.name,
            "image": product.image,
            "salt_content": product.salt_content,
            "price": product.price,
            "reviews": product.reviews
        } for product in products
    ])
# Run the server
if __name__ == '__main__':
    app.run(debug=True)
