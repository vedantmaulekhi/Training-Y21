import numpy as np
import pandas as pd


def evaluate():
    # Input the csv file
    """
    Sample evaluation function
    Don't modify this function
    """
    df = pd.read_csv('sample_input.csv')
     
    actual_close = np.loadtxt('sample_close.txt')
    
    pred_close = predict_func(df)
    
    # Calculation of squared_error
    actual_close = np.array(actual_close)
    pred_close = np.array(pred_close)
    mean_square_error = np.mean(np.square(actual_close-pred_close))


    pred_prev = [df['Close'].iloc[-1]]
    pred_prev.append(pred_close[0])
    pred_curr = pred_close
    
    actual_prev = [df['Close'].iloc[-1]]
    actual_prev.append(actual_close[0])
    actual_curr = actual_close

    # Calculation of directional_accuracy
    pred_dir = np.array(pred_curr)-np.array(pred_prev)
    actual_dir = np.array(actual_curr)-np.array(actual_prev)
    dir_accuracy = np.mean((pred_dir*actual_dir)>0)*100

    print(f'Mean Square Error: {mean_square_error:.6f}\nDirectional Accuracy: {dir_accuracy:.1f}')
    

    

def predict_func(data):
    # Importing required libraries
    import math
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler
    import tensorflow as tf
    from tensorflow import keras
    from keras.models import load_model
    from tensorflow import keras

    from keras.models import Sequential
    from keras.layers import LSTM
    from keras.models import load_model

    # Loading the pre-trained LSTM model
    model = load_model('stock_prediction5.h5')


    # Interpolating missing values in the 'Close' column
    close_prices = data['Close']
    close_prices.interpolate(method='linear', inplace=True)

   


    # Scaling the 'Close' prices between 0 and 1
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_close_prices = scaler.fit_transform(np.array(close_prices).reshape(-1,1))

    
    x_input = scaled_close_prices.reshape(1, -1)
    #Reshapes the scaled_close_prices array to have dimensions (1, n) where n is the length of the array. 
    
    x_input_shape = x_input.shape

    sequence_length = 50

    temp_input = list(x_input[0][-sequence_length:])

    #temp_input = list(x_input)
    #Converts the reshaped x_input array into a Python list and assigns it to the variable temp_input. 
    
    #temp_input = temp_input[0].tolist()
    #Since x_input is a 2D array with a single row, accessing temp_input[0] returns the list containing the sequence of input values.

    # Predicting the next two days' stock prices
    from numpy import array
    predicted_prices = []
    sequence_length = 50
    i = 0
    while i < 2:
        if len(temp_input) > sequence_length:
            sequence = np.array(temp_input[1:])
            sequence = sequence.reshape(1, -1)
            sequence = sequence.reshape((1, sequence_length, 1))
            predictions = model.predict(sequence, verbose=0)
            temp_input.extend(predictions[0].tolist())
            temp_input = temp_input[1:]
            predicted_prices.extend(predictions.tolist())
            i += 1
        else:
            sequence = x_input.reshape((1, sequence_length, 1))
            predictions = model.predict(sequence, verbose=0)
            temp_input.extend(predictions[0].tolist())
            predicted_prices.extend(predictions.tolist())
            i += 1

    # Scaling back the predicted stock prices to the original range
    predicted_prices = scaler.inverse_transform(predicted_prices).flatten().tolist()
    
    print(predicted_prices)
    return predicted_prices

# The code above defines the predict_func() function, which takes data as input, applies the trained model
# to predict the next two days' stock prices based on the 'Close' index, and returns the predictions.

if __name__ == "__main__":
    evaluate()


