import requests
import json
import io
import pygame
from urllib.request import urlopen

def getJsonRequest(url):
    page = requests.get(url)
    return json.loads(page.content)

def getImage(url):
    page = urlopen(url).read()
    image_file = io.BytesIO(page)
    print(image_file)
    return pygame.image.load(image_file)
