from dotenv import load_dotenv
import os

load_dotenv()

secret_key = os.getenv("MY_SECRET_KEY")

print("Secret key loaded:", secret_key)