import lime
import lime.lime_tabular
import numpy as np
from sklearn.linear_model import LogisticRegression

def generate_lime_explanation(data):
    # Assume that the model is already trained
    model = LogisticRegression()
    model.fit(data['X_train'], data['y_train'])

    explainer = lime.lime_tabular.LimeTabularExplainer(data['X_train'].values,
                                                       mode='classification',
                                                       feature_names=data['feature_names'],
                                                       class_names=['Class 0', 'Class 1'],
                                                       discretize_continuous=True)
    
    # Get a single instance for explanation
    instance = data['X_test'].iloc[0]
    
    # Generate explanation
    explanation = explainer.explain_instance(instance, model.predict_proba)
    
    # Save explanation as HTML
    explanation.save_to_file('./results/outputs/lime_explanation.html')

    return explanation.as_html()

