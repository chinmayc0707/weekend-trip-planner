# app.py
from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv
import openweather as openweather

load_dotenv()

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel('gemma-3-27b-it')


# Decision Tree Dataset (From previous examples)





def generate_trip_plan(inputs):
    prompt = f"""Create a detailed stress-free trip plan considering the following inputs:
    Budget: {inputs['budget']} rupees
    Starting Point: {inputs['starting_point']}
    Destination: {inputs['destination']}
    Activities: {inputs['activities']}
    Dining Preferences: {inputs['dining']}
    Accommodation Type: {inputs['accommodation']}
    Real-time Conditions: {inputs['conditions'] if inputs['conditions'] else 'N/A'}
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
    
    response = model.generate_content(prompt)
    return response.text

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
            'conditions': request.form['conditions']
        }
        
        try:
            plan = generate_trip_plan(inputs)
            return render_template('result.html', plan=plan)
        except Exception as e:
            return render_template('error.html', error=str(e))
    
    return render_template('index.html')

if __name__ == '__main__':

    app.run(debug=True)