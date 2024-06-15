import { createChatBotMessage } from 'react-chatbot-kit'

// Chatbot style / initial configurations
const config = {
    initialMessages: [createChatBotMessage('Hello! Enter a staff query:')],
    botName: 'DemoCo Bot'
}

export default config;