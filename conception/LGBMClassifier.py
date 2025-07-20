import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
from lightgbm import LGBMClassifier
# from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import joblib

from imblearn.over_sampling import SMOTE

up = 3

class_2 = r"Data\class_2\dataset_with_extra_ft.xlsx"

class_3 = r"Data\class_3\dataset_with_extra_ft.xlsx"

class_4 = r"Data\class_4\dataset_with_extra_ft.xlsx" 

# Load dataset
rl = pd.read_excel(class_2)

# Create lag features
lag_cols = ['volume %', 'chng %', 'price_vs_sma']
for col in lag_cols:
    for lag in range(1, up):  # 3 lag periods
        rl[f'{col}_lag_{lag}'] = rl[col].shift(lag)

# Drop rows with missing values caused by lag
rl.dropna(inplace=True)

# Feature and target columns
feature_cols = [
    'Volume'

]

# Add lag features to feature list
for col in lag_cols:
    for lag in range(1, up):
        feature_cols.append(f'{col}_lag_{lag}')

# Define X and y
X = rl[feature_cols]
y = rl["direction_class"]

sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_res, y_res, test_size=0.2, random_state=42, stratify=y_res
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define XGBoost model
model = LGBMClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=3,
    num_leaves=15,
    reg_alpha=1.0,
    reg_lambda=2.0,
    subsample=0.7,
    colsample_bytree=0.7,
    random_state=42
)

# Train the model
model.fit(X_train_scaled, y_train)

# Evaluate
X_test_df = pd.DataFrame(X_test_scaled, columns=X.columns)
y_pred = model.predict(X_test_df)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
X_train_df = pd.DataFrame(X_train_scaled, columns=X.columns)
train_pred = model.predict(X_train_df)
print("Train Accuracy:", accuracy_score(y_train, train_pred))


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
joblib.dump(model, "LGBM_1.pkl")
