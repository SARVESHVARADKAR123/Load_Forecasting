"# Load_Forecasting" 
connected to dagshub acc

project/
├── data/                  # Raw and processed data
│   ├── raw/               # Raw input data (e.g., holidays.csv, load data)
│   ├── processed/         # Processed data with features
├── models/                # Saved impact and LSTM models
├── src/                   # Scripts for each pipeline stage
│   ├── preprocess.py      # Preprocessing script
│   ├── train_impact.py    # Impact model training
│   ├── train_lstm.py      # LSTM training
│   ├── predict.py         # Prediction script
├── dvc.yaml               # DVC pipeline configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
