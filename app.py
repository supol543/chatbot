from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Initialize the OpenAI API with your API key
openai.api_key = "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"

# Define the chatbot's prompt and response format
prompt = "Please ask me a question."
response_format = "{}"

# Define a function that sends a request to the OpenAI API to generate a response based on the user's input
def generate_response(prompt, response_format, user_input):
    if "who made" in user_input or "make you" in user_input:
        return "Supol is my owner."

    if "who are you" in user_input or "what is your name" in user_input:
        return "I am Supol."

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt + "\nQ: " + user_input + "\nA:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response_format.format(response.choices[0].text.strip())

# Define the app route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    chat_history = []
    if request.method == 'POST':
        user_input = request.form['message']
        if user_input:
            response_text = generate_response(prompt, response_format, user_input)
            chat_history.append(('user', user_input))
            chat_history.append(('bot', response_text))
    return render_template('index.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)
