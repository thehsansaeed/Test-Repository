# huggingface_example.py

import os
from transformers import pipeline

# Dynamically set Hugging Face API key in the environment (for secure access)
os.environ["HF_HOME"] = "/path/to/your/cache"  # Optional, if you want to set a custom cache location
os.environ["HF_API_KEY"] = "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"  # Set your Hugging Face API key here

# Example: Using a Hugging Face model for text generation (GPT-2 or another model)
def generate_text(prompt):
    # Fetch the Hugging Face API key from the environment
    api_key = os.getenv("HF_API_KEY")
    
    if api_key is None:
        print("Hugging Face API key not set.")
        return None
    
    # Load the text generation model from Hugging Face using transformers
    generator = pipeline('text-generation', model='gpt2', device=0)  # Using GPT-2 model

    # Generate text from the prompt
    result = generator(prompt, max_length=50, num_return_sequences=1)
    
    return result[0]['generated_text']

# Test the function with a prompt
prompt = "Once upon a time in a land far, far away"
generated_text = generate_text(prompt)

if generated_text:
    print("Generated Text:", generated_text)
