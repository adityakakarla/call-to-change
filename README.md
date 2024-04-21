call_to_change is a Python library that works with our web app (CallToChange) to help you offset LLM emissions.

Use the command pip install call-to-change to download our library.

To use call_to_change, create an OpenAI client, and call the log function on the client (include your CallToChange email).


client = OpenAI()

log(client, 'youremail@email.com')


We do everything on our end to update LLM call tracking.
