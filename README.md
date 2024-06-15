# Chatbot System

## Introduction
This project is a simple chatbot system designed as a basic demonstration of integrating a Flask backend, a React frontend, and a Rasa NLU server. The project was developed in a limited time frame of 1.5 days following the end of my academic examinations on June 13th. Due to the brief development period, the current functionality and styling are minimal but provide a solid foundation for future expansion.

## Key Features
- **Basic Functionality**: Currently handles the specific functionalities outlined in the project requirements document.
- **Scalability**: Designed with scalability in mind; additional functionalities can be added with more training data and expanded intents.

## Prerequisites
- Docker must be installed on your system.

## How to Run
1. Open a terminal in the project folder.
2. Build the Docker containers: docker-compose build
3. Launch the containers: docker-compose up
4. Access chatbot using http://localhost:3000

## Project Structure

### Backend
- **Flask Backend**: Handles requests from the frontend and communicates with the Rasa server.

### Frontend
- **React Frontend**: Utilizes the `react-chatbot-kit` for managing chatbot interactions.

### Rasa
- **Model Training**: The Rasa model is trained on examples primarily for the "find employee" intent.
- **Data and Stories**: Training data is located in `rasa/data/nlu.yml`, with corresponding stories in the same directory.
- **Action Server**: A separate server that receives requests from the Rasa server to query a database.

### Database
- **SQLite**: Currently uses a simple SQLite database. The structure is designed to be easily upgraded to a more robust system like PostgreSQL with minimal changes.

### Docker
- **Containerization**: The project components (frontend, backend, and Rasa) are containerized using Docker, facilitating consistent dependencies management and simplified deployment to cloud platforms like AWS.

## Limitations and Future Work
As of now, the chatbot operates under limited functionality and is tailored to specific use-cases defined in the initial requirements. Future improvements could include:
- **Enhanced Styling and UX**: Improvements to the frontend design for a better user experience.
- **Expanded Training Data and Intents**: To broaden the scope of user interactions and responses.
- **Database Scalability**: Transition from SQLite to PostgreSQL for enhanced performance and scalability.
- **Design Issues**: There are a few design issues such as using fetch localhost instead of fetching the backend container which need to be fixed.
- **Security**: Need to update so that the api calls are secured, through limits, oath, etc.
