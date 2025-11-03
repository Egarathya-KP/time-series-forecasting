import os
import sys
import pandas as pd

# Add src folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.data_loader import load_dataset
from src.arima_model import train_arima
from src.sarima_model import train_sarima
from src.visualization import plot_forecasts
from src.evaluation import evaluate_models

# ==========================
# Load dataset
# ==========================
data = load_dataset(os.path.join("data", "dataset.csv"))

print("✅ Dataset Loaded Successfully!")
train_size = int(len(data) * 0.8)
train, test = data.iloc[:train_size], data.iloc[train_size:]
print(f"Training size: {len(train)}, Testing size: {len(test)}")

# ==========================
# ARIMA model
# ==========================
print("\n📈 Training ARIMA model...")
arima_forecast, arima_model = train_arima(train['Sales'], test['Sales'])
print("✅ ARIMA model trained successfully!")

# ==========================
# SARIMA model
# ==========================
print("\n🧠 Training SARIMA model...")
sarima_forecast, sarima_model = train_sarima(train['Sales'], steps=len(test))

print("✅ SARIMA model trained successfully!")

# ==========================
# Evaluation
# ==========================
print("\n📉 Evaluating models...\n")
results = evaluate_models(test['Sales'], arima_forecast, sarima_forecast)
print("📊 Model Evaluation Results:\n", results)

# ==========================
# Visualization
# ==========================
os.makedirs("results", exist_ok=True)
plot_forecasts(train, test, arima_forecast, sarima_forecast, "results/")

print("\n✅ Forecasting Completed! Check 'results' folder for graphs.")
