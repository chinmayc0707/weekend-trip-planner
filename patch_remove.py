import re

with open('weekend.py', 'r') as f:
    content = f.read()

content = re.sub(r'# Configure Gemini API\n.*?\nmodel = genai\.GenerativeModel\(\'gemma-3-27b-it\'\)\n', '# Configure Gemini API\n', content, flags=re.DOTALL)

with open('weekend.py', 'w') as f:
    f.write(content)
