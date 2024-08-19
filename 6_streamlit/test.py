import os

from dotenv import load_dotenv

load_dotenv()
openaiapikey = os.environ["OPENAI_API_KEY"]
print(openaiapikey)