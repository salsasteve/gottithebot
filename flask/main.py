from flask import Flask
from flask import request
import openai


openai.api_key = ""


app = Flask(__name__)


@app.route("/")
def index():
    
    print('Welcome to the App!')
    
    return (
        """<a href="/image">DALL-E</a>
           <a href="/text">ChatGPT</a>"""
    )



@app.route("/text")
def index1():
    textInput = request.args.get("textInput", "")
    if textInput:
        textOutput = chatGPT(textInput)
    else:
        textOutput = ""
    return (
        """<form action="" method="get">
                Type Something <input type="text" name="textInput">
                <input type="submit" value="Generate Text!">
            </form>"""
        + textOutput
    )

@app.route("/image")
def index2():
    imageInput = request.args.get("imageInput", "")
    if imageInput:
        imageInput = dalle_2(imageInput)
    else:
        imageInput = ""
    return (
        """<form action="" method="get">
                Type Something <input type="text" name="imageInput">
                <input type="submit" value="Generate Image!">
            </form>"""
        + imageInput
    )


def chatGPT(textInput):
    try:
        response = openai.Completion.create ( 
            model="text-davinci-003",
            prompt=textInput,
            max_tokens=150,
            temperature=0.5
        )
        return response['choices'][0]['text']

    except ValueError:
        return "invalid input"



def dalle_2(imageInput):
    response = openai.Image.create(
      prompt=imageInput,
      n=1,
      size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)