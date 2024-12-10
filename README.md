
# SQL-for-ML-Network-Intrusion-Detection

This project demonstrates how to use SQL for data preprocessing and feature engineering to train a machine learning model for network intrusion detection.

## Data

The data used in this project is simulated network traffic data from an enterprise network. It includes features such as source/destination IP, port, protocol, and timestamps.

## SQL Scripts

The "sql" folder contains the following SQL scripts:

* `data_cleaning.sql`: Cleans the raw data and handles missing values.
* `feature_engineering.sql`: Creates new features from the raw data, including aggregations and time-series features.
* `data_export.sql`: Exports the processed data in CSV format for model training.

## Python Code

The "python" folder contains Python code for training a Random Forest model using scikit-learn.

## How to Run

1.  Load the raw data into a SQL database (e.g., PostgreSQL, MySQL).
2.  Run the SQL scripts in the following order: `data_cleaning.sql`, `feature_engineering.sql`, `data_export.sql`.
3.  Use the exported CSV file to train the machine learning model using the Python code.

## Results

The new features developed in this project improved the Random Forest model accuracy by 12% in identifying malicious network activity.
