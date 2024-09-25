import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(filepath):
    """Loads the CSV dataset from the given filepath."""
    return pd.read_csv(filepath)

def preprocess_data(data):
    """Preprocesses the data for the model."""
    # Example: Assuming 'target' is the column to predict and rest are features
    X = data.drop(columns='target')
    y = data['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return {
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test,
        'feature_names': X.columns
    }
