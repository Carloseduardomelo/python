import requests
from senha import ( url , urlChat , hearder , body , bodyT)

response = requests.get(url , headers=hearder)

print(response)
print(response.text)


responseChat = requests.post(urlChat, headers=hearder , data=bodyT)

print(responseChat.text)