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



def result(request):
    model=joblib.load('loan_approval/model/gold_loan_linear_model.sav')
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
    if result[0]==1:
        result="Rejected"
    else:
        result="Approved"
    
    
    return render(request,'loan_approval/result.html',{'result':result})


def home_result(request):
    model=joblib.load('loan_approval/model/home_loan_model.sav')
    if request.method=='POST':
        Age=float(request.POST.get("Age","0"))
        WorkExperience=float(request.POST.get("WorkExperience","0"))
        CIBILScore=float(request.POST.get("CIBILScore","0"))
        Existing_Loan=float(request.POST.get("Existing_Loan","0"))
        property_Value=float(request.POST.get("property_Value","0"))
        loanAmount=float(request.POST.get("loanAmount","0"))
        income=float(request.POST.get("income","0"))
        home_loan=float(request.POST.get("home_loan","0").strip() or 0)
        car_loan=float(request.POST.get("car_loan","0").strip() or 0)
        personal_loan=float(request.POST.get("personal_loan","0").strip() or 0)
        credit_card=float(request.POST.get("credit_card","0").strip() or 0)
        print(loanAmount)
        print(income)
        print(property_Value)
       
        Dept_payment=home_loan + car_loan + personal_loan + credit_card
        down_Payment=property_Value-loanAmount
        print("Down:",down_Payment)
        print("Dept:",Dept_payment)
        month_income=income/12
     
        DTI=((Dept_payment/month_income)*100) if Dept_payment >0 else 0
        
        LTV=(loanAmount/property_Value)*100
        print(DTI)
        print(LTV)
        result=model.predict([[Age,WorkExperience,CIBILScore,down_Payment,Existing_Loan,property_Value,loanAmount,income,DTI,LTV]])
        input_features=np.array([[Age,WorkExperience,CIBILScore,down_Payment,Existing_Loan,property_Value,loanAmount,income,DTI,LTV]])
        Approval_probability=model.predict_proba(input_features)[0][1] * 100 
        Rejection_probability=100-Approval_probability
        print(result)
        print('Approval_probability',Approval_probability)

        if result[0]==0:
         result="Rejected"
        else:
         result="Approved"
        return render(request,'loan_approval/result.html',{'result':result,'CIBILScore':CIBILScore,'DTI':DTI,'LTV':LTV,'Approval_probability':Approval_probability,'Rejection_probability':Rejection_probability})


def personal_result(request):
    model=joblib.load('loan_approval/model/personal_loan_model2.sav')
    if request.method=='POST':
        Age=float(request.POST.get("Age","0"))
        WorkExperience=float(request.POST.get("WorkExperience","0"))
        CIBILScore=float(request.POST.get("CIBILScore","0"))
        ExistingLoan=float(request.POST.get("Existing_Loan","0"))
        LoanTenure=float(request.POST.get("LoanTenure","0"))
        LoanAmount=float(request.POST.get("LoanAmount","0") or 0)
        Income=float(request.POST.get("Income","0"))
        Self_Employeed=float(request.POST.get("Self_Employeed","0"))
        No_Dependencies=float(request.POST.get("No_Dependencies","0"))
        home_loan=float(request.POST.get("home_loan","0").strip() or 0)
        car_loan=float(request.POST.get("car_loan","0").strip() or 0)
        personal_loan=float(request.POST.get("personal_loan","0").strip() or 0)
        credit_card=float(request.POST.get("credit_card","0").strip() or 0)
        print(LoanAmount)
        print(Income)
        print(LoanTenure)
        Dept_payment=home_loan + car_loan + personal_loan + credit_card
        month_income=Income/12
        DTI=((Dept_payment/month_income)*100) if Dept_payment >0 else 0
        print(DTI)
        
        result=model.predict([[Age,WorkExperience,CIBILScore,LoanTenure,No_Dependencies,ExistingLoan,LoanAmount,Income,DTI,Self_Employeed]])
        input_features=np.array([[Age,WorkExperience,CIBILScore,LoanTenure,No_Dependencies,ExistingLoan,LoanAmount,Income,DTI,Self_Employeed]])
        Approval_probability=model.predict_proba(input_features)[0][1] * 100 
        Rejection_probability=100-Approval_probability
        print(result)
        print('Approval_probability',Approval_probability)

        if result[0]==0:
         result="Rejected"
        else:
         result="Approved"
        return render(request,'loan_approval/result.html',{'result':result,'Income':Income,'CIBILScore':CIBILScore,'DTI':DTI,'Self_Employeed':Self_Employeed,'Approval_probability':Approval_probability,'Rejection_probability':Rejection_probability})





