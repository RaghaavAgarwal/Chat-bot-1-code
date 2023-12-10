import openai
openai.api_key = "*********"  #Generate Yours own API Key Using Openai
def get_apiresponse(prompt : str) -> str | None:
    text : str | None = None
    try:
        response : dict = openai.Completion.create(
            model='gpt-3.5-turbo',
            prompt=prompt,
            temperature=0.9,
            Max_token=150,
            top_p=1,
            Frequency_penaty=0,
            Presence_penalty=0.6,
            Stop=[' Human:' , ' AI:']
        )
        print(response)
    except Exception as e:
        print('ERROR:' , e) 

prompt = "The following is a conversation with a AI assistance. The assistance is helpful, creative, clever, and very friendly.\n\nHuman: hello, who are you?\n AI: I am an AI created by RAghav Agarwal. How can I help you today?\n Human: Hello again! Hi there! What can I do for you?"
get_apiresponse(prompt)
