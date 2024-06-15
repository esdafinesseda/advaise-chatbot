import config from '../chatbot/config'
import MessageParser from '../chatbot/MessageParser'
import ActionProvider from '../chatbot/ActionProvider'
import Chatbot from 'react-chatbot-kit'
import 'react-chatbot-kit/build/main.css'

// Chatbot component to embedded in react app
const ChatBotComponent = () => {
    return (
        <div>
            <Chatbot
                config={config}
                messageParser={MessageParser}
                actionProvider={ActionProvider}
            />
        </div>
    );
}

export default ChatBotComponent;