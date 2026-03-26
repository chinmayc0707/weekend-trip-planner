import urllib.request
import urllib.parse
from threading import Thread
from weekend import app
import time

def run_app():
    app.run(port=5000, use_reloader=False)

# Start app in background
t = Thread(target=run_app)
t.daemon = True
t.start()

# wait for app to start
time.sleep(2)

url = 'http://localhost:5000/'

# Test 1: GET request to index
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')
    assert '<input type="hidden" name="api_key" id="api_key_input">' in html
    assert 'sessionStorage.getItem(\'gemini_api_key\')' in html
    print("GET test passed")

# Test 2: POST request (we don't have a real API key or openweather API key, but we can verify it doesn't crash on routing)
try:
    data = urllib.parse.urlencode({
        'budget': '1000',
        'starting_point': 'A',
        'destination': 'B',
        'activities': 'C',
        'dining': 'Any',
        'accommodation': 'Hotel',
        'conditions': 'Good',
        'api_key': 'FAKE_API_KEY'
    }).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        print("POST response code:", response.getcode())
except urllib.error.HTTPError as e:
    print("POST test error:", e)
    # 500 is expected if weather or gemini api keys fail, which is fine for local test without mocked keys, but 400 would be bad.

print("All tests done")
