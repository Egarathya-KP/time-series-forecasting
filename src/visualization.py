import matplotlib.pyplot as plt
import os

def plot_forecasts(train, test, arima_forecast, sarima_forecast, save_dir="results"):
    plt.style.use("seaborn-v0_8")

    # 1️⃣ Plot ARIMA Forecast
    plt.figure(figsize=(10, 5))
    plt.plot(train.index, train['Sales'], label='Train Data', color='blue')
    plt.plot(test.index, test['Sales'], label='Actual Test Data', color='black')
    plt.plot(test.index, arima_forecast, label='ARIMA Forecast', color='red', linestyle='--')
    plt.title("ARIMA Forecast Results")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, "arima_forecast.png"))
    plt.show()

    # 2️⃣ Plot SARIMA Forecast
    plt.figure(figsize=(10, 5))
    plt.plot(train.index, train['Sales'], label='Train Data', color='blue')
    plt.plot(test.index, test['Sales'], label='Actual Test Data', color='black')
    plt.plot(test.index, sarima_forecast, label='SARIMA Forecast', color='green', linestyle='--')
    plt.title("SARIMA Forecast Results")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, "sarima_forecast.png"))
    plt.show()

    # 3️⃣ Combined Comparison Plot
    plt.figure(figsize=(10, 5))
    plt.plot(train.index, train['Sales'], label='Train Data', color='blue')
    plt.plot(test.index, test['Sales'], label='Actual Test Data', color='black')
    plt.plot(test.index, arima_forecast, label='ARIMA Forecast', color='red', linestyle='--')
    plt.plot(test.index, sarima_forecast, label='SARIMA Forecast', color='green', linestyle='--')
    plt.title("ARIMA vs SARIMA Forecast Comparison 📊")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, "combined_forecast.png"))
    plt.show()
