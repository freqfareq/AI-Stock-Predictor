import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import joblib

# Load dataset
rl = pd.read_excel("Data\dataset_with_3Class_nlg.xlsx")

# Create lag features
lag_cols = ['Close', 'volume %', 'chng %', 'percent_b', 'price_vs_sma', 'future_target_1wk']
for col in lag_cols:
    for lag in range(1, 4):  # 3 lag periods
        rl[f'{col}_lag_{lag}'] = rl[col].shift(lag)

# Drop rows with missing values caused by lag
rl.dropna(inplace=True)

# Feature and target columns
feature_cols = [
    'Open', 'future_target_1wk_lag_3', 'Middle Band',
    'Upper Band', 'Close_lag_3', 'Lower Band', 'Low', 'Close_lag_2', 'sma_20'
]

# Add lag features to feature list
# for col in lag_cols:
#     for lag in range(1, 4):
#         feature_cols.append(f'{col}_lag_{lag}')

# Define X and y
X = rl[feature_cols]
y = rl["direction_class"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define XGBoost model
model = XGBClassifier(
    n_estimators=150,
    learning_rate=0.1,
    max_depth=5,
    subsample=0.8,
    colsample_bytree=0.8,
    use_label_encoder=False,
    eval_metric='mlogloss',
    random_state=42
)

# Train the model
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Feature importance plot
importances = model.feature_importances_
feat_names = X.columns
sorted_idx = importances.argsort()

plt.figure(figsize=(12, 6))
plt.barh(range(len(importances)), importances[sorted_idx], align='center')
plt.yticks(range(len(importances)), feat_names[sorted_idx])
print(f"features ?? {feat_names[sorted_idx]}")

plt.title("Feature Importances - XGBoost")
plt.tight_layout()
plt.show()

# Save the model
joblib.dump(model, "XGBoostSTM_2.pkl")
