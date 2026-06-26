# USA Sales Dashboard

An interactive Business Intelligence dashboard built with **Python**, **Streamlit**, and **Plotly** for exploring and analyzing the USA Sales dataset.

---

## Project Overview

This project aims to transform raw sales transaction data into meaningful business insights through interactive visualizations.

The dashboard enables users to:

- Monitor overall business performance
- Analyze sales and profit trends
- Explore regional performance
- Evaluate product and customer performance
- Examine operational efficiency
- Forecast future sales
- Perform custom interactive analysis

---

## 📂 Dataset

**Dataset Name**

USA Sales Dataset (Updated)

**Source**

https://www.kaggle.com/datasets/sulaimanahmed/sales-dataset-of-usa-updated

The dataset contains information such as:

- Order Date
- Ship Date
- Sales
- Profit
- Quantity
- Discount
- Category
- Sub-Category
- Product Name
- Region
- State
- City
- Customer Segment
- Ship Mode

---

# 🏗 Project Structure

```
sales_dashboard/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw/
│   │   └── usa_sales.csv
│   │
│   └── processed/
│       └── processed_sales.csv
│
├── preprocessing/
│   └── preprocess.py
│
├── utils.py
│
└── pages/
    ├── 1_Overview.py
    ├── 2_Geography.py
    ├── 3_Product_Analysis.py
    ├── 4_Customer_Analysis.py
    ├── 5_Operations.py
    ├── 6_Forecasting.py
    ├── 7_Custom_Analysis.py
    └── 8_Insights.py
```

---

# ⚙️ Data Processing Pipeline

The project follows a complete data processing pipeline before visualization.

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Missing Value Handling
      │
      ▼
Data Type Conversion
      │
      ▼
Feature Engineering
      │
      ▼
Processed Dataset
      │
      ▼
Dashboard Visualization
```

### Data Cleaning

- Remove duplicate records
- Handle missing values
- Convert date columns
- Remove invalid rows

### Feature Engineering

Additional features include:

- Year
- Month
- Quarter
- Shipping Days
- Profit Margin
- Loss Order

These engineered features improve analysis and visualization.

---

# 📊 Dashboard Pages

## 1. Executive Overview

Provides a high-level summary of business performance.

Visualizations

- KPI Cards
- Monthly Sales Trend
- Monthly Profit Trend
- Sales by Category
- Profit by Category
- Sales vs Profit Scatter Plot

---

## 2. Geography Analysis

Analyze regional performance.

Visualizations

- Sales by Region
- Profit by Region
- Top States by Sales
- Top Cities by Sales

---

## 3. Product Analysis

Evaluate product performance.

Visualizations

- Profit by Sub-Category
- Treemap
- Top Products by Sales
- Bottom Products by Profit

---

## 4. Customer Analysis

Understand customer purchasing behavior.

Visualizations

- Sales by Segment
- Profit by Segment
- Top Customers

---

## 5. Operations Analysis

Evaluate logistics efficiency.

Visualizations

- Average Shipping Days by Ship Mode

---

## 6. Forecasting

Predict future sales using Prophet.

Visualizations

- Historical Sales
- Forecast Sales

---

## 7. Custom Analysis

Interactive analysis where users choose:

- Metric
- Dimension

The dashboard automatically generates the appropriate visualization.

Supported metrics

- Sales
- Profit
- Quantity
- Shipping Days

Supported dimensions

- Category
- Region
- Segment
- State
- City
- Ship Mode
- Order Date

---

## 8. Insights

Summarizes important findings and recommendations.

---

# 📈 Visualization Techniques

The dashboard applies several visualization techniques.

| Visualization | Purpose |
|---------------|----------|
| KPI Cards | Business Summary |
| Line Chart | Trend Analysis |
| Bar Chart | Category Comparison |
| Scatter Plot | Relationship Analysis |
| Treemap | Hierarchical Data |
| Pie Chart | Composition Analysis |
| Forecast Chart | Time Series Prediction |

---

# 🛠 Technologies Used

- Python 3
- Streamlit
- Plotly Express
- Plotly Graph Objects
- Pandas
- NumPy
- Prophet
- Scikit-learn

---


## Install required packages

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

### Step 1

Run the preprocessing script

```bash
python preprocessing/preprocess.py
```

This generates the cleaned dataset:

```
data/processed/processed_sales.csv
```

---

### Step 2

Launch the Streamlit dashboard

```bash
streamlit run app.py
```

The dashboard will open automatically in your browser.

Default address:

```
http://localhost:8501
```

---

# 📌 Dashboard Features

- Interactive sidebar filters
- Dynamic charts
- KPI Cards
- Time series analysis
- Geographic analysis
- Product analysis
- Customer analysis
- Forecasting
- Custom visualization
- Responsive layout

---

# 📖 Business Questions Answered

The dashboard helps answer questions such as:

- How do sales evolve over time?
- Which regions generate the highest revenue?
- Which products are the most profitable?
- Which products generate losses?
- Which customer segment contributes the most?
- Which shipping method is most efficient?
- What are the projected future sales?

---

# 👥 Authors

Group Project

Course: Information Visualization

Developed using Python, Streamlit, and Plotly.

---

