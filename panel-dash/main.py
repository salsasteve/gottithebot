import os
import openai
import panel 

openai.api_key = ""


def chatgpt(prompt):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      max_tokens=150,
      temperature=0.5
    )
    return response['choices'][0]['text']

def dalle_2(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url



pn.extension(loading_spinner='dots', loading_color='#00aa41')

inp = pn.widgets.TextInput(value="", placeholder="What's in your mind?")
button_conversation = pn.widgets.Button(name="ChatGPT")
button_image = pn.widgets.Button(name="DALL·E 2")
convos_text = [] # store all texts in a list
convos = [] # store all panel objects in a list

def get_conversations(_):
    prompt = inp.value
    inp.value = ''
    if prompt != "":
        convos_text.append(prompt)
        openai_answer = chatgpt('\n'.join(convos_text)) # prompt includes all history
        convos_text.append(openai_answer)
        convos.append(
            pn.Row('\U0001F60A', pn.pane.Markdown(prompt, width=600))
        )
        convos.append(
            pn.Row('\U0001F916', pn.pane.Markdown(openai_answer, width=600, style={'background-color': '#F6F6F6'}))
        )
    if len(convos_text) == 0:
        convos.append(pn.Row('\U0001F916', pn.pane.Markdown("Coming...", width=600, style={'background-color': '#F6F6F6'})))

    return pn.Column(*convos)


def get_image(_):
    if len(convos_text)>0:
        image_prompt = convos_text[-1]
        image_url = dalle_2(image_prompt)
        return pn.pane.PNG(image_url, width=600)



interactive_conversation = pn.bind(get_conversations, button_conversation)
interactive_image = pn.bind(get_image, button_image)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation,button_image),
       pn.panel(interactive_conversation, loading_indicator=True, height=500),
    pn.panel(interactive_image, loading_indicator=True, height=500),
    
)

dashboard.servable()

