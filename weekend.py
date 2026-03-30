# app.py
from flask import Flask, render_template, request, Response, stream_with_context
import json
import google.generativeai as genai
import os
from dotenv import load_dotenv
import openweather as openweather

load_dotenv()

app = Flask(__name__)

# Configure Gemini API (deferred to generate_trip_plan)


# Decision Tree Dataset (From previous examples)





def generate_trip_plan(inputs, api_key=None):
    if api_key:
        genai.configure(api_key=api_key)
    else:
        genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemma-3-27b-it")

    prompt = f"""Create a detailed stress-free trip plan considering the following inputs:
    Budget: {inputs['budget']} rupees
    Starting Point: {inputs['starting_point']}
    Destination: {inputs['destination']}
    Activities: {inputs['activities']}
    Dining Preferences: {inputs['dining']}
    Accommodation Type: {inputs['accommodation']}
    Real-time Conditions: {inputs['conditions'] if inputs['conditions'] else 'N/A'}
    Additional Details: {inputs['additional_details'] if inputs['additional_details'] else 'None'}
    current Temperature: {openweather.get_weather_data(inputs['destination'])} Celsius

    The plan should include:
    - A realistic daily itinerary
    - Budget-friendly options matching the specified budget
    - Recommendations considering current weather and local conditions
    - Stress-free transportation options
    - Dining suggestions matching preferences
    - Suitable accommodation options
    - Backup options for unexpected changes
    - Tips for avoiding crowds and stress
    - Include estimated costs for each category
    - Its a weekend trip so duration should be 2 days and 1 night
    - At last give the detailed list of budget you have used for the trip in tabular format
    """

    response = model.generate_content(prompt, stream=True)
    for chunk in response:
        yield chunk.text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        inputs = {
            'budget': request.form['budget'],
            'starting_point': request.form['starting_point'],
            'destination': request.form['destination'],
            'activities': request.form['activities'],
            'dining': request.form['dining'],
            'accommodation': request.form['accommodation'],
            'conditions': request.form['conditions'],
            'additional_details': request.form.get('additional_details', ''),
            'conditions': request.form['conditions']
        }

        try:
            api_key = request.form.get('api_key')
            return render_template('result.html', inputs=json.dumps(inputs), api_key=api_key)
        except Exception as e:
            return render_template('error.html', error=str(e))

    return render_template('index.html')


@app.route('/stream', methods=['POST'])
def stream():
    data = request.json
    inputs = data.get('inputs', {})
    api_key = data.get('api_key')
    response = Response(stream_with_context(generate_trip_plan(inputs, api_key)), mimetype='text/plain')
    response.headers['X-Accel-Buffering'] = 'no'
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Connection'] = 'keep-alive'
    return response

if __name__ == '__main__':


    app.run(debug=True,port=8080)