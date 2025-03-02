function openCalculator(type) {
    // Hide all calculator contents
    document.querySelectorAll('.calculator-content').forEach(content => {
        content.classList.remove('active');
    });
    
    // Remove active class from all tabs
    document.querySelectorAll('.tab-btn').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Show selected calculator and activate tab
    document.getElementById(`${type}Calculator`).classList.add('active');
    event.target.classList.add('active');
}

// Initialize charts with proper sizing
let emiChart = null;
let interestChart = null;

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tabs
    initializeTabs();
    
    // Initialize first calculator
    calculateEMI();

    // Common chart options
    const chartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                    padding: 20,
                    font: {
                        size: 14
                    },
                    color: '#333'
                }
            }
        }
    };

    // Initialize EMI Chart
    const emiCtx = document.getElementById('emiChart').getContext('2d');
    emiChart = new Chart(emiCtx, {
        type: 'pie',
        data: {
            labels: ['Principal Amount', 'Total Interest'],
            datasets: [{
                data: [0, 0],
                backgroundColor: ['#4CAF50', '#FF5722'],
                borderWidth: 0,
                hoverOffset: 4
            }]
        },
        options: chartOptions
    });

    // Initialize Interest Chart
    const interestCtx = document.getElementById('interestChart').getContext('2d');
    interestChart = new Chart(interestCtx, {
        type: 'pie',
        data: {
            labels: ['Principal Amount', 'Total Interest'],
            datasets: [{
                data: [0, 0],
                backgroundColor: ['#2196F3', '#FFC107'],
                borderWidth: 0,
                hoverOffset: 4
            }]
        },
        options: chartOptions
    });

    // Add event listeners to all inputs
    addInputListeners();
});

// EMI Calculator
function calculateEMI() {
    const amount = Number(document.getElementById('emiAmount').value);
    const rate = Number(document.getElementById('emiRate').value);
    const tenure = Number(document.getElementById('emiTenure').value);

    if (amount && rate && tenure) {
        const monthlyRate = rate / (12 * 100);
        const months = tenure * 12;
        
        // Calculate EMI
        const emi = (amount * monthlyRate * Math.pow(1 + monthlyRate, months)) / 
                   (Math.pow(1 + monthlyRate, months) - 1);
        
        // Calculate total payment and interest
        const totalAmount = emi * months;
        const totalInterest = totalAmount - amount;

        // Format numbers for display
        const formattedEMI = new Intl.NumberFormat('en-IN', {
            style: 'currency',
            currency: 'INR'
        }).format(emi);

        // Update results with formatted numbers
        document.getElementById('monthlyEMI').textContent = formattedEMI;
        document.getElementById('totalInterest').textContent = 
            new Intl.NumberFormat('en-IN', {
                style: 'currency',
                currency: 'INR'
            }).format(totalInterest);
        document.getElementById('totalAmount').textContent = 
            new Intl.NumberFormat('en-IN', {
                style: 'currency',
                currency: 'INR'
            }).format(totalAmount);

        // Update chart with animation
        emiChart.data.datasets[0].data = [amount, totalInterest];
        emiChart.update('show');
    }
}

// Loan Eligibility Calculator
function calculateEligibility() {
    const monthlyIncome = Number(document.getElementById('monthlyIncome').value);
    const existingEMI = Number(document.getElementById('existingEMI').value) || 0;
    const rate = Number(document.getElementById('eligibilityRate').value);
    const tenure = Number(document.getElementById('eligibilityTenure').value);

    if (monthlyIncome && rate && tenure) {
        try {
            // Maximum EMI capacity (50% of monthly income)
            const maxEMI = (monthlyIncome * 0.5) - existingEMI;
            
            if (maxEMI <= 0) {
                document.getElementById('eligibleAmount').textContent = 'Not Eligible';
                updateEligibilityMeter(0);
                return;
            }

            // Convert annual interest rate to monthly
            const monthlyRate = rate / (12 * 100);
            const months = tenure * 12;

            // Calculate eligible loan amount using EMI formula
            const eligibleAmount = maxEMI * ((Math.pow(1 + monthlyRate, months) - 1) / 
                                 (monthlyRate * Math.pow(1 + monthlyRate, months)));

            // Format the eligible amount
            const formattedAmount = new Intl.NumberFormat('en-IN', {
                style: 'currency',
                currency: 'INR',
                maximumFractionDigits: 0
            }).format(eligibleAmount);

            // Update the display
            document.getElementById('eligibleAmount').textContent = formattedAmount;
            
            // Calculate and update eligibility meter
            const maxLoanAmount = monthlyIncome * 60; // Rough estimate of max possible loan
            const eligibilityPercentage = Math.min((eligibleAmount / maxLoanAmount) * 100, 100);
            updateEligibilityMeter(eligibilityPercentage);

            // Show additional details
            document.getElementById('maxEMI').textContent = new Intl.NumberFormat('en-IN', {
                style: 'currency',
                currency: 'INR',
                maximumFractionDigits: 0
            }).format(maxEMI);

            // Update eligibility status
            updateEligibilityStatus(eligibilityPercentage);

        } catch (error) {
            console.error('Calculation Error:', error);
            document.getElementById('eligibleAmount').textContent = 'Error in calculation';
            updateEligibilityMeter(0);
        }
    } else {
        document.getElementById('eligibleAmount').textContent = 'Please fill all fields';
        updateEligibilityMeter(0);
    }
}

function updateEligibilityMeter(percentage) {
    const meterBar = document.getElementById('eligibilityMeter');
    if (meterBar) {
        meterBar.style.width = `${percentage}%`;
        meterBar.style.backgroundColor = getEligibilityColor(percentage);
    }
}

function getEligibilityColor(percentage) {
    if (percentage >= 80) return '#4CAF50'; // Green
    if (percentage >= 50) return '#FFC107'; // Yellow
    if (percentage >= 20) return '#FF9800'; // Orange
    return '#F44336'; // Red
}

function updateEligibilityStatus(percentage) {
    const statusElement = document.getElementById('eligibilityStatus');
    if (statusElement) {
        let status = '';
        let color = '';

        if (percentage >= 80) {
            status = 'Excellent Eligibility';
            color = '#4CAF50';
        } else if (percentage >= 50) {
            status = 'Good Eligibility';
            color = '#FFC107';
        } else if (percentage >= 20) {
            status = 'Fair Eligibility';
            color = '#FF9800';
        } else {
            status = 'Poor Eligibility';
            color = '#F44336';
        }

        statusElement.textContent = status;
        statusElement.style.color = color;
    }
}

// Add these event listeners specifically for eligibility calculator
document.addEventListener('DOMContentLoaded', function() {
    const eligibilityInputs = [
        'monthlyIncome',
        'existingEMI',
        'eligibilityRate',
        'eligibilityTenure'
    ];

    eligibilityInputs.forEach(id => {
        const input = document.getElementById(id);
        if (input) {
            input.addEventListener('input', calculateEligibility);
            
            // Add slider listener if exists
            const sliderId = id.replace('eligibility', '').toLowerCase() + 'Slider';
            const slider = document.getElementById(sliderId);
            if (slider) {
                slider.addEventListener('input', function() {
                    input.value = this.value;
                    calculateEligibility();
                });
            }
        }
    });
});

// Interest Calculator
function calculateInterest() {
    const principal = Number(document.getElementById('principalAmount').value);
    const rate = Number(document.getElementById('interestRate').value);
    const time = Number(document.getElementById('timePeriod').value);

    if (principal && rate && time) {
        // Calculate compound interest
        const totalAmount = principal * Math.pow(1 + (rate / 100), time);
        const interest = totalAmount - principal;

        // Update results
        document.getElementById('totalInterestAmount').textContent = `₹${interest.toFixed(2)}`;
        document.getElementById('totalPayableAmount').textContent = `₹${totalAmount.toFixed(2)}`;

        // Update chart
        interestChart.data.datasets[0].data = [principal, interest];
        interestChart.update();
    }
}

// Add input listeners
function addInputListeners() {
    // EMI Calculator
    ['emiAmount', 'emiRate', 'emiTenure'].forEach(id => {
        const input = document.getElementById(id);
        const slider = document.getElementById(id + 'Slider');
        
        if (input && slider) {
            input.addEventListener('input', () => {
                slider.value = input.value;
                calculateEMI();
            });
            
            slider.addEventListener('input', () => {
                input.value = slider.value;
                calculateEMI();
            });
        }
    });

    // Interest Calculator
    ['principalAmount', 'interestRate', 'timePeriod'].forEach(id => {
        const input = document.getElementById(id);
        const slider = document.getElementById(id.replace('Amount', '').toLowerCase() + 'Slider');
        
        if (input && slider) {
            input.addEventListener('input', () => {
                slider.value = input.value;
                calculateInterest();
            });
            
            slider.addEventListener('input', () => {
                input.value = slider.value;
                calculateInterest();
            });
        }
    });
}

// Helper Functions
function initializeSliders() {
    // EMI Calculator Sliders
    initializeSlider('emiAmount', 'emiAmountSlider', calculateEMI);
    initializeSlider('emiRate', 'emiRateSlider', calculateEMI);
    initializeSlider('emiTenure', 'emiTenureSlider', calculateEMI);

    // Interest Calculator Sliders
    initializeSlider('principalAmount', 'principalSlider', calculateInterest);
    initializeSlider('interestRate', 'interestRateSlider', calculateInterest);
    initializeSlider('timePeriod', 'timeSlider', calculateInterest);
}

function initializeSlider(inputId, sliderId, calculateFunction) {
    const input = document.getElementById(inputId);
    const slider = document.getElementById(sliderId);

    if (input && slider) {
        slider.addEventListener('input', function() {
            input.value = this.value;
            calculateFunction();
        });

        input.addEventListener('input', function() {
            slider.value = this.value;
            calculateFunction();
        });
    }
}

function updateEMIChart(principal, interest) {
    if (emiChart) {
        emiChart.data.datasets[0].data = [principal, interest];
        emiChart.update();
    }
}

function updateInterestChart(principal, interest) {
    if (interestChart) {
        interestChart.data.datasets[0].data = [principal, interest];
        interestChart.update();
    }
}

// Add animation to results
function animateValue(element, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const value = Math.floor(progress * (end - start) + start);
        element.textContent = `₹${value.toFixed(2)}`;
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

function initializeTabs() {
    const tabs = document.querySelectorAll('.tab-btn');
    const panels = document.querySelectorAll('.calculator-panel');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active class from all tabs and panels
            tabs.forEach(t => t.classList.remove('active'));
            panels.forEach(p => {
                p.classList.remove('active');
                p.classList.remove('fade-in');
            });

            // Add active class to clicked tab
            tab.classList.add('active');

            // Show corresponding panel
            const panelId = `${tab.dataset.tab}-panel`;
            const panel = document.getElementById(panelId);
            panel.classList.add('active', 'fade-in');

            // Initialize the calculator for the active tab
            switch(tab.dataset.tab) {
                case 'emi':
                    calculateEMI();
                    break;
                case 'eligibility':
                    calculateEligibility();
                    break;
                case 'interest':
                    calculateInterest();
                    break;
            }
        });
    });
}

// Add smooth transitions between tabs
function switchTab(tabId) {
    const currentPanel = document.querySelector('.calculator-panel.active');
    const newPanel = document.getElementById(`${tabId}-panel`);
    
    currentPanel.classList.add('fade-out');
    
    setTimeout(() => {
        currentPanel.classList.remove('active', 'fade-out');
        newPanel.classList.add('active', 'fade-in');
    }, 300);
} 