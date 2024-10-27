from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

# Initialize configuration
genai.configure(api_key='your Gemini API key')
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Show the web page from index.html 

@app.route('/generate', methods=['POST'])
def generate_response():
    data = request.get_json()  # Get JSON data with request
    prompt = data.get("prompt")  # Get the prompt with request

    # Using API to generate the response
    try:
        response = model.generate_content(prompt)
        result = response.text  # Get the response text
        return jsonify({"response": result})  # Send the response as a JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Give an error

if __name__ == '__main__':
    app.run(debug=True)