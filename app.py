from flask import Flask, request, render_template
from feature_extraction import extract_features
import joblib

app = Flask(__name__)

# Load your pre-trained model
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    # Extract features from the URL
    features = extract_features(url)
    
    # Predict using the model
    result = model.predict([features])[0]
    
    # Return the result
    output = "Phishing Website ⚠️" if result == 1 else "Legitimate Website ✅"
    
    # Pass the result to the result page
    return render_template('result.html', url=url, prediction=output, prediction_class='phishing' if result == 1 else 'legitimate')

if __name__ == '__main__':
    app.run(debug=True)
