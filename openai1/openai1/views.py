from django.http import HttpResponse
from django.shortcuts import render

import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
  prompt="20age korean student girl photo face beautiful",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)


def home(request):
    
    context = { 'image_url' : image_url}
    return render(request, 'index.html', context)
