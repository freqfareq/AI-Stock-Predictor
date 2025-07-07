import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import joblib


rl = pd.read_excel("reliance_1wk_BollingerBands.xlsx")
# rl.dropna(inplace=True) #dropping nulls if there

feature_cols=['Close', 'High', 'Low', 'Open', 'Volume','20 SMA', 'SD', 'Upper Band', 'Middle Band', 'Lower Band',
    'chng %', 'volume %', 'sma_20', 'price_vs_sma', 'percent_b']

X=rl[feature_cols]
Y=rl["direction_class"]

X_train , X_test, Y_train,Y_test = train_test_split(X,Y , test_size=0.2, random_state=42,stratify=Y) # training and testing the data 

scaler = StandardScaler()
X_train_scaled= scaler.fit_transform(X_train)
X_test_scaled= scaler.transform(X_test) # feature scaling 


model = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    random_state=42,
    class_weight='balanced'  # Optional: handles class imbalance
)

model.fit(X_train_scaled, Y_train) #making random forest 


y_pred = model.predict(X_test_scaled)

print("Classification Report:\n", classification_report(Y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(Y_test, y_pred))  # evaluate the model 



importances = model.feature_importances_
feat_names = X.columns
sorted_idx = importances.argsort()

plt.figure(figsize=(10, 6))
plt.barh(range(len(importances)), importances[sorted_idx], align='center')
plt.yticks(range(len(importances)), feat_names[sorted_idx])
plt.title("Feature Importances - Random Forest")
plt.show()  # important features selection 

joblib.dump(model, "random_forest_model.pkl") #saving the model 





