from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from the .env file
load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Say hello to a new Python developer in one short sentence."
)

print(response.output_text)