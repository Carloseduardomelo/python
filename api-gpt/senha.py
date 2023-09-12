import json

OPENAI_API_KEY = "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"
url = 'https://api.openai.com/v1/models'
urlChat = "https://api.openai.com/v1/chat/completions"

hearder = {"Authorization" : f"Bearer {OPENAI_API_KEY}" , "Content-Type": "application/json"}

idChat = "gpt-3.5-turbo-0613"

body = {
    "model": idChat,
    "messages" : [{"role": "user" , "content" : "ola mundo"}]
}

bodyT = json.dumps(body)