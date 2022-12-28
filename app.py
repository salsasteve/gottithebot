import os
import openai
from dotenv import load_dotenv
import time

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# record the time before the request is sent
start_time = time.time()


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="How do you use bleach on white laundry?",
  temperature=0.7,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stream=True
)

# create variables to collect the stream of events
collected_events = []
completion_text = ''
# iterate through the stream of events
for event in response:
    event_time = time.time() - start_time  # calculate the time delay of the event
    collected_events.append(event)  # save the event response
    event_text = event['choices'][0]['text']  # extract the text
    completion_text += event_text  # append the text
    print(f"Text received: {event_text} ({event_time:.2f} seconds after request)")  # print the delay and text

# print the time delay and text received
print(f"Full response received {event_time:.2f} seconds after request")
print(f"Full text received: {completion_text}")