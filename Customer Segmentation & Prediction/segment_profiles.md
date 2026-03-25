# Customer Segment Profiles

## Overview
| Segment | Count | Share (%) | Churn Rate |
|---------|-------|-----------|------------|
| At-Risk Customers | 130 | 26.0% | 14.0% |
| Loyal Savers | 119 | 23.8% | 6.0% |
| Premium Spenders | 251 | 50.2% | 11.0% |

---

## 1. Premium Spenders (50.2%)
**Description**: The largest and most valuable segment. Non-senior customers with the highest monthly charges and solid tenure.

| Metric | Value |
|--------|-------|
| Avg Tenure | 37.4 months |
| Avg Monthly Charges | $119.1 |
| Avg Total Charges | $4,201 |
| Senior Citizens | 0% |
| Churn Rate | 11.2% |

**Profile**: Long-term, high-value customers who are not senior citizens. They pay premium prices and tend to stay. Key risk factors include Month-to-month contracts and Electronic Check payments.

**Model Performance**: Accuracy 98.4% | F1 0.933 | ROC-AUC 0.995

---

## 2. At-Risk Customers (26.0%)
**Description**: Senior customers with mid-range charges but the highest churn rate in the cohort.

| Metric | Value |
|--------|-------|
| Avg Tenure | 36.0 months |
| Avg Monthly Charges | $107.5 |
| Avg Total Charges | $4,080 |
| Senior Citizens | 100% |
| Churn Rate | 13.8% |

**Profile**: All senior citizens in this segment. Despite reasonable tenure, they churn at the highest rate—likely due to pricing sensitivity, support needs, or contract flexibility.

**Model Performance**: Accuracy 100% | F1 1.000 | ROC-AUC 1.000

---

## 3. Loyal Savers (23.8%)
**Description**: Senior customers with the lowest churn rate—loyal despite similar charges to At-Risk customers.

| Metric | Value |
|--------|-------|
| Avg Tenure | 35.4 months |
| Avg Monthly Charges | $108.8 |
| Avg Total Charges | $4,488 (highest) |
| Senior Citizens | 100% |
| Churn Rate | 5.9% |

**Profile**: Senior customers who accumulate the highest total charges—meaning they've been customers longest or use more services. Despite being seniors, they are the most loyal segment. Tenure is the strongest predictor of retention.

**Model Performance**: Accuracy 93.3% | F1 0.000* | ROC-AUC 0.875
> *Low F1 due to very small churn class (7 churners in test set); AUC of 0.875 indicates strong discriminative ability.

---

## Key Insights
- **Tenure is the #1 predictor** of churn across ALL three segments (feature importance 0.52–0.69)
- **Senior citizens split into two very different groups**: loyal long-termers vs. high-risk churners
- **Premium Spenders** need contract upgrade incentives (month-to-month → annual)
- **At-Risk Customers** need proactive senior-targeted retention programs
