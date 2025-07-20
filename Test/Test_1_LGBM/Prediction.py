import pickle
import joblib


# with open("LGBM_1.pkl", "rb") as f:
#     model = pickle.load(f)


model = joblib.load("LGBM_1.pkl")

import pandas as pd

# Example: Single row of feature data
data = pd.DataFrame([{
    'volume %_lag_2': -58.64497614474195,
    'price_vs_sma_lag_1': 0.0006919959851742037,
    'chng %_lag_1': -9.205683091303275,
    'price_vs_sma_lag_2': 0.1091001644648946,
    'chng %_lag_2': 0.4706009291345792,
    'volume %_lag_1': 35.60172747542223,
    'Volume': 2251191709.0
}]
)


prediction = model.predict(data)
print("Prediction:", prediction)


