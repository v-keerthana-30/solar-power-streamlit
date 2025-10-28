## 📂 Project Structure

solar-power-project/
│
├─ data/
│    └─ solarpowergeneration.csv
│
├─ notebooks/
│    ├─ 1_EDA.ipynb
│    ├─ 2_Model_Building.ipynb
│    └─ 3_Model_Evaluation.ipynb
│
├─ models/
│    └─ best_model_rf.pkl
│
├─ app/
│    └─ app.py
│
├─ requirements.txt
└─ README.md

***

###  Solar Power Generation Data Analysis (Regression Project)

### 📌 **Project Overview**
This project focuses on analyzing and predicting solar power generation based on various environmental factors. Using regression techniques, it aims to model the relationship between weather parameters and energy output to enhance power forecasting accuracy and support efficient energy management.

***

### 🎯 **Objectives**
The main goals of this analysis are to:

* Identify key environmental factors influencing solar power output.
* Perform Exploratory Data Analysis (EDA) to uncover data patterns and trends.
* Build and evaluate regression models for energy prediction.
* Visualize the relationship between variables like temperature, wind speed, and humidity with power generation.
* Support sustainable energy planning through data-driven insights.

***

### 🧠 **Analytical Sections & Sample Insights**
1️⃣ **Data Understanding & Cleaning**

* Loaded and explored the *solarpowergeneration.csv* dataset with 10 variables and 2920 instances.
* Handled missing values, standardized data, and checked for data consistency.

2️⃣ **Exploratory Data Analysis (EDA)**

* Visualized relationships among temperature, humidity, and power generation.
* Observed that solar power peaks near solar noon with clear sky conditions.
* Identified strong correlations between sky cover and energy output.

3️⃣ **Model Building & Evaluation**

* Implemented multiple regression models to predict *power_generated* (target).
* Compared model performances based on RMSE and R² metrics.
* Selected the best-performing regression model for deployment.

4️⃣ **Result Interpretation & Insights**

* Temperature and solar noon proximity were the most significant predictors.
* High humidity and dense sky cover led to reduced energy production.
* Model achieved strong predictive accuracy, supporting reliable power forecasting.

***

### ⚙️ **Tools & Technologies**

* **Programming Language:** Python
* **Libraries Used:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
* **Dataset:** `solarpowergeneration.csv`
* **Type:** Regression Project

***

### 🧾 **How to Run the Project**

1. Open the Jupyter Notebook or Python file.
2. Load the dataset (`solarpowergeneration.csv`).
3. Execute each code cell to perform EDA, model building, and evaluation.
4. Review plots and metrics for insights and predictions.
   
Streamlit Link: https://solar-power-app-zmtxuaeaigwvasls727hfa.streamlit.app/
