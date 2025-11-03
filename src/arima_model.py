import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error


def train_arima(train, test):
    """
    Train an ARIMA model (without pmdarima) and return forecast + model.
    Automatically tries a few (p, d, q) combinations to find the best fit.
    """

    print("🧠 Training ARIMA Model (manual tuning, no pmdarima)...")

    # Ensure index is datetime and has proper frequency
    train.index = pd.to_datetime(train.index)
    test.index = pd.to_datetime(test.index)
    train = train.asfreq('MS')
    test = test.asfreq('MS')

    best_aic = np.inf
    best_order = None
    best_model = None

    # Try different (p, d, q) combinations to find the best one
    for p in range(0, 4):
        for d in range(0, 3):
            for q in range(0, 4):
                try:
                    model = ARIMA(train, order=(p, d, q))
                    fitted = model.fit()
                    if fitted.aic < best_aic:
                        best_aic = fitted.aic
                        best_order = (p, d, q)
                        best_model = fitted
                except:
                    continue

    print(f"✅ Best ARIMA order found: {best_order}, AIC={best_aic:.2f}")

    # Forecast future values
    forecast = best_model.forecast(steps=len(test))

    # Evaluate
    mae = mean_absolute_error(test, forecast)
    rmse = np.sqrt(mean_squared_error(test, forecast))
    print(f"\n📊 ARIMA Model Performance:")
    print(f"   MAE : {mae:.2f}")
    print(f"   RMSE: {rmse:.2f}\n")

    # Plot results
    plt.figure(figsize=(10, 5))
    plt.plot(train.index, train, label='Train', color='blue')
    plt.plot(test.index, test, label='Test', color='green')
    plt.plot(test.index, forecast, label='ARIMA Forecast', color='red', linestyle='--')
    plt.title(f'ARIMA Forecast (order={best_order})')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/arima_forecast.png")
    plt.show()

    print("📈 ARIMA Forecast Plot Saved in 'results/arima_forecast.png'")

    return forecast, best_model
