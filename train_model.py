from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pickle

# Dummy model - in the real world, train with historical data
def train_model():
    # Train a basic random forest model with dummy data
    X = np.random.rand(100, 4)
    y = np.random.rand(100)
    model = RandomForestRegressor()
    model.fit(X, y)
    with open('model.pkl', 'wb') as file:
        pickle.dump(model, file)

def predict_yield(data):
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model.predict(np.array([list(data.values())]).reshape(1, -1))[0]

train_model()
