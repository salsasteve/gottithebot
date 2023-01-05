import os

import pytest

from app.OpenAIClient import OpenAIClient


@pytest.fixture
def openai_response():
    return [
        {
            "choices": [
                {"finish_reason": None, "index": 0, "logprobs": None, "text": "Paris"}
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
