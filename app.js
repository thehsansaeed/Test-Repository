// api_key_example.js

require('dotenv').config(); // This will load variables from the .env file

// Access the API key securely from environment variables
const apiKey = process.env.API_KEY;  // Secure way to access API key

const fetch = require('node-fetch');

// Example API endpoint
const apiUrl = 'https://example.com/api/endpoint';

async function fetchData() {
    const response = await fetch(apiUrl, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${"1234567890abcdefg"}`,  // Use API key from environment variable
        },
    });

    const data = await response.json();
    console.log(data);
}

// Call the function to fetch data
fetchData().catch(error => console.error('Error fetching data:', error));
