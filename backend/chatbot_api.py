from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import logging
from logging import StreamHandler
import coloredlogs

app = Flask(__name__)

CORS(app, resources={r"/chat": {"origins": "*"}})

logging.basicConfig(level=logging.DEBUG)

# Configure logging to terminal
stream_handler = StreamHandler()
coloredlogs.install(level='INFO', logger=app.logger, stream=stream_handler)
app.logger.setLevel(logging.INFO)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        app.logger.debug('Received data: %s', data)
        message = data['message']

        # Sending the message to the Rasa server
        response = requests.post(
            'http://rasa:5005/webhooks/rest/webhook',
            json={'sender': 'user', 'message': message}
        )
        
        # Check if the request was successful
        response.raise_for_status()

        # Log the response from Rasa
        app.logger.debug('Received response: %s', response.json())
        return jsonify(response.json())

    except requests.exceptions.RequestException as e:
        app.logger.error("Failed to send message to Rasa: %s", e)
        return jsonify({"error": "Failed to communicate with Rasa backend"}), 500

    except Exception as e:
        app.logger.error("An error occurred: %s", e)
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
