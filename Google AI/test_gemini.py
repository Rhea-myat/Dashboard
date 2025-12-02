from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Say you are beautiful in chinese"
)
print(response.text)

import os 
print(os.environ.get("GEMINI_API_KEY"))