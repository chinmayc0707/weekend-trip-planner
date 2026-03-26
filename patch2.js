const fs = require('fs');
let py = fs.readFileSync('weekend.py', 'utf8');
py = py.replace(/# Configure Gemini API\ngenai\.configure\(api_key=os\.environ\['GEMINI_API_KEY'\]\)\nmodel = genai\.GenerativeModel\('gemma-3-27b-it'\)/, '# Configure Gemini API');
fs.writeFileSync('weekend.py', py);
