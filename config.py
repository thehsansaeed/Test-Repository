# Exposing an API key (this is just an example, DO NOT use real keys)
API_KEY = "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"  # Hugging Face API Key (hardcoded)

# Example API call using the hardcoded API key
def call_huggingface_api():
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    print(f"API Key used: {API_KEY}")
    # Simulating an API call
    # response = requests.get('https://huggingface.co/api/endpoint', headers=headers)
    # return response.json()

call_huggingface_api()
