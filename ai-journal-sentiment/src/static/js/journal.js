class JournalEntry {
    constructor() {
        this.initializeElements();
        this.bindEvents();
    }

    initializeElements() {
        this.journalTextarea = document.querySelector('#journal-entry');
        this.submitButton = document.querySelector('#submit-btn');
        this.sentimentDisplay = document.querySelector('#sentiment-result');
        this.emojiDisplay = document.querySelector('#emoji-display');
    }

    bindEvents() {
        this.submitButton.addEventListener('click', () => this.analyzeEntry());
        this.journalTextarea.addEventListener('input', () => this.handleInput());
    }

    async analyzeEntry() {
        const text = this.journalTextarea.value;
        if (!text.trim()) return;

        try {
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });
            const result = await response.json();
            this.displayResults(result);
        } catch (error) {
            console.error('Error analyzing entry:', error);
        }
    }

    handleInput() {
        this.submitButton.disabled = !this.journalTextarea.value.trim();
    }

    displayResults(result) {
        this.sentimentDisplay.innerHTML = `
            <div class="analysis-result">
                <h3>Mood Analysis</h3>
                <p>Primary emotion: ${result.sentiment}</p>
                <p>Confidence: ${result.confidence}%</p>
            </div>
        `;
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    new JournalEntry();
});