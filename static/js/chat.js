document.addEventListener('DOMContentLoaded', function() {
    const chatContainer = document.querySelector('.chat-container');
    const chatForm = document.querySelector('#chat-form');
    const messageInput = document.querySelector('#message-input');
    const typingIndicator = document.querySelector('.typing-indicator');

    // Add initial greeting
    addMessage("Hai bestie! 👋 Gue Irfa, AI yang siap bantuin lo belajar dengan cara yang seru! Ada yang bisa gue bantu?", 'bot');

    chatForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const message = messageInput.value.trim();
        if (!message) return;

        // Add user message
        addMessage(message, 'user');
        messageInput.value = '';

        // Show typing indicator
        typingIndicator.style.display = 'block';
        scrollToBottom();

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });

            const data = await response.json();
            
            // Hide typing indicator
            typingIndicator.style.display = 'none';

            if (response.ok) {
                addMessage(data.response, 'bot');
            } else {
                addMessage(data.error || 'Waduh error nih bestie, coba lagi ya!', 'bot');
            }
        } catch (error) {
            console.error('Error:', error);
            typingIndicator.style.display = 'none';
            addMessage('Koneksi bermasalah nih bestie, cek internet kamu ya!', 'bot');
        }
    });

    function addMessage(message, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('chat-message');
        messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
        messageDiv.textContent = message;
        chatContainer.appendChild(messageDiv);
        scrollToBottom();
    }

    function scrollToBottom() {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
});

