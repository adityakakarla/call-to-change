call_to_change is a Python library that works with our web app (CallToChange) to help you offset LLM emissions.

## How To Use

Use the command pip install call-to-change to download our library. Ensure the downloaded version is >= 0.8.6.

Here is a sample script utilizing call-to-change.

~~~
from openai import OpenAI
from call_to_change import log

client = OpenAI()

log(client, 'test@test.com')

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
  ]
)

print(response.choices[0].message.content)
~~~

## How To Use The Log Function

The log function takes in two parameters, an OpenAI client and an email address.

It modifies the client to log any text generation or image generation calls you made. These calls will be tied to the email address you input into the log function.

If you have an account with _[our web app](https://calltochange.vercel.app)_, your logged calls can be seen through your dashboard. From there, you can view the carbon emissions tied to your OpenAI calls and the cost to offset these emissions.

If not, your text generation and image generation calls will still be saved. To access your data, create an account with us _[here](https://calltochange.vercel.app/auth/sign-up)_ and go to the Dashboard page.

## How Does The Log Function Work?

It modifies the OpenAI client to log the calls you make.

For instance, let's say you generate text (for reference, view the code block in the "How To Use" section). The modified client will still generate text normally. However, it will also send a POST request to our web app. Our API routes work with our database to increment the number of LLM calls you have made.

## Do You Support Other Gen AI Tools?

Sadly, no. I built this tool as part of a hackathon and need to spend some time updating it. Maybe in the future?
