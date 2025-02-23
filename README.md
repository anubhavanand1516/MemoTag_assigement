# Memotag Flask API 🚀

## 📌 Overview
This Flask API analyzes sales data and product features to provide **sales recommendations, sales strategies, and marketing funnels**. It uses **data analysis** to generate unique and actionable insights.

---

## 💒 Folder Structure
```
Memotag-Flask-API/
│️── app/
│   ├── __init__.py        # Initializes the Flask app
│   ├── routes.py          # Defines API routes
│   ├── services.py        # Contains business logic and data processing
│   ├── models.py          # (Optional) Defines data structures
│️── data/
│   ├── sales_data.csv     # Sales dataset
│️── requirements.txt       # Python dependencies
│️── run.py                 # Entry point to start the Flask app
│️── README.md              # Project documentation
```

---

## 🛠 Dependencies

### **Install the required packages:**
```bash
pip install -r requirements.txt
```

### **`requirements.txt`**
```txt
Flask
pandas
```

---

## 🚀 How to Run the Project

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-repo/Memotag-Flask-API.git
cd Memotag-Flask-API
```

### **Step 2: Create a Virtual Environment & Activate**
```bash
python -m venv venv
```
- Windows (CMD): `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Verify `sales_data.csv` Exists**
```bash
ls data/
```

### **Step 5: Run the Flask App**
```bash
python run.py
```

### **Step 6: Access API Endpoints**
- **Base URL:** `http://127.0.0.1:5000/`
- **Sales Recommendations:** `http://127.0.0.1:5000/sales_recommendations`
- **Sales Strategies:** `http://127.0.0.1:5000/sales_strategies`
- **Marketing Funnels:** `http://127.0.0.1:5000/marketing_funnels`
- **Sales Data:** `http://127.0.0.1:5000/sales_data`

---

## 📌 API Endpoints Documentation

### **1⃣ Home (`/`)**
- **Method:** `GET`
- **Response:**
```json
{
    "message": "Welcome to Memotag Flask API"
}
```

### **2⃣ Sales Recommendations (`/sales_recommendations`)**
- **Method:** `GET`
- **Response:** 10 unique sales recommendations based on data.

### **3⃣ Sales Strategies (`/sales_strategies`)**
- **Method:** `GET`
- **Response:** 3 unique sales strategies.

### **4⃣ Marketing Funnels (`/marketing_funnels`)**
- **Method:** `GET`
- **Response:** 5 marketing funnels.

### **5⃣ Sales Data (`/sales_data`)**
- **Method:** `GET`
- **Response:** Raw sales data in JSON format.

## 📌 Summary
| Endpoint | Description |
|----------|-------------|
| `/` | Home - API Welcome Message |
| `/sales_recommendations` | Returns 10 unique sales recommendations |
| `/sales_strategies` | Returns 3 sales strategies |
| `/marketing_funnels` | Returns 5 marketing funnels |
| `/sales_data` | Returns raw sales data in JSON format |

---

