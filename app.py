from flask import Flask

# Create a Flask web app instance
app = Flask(__name__)

# Define the homepage route ("/")
@app.route("/")
def home():
    return "Say hello to my litle friend!"

# Run the app on port 5000, accessible from outside
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
