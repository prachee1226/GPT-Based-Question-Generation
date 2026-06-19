import requests

try:
    response = requests.get("https://huggingface.co")
    print(response.status_code)
except Exception as e:
    print(e)
    