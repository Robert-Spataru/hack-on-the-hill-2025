// Handle user interactions
document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#user-form');
  const submitButton = document.querySelector('#submit-btn');
  const resultDiv = document.querySelector('#result');

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const username = formData.get('username');
    
    if (username) {
      resultDiv.textContent = `Welcome, ${username}!`;
      submitButton.disabled = true;
    }
  });

  // Reset form
  document.querySelector('#reset-btn').addEventListener('click', () => {
    form.reset();
    resultDiv.textContent = '';
    submitButton.disabled = false;
  });
});