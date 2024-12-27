import joblib

def load_model(filename='sentiment_model.pkl'):
    return joblib.load(filename)

def save_model(model, filename='sentiment_model.pkl'):
    joblib.dump(model, filename)
