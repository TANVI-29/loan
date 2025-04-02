let currentMode = "emi"; // Default mode is EMI Calculator
let chart;

function switchCalculator(mode) {
    currentMode = mode;
    if (mode === "emi") {
        document.getElementById("calcTitle").innerText = "EMI CALCULATOR";
        document.getElementById("resultText").innerText = "Per month";
    } else {
        document.getElementById("calcTitle").innerText = "SIMPLE INTEREST CALCULATOR";
        document.getElementById("resultText").innerText = "Total Simple Interest";
    }
    calculate(); // Recalculate when switching mode
}

function calculate() {
    let amount = parseFloat(document.getElementById("amount").value);
    let rate = parseFloat(document.getElementById("rate").value);
    let years = parseFloat(document.getElementById("years").value);

    if (currentMode === "emi") {
        calculateEMI(amount, rate, years);
    } else {
        calculateSimpleInterest(amount, rate, years);
    }
}

function calculateEMI(amount, rate, years) {
    let monthlyRate = rate / 100 / 12;
    let numPayments = years * 12;
    let emi = (amount * monthlyRate * Math.pow(1 + monthlyRate, numPayments)) / 
              (Math.pow(1 + monthlyRate, numPayments) - 1);
    
    let totalPayment = emi * numPayments;
    let totalInterest = totalPayment - amount;

    document.getElementById("resultAmount").innerText = emi.toFixed(2);
    updateChart(amount, totalInterest);
}

function calculateSimpleInterest(amount, rate, years) {
    let interest = (amount * rate * years) / 100;
    document.getElementById("resultAmount").innerText = interest.toFixed(2);
    updateChart(amount, interest);
}

function updateChart(principal, interest) {
    let ctx = document.getElementById("loanChart").getContext("2d");

    if (chart) chart.destroy();

    chart = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: ["Principal", "Interest"],
            datasets: [{
                data: [principal, interest],
                backgroundColor: ["#007BFF", "#FFD700"], // Blue for Principal, Yellow for Interest
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

// Initialize with default calculation
calculate();
