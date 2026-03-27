# Stress-Free Trip Planner

A Flask-based web application that generates personalized, stress-free trip plans using Google's Gemini AI. Users can input their budget, starting point, destination, activities, dining preferences, accommodation type, and current conditions. The application also fetches current weather conditions using OpenWeather API to provide tailored recommendations.

## Features

- **Personalized Itineraries:** Generates 2-day, 1-night weekend trip plans.
- **Budget Tracking:** Keeps track of estimated costs for each category.
- **AI-Powered:** Utilizes the `gemma-3-27b-it` model from Google's Gemini API.
- **Dynamic API Key Input:** Users are prompted to securely provide their Gemini API key via the frontend, storing it temporarily in their browser session. Alternatively, it falls back to a server-side environment variable.

## Setup & Installation

### 1. Prerequisites
- Python 3.8+
- An API key for Google Gemini (optional if user provides on frontend)
- An API key for OpenWeather (configured locally, likely in your environment)

### 2. Install Dependencies
Install the required packages using `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root of the project to specify any server-wide fallback keys (optional if relying purely on frontend):
```
GEMINI_API_KEY=your_default_server_api_key_here
```

### 4. Running the Application
Start the Flask development server:
```bash
python weekend.py
```
Then, open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage
1. Open the app in your browser.
2. If prompted, enter your Gemini API Key. This will be saved in your browser's session storage for the session.
3. Fill out the form with your trip details (Budget, Starting Point, Destination, etc.).
4. Click **Generate Trip Plan**.
5. Wait a moment while the AI creates your detailed, stress-free itinerary.
