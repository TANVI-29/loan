// document.addEventListener('DOMContentLoaded', function() {
    
//     // Initialize form validation and enhancements
//     initializeForm();
// });

// function initializeForm() {
//     // Add input validations
//     addInputValidations();
    
//     // Add dynamic calculations
//     addDynamicCalculations();
    
//     // Initialize form auto-save
//     initializeAutoSave();
// }

// function addInputValidations() {
//     // Phone number validation
//     const phoneInput = document.getElementById('phone');
//     if (phoneInput) {
//         phoneInput.addEventListener('input', function(e) {
//             let value = e.target.value.replace(/\D/g, '');
//             if (value.length > 10) value = value.slice(0, 10);
//             e.target.value = value;
//         });
//     }

//     // Email validation
//     const emailInput = document.getElementById('email');
//     if (emailInput) {
//         emailInput.addEventListener('input', function(e) {
//             const email = e.target.value;
//             const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//             if (email && !emailPattern.test(email)) {
//                 emailInput.setCustomValidity('Please enter a valid email address');
//             } else {
//                 emailInput.setCustomValidity('');
//             }
//         });
//     }

//     // Amount validation
//     const amountInputs = document.querySelectorAll('input[type="number"]');
//     amountInputs.forEach(input => {
//         input.addEventListener('input', function(e) {
//             if (e.target.value < 0) e.target.value = 0;
//         });
//     });
// }

// function addDynamicCalculations() {
//     // For Gold Loan
//     const goldWeight = document.getElementById('goldWeight');
//     const goldPurity = document.getElementById('goldPurity');
//     const loanAmount = document.getElementById('loanAmount');

//     if (goldWeight && goldPurity && loanAmount) {
//         const calculateEstimatedLoan = () => {
//             const weight = parseFloat(goldWeight.value) || 0;
//             const purity = parseFloat(goldPurity.value) || 0;
//             // Assuming current gold rate is ₹5000 per gram (you should fetch this dynamically)
//             const goldRate = 5000;
//             const estimatedValue = weight * (purity/24) * goldRate * 0.75; // 75% of gold value
//             loanAmount.value = Math.round(estimatedValue);
//         };

//         goldWeight.addEventListener('input', calculateEstimatedLoan);
//         goldPurity.addEventListener('change', calculateEstimatedLoan);
//     }
// }

// function initializeAutoSave() {
//     const form = document.querySelector('form');
//     const formInputs = form.querySelectorAll('input, select');

//     // Save form data every 30 seconds
//     setInterval(() => {
//         const formData = {};
//         formInputs.forEach(input => {
//             formData[input.id] = input.value;
//         });
//         localStorage.setItem('loanFormData', JSON.stringify(formData));
//     }, 30000);

//     // Load saved data
//     const savedData = localStorage.getItem('loanFormData');
//     if (savedData) {
//         const formData = JSON.parse(savedData);
//         Object.keys(formData).forEach(key => {
//             const input = document.getElementById(key);
//             if (input) input.value = formData[key];
//         });
//     }
// }

// function submitLoanApplication(event, loanType) {
//     event.preventDefault();

//     // Gather form data
//     const formData = new FormData(event.target);
//     const data = Object.fromEntries(formData.entries());
//     data.loanType = loanType;

//     // Show loading state
//     const submitBtn = event.target.querySelector('button[type="submit"]');
//     const originalText = submitBtn.innerHTML;
//     submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
//     submitBtn.disabled = true;

//     // Simulate API call
//     setTimeout(() => {
//         // Show success message
//         showSuccessMessage('Application submitted successfully!');
        
//         // Reset form
//         event.target.reset();
//         localStorage.removeItem('loanFormData');
        
//         // Reset button
//         submitBtn.innerHTML = originalText;
//         submitBtn.disabled = false;
//     }, 2000);
// }

// function showSuccessMessage(message) {
//     const messageDiv = document.createElement('div');
//     messageDiv.className = 'success-message';
//     messageDiv.textContent = message;
    
//     document.body.appendChild(messageDiv);
    
//     setTimeout(() => {
//         messageDiv.style.animation = 'slideOut 0.5s ease';
//         setTimeout(() => messageDiv.remove(), 500);
//     }, 3000);
// } 



document.addEventListener('DOMContentLoaded', function () {
    // Initialize form validation and enhancements
    initializeForm();

    // Attach event listener to gold loan form submission
    const goldLoanForm = document.getElementById("goldLoanForm");
    if (goldLoanForm) {
        goldLoanForm.addEventListener("submit", handleGoldLoanSubmission);
    }
});

function initializeForm() {
    addInputValidations();
    addDynamicCalculations();
    initializeAutoSave();
}

function addInputValidations() {
    // Amount validation: Prevents negative values
    document.querySelectorAll('input[type="number"]').forEach(input => {
        input.addEventListener('input', function (e) {
            if (e.target.value < 0) e.target.value = 0;
        });
    });
}

function addDynamicCalculations() {
    const goldWeight = document.getElementById('goldWeight');
    const goldPurity = document.getElementById('goldPurity');
    const loanAmount = document.getElementById('loanAmount');

    if (goldWeight && goldPurity && loanAmount) {
        const calculateEstimatedLoan = () => {
            const weight = parseFloat(goldWeight.value) || 0;
            const purity = parseFloat(goldPurity.value) || 0;
            const goldRate = 5000; // Static rate, can be made dynamic
            const estimatedValue = weight * (purity / 24) * goldRate * 0.75;
            loanAmount.value = Math.round(estimatedValue);
        };

        goldWeight.addEventListener('input', calculateEstimatedLoan);
        goldPurity.addEventListener('change', calculateEstimatedLoan);
    }
}

function initializeAutoSave() {
    const form = document.getElementById("goldLoanForm"); // More specific selection
    if (!form) return;

    const formInputs = form.querySelectorAll('input, select');

    setInterval(() => {
        const formData = {};
        formInputs.forEach(input => {
            formData[input.id] = input.value;
        });
        localStorage.setItem('loanFormData', JSON.stringify(formData));
    }, 30000);

    // Restore saved data
    const savedData = localStorage.getItem('loanFormData');
    if (savedData) {
        const formData = JSON.parse(savedData);
        Object.keys(formData).forEach(key => {
            const input = document.getElementById(key);
            if (input) input.value = formData[key];
        });
    }
}

function handleGoldLoanSubmission(event) {
    event.preventDefault();
    let formData = new FormData(event.target);

    fetch("gold-loan-form/", {
        method: "POST",
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            let resultBox = document.getElementById("resultBox");
            if (resultBox) {
                resultBox.style.display = "block";
                resultBox.innerText = data.prediction;
                resultBox.className = data.prediction === "Approved" ? "approved" : "rejected";
            }
        })
        .catch(error => console.error("Error:", error));
}

function submitLoanApplication(event, loanType) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    data.loanType = loanType;

    const submitBtn = event.target.querySelector('button[type="submit"]');
    if (!submitBtn) return;
    
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
    submitBtn.disabled = true;

    setTimeout(() => {
        showSuccessMessage('Application submitted successfully!');
        event.target.reset();
        localStorage.removeItem('loanFormData');
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
    }, 2000);
}

function showSuccessMessage(message) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'success-message';
    messageDiv.textContent = message;
    document.body.appendChild(messageDiv);

    setTimeout(() => {
        messageDiv.style.animation = 'slideOut 0.5s ease';
        setTimeout(() => messageDiv.remove(), 500);
    }, 3000);
}
