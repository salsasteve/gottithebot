import os
import openai
from dotenv import load_dotenv
import time
from PIL import Image  # used to print and edit images
from IPython.display import display
import requests

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# record the time before the request is sent
start_time = time.time()


def ask_question(question):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.7,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stream=True,
    )

    # create variables to collect the stream of events
    collected_events = []
    completion_text = ""
    # iterate through the stream of events
    for event in response:
        event_time = time.time() - start_time  # calculate the time delay of the event
        collected_events.append(event)  # save the event response
        event_text = event["choices"][0]["text"]  # extract the text
        completion_text += event_text  # append the text
        # print(f"Text received: {event_text} ({event_time:.2f} seconds after request)")  # print the delay and text

    # print the time delay and text received
    print(f"Full response received {event_time:.2f} seconds after request")
    print(f"Full text received: {completion_text}")

    return completion_text


def generate_image(prompt):
    """
    Generate an image from a prompt
    """
    # call the OpenAI API
    generation_response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url",
    )
    print(generation_response)
    # set a directory to save DALL-E images to
    image_dir_name = "images"
    image_dir = os.path.join(os.curdir, image_dir_name)

    # create the directory if it doesn't yet exist
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # print the directory to save to
    print(f"{image_dir=}")

    generated_image_name = (
        "generated_image.png"  # any name you like; the filetype should be .png
    )
    generated_image_filepath = os.path.join(image_dir, generated_image_name)
    generated_image_url = generation_response["data"][0][
        "url"
    ]  # extract image URL from response
    generated_image = requests.get(generated_image_url).content  # download the image

    with open(generated_image_filepath, "wb") as image_file:
        image_file.write(generated_image)  # write the image to the file

    # print the image
    print(generated_image_filepath)
    return generated_image_filepath, prompt
