import requests
import json
import io
import pygame
from urllib.request import urlopen

def getJsonRequest(url):
    page = requests.get(url)
    return json.loads(page.content)
