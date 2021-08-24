import requests
import json
import io


def getJsonRequest(url):
    page = requests.get(url)
    return json.loads(page.content)
