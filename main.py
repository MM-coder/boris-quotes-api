from flask import Flask, jsonify, request
import quotes


# Initialize Flask Application

app = Flask(__name__)


# Add base route

@app.route('/') 
def base_url():

    # Gets the random quote from the "quotes" module
    # Returns the quote as a jsonified dict

    return jsonify({'quote': quotes.get_random_quote()})

# Run the Flask Application
# By default it will run @ 127.0.0.1:5000

if __name__ == "__main__":
    app.run()