# 🚀 Transit Safety Insights

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-supported-informational.svg)](https://en.wikipedia.org/wiki/SQL)

## 📚 Project Overview

This repository contains an exploratory data analysis project on the **Major Safety Events** dataset from [data.transportation.gov](https://data.transportation.gov/Public-Transit/Major-Safety-Events/9ivb-8ae9/about_data). Our goal is to explore and analyze public transit safety incidents, uncover patterns, and build predictive models.

### 🔍 Research Questions

- **Regression:**  
  Do factors like time of day, weather conditions, and type of transit service predict the severity of safety incidents (e.g., number of injuries or fatalities)?

- **Classification:**  
  What factors are most predictive of a major safety incident occurring?

## 👥 Team Members

- **Louis Chuk**
- **Stephen Fong**
- **Mychelle Wong**
- **Nithursan Elamuhilan**

## Dataset ##
This dataset consolidates transit-safety reports from multiple agencies. Each record captures essential details such as date, time, location, involved vehicles, environmental conditions, and the severity of injuries and fatalities. Combining these data points offers a comprehensive view of transit incidents and provides opportunities for analysis on vehicle operations, safety measures, passenger risk, and other critical factors that can inform decision-making and research on transit system improvements.

## File Contents

- **Major_Safety_Events_20250313.csv**: Main dataset in CSV format.

### Key Columns (list what was kept*)

| Column Name                                | Description                                                                                                     |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `Event Date`                               | Date the incident occurred.                                                                                     |
| `Event Type`                               | Type of incident (e.g., Collision, Derailment, Fire).                                                           |
| `Transit Vehicle Action`                   | Action of the transit vehicle at the time (e.g., Going Straight, Stopped, Making a turn).                       |
| `Non-Transit Vehicle Action List`          | Action(s) of other vehicle(s) involved (e.g., Going straight, Changing lanes).                                   |
| `Total Injuries`                           | Number of injuries caused by the event.                                                                          |
| `Total Fatalities`                         | Number of fatalities caused by the event.                                                                        |
| `Property Damage`                          | Estimated property damage amount.                                                                                |
| `Weather`                                  | Weather conditions (e.g., Clear, Rain).                                                                          |
| `Location Type`                            | General location classification (e.g., Intersection, Stop, Station).                                             |
| `Transit Worker Assault Flag`              | Indicator for assaults on transit personnel.                                                                     |
| `Other Transit Vehicle Action Description` | Additional details about the vehicle's movement (e.g., “Side Impact,” “Rear-ended”).                             |


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
