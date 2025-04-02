import pickle
from django.shortcuts import render,redirect
import joblib
import numpy as np
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Feedback
from django.urls import reverse

from loan_approval.forms import FeedbackForm

# Create your views here.
def home(request):
    return render(request,"loan_approval/index2.html")

def calculator(request):
    print("✅ Calculator View Called!") 
    return render(request,"loan_approval/calculator.html")

# def feedback(request):
#     print("Request method:", request.method)
#     if request.method == "GET":
#         print("Get request")
#     elif request.method == "POST":
#         form = FeedbackForm(request.POST)
#         print("Form is valid:", form.is_valid())
#         if form.is_valid():
#             form.save()  # Save the feedback to the database
#             return redirect('index')
#         else:
#          form = FeedbackForm()  
#         return render(request,"loan_approval/feedback.html")


from django.shortcuts import render, redirect
from .forms import FeedbackForm  # Import your FeedbackForm

# def feedback(request):
#     print("Request method:", request.method)
    
#     if request.method == "GET":
#         print("Get request")
#         name = request.POST.get('name')
#         email= request.POST.get('email')
#         type=request.POST.get('feedbackType')
#         message = request.POST.get('message')
#         rating= request.POST.get('rating')
        
#         # Save the data to the database
#         Feedback.objects.create(
#             email=email,
#             type=type,
#             message=message,
#             rating=rating
#         )
#         # Render the form for GET requests
#         # form = FeedbackForm()
#         return render(request, "loan_approval/feedback.html")
    
#     elif request.method == "POST":
#         form = FeedbackForm(request.POST)
#         print("Form data:", request.POST)  # Print form data
       
#         print("Form is valid:", form.is_valid())
        
#         if form.is_valid():
#             form.save()  # Save the feedback to the database
#             # return redirect('home')  # Redirect to the index page after
#         else:
#             print("Form errors:", form.errors)  # Print form errors
#         home_url = reverse("loan_approval:home")  # Generates the correct URL
#         return redirect(home_url)
#     else:
#             return render(request, "loan_approval/feedback.html", {'form': form})



# def feedback(request):
#     if request.method == "POST":
#         print("Received Data:", request.POST)
        
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('loan_approval:home')  # Redirect to the home page after successful submission
#         else:
#             # If the form is invalid, render the form again with error messages
#             return render(request, "loan_approval/feedback.html", {'form': form})
#     else:
#         form = FeedbackForm()
#         return render(request, "loan_approval/feedback.html", {'form': form})


from django.shortcuts import render, redirect
from .models import Feedback  # Import your Feedback model


from django.shortcuts import render, redirect
from .forms import FeedbackForm

# def feedback(request):
#     if request.method == "POST":
#         form = FeedbackForm(request.POST)
#         print("Form data:", request.POST)  # Print form data
#         print(form.is_valid())
#         if form.is_valid():
#             form.save() 
#             print("Form saved successfully!")
#             return redirect("loan_approval:home")
#         else:
#             print("Form errors:", form.errors) # ✅ Save data to the database
#               # Redirect after submission
#     else:
#         form = FeedbackForm()
        
#     return render(request, "loan_approval/feed3.html", {"form": form})



from django.shortcuts import render, redirect
from django.db import connection
from .models import Feedback
from .forms import FeedbackForm
from django.db import connection, transaction
# def feedback(request):
#     if request.method == "POST":
#         form = FeedbackForm(request.POST)
#         print("Received Form Data:", request.POST)

#         if form.is_valid():
#             feedback = form.save(commit=False)  # Save but don't commit yet
#             feedback.save()  # Now commit explicitly
#             transaction.commit()
#             print("committed")
#             # Force commit in MySQL
            
#             # Ensure data is committed by checking in MySQL
#             with connection.cursor() as cursor:
#                 cursor.execute("COMMIT;")
#                 print("Form data saved to database:", feedback)
#             print("Form saved successfully!")  
#             return redirect('loan_approval:home')
#         else:
#             print("Form errors:", form.errors)

#     form = FeedbackForm()
#     return render(request, "loan_approval/feed3.html", {'form': form})



from django.db import connection
from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        print("Received Form Data:", request.POST)

        if form.is_valid():
            feedback = form.save(commit=False)  
            feedback.save()
            print("Saved Feedback Object:", feedback)   # Save to database
            
            # Print SQL Queries Executed
            print("Executed SQL Queries:")
            for query in connection.queries:
                print(query['sql'])

            # Force Commit in MySQL
            with connection.cursor() as cursor:
                cursor.execute("COMMIT;")
            
            print("Form saved successfully!")  
            return redirect('loan_approval:home')
        else:
            print("Form errors:", form.errors)

    form = FeedbackForm()
    return render(request, "loan_approval/feed3.html", {'form': form})




# def feedback(request):
#     print("Request method:", request.method)

#     if request.method == "POST":
#         # Collect data from POST request
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         feedback_type = request.POST.get('feedbackType')
#         message = request.POST.get('message')
#         rating = request.POST.get('rating')
#         print(name,email,feedback_type,message,rating)
#         # Ensure all required fields are provided
#         # if not all([name, email, feedback_type, message, rating]):
#         #     return render(request, "loan_approval/feedback.html", {"error": "All fields are required"})

#         # Save feedback to the database
#         Feedback.objects.create(
#             name=name or None,
#             email=email or None,
#             type=feedback_type or None,
#             message=message or None,
#             rating=rating or 1
#         )

#         # Redirect to a success page or back to the feedback form
#         return redirect("loan_approval:home")  # Make sure this URL exists

    # If GET request, render the feedback form
    # return render(request, "loan_approval/feed3.html")



# def feedback(request):
#    return render(request, "loan_approval/feed3.html")

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



def gold_result(request):
    model=joblib.load('loan_approval/model/gold_loan_model.sav')
    if request.method == 'POST':
      
      goldWeight = float(request.POST.get("goldWeight","0"))
      income = float(request.POST.get("income","0"))
      goldPurity = float(request.POST.get("goldPurity","0"))
      
      loanAmount =float( request.POST.get("loanAmount","0"))
      CIBILScore = float(request.POST.get("CIBILScore","0"))
      print(goldWeight)
      print(goldPurity)
      print(income)
      print(loanAmount)
      print(CIBILScore)
      gold_price_per_gram = 8500  # Example: Fixed price per gram
    # loanAmount = goldWeight * gold_price_per_gram * (goldPurity / 100)
      LTV = (loanAmount / (goldWeight * gold_price_per_gram))*100 if goldWeight > 0 else 0
    
      print(LTV)
    result=model.predict([[goldPurity,income,goldWeight,loanAmount,CIBILScore,LTV]])
    print("result:",result)
    input_features=np.array([[goldWeight,CIBILScore,goldPurity,loanAmount,income,LTV]])
    Rejection_probability=model.predict_proba(input_features)[0][1] * 100 
    Approval_probability=100-Rejection_probability
    print(result)
    print('Approval_probability',Approval_probability)
    if result[0]==0:
        result="Will Rejected"
    else:
        result="Will Approved"
    
    
    
    return render(request,'loan_approval/result.html',{'result':result, 'CIBILScore':CIBILScore,'income':income,'LTV':LTV,'Approval_probability':Approval_probability,'Rejection_probability':Rejection_probability})


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
         result="Will Rejected"
        else:
         result="Will Approved"
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
         result="Will Rejected"
        else:
         result="Will Approved"
        return render(request,'loan_approval/result.html',{'result':result,'Income':Income,'CIBILScore':CIBILScore,'DTI':DTI,'Self_Employeed':Self_Employeed,'Approval_probability':Approval_probability,'Rejection_probability':Rejection_probability})





# def gold_result(request):
#    model=joblib.load('loan_approval/model/gold_loan_model1.sav')
#    if request.method=='POST':
#         Age=float(request.POST.get("Age","0"))
#         WorkExperience=float(request.POST.get("WorkExperience","0"))
#         CIBILScore=float(request.POST.get("CIBILScore","0"))
#         ExistingLoan=float(request.POST.get("Existing_Loan","0"))
#         LoanTenure=float(request.POST.get("LoanTenure","0"))
#         LoanAmount=float(request.POST.get("LoanAmount","0") or 0)
#         Income=float(request.POST.get("Income","0"))