from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from src.lime_explainer import generate_lime_explanation
from src.utils import load_data, preprocess_data

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './data'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('explain', filename=filename))
    return render_template('upload.html')

@app.route('/explain/<filename>', methods=['GET'])
def explain(filename):
    # Load and preprocess data
    data = load_data(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    processed_data = preprocess_data(data)

    # Generate LIME explanation
    lime_results = generate_lime_explanation(processed_data)

    return render_template('explanation.html', explanation=lime_results)

if __name__ == '__main__':
    app.run(debug=True)
