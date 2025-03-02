import pickle
from django.shortcuts import render
import joblib
import numpy as np
from django.http import JsonResponse
from django.http import HttpResponse



# Create your views here.
def home(request):
    return render(request,"loan_approval/index.html")

def calculators(request):
    print("✅ Calculators View Called!") 
    return render(request,"loan_approval/calculators.html")

def feedback(request):
    return render(request,"loan_approval/feedback.html")

def home_loan(request):
    return render(request,"loan_approval/home-loan.html")

def home_form(request):
    return render(request,"loan_approval/home-loan-form.html")

def persona_loan(request):
    return render(request,"loan_approval/personal-loan.html")

def personal_loan_form(request):
    return render(request,"loan_approval/personal-loan-form.html")

def gold_form(request):
    # if request.method == "POST":
    #     # Get form data
    #     age = float(request.POST["age"])
    #     income = float(request.POST["income"])
    #     gold_weight = float(request.POST["gold_weight"])
    #     credit_score = float(request.POST["credit_score"])

    #     # Prepare input for model
    #     input_data = np.array([[age, income, gold_weight, credit_score]])

    #     # Make prediction
    #     prediction = model.predict(input_data)[0]

    #     # Convert to readable output
    #     result = "Approved" if prediction == 1 else "Rejected"

    #     return JsonResponse({"prediction": result})
    
   
    return render(request, "loan_approval/gold-loan-form.html")
    

def privacy_policy(request):
    return render(request,"loan_approval/privacy-policy.html")

def about_us(request):
    return render(request,"loan_approval/about-us.html")



def getPrediction(goldType,goldPurity,income,goldWeight,loanAmount,CIBILScore):
    model=pickle.load(open("gold_loan_model.sav",'rb'))
    scaled=pickle.load(open("scaler.sav",'rb'))

    prediction=model.predict(scaled.transform([
        [goldType,goldPurity,income,goldWeight,loanAmount,CIBILScore]
    ]))
    
    if prediction == 0:
        return 'Will Approve'
    else:
        return 'Will get reject'

# def result(request):
#     if request.method == 'POST':
#      goldWeight = float(request.GET["goldweight"])
#      income = float(request.GET["income"])
#      goldPurity = int(request.GET["goldPurity"])
#      goldType=(request.GET["goldType"])
#      loanAmount = float(request.GET["loanAmount"])
#      CIBILScore = float(request.GET["CIBILScore"])

#     result=getPrediction(goldType,goldPurity,income,goldWeight,loanAmount,CIBILScore)
#     return render(request,'loan_approval/result.html',{'result':result})

def result(request):
    if request.method == 'POST':
        goldType = request.POST.get("goldType", None)  # ✅ Avoids KeyError
        goldWeight = request.POST.get("goldWeight", 0)  # Default to 0 if missing
        goldPurity = request.POST.get("goldPurity", None)
        loanAmount = request.POST.get("loanAmount", 0)
        income = request.POST.get("income", 0)
        CIBILscore = request.POST.get("CIBILscore", 0)

        if goldType is None:
            return HttpResponse("Error: Gold Type is required!", status=400)  # Handle missing data

        # Process form data
        result=getPrediction(goldType,goldPurity,income,goldWeight,loanAmount,CIBILscore)
        return render(request, 'loan_approval/result.html', {result})
