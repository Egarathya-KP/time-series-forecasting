<<<<<<< HEAD
📊 Time Series Sales Forecasting — ARIMA vs SARIMA
🧠 Overview

This project focuses on forecasting future sales using Time Series Analysis techniques.
We implement and compare two statistical models — ARIMA (AutoRegressive Integrated Moving Average) and SARIMA (Seasonal ARIMA) — to determine which performs better for monthly sales prediction.

The project showcases the end-to-end forecasting pipeline, including:

Data loading and preprocessing

Exploratory Data Analysis (EDA)

Model training and evaluation

Forecast visualization and performance comparison

🗂️ Project Structure
time-series-forecasting/
│
├── data/
│   └── dataset.csv                 # Monthly sales dataset
│
├── results/
│   ├── arima_forecast.png          # ARIMA forecast
│   ├── sarima_forecast.png         # SARIMA forecast
│   └── combined_forecast.png       # ARIMA vs SARIMA comparison
│
├── src/
│   ├── data_loader.py              # Loads and preprocesses data
│   ├── eda.py                      # Performs EDA
│   ├── arima_model.py              # Trains ARIMA model
│   ├── sarima_model.py             # Trains SARIMA model
│   ├── evaluation.py               # Computes MAE & RMSE
│   └── visualization.py            # Handles forecast plotting
│
├── main.py                         # Main entry point
├── requirements.txt                # Dependencies
└── README.md

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/<your-username>/time-series-sales-forecasting.git
cd time-series-sales-forecasting

2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

3. Install Dependencies
pip install -r requirements.txt


📝 Note: If using Python 3.13, pmdarima may not install.
You can still run the project with statsmodels (works perfectly).

▶️ Run the Project
python main.py

📈 Results

The project generates:

Two forecast graphs:

arima_forecast.png

sarima_forecast.png

One combined comparison graph:

combined_forecast.png

Performance metrics file (metrics.txt) with:

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

Example Output:

📊 Model Evaluation Results:

ARIMA -> MAE: 78.83, RMSE: 84.23
SARIMA -> MAE: 1.64, RMSE: 2.73

🔍 Key Learnings

Handling time series data using Pandas

Forecasting using ARIMA and SARIMA models

Evaluating predictions using MAE and RMSE

Visualizing sales trends with Matplotlib

🧩 Tech Stack

Python 3.13

Pandas, NumPy, Statsmodels, Matplotlib

(Optional: pmdarima for Auto ARIMA tuning)

📚 Future Enhancements

Integrate Facebook Prophet or LSTM models

Add cross-validation for improved accuracy

Deploy as a Flask/Django web dashboard

🤝 Team Members
Name	Role	Contribution
Janarthanan M	Team Lead & Data Analyst	Dataset curation, preprocessing, and insights
Egarathya K P	Model Developer	Implemented ARIMA & SARIMA models, handled visualization
Kishore K	Evaluation & Testing	Computed MAE/RMSE, optimized model parameters
Archana A	Documentation & Reporting	Prepared report, README, and presentation content
=======
📊 Time Series Sales Forecasting — ARIMA vs SARIMA
🧠 Overview

This project focuses on forecasting future sales using Time Series Analysis techniques.
We implement and compare two statistical models — ARIMA (AutoRegressive Integrated Moving Average) and SARIMA (Seasonal ARIMA) — to determine which performs better for monthly sales prediction.

The project showcases the end-to-end forecasting pipeline, including:

Data loading and preprocessing

Exploratory Data Analysis (EDA)

Model training and evaluation

Forecast visualization and performance comparison

🗂️ Project Structure
time-series-forecasting/
│
├── data/
│   └── dataset.csv                 # Monthly sales dataset
│
├── results/
│   ├── arima_forecast.png          # ARIMA forecast
│   ├── sarima_forecast.png         # SARIMA forecast
│   └── combined_forecast.png       # ARIMA vs SARIMA comparison
│
├── src/
│   ├── data_loader.py              # Loads and preprocesses data
│   ├── eda.py                      # Performs EDA
│   ├── arima_model.py              # Trains ARIMA model
│   ├── sarima_model.py             # Trains SARIMA model
│   ├── evaluation.py               # Computes MAE & RMSE
│   └── visualization.py            # Handles forecast plotting
│
├── main.py                         # Main entry point
├── requirements.txt                # Dependencies
└── README.md

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/<your-username>/time-series-sales-forecasting.git
cd time-series-sales-forecasting

2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

3. Install Dependencies
pip install -r requirements.txt


📝 Note: If using Python 3.13, pmdarima may not install.
You can still run the project with statsmodels (works perfectly).

▶️ Run the Project
python main.py

📈 Results

The project generates:

Two forecast graphs:

arima_forecast.png

sarima_forecast.png

One combined comparison graph:

combined_forecast.png

Performance metrics file (metrics.txt) with:

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

Example Output:

📊 Model Evaluation Results:

ARIMA -> MAE: 78.83, RMSE: 84.23
SARIMA -> MAE: 1.64, RMSE: 2.73

🔍 Key Learnings

Handling time series data using Pandas

Forecasting using ARIMA and SARIMA models

Evaluating predictions using MAE and RMSE

Visualizing sales trends with Matplotlib

🧩 Tech Stack

Python 3.13

Pandas, NumPy, Statsmodels, Matplotlib

(Optional: pmdarima for Auto ARIMA tuning)

📚 Future Enhancements

Integrate Facebook Prophet or LSTM models

Add cross-validation for improved accuracy

Deploy as a Flask/Django web dashboard

🤝 Team Members

Janarthanan M	
Egarathya K P	
Kishore K	
Archana A	
>>>>>>> 5eb9c8b (Save local changes before pulling)
