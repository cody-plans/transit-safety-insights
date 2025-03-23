# 🚀 Transit Safety Insights on Major Safety Events in the US

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-supported-informational.svg)](https://en.wikipedia.org/wiki/SQL)

As part of the Machine Learning Certificate program at the University of Toronto’s Data Science Institute, this project allowed us to apply the skills and knowledge gained throughout the program to a real-world problem. We focused on analyzing major safety events within U.S. transit systems to uncover key risk factors and generate actionable insights. This end-to-end project involved data preparation, applying machine learning techniques, and delivering findings to support informed decision-making for stakeholders aiming to enhance transit safety nationwide.

## University of Toronto | Data Science Institute Presentation Showcase
- Our project summarized in 5 minutes is available
- Presentaion slide are available [here](https://docs.google.com/presentation/d/1demXXfDs7kidJ94kQZ-SZ2-DHwst0ReC_PmsrZXU8-c/edit?usp=sharing)

## 👥 Team Members

- **Louis Chuk**
- **Stephen Fong**
- **Mychelle Wong**
- **Nithursan Elamuhilan**


## 📚 Project Overview

## 💼 Business Case

Transportation is the backbone of our communities - it connects peoples to jobs, services and our loved ones. A safe, reliable and efficient transit system supports public safety, boosts the economy and improves everyday life for everyone. In the United States alone, over 98,000 major safety events were reported between 2014 - 2024. To ensure the safety of all those making their daily travels on the transit systems in the US, this project seeks to uncover the key predictors of major safety incidents that occur. Our goal is to support data-driven decisions for stakeholders such as Public Safety Organizations, Transit Authorities, and City Planners by identifying patterns and risk factors that contribute to serious safety events.

### 🔍 Research Questions
What factors are most predictive of a major safety incident occurring?

To address this, we will implement classification models to determine which variables most strongly indicate the likelihood of a major incident. Time permitting, we may also explore regression models to analyze incident severity or frequency. Techniques such as Principal Component Analysis (PCA) will be employed to reduce dimensionality and improve model performance.

The dataset used in this analysis is sourced from the U.S. Department of Transportation and contains records of major safety events from 2014 to 2024.

#### Objectives
- Identify critical factors leading to major safety incidents
- Inform safety improvements and resource deployment
- Support planning to minimize transit disruptions and improve public safety

#### Assumptions & Risks
- Dataset has sufficient quality and structure to train accurate models
- Risk of incomplete or missing data that could affect predictive accuracy
- No unstructured data is currently being processed that could enhance the model

## 🛠️ Tech Stack

- **Python:** Data cleaning, processing, analysis, and model building.
- **SQL:** Data querying and management.



## Data Description ##
The National Transit Database maintained by the Federal Transit A requires that transit authorities complete a “Major Event Report” when significant safety events occur

This dataset consolidates transit-safety reports from multiple agencies. Each record captures essential details such as date, time, location, involved vehicles, environmental conditions, and the severity of injuries and fatalities. Combining these data points offers a comprehensive view of transit incidents and provides opportunities for analysis on vehicle operations, safety measures, passenger risk, and other critical factors that can inform decision-making and research on transit system improvements.



### Predictor Variables

| Column Name                              | Description                                                                                                                                                                                                                                                                            |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **NTD ID**                               | A five-digit identifying number for each agency used in the current NTD system.                                                                                                                                                                                                        |
| **Primary UZA UACE Code**               | The Census Bureau's Urban Area Census Code (UACE). This five-digit code uniquely identifies an urban area and remains unchanged from census to census.                                                                                                                                 |
| **Rail/Bus/Ferry**                      | Groups modes based on whether they are: Rail, Running Non-Rail Surface Transportation, or Ferryboat.                                                                                                                                                                                   |
| **Mode Name**                            | A system for carrying transit passengers described by specific right-of-way (ROW), technology, and operational features.                                                                                                                                                               |
| **Mode**                                 | Abbreviation of mode name.                                                                                                                                                                                                                                                             |
| **TOS**                                  | Abbreviation for “Type of Service.” Describes how public transportation services are provided by the transit agency: directly operated (DO) or purchased transportation (PT, TX, TN).                                                                                                 |
| **Fixed Route Flag**                     | Fixed Route Flag                                                                                                                                                                                                                                                                       |
| **Year**                                 | The calendar year in which the event occurred.                                                                                                                                                                                                                                         |
| **Event Date**                           | The date on which the event occurred.                                                                                                                                                                                                                                                  |
| **Event Time**                           | The actual time of day the event occurred.                                                                                                                                                                                                                                              |
| **Event Type**                           | The type of event that occurred.                                                                                                                                                                                                                                                        |
| **Event Type Group**                     | A derived column to allow users to filter based on broader event type (e.g., Collision, Derailment, Assault).                                                                                                                                                                          |
| **Transit Worker Type**                  | Indicates whether the person assaulted is a transit operator, other transit worker, not a transit worker, or not specified. Only applies to assaults.                                                                                                                                    |
| **Transit Worker Assault Detail Type**   | Identifies the type of assault on a transit worker as physical, non-physical, or not specified. Only applies to assaults.                                                                                                                                                               |
| **Transit Worker Assault Flag**          | When the value is True, the event is reported as an Assault on Transit Worker of any type. Otherwise, the value is false. Note, the value will appear as False for all events prior to 2023.                                                                                           |
| **Safety/Security**                      | Identifier of a Safety (SFT) or Security (SEC) Event. A safety event is a collision, derailment, fire, hazardous material spill, act of nature, evacuation, or OSONOC meeting NTD thresholds. A security event includes bomb threats, arson, assaults, and other security-related incidents.      |
| **Collision With**                       | Identifies what the transit vehicle collided with (e.g., Motor Vehicle, Fixed Object, Person, Animal, Vessel, etc.).                                                                                                                                                                    |
| **Property Damage**                      | Non-rail mode: The estimated dollar value of all property damaged in a Reportable Event, including transit-owned property and other involved property (excluding personal belongings like cell phones).                                                                                 |
| **Total Injuries**                       | Total number of involved injuries as a result of the event.                                                                                                                                                                                                                             |
| **Total Fatalities**                     | Total number of involved fatalities as a result of the event.                                                                                                                                                                                                                           |
| **Towed (Y/N)**                          | Identifier of collisions where a transit or non-transit roadway vehicle was towed away from the scene due to disabling damage.                                                                                                                                                          |
| **Number of Transit Vehicles Involved**  | Identifies the number of transit vehicles involved in the event.                                                                                                                                                                                                                       |
| **Number of Non-Transit Vehicles Involved** | Identifies the number of non-transit vehicles involved in the event.                                                                                                                                                                                                                  |
| **Number of Cars on Involved Transit Vehicles** | The number of rail cars on transit vehicle consists involved in the event.                                                                                                                                                                                                             |
| **Non-Transit Vehicle Type List**        | The list of types of non-transit vehicles involved in the event.                                                                                                                                                                                                                       |
| **Location Type**                        | Location of the event.                                                                                                                                                                                                                                                                 |
| **Latitude**                             | Geographic coordinate that specifies the north–south position of a point on Earth. NTD requires a minimum of 4 decimal places; if fewer are provided, the system pads out to 7 decimals.                                                                                                                                 |
| **Longitude**                            | Geographic coordinate that specifies the east–west position of a point on Earth. NTD requires a minimum of 4 decimal places; if fewer are provided, the system pads out to 7 decimals.                                                                                                                                    |
| **Weather**                              | Identifies the weather at the time of the event.                                                                                                                                                                                                                                       |
| **Lighting**                             | Identifies the indoor or outdoor lighting conditions at the time of the collision or derailment.                                                                                                                                                                                       |
| **Road Configuration**                   | Identifies the roadway configuration at the scene of a non-rail collision.                                                                                                                                                                                                              |
| **Path Condition**                       | Identifies the pathway (roadway) conditions for a non-rail collision.                                                                                                                                                                                                                   |
| **Right of Way Condition**               | Identifies the right-of-way conditions for non-rail or rail collision or rail derailment.                                                                                                                                                                                               |
| **Intersection Control Device**          | Identifies the intersection control device for a non-rail or rail collision.                                                                                                                                                                                                            |
| **Intentional (Y/N)**                    | Identifies if the security event was intentional or not.                                                                                                                                                                                                                                |
| **Transit Vehicle Action**               | Identifies the non-rail, ferry, or rail vehicle action at the time of the collision or derailment.                                                                                                                                                                                     |
| **Other Transit Vehicle Action Description** | Text explanation when “Other” is selected for the Transit Vehicle Action.                                                                                                                                                                                                              |
| **Non-Transit Vehicle Action List**      | Identifies the other vehicle action(s) at the time of the collision or derailment.                                                                                                                                                                                                      |
| **Transit (Y/N)**                        | Identifies which vehicles involved in the event are transit vehicles (Y) vs. non-transit (N).                                                                                                                                                                                           |
| **Fuel Type**                            | Identifies the type of fuel used to power the transit vehicle involved.                                                                                                                                                                                                                 |
| **Vehicle Speed**                        | Actual or estimated speed at the time of the collision or derailment.                                                                                                                                                                                                                   |
| **Transit Vehicle Type**                 | The form of passenger conveyance used for revenue operations (e.g., bus, heavy rail, commuter rail).                                                                                                                                                                                   |
| **Non-Transit Vehicle Type**             | A list of vehicle types for non-transit vehicles involved in the event.                                                                                                                                                                                                                 |
| **Transit Vehicle Manufacturer**         | Identifies the manufacturer of the transit vehicle for collisions.                                                                                                                                                                                                                     |
| **Total Serious Injuries**               | Sum of the count of all serious injuries for the given event.                                                                                                                                              

A CLI script has been provided to download the dataset into the `data` folder automatically.

### Using the CLI Script

**Script Location:**  
The download script is located at `scripts/download_data.py`.

**Run the script using python:**  
```bash
python scripts/download_data.py
```

## Methodology

## Findings
Extra Trees outperformed Bagging Classifier and Random Forest, likely due to its more reliable feature selection and ability to avoid overfitting. Extra Trees achieved the highest ROC-AUC score (0.87) compared to 0.81 for the Bagging Classifier and Random Forest 0.67. This stronger performance may be attributed to Extra Trees’ randomized split selection strategy which tends to reduce variance and overfitting particularly with complex data or imbalance datasets. Random Forest has the lowest ROC-AUC score of the three models, likely due to overfitting or its inability to address the dataset’s complexity.

The differences in feature importance across the models arise in how they handle feature selection, data complexity, correlated features and overfitting.

- Extra Trees (“Extremely Randomized Trees”) selects both features and split thresholds at random. This additional randomness lowers variance. This often results in a more balanced and less biased distribution of feature importance, helping uncover predictive features that other models may overlook
- Random Forest builds trees using random subsets of features at each split which can lead to overemphasis on correlated features. It is more sensitive to feature redundancy and my prioritize less informative features due to randomness in feature selection
- Bagging Classifier trains decision trees on different bootstrap samples, typically using all features at each split (unless otherwise specified). This results in more stable feature importance by producing more correlated trees. We tuned the Bagging Classifier using a grid search and applied class_weight = ‘balanced’ in the base estimator to address the datasets’ imbalance (with only ~5% of samples belonging to the minority class). Stratified sampling was used during cross-validation to maintain class proportions throughout training and evaluation - mitigating bias towards the majority class

Imbalanced settings, Extra Trees may provide more robust performance by identifying stronger predictors for the minority class. While Bagging and Random Forest can perform well, they are more prone to bias towards the majority class unless corrective measures (like class weights or resampling) are applied.
	
When discussing feature importance, impurity-based models (used by the three in our project) can be biased, particularly in the case of irrelevant or correlated features. As an alternative, permutation importance could be used to evaluate feature importance. It evaluates the decrease in a model’s importance when a feature’s values are randomly shuffled - it is less prone to biases caused by impurity-based methods in models. Importance derived from impurity-based methods can be high even for features that are not predictive of the target variable. 

![image](https://github.com/user-attachments/assets/02f46b76-963d-4e87-a1dc-d24dd68c53ba) 

![image](https://github.com/user-attachments/assets/d18b0dfc-f89b-4a84-8558-66ba6216f950)

![image](https://github.com/user-attachments/assets/24c8e49c-993c-4d5b-bb8e-5cc7cc4fa7ab)



![image](https://github.com/user-attachments/assets/67ad9b54-d851-445c-9112-42601c98c386)


## Conclusion

## 📋 Task List & Workflow

1. **Data Acquisition:**  
2. **Data Cleaning:**  
3. **Data Processing & Feature Engineering:**  
4. **Exploratory Data Analysis (EDA):**  
5. **Model Building:**  
6. **Model Fine Tuning & Evaluation:**  
7. **Visualization & Reporting:**  




