import React from 'react';

// Fetches a response from the backend server using message
const MessageParser = ({ children, actions }) => {
    const parse = (message) => {
        fetch('http://localhost:5001/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                sender: 'user'
             })
        })
        .then(response => {
            if (response.ok) {
                // Response ok, so return message
                return response.json();
            } else {
                // Response not ok, throw error
                throw new Error("Network Response Failure");
            }
        })
        .then(data => {
            data.forEach(msg => {
                // Send message response to the message handler
                actions.handleMessage(msg.text);
            });
        })
        .catch(error => {
            // Error parsing the message
            console.error("Error during message parsing:", error);
            actions.handleError('Failed to communicate with server. Try again later!');
        });
    };

    return (
        <div>
            {React.Children.map(children, (child) => {
                return React.cloneElement(child, {
                    parse: parse,
                    actions: {},
                });
            })}
        </div>
    );
};

export default MessageParser;