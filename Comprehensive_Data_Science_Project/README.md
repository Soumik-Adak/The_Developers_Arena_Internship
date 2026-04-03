# 📊 Business Intelligence & Predictive Analytics Suite

> **Capstone Data Science Project** — End-to-end ML pipeline covering customer churn prediction, real estate price estimation, and sales revenue analytics.

---

## 🎯 Project Overview

This project solves three real-world business problems using machine learning and data analytics:

| Problem | Type | Dataset | Key Metric |
|---|---|---|---|
| Customer Churn Prediction | Binary Classification | 500 customer records | ROC-AUC: **0.9939** |
| House Price Estimation | Regression | 300 property listings | R²: **0.9725** |
| Sales Revenue Analysis | Descriptive Analytics | 100 transactions | Total Revenue: ₹1.24 Cr |

---

## 📁 Repository Structure

```
capstone_project/
├── README.md                    ← You are here
├── capstone_project.py          ← Main end-to-end pipeline
├── requirements.txt             ← Python dependencies
│
├── data/                        ← Raw datasets
│   ├── customer_churn.csv
│   ├── house_prices.csv
│   └── sales_data.csv
│
├── src/                         ← Modular source code
│   ├── preprocessing.py         ← Data loading & feature engineering
│   └── model_training.py        ← Training, evaluation & persistence
│
├── reports/                     ← Documentation & results
│   ├── model_results.json       ← Quantitative model metrics
│   ├── technical_documentation.md
│   └── business_report.md
│
├── deployment/                  ← Production-ready API
│   ├── app.py                   ← Flask REST API (2 endpoints)
│   ├── churn_model.pkl          ← Serialized churn classifier
│   ├── scaler.pkl               ← Fitted StandardScaler
│   └── house_model.pkl          ← Serialized price regressor
│
└── presentation/                ← Stakeholder materials
    └── presentation.html        ← Interactive slide deck
```

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.9+
- pip

### 1. Clone & Install
```bash
git clone https://github.com/yourusername/capstone-project.git
cd capstone-project
pip install -r requirements.txt
```

### 2. Run the Full Pipeline
```bash
python capstone_project.py
```

### 3. Launch the Prediction API
```bash
cd deployment
python app.py
# API available at http://localhost:5000
```

### 4. Test the API
```bash
# Health check
curl http://localhost:5000/health

# Churn prediction
curl -X POST http://localhost:5000/predict/churn \
  -H "Content-Type: application/json" \
  -d '{"Tenure":6,"MonthlyCharges":80,"TotalCharges":500,
       "Contract":"Month-to-month","PaymentMethod":"Electronic check",
       "PaperlessBilling":"Yes","SeniorCitizen":0}'

# House price prediction
curl -X POST http://localhost:5000/predict/house_price \
  -H "Content-Type: application/json" \
  -d '{"Area":2500,"Bedrooms":3,"Bathrooms":2,"Age":10,
       "Location":"Urban","Property_Type":"House"}'
```

---

## 🏗️ Architecture

```
Raw CSV Data → Preprocessing (src/preprocessing.py)
                    ↓
            Feature Engineering
                    ↓
         Train/Test Split (80/20)
                    ↓
       Random Forest Models × 2
                    ↓
        Evaluation & Cross-Validation
                    ↓
       Serialized Models (.pkl files)
                    ↓
        Flask REST API (deployment/app.py)
```

---

## 📈 Model Performance

### Customer Churn Classifier (Random Forest)
| Metric | Value |
|---|---|
| ROC-AUC | **0.9939** |
| Accuracy | **96.0%** |
| F1-Score (Churn class) | **0.7778** |
| 5-Fold CV ROC-AUC | **0.9946 ± 0.0022** |

**Top Predictors:** TotalCharges > Tenure > MonthlyCharges > Contract type

### House Price Regressor (Random Forest)
| Metric | Value |
|---|---|
| R² | **0.9725** |
| MAE | ₹15,14,263 |
| RMSE | ₹19,78,881 |
| Mean Price in Dataset | ₹2.49 Cr |

**Top Predictors:** Area (sq ft) > Location > Age > Bedrooms

---

## 💡 Key Business Insights

### Churn
- **10.6% churn rate** — aligned with industry average
- Month-to-month contract customers churn **3× more** than two-year contracts
- Electronic check payers show significantly higher churn risk
- Customers with tenure < 12 months are the highest-risk cohort

### Real Estate
- **Urban properties** command a 40% premium over rural equivalents
- Each additional 100 sq ft adds approximately ₹4.5L to valuation
- Villas outperform Houses and Apartments at the same area
- Properties under 10 years old fetch a 20% age premium

### Sales
- **Laptops** are the top revenue product (₹38.9L, 31% of revenue)
- **North region** leads all four regions (₹39.8L)
- Peak sales observed in January — opportunity for Q1 campaign planning
- Average transaction value: ₹1.24L

---

## 🧪 Testing & Validation

**Data Quality:** All three datasets pass validation — zero missing values, zero duplicates.

**Model Validation Strategy:**
- 80/20 stratified train-test split
- 5-fold cross-validation on training set
- Hold-out test metrics reported above

**API Testing:** All endpoints tested with valid and invalid payloads. Error handling returns descriptive 400/500 responses.

---

## 🚀 API Reference

| Endpoint | Method | Description |
|---|---|---|
| `/health` | GET | Service status & loaded models |
| `/docs` | GET | Full API documentation |
| `/predict/churn` | POST | Predict customer churn risk |
| `/predict/house_price` | POST | Estimate property market value |

---

## 📚 Technologies Used

| Category | Tools |
|---|---|
| Language | Python 3.11 |
| ML Framework | scikit-learn 1.3 |
| Data Processing | pandas, numpy |
| API | Flask 3.0 |
| Model Serialization | joblib |
| Visualization | matplotlib, seaborn |

---

## 👤 Author

**Capstone Student**  
Data Science Program — April 2026  
📧 student@email.com | 🔗 linkedin.com/in/student | 💻 github.com/student
