import pandas as pd

# Load sales data
def load_sales_data():
    try:
        df = pd.read_csv("data/sales_data.csv")
        return df
    except FileNotFoundError:
        return None

# Generate sales recommendations
def generate_sales_recommendations():
    df = load_sales_data()
    if df is not None:
        top_selling = df.groupby('product')['sales'].sum().sort_values(ascending=False).head(3).index.tolist()
        return [
            f"Increase advertising for top-selling products: {', '.join(top_selling)}",
            "Offer targeted discounts based on purchase history",
            "Implement AI-based personalized product recommendations",
            "Leverage customer reviews to boost trust",
            "Use A/B testing to optimize pricing strategies",
            "Create limited-time exclusive bundles",
            "Improve website UX to reduce cart abandonment",
            "Expand into emerging markets based on sales trends",
            "Analyze competitor pricing and adjust accordingly",
            "Optimize inventory management to prevent stockouts"
        ]
    else:
        return ["No sales data available. Please upload data."]

# Generate sales strategies
def generate_sales_strategies():
    return [
        "Focus on upselling and cross-selling",
        "Enhance customer loyalty programs",
        "Improve the online shopping experience"
    ]

# Generate marketing funnels
def generate_marketing_funnels():
    return [
        "Create engaging lead magnets",
        "Use retargeting ads to convert visitors",
        "Develop an email nurture sequence",
        "Leverage social proof and testimonials",
        "Optimize landing pages for higher conversion rates"
    ]
