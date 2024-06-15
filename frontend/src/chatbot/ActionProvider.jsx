import React from 'react';
import { createChatBotMessage } from 'react-chatbot-kit';

// Handles actions sent from the message parser
const ActionProvider = ({ createChatBotMessage, setState, children }) => {

    // Handles valid messages returned
    const handleMessage = (messageText) => {

        // Creates the message text
        const botMessage = createChatBotMessage(messageText);

        // Update the previous message state
        setState((prevState) => ({
            ...prevState,
            messages: [...prevState.messages, botMessage],
        }));
    };

    // Handles error messages returned
    const handleError = (errorText) => {

        // Creates the error text
        const errorMessage = createChatBotMessage(errorText);

        // Update the previous message state
        setState((prevState) => ({
            ...prevState,
            messages: [...prevState.messages, errorMessage],
        }));
    };

    return (
        <div>
            {React.Children.map(children, (child) => {
                return React.cloneElement(child, {
                    actions: {
                        handleMessage,
                        handleError
                    },
                })
            })}
        </div>
    );
};

export default ActionProvider;
