import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

def train_and_save_model():
    # Load the dataset
    data = pd.read_csv('./data/sample_dataset.csv')
    
    # Split data into features and target
    X = data.drop(columns='target')
    y = data['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a simple logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Save the trained model
    joblib.dump(model, './models/saved_models/logistic_regression_model.pkl')
    
    print("Model trained and saved successfully.")
    
if __name__ == "__main__":
    train_and_save_model()
