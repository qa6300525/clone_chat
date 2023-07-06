
// Get references to the input field, send button, and display window
var userInput = document.getElementById('user-input');
var sendButton = document.getElementById('send-button');
var displayWindow = document.getElementById('display-window');


// Function to add a user message to the display window
function addUserMessage(message) {
    // Create a new message element
    var messageElement = document.createElement('div');
    messageElement.className = 'message text-right';
    const htmlText = convertMarkdownToHTML(message);

    // Add the message content and avatar
    messageElement.innerHTML = `
        <div class="d-flex align-items-start justify-content-end">
            <div class="bg-primary text-white p-3 rounded">
                ${htmlText}
            </div>
            <img src="https://plus.unsplash.com/premium_photo-1683865775631-3283bfaf6508?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGF2YXRhcnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=800&q=60" alt="User Avatar" width="40" height="40" class="rounded-circle ml-2">
        </div>
    `;
    // Add the new message to the display window
    displayWindow.appendChild(messageElement);

    // Scroll to the bottom of the display window
    displayWindow.scrollTop = displayWindow.scrollHeight;
}

function addAIMessage(message) {
    // Create a new message element
    var messageElement = document.createElement('div');
    messageElement.className = 'message';
    const htmlText = convertMarkdownToHTML(message);

    // Add the message content and avatar
    messageElement.innerHTML = `
                <div class="d-flex align-items-start">
                <img src="https://plus.unsplash.com/premium_photo-1683690944936-18103fa341dd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1100&q=80" alt="Model Avatar" width="40" height="40" class="rounded-circle mr-2">
                <div class="bg-light p-3 rounded">
                    ${htmlText}
                </div>
              </div>
    `;

    // Add the new message to the display window
    displayWindow.appendChild(messageElement);

    // Scroll to the bottom of the display window
    displayWindow.scrollTop = displayWindow.scrollHeight;
}

function checkInput() {
    if(userInput.value.trim() === '') {
        sendButton.disabled = true;
    } else {
        sendButton.disabled = false;
    }
}

function sendMessageToServer(message) {
    fetch('/chat/get_msg', {  // The URL of the server-side route
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        // Process the server's response here
        console.log(data);
        addAIMessage(data.message);
        MathJax.typeset();

    });
}

checkInput();

userInput.addEventListener('input', checkInput);


// Listen for the send button being clicked
sendButton.addEventListener('click', function() {
    // Get the user's input
    var message = userInput.value;

    // Add the user's message to the display window
    addUserMessage(message);
    MathJax.typeset();

    // Clear the input field
    userInput.value = '';

    checkInput();

    // Send the user's message to the server
    sendMessageToServer(message);
});
