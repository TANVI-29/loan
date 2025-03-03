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



# def getPrediction(goldType,goldPurity,income,goldWeight,loanAmount,CIBILScore):
#     model=pickle.load(open("gold_loan_model.sav",'rb'))
#     scaled=pickle.load(open("scaler.sav",'rb'))

#     prediction=model.predict(scaled.transform([
#         [goldType,goldPurity,income,goldWeight,loanAmount,CIBILScore]
#     ]))
    
#     if prediction == 0:
#         return 'Will Approve'
#     else:
#         return 'Will get reject'

model=joblib.load('loan_approval/model/gold_loan_linear_model.sav')

def result(request):
    if request.method == 'POST':
      print("recieved data:",request.POST)
      goldWeight = float(request.POST.get("goldWeight","0"))
      income = float(request.POST.get("income","0"))
      goldPurity = float(request.POST.get("goldPurity","0"))
      
      loanAmount =float( request.POST.get("loanAmount","0"))
      CIBILscore = float(request.POST.get("CIBILscore","0"))
      print(goldWeight)
      print(goldPurity)
      print(income)
      print(loanAmount)
      print(CIBILscore)
      gold_price_per_gram = 8500  # Example: Fixed price per gram
    # loanAmount = goldWeight * gold_price_per_gram * (goldPurity / 100)
      ltv = loanAmount / (goldWeight * gold_price_per_gram) if goldWeight > 0 else 0
    

    result=model.predict([[goldPurity,income,goldWeight,loanAmount,CIBILscore,ltv]])
    print("result:",result)
    if result[0]=="Rejected":
        result="Rejected"
    else:
        result="Approved"
    
    
    return render(request,'loan_approval/result.html',{'result':result})


  
