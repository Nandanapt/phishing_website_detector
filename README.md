# phishing_website_detector
The goal of this project is to develop a machine learning-based system that can detect phishing websites.
## Overview
Phishing attacks are a growing threat to internet users, often tricking individuals into entering sensitive information on fraudulent websites. This project uses machine learning to detect phishing websites based on features extracted from their URLs. The model is trained on a dataset containing labeled URLs, and a Random Forest Classifier is used for classification.
# Model
The system uses a **Random Forest Classifier** to predict whether a given URL is phishing or legitimate based on these features.
# Prediction:
After training, the model can predict whether a new URL is phishing or legitimate based on the same features extracted during training.

# how to run
first run  **python model_training.py** in the terminal and it automatically saved model.pkl
secondly run **python app.py**,in app.py you will get a link in the terminal ,after you click the link directly you get a webpage where you can test whether it is a ral or fake website

Note:Download the dataset from the kaggle and paste it in dataset.csv

![image](https://github.com/user-attachments/assets/d54f537c-e2b8-4de0-ba21-e1c810e3d969)
![image](https://github.com/user-attachments/assets/6d2976b9-64f3-4120-9668-d80a203e2232)

check out the images to know more about it.
