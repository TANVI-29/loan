document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('feedbackForm');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form values
        // const formData = {
        //     name: document.getElementById('name').value,
        //     email: document.getElementById('email').value,
        //     type: document.getElementById('feedbackType').value,
        //     message: document.getElementById('message').value,
        //     rating: document.querySelector('input[name="rating"]:checked')?.value || '',
        //     subscribe: document.getElementById('subscribe').checked
        // };

        // Validate form
        // if (!validateForm(formData)) {
        //     return;
        // }

        // Show success message
        showMessage('Thank you for your feedback!');
        
        // Reset form
        form.reset();
    });

    // Add email validation on input
//     const emailInput = document.getElementById('email');
//     emailInput.addEventListener('input', function() {
//         if (this.value && !validateEmail(this.value)) {
//             this.setCustomValidity('Please enter a valid email address');
//         } else {
//             this.setCustomValidity('');
//         }
//     });
});

// function validateForm(data) {
//     if (!data.name || !data.email || !data.type || !data.message) {
//         showMessage('Please fill in all required fields', 'error');
//         return false;
//     }

//     if (!validateEmail(data.email)) {
//         showMessage('Please enter a valid email address', 'error');
//         return false;
//     }

//     return true;
// }

// function validateEmail(email) {
//     return email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/);
// }

function showMessage(message, type = 'success') {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    messageDiv.textContent = message;
    
    document.body.appendChild(messageDiv);
    
    messageDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 25px;
        background: ${type === 'success' ? '#4CAF50' : '#f44336'};
        color: white;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        animation: slideIn 0.5s ease;
    `;

    setTimeout(() => {
        messageDiv.style.animation = 'slideOut 0.5s ease';
        setTimeout(() => messageDiv.remove(), 500);
    }, 3000);
}

// Add these animations to your CSS
document.head.insertAdjacentHTML('beforeend', `
    <style>
        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        @keyframes slideOut {
            from { transform: translateX(0); opacity: 1; }
            to { transform: translateX(100%); opacity: 0; }
        }
    </style>
`);

// Add animation to rating stars
const ratingLabels = document.querySelectorAll('.rating label');
ratingLabels.forEach(label => {
    label.addEventListener('mouseover', function() {
        this.style.transform = 'scale(1.2)';
    });
    
    label.addEventListener('mouseout', function() {
        this.style.transform = 'scale(1)';
    });
 }); 