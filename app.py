import requests

#apikey import
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": API_KEY}

inp = input("What is your query?:")

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": str(inp),
	"parameters": {
        "width": 1920, 
        "height": 1080,  
    },
})
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
image.show()