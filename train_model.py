import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load the processed data
data = pd.read_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/processed_network_traffic.csv', low_memory=False)

# Separate features (X) and target variable (y)
X = data.drop(data.columns[10], axis=1)  # Drop the 11th column (index 10)
y = data[data.columns[10]]              # Select the 11th column (index 10)

# --- Feature Encoding ---

# One-Hot Encoding for categorical features
categorical_features = [X.columns[4], X.columns[5], X.columns[13]]  # Get column names
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_features = encoder.fit_transform(X[categorical_features])  # Use column names directly
encoded_df = pd.DataFrame(encoded_features)
X = pd.concat([X, encoded_df], axis=1)
X.drop(categorical_features, axis=1, inplace=True)  # Drop original columns

# Label Encoding for the target variable
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# --- Continue with model training ---

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Print a classification report for more detailed evaluation
print(classification_report(y_test, y_pred))