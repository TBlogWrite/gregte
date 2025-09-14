import pandas as pd
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from flask import Flask, request, jsonify


# ======================
# 1. TẠO MÔ HÌNH LSTM
# ======================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "number_lucky.csv")
df = pd.read_csv(file_path)

sequence = []
for col in df.columns[1:]:   # bỏ cột đầu (ví dụ cột Ngày/Tháng)
    for idx, val in enumerate(df[col].values):
        if pd.notna(val) and val > 0:  # có số xuất hiện
            sequence.extend([idx] * int(val))  # lặp lại theo Count

def create_dataset(seq, look_back=5):
    X, y = [], []
    for i in range(len(seq) - look_back):
        X.append(seq[i:i+look_back])
        y.append(seq[i+look_back])
    return np.array(X), np.array(y)

look_back = 5
X, y = create_dataset(sequence, look_back)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

model = Sequential()
model.add(LSTM(64, input_shape=(look_back, 1)))
model.add(Dense(1, activation="linear"))
model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=5, batch_size=16, verbose=0)

# ======================
# 2. FLASK API
# ======================
app = Flask(__name__)

@app.route("/predict", methods=["GET"])
def predict():
    last_sequence = sequence[-look_back:]
    input_seq = np.reshape(last_sequence, (1, look_back, 1))
    predicted = model.predict(input_seq, verbose=0)
    predicted_number = int(predicted[0][0] * 100) % 100
    return jsonify({"prediction": predicted_number})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
