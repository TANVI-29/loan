// Function to open loan application forms
function openForm(loanType) {
    const modal = document.getElementById(`${loanType}LoanForm`);
    modal.style.display = "block";
}

// Close modal when clicking the close button or outside the modal
document.querySelectorAll('.close').forEach(closeBtn => {
    closeBtn.onclick = function() {
        this.parentElement.parentElement.style.display = "none";
    }
});

window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = "none";
    }
}

// EMI Calculator Function
function calculateEMI(principal, rate, time) {
    rate = rate / (12 * 100);
    time = time * 12;
    return (principal * rate * Math.pow(1 + rate, time)) / (Math.pow(1 + rate, time) - 1);
}

// Loan Eligibility Calculator
function calculateEligibility(income, expenses, existingEMI) {
    const eligibleEMI = (income * 0.5) - expenses - existingEMI;
    return eligibleEMI * 60; // Approximate loan amount (considering 5 years tenure)
}

function togglePrivacy() {
    const modal = document.getElementById('privacyModal');
    if (modal.style.display === 'block') {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    } else {
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('privacyModal');
    if (event.target === modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
}

function openFeedbackModal() {
    const modal = document.getElementById('feedbackModal');
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden'; // Prevent scrolling
}

function closeFeedbackModal() {
    const modal = document.getElementById('feedbackModal');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto'; // Restore scrolling
}

// Handle star ratings
document.addEventListener('DOMContentLoaded', function() {
    const starContainers = document.querySelectorAll('.star-rating');
    
    starContainers.forEach(container => {
        const stars = container.querySelectorAll('i');
        
        stars.forEach(star => {
            star.addEventListener('mouseover', function() {
                const value = this.dataset.value;
                highlightStars(stars, value);
            });

            star.addEventListener('click', function() {
                const value = this.dataset.value;
                container.dataset.selected = value;
                highlightStars(stars, value);
            });
        });

        container.addEventListener('mouseleave', function() {
            const selected = this.dataset.selected;
            highlightStars(stars, selected || 0);
        });
    });
});

function highlightStars(stars, value) {
    stars.forEach(star => {
        star.classList.toggle('active', star.dataset.value <= value);
    });
}

// Handle form submission
document.getElementById('feedbackForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Show success message
    alert('Thank you for your feedback!');
    
    // Reset form and close modal
    this.reset();
    closeFeedbackModal();
    
    // Reset star ratings
    document.querySelectorAll('.star-rating').forEach(container => {
        container.dataset.selected = '';
        highlightStars(container.querySelectorAll('i'), 0);
    });
});

// Navbar Scroll Effect
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Active Link Highlighting
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Set active link based on current page
    const currentPath = window.location.pathname;
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});

function openLoanForm(loanType) {
    // Store the loan type in session storage
    sessionStorage.setItem('selectedLoanType', loanType);
    
    // Open the respective loan form in a new tab
    let formUrl;
    switch(loanType) {
        case 'personal':
            formUrl = 'personal-loan-form/';
            break;
        case 'home':
            formUrl = 'home-loan-form/';
            break;
        case 'gold':
            formUrl = 'gold-loan-form/';
            break;
        default:
            formUrl = 'loan-form.html';
    }
    
    window.location.href = formUrl; 
}

// Add hover animation
document.querySelectorAll('.loan-type').forEach(card => {
    card.addEventListener('mouseover', () => {
        card.querySelector('.loan-icon').style.transform = 'scale(1.1) rotate(5deg)';
    });
    
    card.addEventListener('mouseout', () => {
        card.querySelector('.loan-icon').style.transform = 'scale(1)';
    });
}); 