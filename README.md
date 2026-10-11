
# Tipwise — Tip Estimator

A machine learning web application that predicts restaurant tips using an XGBoost model and Django.

**Live Demo:** https://tips-prediction-django-aap.onrender.com

**Tech Stack:** Python, Django, XGBoost, HTML, CSS

---

# python ml model deployment with django

A machine learning model deployment project using Python and Django. This project demonstrates how a trained ML model can be integrated with a Django web application to make predictions through a user-friendly interface.
## Create a readme.md file of your project

## 1. Create python environment

we will use python env to create the env.

'''bash
<!-- create a virtual environment -->
python -m venv .venv

<!-- activate the virtual environment of mac -->
source .venv/bin/activate

<!-- activate the virtual env of windows -->
.venv\Scripts\activate

<!-- for linux -->
source .venv/bin/activate

<!-- fro windows and git bash -->
source .venv/Scripts/activate
'''
## 2. install python libraries

'''bash
#web development framework
pip install django

#machine learning libraries
pip install numpy pandas matplotlib seaborn plotly scikit-learn , xgboost

#for saving and loading the model
pip install joblib

#jupyter notebook support
pip install ipykernel
'''

## 3. Train machine learning model
1. Find the data 
2. Preprocess the data 
3. Train the model
4. Evaluate the model
5. save the model

i have saaved the model as 'xgb_model.pkl' in the 'models' directory.
> you can see the procedure of ml training a model in this [jupyter notebook](./ml_project/01_ml.ipynb).

## 4. Create a Django project
'''bash
django-admin startproject tip_prediction 
cd tip_prediction

## 5. Create a Django App
'''bash
python manage.py startapp ml_app
'''

## 6. Update settings.py
Add the new app to the 'INSTALLED_APPS' list in 'tip_prediction/settings.py':

'''python
INSTALLED_APPS =[
    '''
    'ml_app',   
]
'''

## 7. Create a form for user input

in 'ml_app/forms.py', create a form to accept user input:
'''python
from django import forms
class predictionForms(forms.Form):
    feature1 = forms.FloatField(label='Feature 1')
    feature2 = forms.FloatField(label='Feature 2')
    feature3 = forms.FloatField(label='Feature 3')
    feature4 = forms.FloatField(label='Feature 4')
    feature5 = forms.FloatField(label='Feature 5')
    feature6 = forms.FloatField(label='Feature 6')
    
