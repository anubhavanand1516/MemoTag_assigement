from flask import Blueprint, jsonify
from app.services import (
    generate_sales_recommendations,
    generate_sales_strategies,
    generate_marketing_funnels,
    load_sales_data
)

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Welcome to Memotag Flask API"})

@main.route('/sales_recommendations')
def sales_recommendations():
    recommendations = generate_sales_recommendations()
    return jsonify({"sales_recommendations": recommendations})

@main.route('/sales_strategies')
def sales_strategies():
    strategies = generate_sales_strategies()
    return jsonify({"sales_strategies": strategies})

@main.route('/marketing_funnels')
def marketing_funnels():
    funnels = generate_marketing_funnels()
    return jsonify({"marketing_funnels": funnels})

@main.route('/sales_data')
def sales_data():
    df = load_sales_data()
    if df is not None:
        return jsonify(df.to_dict(orient='records'))
    else:
        return jsonify({"error": "Sales data not found!"}), 404
