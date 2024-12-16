# Muscle Monitoring Project

This project provides a solution for muscle monitoring using an Arduino and a machine learning classification model. The system acquires electromyographic (EMG) data in two distinct conditions: resting state and muscle contraction state, and uses this data to make real-time predictions about the muscle contraction state.

The methodology and algorithm implemented in this project were utilized in the research study **"Human-to-Human Knowledge Transfer using Functional Electrical Stimulation"**, published at the **2020 IEEE International Conference on Systems, Man, and Cybernetics (SMC)**. You can access the paper [here](https://ieeexplore.ieee.org/abstract/document/9283319).

---

## Project Structure

The project is organized as follows:

```
EMGModelsPrediction/
├── data/                   # Raw and processed data files
│   ├── datos_contraccion_1687770256.csv
│   ├── datos_rest_1687770256.csv
│   └── features.csv
├── notebooks/              # Jupyter notebooks for exploratory analysis
├── src/                    # Source code for the project
│   ├── data_processing/    # Scripts for data acquisition and processing
│   │   ├── csvgenerator.py
│   │   ├── features.py
│   │   └── cortarcsv.py
│   ├── model_training.py   # Training and evaluation of machine learning models
│   └── real_time_classification.py  # Real-time EMG classification
├── tests/                  # Unit tests
├── scripts/                # Standalone utility scripts
├── models/                 # Saved machine learning models (.pkl files)
├── README.md               # Documentation for the project
└── requirements.txt        # Python dependencies
```

---

## Hardware Setup

### Components:
- **Arduino**: Used to interface with EMG sensors, enabling data acquisition from muscle activity.
- **EMG Sensor**: Measures electrical activity produced by muscle movements. Signals are amplified and filtered before being sent to the Arduino.
- **Electrodes**: Surface electrodes capture muscle activity. Proper placement is crucial for minimizing noise and ensuring reliable signal acquisition.

### Connections:
1. Connect the EMG sensor to the Arduino following the sensor’s documentation.
2. Place the electrodes on the desired muscle group (active electrode, ground, and reference).
3. Connect the Arduino to your computer via USB.

---

## How to Use

### 1. Install Dependencies
Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

### 2. Running the Project

#### Step 1: Data Acquisition
Run the script `csvgenerator.py` to record EMG data during resting and contraction cycles. The script will prompt you to alternate between resting and contracting your muscles for specific time intervals. The recorded data will be saved in the `data/` folder as CSV files.

#### Step 2: Feature Extraction
Run the script `features.py` to process the raw data and extract features such as:
- **Standard Deviation**: Variability of the signal.
- **Mean**: Average value of the signal.
- **Amplitude**: Difference between maximum and minimum values.
- **Periodogram**: Power spectral density estimation.

This will generate a combined dataset (`features.csv`) in the `data/` folder.

#### Step 3: Model Training
Run `model_training.py` to train and evaluate three machine learning models (e.g., Random Forest, Decision Tree). The best-performing model will be saved as a `.pkl` file in the `models/` folder.

#### Step 4: Real-Time Classification
Run `real_time_classification.py` to classify muscle activity in real time. This script:
1. Acquires EMG signals via serial communication.
2. Extracts features from the incoming data.
3. Uses the pre-trained model to predict the muscle state (resting or contracting).

---

## Files and Scripts

### 1. Data Files (`data/`):
- `datos_contraccion_1687770256.csv`: EMG data for muscle contraction.
- `datos_rest_1687770256.csv`: EMG data for resting state.
- `features.csv`: Extracted features for model training.

### 2. Main Scripts (`src/`):
- **`csvgenerator.py`**: Records EMG data during rest and contraction cycles.
- **`features.py`**: Extracts statistical features from raw EMG data.
- **`model_training.py`**: Trains and evaluates classification models.
- **`real_time_classification.py`**: Performs real-time muscle activity classification.

---

## Testing

Add unit tests for the scripts in the `tests/` directory to ensure functionality. These tests can validate data processing, feature extraction, and model predictions.

---

## Additional Information

This project demonstrates the potential for combining hardware and machine learning to monitor muscle activity effectively. It showcases its applicability in real-world scenarios, including healthcare and rehabilitation.

For more details, refer to the paper on IEEE: [Human-to-Human Knowledge Transfer using Functional Electrical Stimulation](https://ieeexplore.ieee.org/abstract/document/9283319).

---

## License

This project is open-source and available under the [MIT License](LICENSE).
