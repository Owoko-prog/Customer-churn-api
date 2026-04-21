import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv(r"C:\Users\Administrator\Downloads\WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Drop ID column
df.drop("customerID", axis=1, inplace=True)

# Fix TotalCharges column
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Encode categorical columns
for column in df.columns:
    if df[column].dtype == "object":
        df[column] = LabelEncoder().fit_transform(df[column])

# Split dataset
X = df.drop("Churn", axis=1)
y = df["Churn"]
print(X.columns.tolist())
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "churn_model.pkl")

print("Model saved successfully")
print(X.columns.tolist())