from django.shortcuts import render
import numpy as np
import pandas as pd
from . import forms
import pickle
import os

# Create your views here.

def readData(filepath='data/vehicle_insurance.csv'):
    df = pd.read_csv(filepath)
    X = df.iloc[:,1:len(df.columns)-1]
    y = df.iloc[:, -1]
    return X, y


def evaluateUserInput(data_features, X_test):
    # X_test = getUserInput(data_features)
    with open(f'app/result/scaler/MinMaxScaler.sav', 'rb') as f:
        scaler = pickle.load(f)
        X_test = scaler.transform([X_test])

    model_accuracy_scores = pd.read_csv(
        'app/result/model_evaluation/ModelEvaluationScores.csv'
    )['Accuracy']

    model_list=[]
    test_results = []
    prediction_score = 0
    model_files = os.listdir('app/result/models')
    for model_file in model_files:
        with open(f'app/result/models/{model_file}', 'rb') as f:
            model = pickle.load(f)
            model_list.append(model)
            test_results.append([str(model)[ : str(model).index('(')]])

    for index, classifier in enumerate(model_list):
        y_pred = classifier.predict(X_test)
        y_pred = 'Positive' if y_pred == 1 else 'Negative'

        if y_pred == 'Positive':
            prediction_score += 1 * model_accuracy_scores[index]
        else:
            prediction_score -= 1 * model_accuracy_scores[index]

        test_results[index].append(y_pred)

    
    prediction_score = prediction_score / sum(model_accuracy_scores)
    if prediction_score < 0:
        prediction_class = 'Negative'
    elif prediction_score > 0:
        prediction_class = 'Positive'
    else:
        prediction_class = 'Indeterminate'


    results = {}
    for test_result in test_results:
        results[test_result[0]] = test_result[1]
    
    final_result = []
    final_result.append(results)
    final_result.append(prediction_score)
    final_result.append(prediction_class)

    return final_result
    


def getUserInput(data_features):
    user_input = []
    for feature in data_features.columns:
        print(f'Enter value for {feature}')
        print(f'Range is {min(data_features[feature])} to {max(data_features[feature])}')
        user_input.append(input('Your input: '))
    return user_input
    

def Home(request):
    X, y = readData(filepath='app/data/parkinsons.csv')
    
    
    if request.method == 'POST':
        form = forms.InputDataForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            holds_driving_license = form.cleaned_data['holds_driving_license']
            previously_insured = form.cleaned_data['previously_insured']
            vehicle_age = form.cleaned_data['vehicle_age']
            is_vehicle_damaged = form.cleaned_data['is_vehicle_damaged']
            annual_premium = form.cleaned_data['annual_premium']
            policy_sales_channel = form.cleaned_data['policy_sales_channel']
            vintage = form.cleaned_data['vintage']


            user_input = []
            user_input.append(int(gender))
            user_input.append(age)
            if holds_driving_license:
                user_input.append(1)
            else:
                user_input.append(0)
            if previously_insured:
                user_input.append(1)
            else:
                user_input.append(0)
            
            for bit in vehicle_age:
                print(bit)
                user_input.append(int(bit))

            user_input.append(is_vehicle_damaged)
            user_input.append(annual_premium)
            user_input.append(policy_sales_channel)
            user_input.append(vintage)
            

            print(user_input)
            results = evaluateUserInput(X, user_input)
            
            return render(request, 'result.html', {'model_results': results[0], 'prediction_score': results[1], 'prediction_class': results[2]})

            

        else:
            pass
    else:
        form = forms.InputDataForm()
        return render(request, 'home.html', {'form': form})




