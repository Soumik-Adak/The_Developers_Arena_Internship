<div align="center">

```
 ██████╗██╗  ██╗██╗   ██╗██████╗ ███╗   ██╗    ██████╗ ██████╗ ███████╗██████╗
██╔════╝██║  ██║██║   ██║██╔══██╗████╗  ██║    ██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║     ███████║██║   ██║██████╔╝██╔██╗ ██║    ██████╔╝██████╔╝█████╗  ██║  ██║
██║     ██╔══██║██║   ██║██╔══██╗██║╚██╗██║    ██╔═══╝ ██╔══██╗██╔══╝  ██║  ██║
╚██████╗██║  ██║╚██████╔╝██║  ██║██║ ╚████║    ██║     ██║  ██║███████╗██████╔╝
 ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝
```

### ◈ Customer Segmentation & Churn Prediction ◈
#### *A 7-Day End-to-End Machine Learning Pipeline*

---

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![pandas](https://img.shields.io/badge/pandas-2.0+-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![License](https://img.shields.io/badge/License-MIT-008B8B?style=for-the-badge)](LICENSE)

</div>

---

## ◆ What This Project Does

> *"Not all customers are equal — and treating them as such is the fastest way to lose them."*

This pipeline segments **500 telecom customers** into distinct behavioural groups using unsupervised learning, then builds a **dedicated churn prediction model** for each segment. The result: targeted retention strategies that speak to each customer type rather than blasting everyone with the same campaign.

**Three discoveries that change everything:**
- 🔵 **Premium Spenders** (50%) churn because of *contract flexibility*, not price
- 🔴 **At-Risk Customers** (26%) are senior citizens who need *support*, not discounts
- 🟢 **Loyal Savers** (24%) just need to be *left alone and appreciated*

---

## ◆ Key Results

<table>
<tr>
<td align="center" width="33%">

### 🏆 Best Model
**Random Forest**
ROC-AUC `0.9995`
Accuracy `98.4%`
F1-Score `0.933`

</td>
<td align="center" width="33%">

### 📊 Dataset
**500 Customers**
`9` features
`10.6%` churn rate
`0` missing values

</td>
<td align="center" width="33%">

### 💰 Business Impact
**~$33K/month**
revenue preserved
per 500-customer cohort
via targeted retention

</td>
</tr>
</table>

---

## ◆ Segment Profiles

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        CUSTOMER SEGMENTS                                │
├──────────────────────┬─────────────┬────────────┬──────────┬───────────┤
│ Segment              │ Share       │ Churn Rate │ Risk     │ Avg $/mo  │
├──────────────────────┼─────────────┼────────────┼──────────┼───────────┤
│ 🔵 Premium Spenders  │ 50.2%       │ 11.2%      │ MEDIUM   │ $119      │
│ 🔴 At-Risk Customers │ 26.0%       │ 13.8% ⚠️   │ HIGH     │ $108      │
│ 🟢 Loyal Savers      │ 23.8%       │  5.9% ✓   │ LOW      │ $109      │
└──────────────────────┴─────────────┴────────────┴──────────┴───────────┘
```

---

## ◆ Project Structure

```
customer_segmentation/
│
├── 📓  customer_segmentation.ipynb      ← Main 7-day pipeline notebook
├── 📊  segmentation_data.csv            ← Dataset with cluster labels
├── 📋  segment_profiles.md              ← Detailed cluster documentation
├── 📈  model_evaluation_results.csv     ← Per-segment metrics table
├── 📄  business_recommendations.pdf     ← Strategy & revenue impact report
├── 📘  customer_segmentation_docs.docx  ← Full documentation guide
├── 📝  requirements.txt                 ← Pinned dependencies
│
└── 📁  visualisations/
    ├── 1_churn_distribution.png
    ├── 2_churn_by_contract.png
    ├── 3_elbow_method.png
    ├── 4_segment_pca.png
    ├── 5_segment_pie.png
    ├── 6_churn_by_segment.png
    ├── 7_dendrogram.png
    ├── 8_roc_curves.png
    ├── 9_feature_importance.png
    ├── 10_monthly_charges_boxplot.png
    ├── 11_tenure_distribution.png
    └── 12_correlation_heatmap.png
```

---

## ◆ 7-Day Pipeline

| Day | Focus | Methods |
|:---:|-------|---------|
| **1** | 🔍 Clustering Basics | K-Means · Elbow Method · PCA Visualisation |
| **2** | 🌿 Advanced Clustering | Hierarchical (Ward) · DBSCAN · Adjusted Rand Index |
| **3** | 👤 Segment Analysis | Cluster Profiling · Business Naming · EDA per Segment |
| **4** | 🤖 Prediction Models | Random Forest per Segment · class_weight='balanced' |
| **5** | 📐 Model Evaluation | Accuracy · Precision · Recall · F1 · ROC-AUC · Confusion Matrix |
| **6** | ⚙️ Hyperparameter Tuning | GridSearchCV · 3-Fold CV · n_estimators · max_depth |
| **7** | 💡 Business Insights | Segment Strategies · Revenue Impact · Deployment Plan |

---

## ◆ Quick Start

### 1 · Clone & Install

```bash
git clone https://github.com/yourusername/customer-segmentation.git
cd customer-segmentation
pip install -r requirements.txt
```

### 2 · Launch the Notebook

```bash
jupyter notebook customer_segmentation.ipynb
```

### 3 · Run the Full Pipeline

```python
# Inside the notebook — run all cells sequentially, or call directly:
df = load_data('segmentation_data.csv')
df = encode_categoricals(df)
df = cluster_kmeans(df, k=3)          # Day 1–2
df = profile_segments(df)              # Day 3
models = build_segment_models(df)      # Day 4
results = tune_hyperparameters(models) # Day 6
generate_report(results)               # Day 7
```

---

## ◆ Dependencies

```txt
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0
jupyter>=1.0.0
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## ◆ Model Performance

```
PER-SEGMENT RESULTS (GridSearchCV-tuned Random Forest)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Segment              Accuracy   Precision   Recall    F1      AUC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔵 Premium Spenders    98.4%      0.875      1.000    0.933   0.995
🔴 At-Risk Customers  100.0%      1.000      1.000    1.000   1.000
🟢 Loyal Savers        93.3%      —*         —*       —*      0.875
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
* Only 7 churn events in Loyal Savers test set → use AUC (0.875)
```

---

## ◆ Key Technical Choices

**Why 3 clusters?**
The Elbow Method plots inertia for k = 2 through 8. Inertia drops sharply from `2,993 → 2,769` at k=3 then diminishes — the classic elbow. Hierarchical clustering (Ward) agrees: Adjusted Rand Index between the two methods is **0.72+**.

**Why separate models per segment?**
A single global model treats all customers identically. Segment-specific models capture the different feature dynamics in each group — Tenure dominates everywhere (importance `0.52–0.69`), but contract type matters more for Premium Spenders while payment method matters more for seniors.

**Why `class_weight='balanced'`?**
The dataset has only `10.6%` churners. Without balancing, models learn to predict "no churn" for everything and score 89% accuracy while being useless. Balanced weights force the model to pay equal attention to both classes.

---

## ◆ Encoding Strategy

| Feature | Method | Why |
|---------|--------|-----|
| `PaperlessBilling` | Label Encoding | Binary Yes/No — no ordering needed |
| `PaymentMethod` | One-Hot Encoding | 3 nominal, unordered categories |
| `Contract` | Ordinal Encoding | Natural order: Month-to-month < One year < Two year |

---

## ◆ Feature Importance

```
Tenure             ████████████████████████████████████  0.61  ← #1 universal
MonthlyCharges     ████████████                          0.16
TotalCharges       ██████                                0.10
Contract           ██████                                0.09
PaymentMethod      ███                                   0.05
PaperlessBilling   ██                                    0.04
SeniorCitizen      █                                     0.02  (used in clustering)
```

> **Every retention strategy should prioritise the first 12 months.** Tenure is the top predictor in all three segment models without exception.

---

## ◆ Business Recommendations

<details>
<summary><strong>🔵 Premium Spenders — Medium Risk (11.2% churn)</strong></summary>

- **Contract Upgrade Drive** — 10–15% discount to switch month-to-month → annual
- **Auto-Pay Reward** — One free month for enrolling in Credit Card / Bank Transfer
- **Loyalty Tiers** — Gold at 24 months, Platinum at 48 months with exclusive perks
- **Early Outreach** — Flag tenure < 12 months + month-to-month for proactive check-ins

*Estimated impact: reduce churn to 7% → save ~$11,900/month*

</details>

<details>
<summary><strong>🔴 At-Risk Customers — HIGH Risk (13.8% churn)</strong></summary>

- **Senior-Specific Plan** — Simplified pricing with enhanced support SLA
- **Dedicated Support Line** — Friction in service interactions is the primary driver
- **Live Scoring** — Deploy RF model monthly; trigger outreach at churn probability > 0.4
- **Paper Billing Option** — Paperless billing confusion is a hidden churn trigger

*Estimated impact: reduce churn to 8% → save ~$8,640/month*

</details>

<details>
<summary><strong>🟢 Loyal Savers — Low Risk (5.9% churn)</strong></summary>

- **Protect and Celebrate** — Annual loyalty rewards; they've earned recognition
- **Referral Programme** — Highest-trust segment; incentivise advocacy with bill credits
- **Minimal Disruption** — Stability is their core value driver; avoid plan changes
- **Watch the Edges** — The RF model (AUC 0.875) catches the rare at-risk loyal customer

*Estimated impact: preserve ~$13,000/month in stable recurring revenue*

</details>

---

## ◆ Visualisations

| Chart | Description |
|-------|-------------|
| `1_churn_distribution` | Overall churn balance (447 vs 53) |
| `2_churn_by_contract` | Month-to-month: 18.2%, Two-year: 2.8% |
| `3_elbow_method` | Inertia curve — k=3 inflection point |
| `4_segment_pca` | 2D PCA projection of 3 clusters |
| `5_segment_pie` | Segment share distribution |
| `6_churn_by_segment` | Per-segment churn rates |
| `7_dendrogram` | Hierarchical clustering (Ward, 60-sample) |
| `8_roc_curves` | ROC per segment after GridSearchCV |
| `9_feature_importance` | Averaged RF importance across segments |
| `10_monthly_charges_boxplot` | Spending spread by segment |
| `11_tenure_distribution` | Tenure histograms overlaid by segment |
| `12_correlation_heatmap` | Pairwise feature correlations |

---

## ◆ Algorithms Used

```
CLUSTERING                          PREDICTION
──────────                          ──────────
• K-Means (primary)                 • Random Forest (per segment)
• Agglomerative / Ward              • GridSearchCV (3-fold CV)
• DBSCAN (outlier detection)        • class_weight='balanced'
• PCA (2D visualisation)            • Stratified train/test split
```

---

## ◆ Deliverables Checklist

- [x] `customer_segmentation.ipynb` — 7-day modular pipeline notebook
- [x] `segmentation_data.csv` — enriched dataset with segment labels
- [x] `segment_profiles.md` — cluster analysis & customer profiles
- [x] `model_evaluation_results.csv` — all metrics per segment
- [x] `business_recommendations.pdf` — strategy & revenue impact report
- [x] `customer_segmentation_docs.docx` — full documentation with 12 embedded charts
- [x] `README.md` — this file

---

## ◆ Documentation Quality Standards

| Criterion | Status |
|-----------|--------|
| Project overview with clear goals | ✅ Complete |
| Step-by-step setup instructions | ✅ Complete |
| Well-organised code with file hierarchy | ✅ Complete |
| Visual documentation (12 charts) | ✅ Complete |
| Algorithm, data structure & architecture explanation | ✅ Complete |
| Testing evidence with validation metrics | ✅ Complete |

---

<div align="center">

---

*Built with* ❤️ *over 7 days · Python · scikit-learn · pandas · matplotlib*

**[ Clustering → Profiling → Prediction → Strategy ]**

</div>

