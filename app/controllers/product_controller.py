import base64
from flask import Blueprint, jsonify, request
from app.models.models import Product
from app.extensions.extensions import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/items/user/<string:userId>', methods=['GET'])
def get_products_by_user_id(userId):
    products = Product.query.filter_by(userId=userId).all()
    if not products:
        return jsonify({"message": "User not found or no products found"}), 404

    return jsonify({"message": "Products fetched successfully", "products": [product.to_dict() for product in products]}), 200



