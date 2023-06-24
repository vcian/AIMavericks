from app import app, request

@app.route('/')
def hello():
    return("data")

def ai_model(input_data):
    # Process the input data using your AI model
    # Replace this with your AI model's logic
    

    return input_data

@app.route('/api/process', methods=['POST'])
def process_data():
    data = request.json  # Assuming the frontend sends JSON data

    # Extract the input from the received data
    input_data = data.get('message')

    # Pass the input to the AI model for processing
    response = ai_model(input_data)
    data['message'] = response
    # Return the AI model response to the frontend
    return data