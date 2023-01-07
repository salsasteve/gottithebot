import base64
import os

import pytest

from app.OpenAIClient import OpenAIClient


@pytest.fixture
def openai_response():
    return [
        {
            "choices": [{"finish_reason": None, "index": 0, "logprobs": None, "text": "Paris"}],
            "created": 1672898297,
            "id": "cmpl-6VDYXBltl88amL5jz8vs4OxJEmx7V",
            "model": "text-davinci-003",
            "object": "text_completion",
        },
        {
            "choices": [
                {
                    "finish_reason": None,
                    "index": 0,
                    "logprobs": None,
                    "text": " is the capital",
                }
            ],
            "created": 1672898297,
            "id": "cmpl-6VDYXBltl88amL5jz8vs4OxJEmx7V",
            "model": "text-davinci-003",
            "object": "text_completion",
        },
        {
            "choices": [
                {
                    "finish_reason": None,
                    "index": 0,
                    "logprobs": None,
                    "text": " of France.",
                }
            ],
            "created": 1672898297,
            "id": "cmpl-6VDYXBltl88amL5jz8vs4OxJEmx7V",
            "model": "text-davinci-003",
            "object": "text_completion",
        },
    ]


def test_init():
    client = OpenAIClient()
    assert client.OPENAI_API_KEY is not None
    assert os.path.exists(client.base_image_path)


def test_response_parser(openai_response):
    client = OpenAIClient()
    response = client.response_parser(openai_response)
    assert response == "Paris is the capital of France."


def test_generate_image_name():
    client = OpenAIClient()
    prompt = "some prompt"
    full_image_path = client.generate_image_name(prompt)

    # Encode test file name to test against
    message_bytes = prompt.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    test_file_name = base64_bytes.decode("ascii")
    test_path = os.path.join("../images", test_file_name)

    # Decode file name to test against orignal prompt
    image_file_name_64 = os.path.basename(full_image_path)
    base64_bytes = image_file_name_64.encode("ascii")
    message_bytes = base64.b64decode(base64_bytes)
    image_file_name = message_bytes.decode("ascii")

    assert full_image_path == test_path
    assert image_file_name == prompt
