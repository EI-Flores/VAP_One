import openai

openai.api_key = "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"

completion = openai.Completion.create(engine="text-davinci-003",
                         prompt="¿Qué eres ChatGPT?",
                         max_tokens=2048)

print(completion.choices[0].text)