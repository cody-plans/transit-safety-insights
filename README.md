# 🚀 Transit Safety Insights

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-supported-informational.svg)](https://en.wikipedia.org/wiki/SQL)

## 📚 Project Overview

This project seeks to uncover the key predictors of major safety incidents that occur in the US. Our goal is to support data-driven decisions for stakeholders such as Public Safety Organizations, Transit Authorities, and City Planners by identifying patterns and risk factors that contribute to serious safety events.

### 🔍 Research Questions
What factors are most predictive of a major safety incident occurring?

We will use classification modeling to assess which variables are most indicative of major incidents, and may also explore regression techniques to understand the severity or frequency of incidents, depending on time and data availability. Techniques like Principal Component Analysis (PCA) will help with dimensionality reduction and model efficiency. The dataset that will be used to train this model is a major safety event that is provided by the US Department of Transportation with events from 2014-2024.

#### Objectives
- Identify critical factors leading to major safety incidents
- Inform safety improvements and resource deployment
- Support planning to minimize transit disruptions and improve public safety

#### Assumptions & Risks
- Dataset has sufficient quality and structure to train accurate models
- Risk of incomplete or missing data that could affect predictive accuracy
- No unstructured data is currently being processed that could enhance the model


## 👥 Team Members

- **Louis Chuk**
- **Stephen Fong**
- **Mychelle Wong**
- **Nithursan Elamuhilan**

## 📋 Task List & Workflow

1. **Data Acquisition:**  
   - Download and inspect the dataset from the [source](https://data.transportation.gov/Public-Transit/Major-Safety-Events/9ivb-8ae9/about_data).

2. **Data Cleaning:**  
   - Handle missing values, data inconsistencies, and convert data types.
   - Remove or impute outliers.

3. **Data Processing & Feature Engineering:**  
   - Extract relevant features (e.g., time of day, weather conditions, transit type).
   - Create new variables to capture trends and patterns.

4. **Exploratory Data Analysis (EDA):**  
   - Generate descriptive statistics.
   - Visualize data distributions, correlations, and trends using graphs and charts.

5. **Model Building:**  
   - **Regression Models:** Predict the severity of incidents.
   - **Classification Models:** Identify key factors predicting major safety incidents.

6. **Model Fine Tuning & Evaluation:**  
   - Apply cross-validation and hyperparameter tuning.
   - Evaluate model performance using appropriate metrics.

7. **Visualization & Reporting:**  
   - Create informative visualizations.
   - Summarize findings and recommend further research directions.

## 🛠️ Tech Stack

- **Python:** Data cleaning, processing, analysis, and model building.
- **SQL:** Data querying and management.

## ⚙️ Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your_username/transit-safety-insights.git
   cd transit-safety-insights
2. **Download the Dataset:**

A CLI script has been provided to download the dataset into the `data` folder automatically.

### Using the CLI Script

**Script Location:**  
The download script is located at `scripts/download_data.py`.

**Run the script using python:**  
```bash
python scripts/download_data.py
