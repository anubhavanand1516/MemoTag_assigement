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
python main.py
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
<img width="1440" alt="Screenshot 2025-02-23 at 2 01 22 PM" src="https://github.com/user-attachments/assets/5046c339-5388-4f56-8737-342af90f8b5c" />


### **2⃣ Sales Recommendations (`/sales_recommendations`)**
- **Method:** `GET`
- **Response:** 10 unique sales recommendations based on data.
<img width="1439" alt="Screenshot 2025-02-23 at 2 01 59 PM" src="https://github.com/user-attachments/assets/2a61eee5-a47b-41a7-80fe-cb36dce5e6b9" />


### **3⃣ Sales Strategies (`/sales_strategies`)**
- **Method:** `GET`
- **Response:** 3 unique sales strategies.
<img width="1438" alt="Screenshot 2025-02-23 at 2 02 31 PM" src="https://github.com/user-attachments/assets/5d5df54c-f6fc-4a21-b3d1-b1733c0c41de" />


### **4⃣ Marketing Funnels (`/marketing_funnels`)**
- **Method:** `GET`
- **Response:** 5 marketing funnels.
<img width="1440" alt="Screenshot 2025-02-23 at 2 03 00 PM" src="https://github.com/user-attachments/assets/05fca6ad-c844-4633-9693-404f4de13d86" />


### **5⃣ Sales Data (`/sales_data`)**
- **Method:** `GET`
- **Response:** Raw sales data in JSON format.
<img width="1440" alt="Screenshot 2025-02-23 at 2 03 40 PM" src="https://github.com/user-attachments/assets/32771754-4ed8-4a6c-96fa-a21e1da1b6ab" />


## 📌 Summary
| Endpoint | Description |
|----------|-------------|
| `/` | Home - API Welcome Message |
| `/sales_recommendations` | Returns 10 unique sales recommendations |
| `/sales_strategies` | Returns 3 sales strategies |
| `/marketing_funnels` | Returns 5 marketing funnels |
| `/sales_data` | Returns raw sales data in JSON format |

---

