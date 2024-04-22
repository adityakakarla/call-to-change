call_to_change is a Python library that works with our web app (CallToChange) to help you offset LLM emissions.

## How To Use

Use the command pip install call-to-change to download our library.
~~~
from openai import OpenAI
from call_to_change import log

client = OpenAI()

log(client, 'adityak0523@gmail.com')

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
  ]
)

print(response.choices[0].message.content)
~~~
