#step:1 : install and import dependencies

import anthropic
from dotenv import load_dotenv
import os
#SStep 2: Create ai keys & clients
load_dotenv()
api_key=os.environ.get("MINIMAX_API_KEY")

base_url="https://api.minimax.io/anthropic"
if not api_key:
    raise ValueError("MiniMax API key not found!")

client = anthropic.Anthropic(
    api_key=api_key,
    base_url="https://api.minimax.io/anthropic",
    default_headers={
        "X-Api-Key": api_key
    }
)
#step 3 : create message

messages =[
    {
        "role":"user",
        "content":[
            {
                "type":"text",
                "text":"Hello, what can i do for you?",
            }
        ],
    }
]


#step 4: send message

response = client.messages.create(
    model="MiniMax-M3",
    max_tokens=1000,
    messages=messages,
)

#step5 : print message

print(response.content[0].text)