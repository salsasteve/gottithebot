# import sys
# from chatgpt import Conversation

# # Initialize the ChatGPT object with your API key
# # model = ChatGPT(api_key="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")
# conversation = Conversation(config_path="./config.json")

# Stream the message as it arrives.
# for chunk in conversation.stream("We are going to start a conversation. I will speak English and you will speak Portuguese."):
#     print(chunk, end="")
#     sys.stdout.flush()

# # Wait until the message is fully received.
# print(conversation.chat("What's the color of the sky?"))

# # The AI will forget it was speaking Portuguese
# conversation.reset()
# print(conversation.chat("What's the color of the sun?"))

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="How do you use bleach on white laundry?",
  temperature=0.7,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response.choices[0]["text"])
