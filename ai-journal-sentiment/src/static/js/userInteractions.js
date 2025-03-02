class UserInterface {
    constructor() {
        this.initializeElements();
        this.bindEvents();
    }

    initializeElements() {
        this.form = document.querySelector('#user-form');
        this.submitButton = document.querySelector('#submit-btn');
        this.resultDiv = document.querySelector('#result');
        this.resetButton = document.querySelector('#reset-btn');
    }

    bindEvents() {
        this.form.addEventListener('submit', (e) => this.handleSubmit(e));
        this.resetButton.addEventListener('click', () => this.resetForm());
    }

    handleSubmit(e) {
        e.preventDefault();
        const formData = new FormData(this.form);
        const username = formData.get('username');
        
        if (username) {
            this.resultDiv.textContent = `Welcome, ${username}!`;
            this.submitButton.disabled = true;
        }
    }

    resetForm() {
        this.form.reset();
        this.resultDiv.textContent = '';
        this.submitButton.disabled = false;
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    new UserInterface();
});