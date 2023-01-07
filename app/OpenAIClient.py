import base64
import os

import openai
import requests
from dotenv import load_dotenv


class OpenAIClient:
    def __init__(self):
        load_dotenv()
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.openai = openai
        self.openai.api_key = self.OPENAI_API_KEY
        self.base_image_path = os.getenv("IMAGE_PATH")  # TODO: Create online storage for images
        self.image_folder = os.getenv("IMAGE_FOLDER")

    def ask_question(self, question: str) -> str:
        """Ask OpenAI for a response

        :param question: short question to ask
        :type question: str
        :return: response from OpenAI
        :rtype: str
        """

        response = self.openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=0.7,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stream=True,
        )

        completion_text = self.response_parser(response)
        return completion_text

    def generate_image(self, prompt: str) -> str:
        """Generate an image from a prompt

        :param prompt: prompt to generate image from
        :type prompt: str
        :return: path to generated image
        :rtype: str
        """
        generation_response = self.openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url",
        )

        image_path = self.generate_image_path(prompt)
        url = generation_response["data"][0]["url"]
        if self.download_image(url, image_path):
            return image_path
        else:
            return None

    def response_parser(self, response: dict) -> str:
        """Parse the response from OpenAI

        :param response: response from OpenAI
        :type response: str
        :return: parsed response
        :rtype: str
        """

        parsed_response = ""
        for event in response:
            event_text = event["choices"][0]["text"]
            parsed_response += event_text
        return parsed_response

    def generate_image_path(self, prompt: str) -> str:
        """Generate a unique image name

        :param prompt: prompt to generate image name from
        :type prompt: str
        :return: unique image name
        :rtype: str
        """

        generated_image_name = self.encode_msg(prompt) + ".png"
        image_dir = os.path.join(os.curdir, self.image_folder)

        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        generated_image_filepath = os.path.join(image_dir, generated_image_name)

        return generated_image_filepath

    def download_image(self, url: str, save_path: str) -> bool:
        """Download an image from a url

        :param url: url to download image from
        :type url: str
        :return: True if image was downloaded, False otherwise
        :rtype: bool
        """

        image_data = requests.get(url).content
        with open(save_path, "wb") as handler:
            handler.write(image_data)

        return os.path.isfile(save_path)

    def encode_msg(self, message: str) -> str:
        message_bytes = message.encode("ascii")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("ascii")
        return base64_message

    def decode_msg(self, base64_message: str) -> str:
        base64_bytes = base64_message.encode("ascii")
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode("ascii")
        return message
