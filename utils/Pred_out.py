import plotly.express as px
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# setting randoms state
tf.random.set_seed(42)

# Time series to LSTM data
def timeseries_to_supervised(data, lag=1):
    df = pd.DataFrame(data)
    columns = [df.shift(i) for i in range(1, lag+1)]
    columns.append(df)
    df = pd.concat(columns, axis=1)
    df.fillna(0, inplace=True)
    return df.to_numpy()

# reading data
df_train = pd.read_csv('data_9hr.csv')

# aggregatin data
df_train["datetime"] = pd.to_datetime(df_train["datetime"], format="%d/%m/%Y %H:%M")
df_train = df_train[["datetime", "ppl_out", "ppl_in"]].groupby(by="datetime").sum()
df_train["Net flow"] = df_train["ppl_in"] - df_train["ppl_out"]

pred_obj = "ppl_out"

# scaling data
scaler = MinMaxScaler(feature_range=(-1, 1))
scaled = scaler.fit_transform(df_train[[pred_obj]])

# train-test split
train_size = int(len(scaled) * 0.8)
test_size = len(scaled) - train_size
train, test = scaled[0:train_size,:], scaled[train_size:,:]

# LSTM dimensions
lag = 7
train_lagged = timeseries_to_supervised(train, lag)
X, y = train_lagged[:,0:-1], train_lagged[:,-1]
X = X.reshape(X.shape[0], 1, X.shape[1])

# Load trained model
saved_model = tf.keras.models.load_model('saved models')

# Prediction 
pred_all = timeseries_to_supervised(test, lag)
pred_X, y_true = pred_all[:,:-1], pred_all[:,-1]
pred_X_final = pred_X.reshape(pred_X.shape[0], 1, pred_X.shape[1])
y_hat = saved_model.predict(pred_X_final, batch_size=1)

# Plotting
real_y_hat = scaler.inverse_transform(y_hat)
prediction = pd.DataFrame({"pred_ppl_out":real_y_hat.reshape(len(real_y_hat))}, index=df_train[train_size:].index)
df_summary = pd.concat([df_train, prediction], axis=1)
df_summary["ppl_out"] = df_summary["ppl_out"][:train_size]


class Prediction():

    def out_pred():
        fig_out = px.line(df_summary[["ppl_out", "pred_ppl_out"]], title="Prediction and raw data plot (People outflow)")
        fig_out.update_xaxes(title="Time")
        fig_out.update_yaxes(title="People outflow")
        return fig_out
