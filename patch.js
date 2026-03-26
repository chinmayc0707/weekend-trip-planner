const fs = require('fs');
let html = fs.readFileSync('templates/index.html', 'utf8');

// Add hidden input for api key inside the form
html = html.replace('<form method="POST" id="form">', '<form method="POST" id="form">\n            <input type="hidden" name="api_key" id="api_key_input">');

// Add javascript to prompt for api key
const js = `
<script>
    document.addEventListener('DOMContentLoaded', function() {
        let apiKey = sessionStorage.getItem('gemini_api_key');
        if (!apiKey) {
            apiKey = prompt("Please enter your Gemini API Key (leave blank to use server default):");
            if (apiKey) {
                sessionStorage.setItem('gemini_api_key', apiKey);
            }
        }
        if (apiKey) {
            document.getElementById('api_key_input').value = apiKey;
        }
    });

    document.getElementById('submit').addEventListener('click', function(event) {
        const form = document.getElementById('form');
        if (form.checkValidity()) {
            alert('Generating your trip plan... It may take a moment. Click "OK" to proceed.');
        }
    });
</script>
`;

html = html.replace(/<script>[\s\S]*?<\/script>/, js);

fs.writeFileSync('templates/index.html', html);
