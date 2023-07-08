import openai
import gradio



openai.api_key = 'Open Api Key'

messages = [{"role": "system", "content": "What type context do you want to set"}]# Context to be input

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Title of Your Interface") # interface title

demo.launch(share=True)

