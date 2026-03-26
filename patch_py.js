const fs = require('fs');
let py = fs.readFileSync('weekend.py', 'utf8');

py = py.replace(
    /def generate_trip_plan\(inputs\):/,
    'def generate_trip_plan(inputs, api_key=None):\n    if api_key:\n        genai.configure(api_key=api_key)\n    else:\n        genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))\n    model = genai.GenerativeModel("gemma-3-27b-it")\n'
);

py = py.replace(
    /plan = generate_trip_plan\(inputs\)/,
    "api_key = request.form.get('api_key')\n            plan = generate_trip_plan(inputs, api_key)"
);

// remove top level genai configure
py = py.replace(/genai\.configure\(api_key=os\.environ\['GEMINI_API_KEY'\]\)\nmodel = genai\.GenerativeModel\('gemma-3-27b-it'\)/, '');

fs.writeFileSync('weekend.py', py);
