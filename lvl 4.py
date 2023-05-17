import requests
import random
import time
import openai

openai.api_key = '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'  # Replace with your OpenAI API key

header = {
    'authorization': 'MTAwNDQyMjM5MzU4ODA4ODk1Mw.GS9aP_.huPnQp5WLIK3dCSGfKJrjBRYPLwDY75d2Nu1Ds'  # Replace with your Discord authorization token
}

def send_message(content, message_reference=None):
    payload = {
        'content': content
    }

    if message_reference:
        payload['message_reference'] = {
            'message_id': message_reference['message_id'],
            'channel_id': message_reference['channel_id']
        }

    requests.post('https://discord.com/api/v9/channels/1016726800526757931/messages', json=payload, headers=header)

def fetch_messages():
    response = requests.get('https://discord.com/api/v9/channels/1016726800526757931/messages', headers=header)
    messages = response.json()
    return messages

def generate_reply(message_content):
    reply = openai.Completion.create(
        engine="text-davinci-003",  # Replace with the appropriate engine name
        prompt=message_content,
        max_tokens=30,  # Limit the reply to 30 tokens (words)
        n=1,
        temperature=0.7
    )
    reply_text = reply.choices[0].text.strip()
    return reply_text

while True:
    messages = fetch_messages()

    if len(messages) > 0:
        for message in messages:
            message_content = message['content']
            author_id = message['author']['id']
            message_id = message['id']
            channel_id = message['channel_id']

            if author_id != '1004422393588088953':  # Replace with your Discord user ID
                reply_text = generate_reply(message_content)
                reply_content = f"{reply_text}"
                send_message(reply_content, {'message_id': message_id, 'channel_id': channel_id})

    # Generate a random time interval between 1 to 2 minutes
    interval = random.randint(150, 180)
    time.sleep(interval)
